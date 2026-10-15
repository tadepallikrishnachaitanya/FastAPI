from timeit import default_timer as timer
import asyncio

async def run_task(name,seconds):
    print(f"{name} started at {timer()}")
    #do task
    await asyncio.sleep(seconds)
    print(f"{name} completed at : {timer()}")
#================


async def main():
    start=timer()
    await asyncio.gather(
        run_task("upload..", 5),
        run_task("download..", 3),
        run_task("backup..", 5) 
    )
    end=timer()
    runtime=end-start
    print(f"Total time taken :{runtime:.2f}secs")

asyncio.run(main())