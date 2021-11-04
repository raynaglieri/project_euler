# problem 1:
# If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
# Find the sum of all the multiples of 3 or 5 below 1000.

# TODO: 1. scale for non-primes
#       2. len(seeds) > 2

from math import floor

MULTIPLE_MAX = 1000

SEEDS = [3, 5]


def sol():

    # Get bound for sum
    def sum_bound(n):
        bound = floor((MULTIPLE_MAX - 1) / n)
        return bound

    # closed sum form for for first n numbers
    def sum_n(n):
        return ((n) * (n + 1)) / 2

    total = 0
    common_multiple = 1

    # Get total sum for all seeds
    for seed in SEEDS:
        # since seed is a shared divisor we can remove it from the sum
        common_multiple *= seed
        total += seed * sum_n(sum_bound(seed))

    # we dont want duplicates
    # i.e 3: 3 * 5 or 5: 5 * 3
    # if we are prime there are no shared multiples less than p1 * p2
    # so we want to calculate the multiples of p1 * p2 less than multiple max
    # for non-prime we need to remove shared multiples n1 <= duplicates <= n2
    duplicates = common_multiple * sum_n(sum_bound(common_multiple))
    sol = int(total - duplicates)

    print(sol)


sol()
