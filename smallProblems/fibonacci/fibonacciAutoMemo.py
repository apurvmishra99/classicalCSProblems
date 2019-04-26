from functools import lru_cache

@lru_cache(maxsize=None)
def fibo_auto_memo(n: int) -> int:
    if n < 2:
        return n
    return fibo_auto_memo(n-1) + fibo_auto_memo(n-2)

if __name__ == "__main__":
    print(fibo_auto_memo(5))
    print(fibo_auto_memo(75))