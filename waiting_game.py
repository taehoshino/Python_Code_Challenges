import time
import random

def waiting_game():
    target_time = random.randint(2,4)
    input(f"Your target time is {target_time} seconds. Press Enter to start...")
    tic = time.perf_counter()
    input(f"Press Enter again after {target_time} seconds...")
    toc = time.perf_counter()
    delta = toc - tic
    print(f"Elapsed time: {delta:0.4f} seconds")
    if delta > target_time:
        print(f"{delta - target_time:0.4f} seconds too slow")
    else:
        print(f"{target_time - delta:0.4f} seconds too fast")


waiting_game()