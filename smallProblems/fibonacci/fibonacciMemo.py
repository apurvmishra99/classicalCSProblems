# Adding memoization to fibonacci series calculator
# base cases
memo : dict = {0: 0, 1: 1}
def fibo_memo(n: int) -> int:
    if n not in memo:
        memo[n] =  fibo_memo(n-1) + fibo_memo(n-2)
    return memo[n]

if __name__ == "__main__":
    print(fibo_memo(5))
    print(fibo_memo(50))