import time

start = time.perf_counter()

def do_somehting():
    print('sleeping for a second')
    time.sleep(1)
    print('done sleeping')

do_somehting()
do_somehting()

finish = time.perf_counter()

print(f'Finished in {round(finish-start,2)} second(s)')



