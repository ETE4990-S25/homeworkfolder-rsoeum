
import threading
import time
import math



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
    print(highest)

def fibonacci():
    while results["prime"]==0:
        time.sleep(0.1)
    n=results["prime"]
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
        if b > 1e8:
            results["fibonacci"] = " fib is Too large"
            return
    results["fibonacci"] = a
    print(f"Fibonacci({n}) = {a}")

def factorial(n):
    return math.factorial(n)

def get_factorial():
    while results["prime"] == 0:
        time.sleep(0.1)

    n = results["prime"]
    try:
        result = factorial(n) 
        if result > 1e12:
            results["factorial"] = " fac is Too large"
            return
        results["factorial"] = result
        print(f"Factorial({n}) = {result}")
    except OverflowError:
        results["factorial"] = "Overflow"


    
        

if __name__ == '__main__':
    t=threading.Thread(target=get_highest_prime)
    tfib=threading.Thread(target=fibonacci)
    tfact=threading.Thread(target=get_factorial)
    t.start()
    t.join()

    tfib.start()
    tfib.join()

    tfact.start()
    tfact.join()
    print(results["prime"])
    print(results["fibonacci"])
    print(results["factorial"])
    

   