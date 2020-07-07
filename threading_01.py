import threading
import time


start = time.perf_counter()

def do_something(seconds):
    print(f'Sleeping {seconds} second(s)...')
    time.sleep(seconds)
    print('Done sleeping...')

threads = []

for _ in range(10):
    t = threading.Thread(target=do_something, args=[1.5])
    t.start()
    threads.append(t)

for thread in threads:
    thread.join()

# # create threads
# t1 = threading.Thread(target=do_something)
# t2 = threading.Thread(target=do_something)
#
# # run function
# t1.start()
# t2.start()
#
# # join threads
# t1.join()
# t2.join()

finish = time.perf_counter()

print(f'Finished in {round(finish-start, 2)} second(s)')