# Each new term in the Fibonacci sequence is generated by adding the previous two terms. By starting with 1 and 2, the first 10 terms will be:
# 1, 2, 3, 5, 8, 13, 21, 34, 55, 89,
# By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms.

# Solve for fibs: if div by two-> add to sum

# 1, (2), 3, 5, (8), 13, 21, (34), 55, 89, (144) 233, 377, (610)
# We notice that for every two odd Fibonacci numbers, there is one even.
# This makes sense since 2k + 2k is always even and (2k + 1) + (2k + 1) is also even
# How can we leverage this?
# f(n) = f(n-1) + f(n-2)
# So then then from an even indexed value the sol is n + F(n-3)
# Without knowing what nth fibonacci number is bounded above by four million
# we need to calculate each fibonacci bounded by an even n until we reach four million

from functools import lru_cache

FIB_VAL_MAX = 4000000


def sol():

    # recursive Fibonacci with memoization
    @lru_cache(maxsize=128)
    def fib(n):

        if n < 2:
            return n

        return fib(n - 1) + fib(n - 2)

    def get_even_fib_sum():

        even_fib_sum = 0

        # First even fib
        # fib(3) == 2
        even_fib = 0
        result = 0

        while result < FIB_VAL_MAX:

            result = fib(even_fib)
            even_fib_sum += result
            even_fib += 3

        # Check for overflow
        if even_fib_sum >= FIB_VAL_MAX:
            even_fib_sum -= result

        return even_fib_sum

    return get_even_fib_sum()


print(sol())
