import sys
import time
from pydbus import SystemBus
from gi.repository import GLib

if len(sys.argv) < 2:
    print("Usage: python stop_systemd_unit.py <unit_name>")
    sys.exit(1)

unit_name = sys.argv[1]

bus = SystemBus()

systemd = bus.get(".systemd1", "/org/freedesktop/systemd1")

waiting_job_id = systemd.StopUnit(unit_name, "fail")
print(f"Waiting for unit {unit_name} to stop, job id: {waiting_job_id}")

unit_path = systemd.GetUnit(unit_name)
unit_proxy = bus.get(".systemd1", unit_path)

while True:
    unit_active_state = unit_proxy.Get("org.freedesktop.systemd1.Unit", "ActiveState")
    print(f"Unit {unit_name} active state: {unit_active_state}")

    if unit_active_state == "inactive" or unit_active_state == "failed":
        break

    time.sleep(1)

print(f"Unit {unit_name} stopped.")