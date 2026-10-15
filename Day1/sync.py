import time
from timeit import default_timer as timer

def run_task(name,seconds):
    print(f"{name} started at {timer()}")
    #do task
    time.sleep(seconds)
    print(f"{name} completed at : {timer()}")
    
start=timer()
run_task("upload..", 5)
run_task("download..", 3)
run_task("backup..", 5)

end=timer()
runtime=end-start
print(f"Total time taken :{runtime:.2f}secs")