import hashlib
import threading
from itertools import *
import time
start_time = time.time()
check = list(product('abcdefghijklmnopqrstuvwxyz', repeat=5))

def solve(check, start, end):
    for i in check[start:end]:
        encode = hashlib.sha256(''.join(i).encode('utf-8')).hexdigest()
        if encode == '1115dd800feaacefdf481f1f9070374a2a81e27880f187396db67958b207cbad' \
        or encode == '3a7bd3e2360a3d29eea436fcfb7e44c735d117c42d1c1835420b6b9942dd4f1b' \
        or encode == '74e1bb62f8dabb8125a58852b63bdf6eaef667cb56ac7f7cdba6d7305c50a22f'    :
            print(''.join(i))

def split_solve(check, number_of_threads):
    split_size = len(check) / number_of_threads
    threads = []
    for i in range(number_of_threads):
        start = int(i * split_size)
        end = None if i+1 == number_of_threads else int((i+1) * split_size )
        threads.append(threading.Thread(target=solve, args=(check, start, end)))
        threads[-1].start()
    for t in threads:
        t.join()
print("Введите количество потоков: ")
c = int(input())
split_solve(check, c)
print("--- %s seconds ---" % (time.time() - start_time))
