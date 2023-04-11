"""
First, install the systemd-python package:
pip install systemd-python

You can use it as a command-line tool like this:
python3 systemd_manager.py <enable|disable|start|stop|status> <unit_name>
"""

import sys
from systemd.journal import JournalHandler
import logging
from systemd import dbus

logger = logging.getLogger(__name__)
logger.addHandler(JournalHandler())
logger.setLevel(logging.INFO)


def get_systemd_manager():
    sys_bus = dbus.SystemBus()
    systemd_manager = sys_bus.get_object('org.freedesktop.systemd1', '/org/freedesktop/systemd1')
    return dbus.Interface(systemd_manager, 'org.freedesktop.systemd1.Manager')


def enable_unit(unit_name):
    manager = get_systemd_manager()
    manager.EnableUnitFiles([unit_name], False, True)
    logger.info(f"{unit_name} enabled")


def disable_unit(unit_name):
    manager = get_systemd_manager()
    manager.DisableUnitFiles([unit_name], False)
    logger.info(f"{unit_name} disabled")


def start_unit(unit_name):
    manager = get_systemd_manager()
    manager.StartUnit(unit_name, 'replace')
    logger.info(f"{unit_name} started")


def stop_unit(unit_name):
    manager = get_systemd_manager()
    manager.StopUnit(unit_name, 'replace')
    logger.info(f"{unit_name} stopped")


def get_unit_status(unit_name):
    manager = get_systemd_manager()
    unit_path = manager.GetUnit(unit_name)
    unit_object = dbus.SystemBus().get_object('org.freedesktop.systemd1', unit_path)
    unit_properties = dbus.Interface(unit_object, 'org.freedesktop.DBus.Properties')
    active_state = unit_properties.Get('org.freedesktop.systemd1.Unit', 'ActiveState')
    logger.info(f"{unit_name} status: {active_state}")
    return active_state


if __name__ == "__main__":
    action = sys.argv[1]
    unit_name = sys.argv[2]

    if action == "enable":
        enable_unit(unit_name)
    elif action == "disable":
        disable_unit(unit_name)
    elif action == "start":
        start_unit(unit_name)
    elif action == "stop":
        stop_unit(unit_name)
    elif action == "status":
        print(get_unit_status(unit_name))
    else:
        print("Invalid action. Usage: python3 systemd_manager.py <enable|disable|start|stop|status> <unit_name>")
