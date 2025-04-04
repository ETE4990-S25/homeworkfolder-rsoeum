import asyncio
import time
import math
import sys

sys.set_int_max_str_digits(1000000000)# fib and fac were too large 

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

results= {"prime": 0,
            "fibonacci": 0,
            "factorial": 0}

async def get_highest_prime():
    start_time=time.time()
    num=0
    highest=0
    while time.time()-start_time<180: #looks for prime for 3 minutes
        if is_prime(num):
            highest=num
        num+=1
        if num% 1000==0:
            await asyncio.sleep(0.1)
    results["prime"]=highest
    print(f"highest prime: {highest}")




async def factorial(n):
    result=math.factorial(n)
    results["factorial"]=result
    print(f"Factorial({n}): {str(result)[:100]}... (total {len(str(result))} digits)", flush=True)



async def fibonacci(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    result=b
    results["fibonacci"]=result
    print(f"Fibonacci({n}): {str(result)[:100]}... (total {len(str(result))} digits)", flush=True)


async def main():
    await get_highest_prime()
    prime=results["prime"]
    await asyncio.gather(
        fibonacci(prime),
        factorial(prime)
    )
    print("highest prime:", results["prime"])
    print("fibonacci:" ,results["fibonacci"])
    print("factorial:" ,results["factorial"])

if __name__ == "__main__":
    await main()




    #laptop was about to explode lol