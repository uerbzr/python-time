import multiprocessing as mp
import time

start = time.perf_counter()

def do_something():
    print('sleeping for a second')
    time.sleep(1)
    print('done sleeping')

p1 = mp.process(target=do_something)
p2 = mp.process(target=do_something)


p1.start()
p2.start()

p1.join()
p2.join()

finish = time.perf_counter()

print(f'Finished in {round(finish-start,2)} second(s)')



#sleeping for a second
#done sleeping
#sleeping for a second
#done sleeping
#Finished in 2.0 second(s)