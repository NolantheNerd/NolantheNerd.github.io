import math
import bisect

def better_prime_gen(cap):
    primes = [2,3,5,7,11]
    for candidate in range(5, cap, 2):
        for poss_factor in primes[:bisect.bisect(primes, math.sqrt(candidate))]:
            if candidate%poss_factor == 0:
                continue
            primes.append(candidate)
    return sum(primes)

print(better_prime_gen(2000000))