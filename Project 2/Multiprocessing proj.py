from multiprocessing import Process, Queue
import math
import time

#given
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def get_highest_prime():
    start_time=time.time()
    num=0
    highest=0
    while time.time()-start_time<180: #looks for prime for 3 minutes
        if is_prime(num):
            highest=num
        num+=1
    print(highest, flush=True)
    Queue.put(highest) #put the highest prime in the queue



if __name__ == '__main__':
    p=Process(target=get_highest_prime())
    p.start()
    p.join()