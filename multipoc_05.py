import multiprocessing
import threading
import time


start = time.perf_counter()

def do_something(seconds):
    print(f'Sleeping {seconds} second(s)...')
    time.sleep(seconds)
    print('Done sleeping...')


processes = []
# create processes
# p1 = multiprocessing.Process(target=do_something, args=(1.5,))
# p2 = multiprocessing.Process(target=do_something, args=(1.5,))

for _ in range(10):
    p = multiprocessing.Process(target=do_something, args=(1.5,))
    p.start()
    processes.append(p)


# p1.start()
# p2.start()

# join means that process will finish before moving on in the script
# p1.join()
# p2.join()

for process in processes:
    process.join()



finish = time.perf_counter()

print(f'Finished in {round(finish-start, 2)} second(s)')



