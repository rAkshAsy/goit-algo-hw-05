from typing import Callable

def caching_fibonacci() -> Callable[[int], int]:

    cache_dict = {}

    def fibonacci(n: int) -> int:
        if n <= 0:
            return 0
        if n == 1:
            return 1
        if n in cache_dict:     # Checking for the presence of a value in the cache
            return cache_dict[n]
        
        # Adding a new key-value to the cache dictionary
        cache_dict[n] = fibonacci(n-1) + fibonacci(n-2)
        return cache_dict[n]
    
    return fibonacci



test_cases = [10, 5, -1, 11, 20, 15]

fib = caching_fibonacci()

for num in test_cases:
    print(fib(num))

