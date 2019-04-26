# A recursive fibonacci number generator

def fibo(n: int) -> int:
    # base case
    if n < 2: 
        return n
    return fibo(n-2) + fibo(n-1)

if __name__ == "__main__":
    num = int(input("num: "))
    print(fibo(num))