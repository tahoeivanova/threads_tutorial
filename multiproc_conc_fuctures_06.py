import concurrent.futures
import time

start = time.perf_counter()

def do_something(seconds):
    print(f'Sleeping {seconds} second(s)...')
    time.sleep(seconds)
    return f'Done sleeping... {seconds}'


with concurrent.futures.ProcessPoolExecutor() as executor:
    # pass a different range of args
    seconds = [5,4,3,2,1]

    # submit method schedules a func to be executed and returns future objects
    # results = [executor.submit(do_something, sec) for sec in seconds]
    # map the function
    # map run the func with every item of the list, returns the results
    # instead of returning the result as it is completed, map returns the results in the order it was started
    results = executor.map(do_something, seconds)

    '''
    f1 = executor.submit(do_something, 2.5)
    f2 = executor.submit(do_something, 2.5)
    '''

    # a future object incapsulates the execution of func and allows to check if it is being executed, or done, or check the result
    # result method
    '''
    print(f1.result())
    print(f2.result())
    '''
    # as_completed
    # for f in concurrent.futures.as_completed(results):
    #     print(f.result())
    for result in results:
        print(result)


finish = time.perf_counter()

print(f'Finished in {round(finish-start, 2)} second(s)')



