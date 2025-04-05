
import threading
import time
import math
import sys

sys.set_int_max_str_digits(100000000000)# fib and fac were too large 



def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

results= {"prime": 0,
            "fibonacci": 0,
            "factorial": 0}


lock=threading.Lock() #thread safety

def get_highest_prime():
    start_time=time.time()
    num=0
    highest=0
    while time.time()-start_time<5:
        if is_prime(num):
            highest=num
        num+=1
    with lock:
        results["prime"]=highest
    print(f"highest prime found :{highest}", flush=True)

def fibonacci():
    while results["prime"]==0:
        time.sleep(0.1)
    n=results["prime"]
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    results["fibonacci"] = a
    print(f"Fibonacci({n}) = {str(a)[:100]}... (total {len(str(a))} digits)", flush=True)


def factorial(n):
    return math.factorial(n)

def run_factorial():
    while results["prime"] == 0:
        time.sleep(0.1)

    n = results["prime"]
    try:
        result = factorial(n) 
        results["factorial"] = result
        print(f"Factorial({n}) = {str(result)[:100]}... (total {len(str(result))} digits)", flush=True)
    except OverflowError:
        results["factorial"]="overflow"

    
        

if __name__ == '__main__':
    t=threading.Thread(target=get_highest_prime)
    tfib=threading.Thread(target=fibonacci)
    tfact=threading.Thread(target=run_factorial)
    t.start()
    tfib.start()
    tfact.start()
    t.join()
    tfib.join()
    tfact.join()

    print(results["prime"])
    print(results["fibonacci"])
    print(results["factorial"])
    

   