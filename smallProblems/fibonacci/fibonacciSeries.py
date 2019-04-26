def fibo_series(n: int):
    # special case
    yield 0
    if n > 0:
        yield 1
    # initial values
    last: int = 0
    next: int = 1

    for _ in range(1,n):
        last, next = next, last + next
        yield next # generation step

if __name__ == "__main__":
    for i in fibo_series(50):
        print(i)
