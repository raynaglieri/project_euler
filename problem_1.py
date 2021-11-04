#problem 1:
#If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
#Find the sum of all the multiples of 3 or 5 below 1000.

# TODO: Write function for removing duplicate multiples

from collections import defaultdict
from math import floor

MULTIPLE_MAX = 1000

SEEDS = [3, 5]

def sol():

    # Get bound for sum
    def sum_bound(n):
        return floor(MULTIPLE_MAX - 1/n)

    # closed sum form for for first n numbers
    def sum_n(n):
        return (n * (n+1) / 2)

    sum = 0

    # Get total sum for all seeds
    for seed in SEEDS:
        sum += seed * sum_n(sum_bound(seed))

    # we dont want duplicates
    # i.e 3: 3 * 5 or 5: 5 * 3

    print(int(sum))

sol()
        