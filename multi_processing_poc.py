import time
import traceback
from multiprocessing import Process, Queue

class MP_POC:
    def __init__(self):
        self.sync_tasks = {
            'A': self.worker,
            'B': self.worker,
            'C': self.worker,
        }

    def worker(self, name, delay, queue, fail=False):
        try:
            time.sleep(delay)
            if fail:
                raise ValueError(f"Process {name} encountered an error!")  # Simulated error
            print(f"Process {name} completed successfully")
        except Exception as e:
            queue.put((name, str(e), traceback.format_exc()))  # Send error details

    def sync(self):
        error_queue = Queue()
        processes = {}
        for name, sync_task in self.sync_tasks.items():
            processes[name] = Process(target=sync_task, name=name, args=(name, 2, error_queue, False))

        for p in processes.values():
            p.start()

        while any(processes.values()):
            for name, p in processes.items():
                if p and not p.is_alive():
                    print(p.name, "has completed!")
                    p.join()
                    processes[name] = None

            time.sleep(0.5)

        # Check if any errors occurred
        while not error_queue.empty():
            name, error_msg, trace = error_queue.get()
            print(f"Error in process {name}: {error_msg}")
            print(f"Traceback:\n{trace}")

inst = MP_POC()
inst.sync()

"""
Best Practices & Considerations:
    Graceful Termination: Always try to terminate the process gracefully first using p.terminate(). This gives the process an opportunity to clean up resources and exit properly. Avoid using p.kill() unless absolutely necessary because it can leave resources or files open.
    Timeout Handling: The amount of time you wait before checking whether the process is alive should be configurable and not too long. A typical value might be between 1 and 5 seconds, depending on the task the process is performing. This waiting period helps balance between allowing the process to terminate properly and not making the parent process wait unnecessarily.
    Force Kill (Fallback): If the process does not terminate after the grace period, you can call p.kill(). This should be your last resort because it doesn’t allow the child process to clean up its resources, which can sometimes cause issues (e.g., file locks, memory leaks).
    
            for name, p in processes.items():
            p.terminate()  # First attempt to gracefully terminate the process
            p.join(timeout)  # Wait for the process to exit or timeout
            
            # If process is still alive, force kill it
            if p.is_alive():
                print(f"Process {name} exceeded {timeout} seconds, forcefully terminating...")
                p.kill()  # Force kill the process

            # Ensure that the process is cleaned up after termination
            p.join()  # Wait for the process to finish (whether gracefully or forcefully)

            # Check if any errors occurred
            if not p.exitcode == 0:
                print(f"Process {name} was killed or failed.")
            else:
                print(f"Process {name} completed successfully.")
"""