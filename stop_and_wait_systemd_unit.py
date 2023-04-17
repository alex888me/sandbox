import sys
from pydbus import SystemBus
from gi.repository import GLib

def unit_stopped_callback(job_id, unit_name, result):
    if job_id == waiting_job_id:
        print(f"Unit {unit_name} stopped with result: {result}")
        loop.quit()

if len(sys.argv) < 2:
    print("Usage: python stop_systemd_unit.py <unit_name>")
    sys.exit(1)

unit_name = sys.argv[1]

bus = SystemBus()

systemd = bus.get(".systemd1", "/org/freedesktop/systemd1")

waiting_job_id = systemd.StopUnit(unit_name, "fail")
print(f"Waiting for unit {unit_name} to stop, job id: {waiting_job_id}")

loop = GLib.MainLoop()

signal_match = systemd.onJobRemoved.connect(unit_stopped_callback)
loop.run()

signal_match.disconnect()