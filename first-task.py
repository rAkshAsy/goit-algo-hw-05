from typing import Callable

def caching_fibonacci() -> Callable[[int], int]:

    cache_dict = {}

    def fibonacci(n:int) -> int:
        if n <= 0:
            return 0
        if n == 1:
            return 1
        if n in cache_dict:
            return cache_dict[n]
        
        cache_dict[n] = fibonacci(n-1) + fibonacci(n-2)

        return cache_dict[n]
    
    return fibonacci


fib = caching_fibonacci()

print(fib(10))
print(fib(5))
print(fib(-1))
print(fib(11))

