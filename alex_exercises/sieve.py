# Exercise 5-4
import sys

limit = int(sys.argv[1]) if len(sys.argv) > 1 else 100

is_prime = [True] * limit

print(1)

for num in range(2, limit + 1):
    if is_prime[num - 1]:
        print(num)
        for i in range(num + 1, limit + 1):
            if i % num == 0:
                is_prime[i - 1] = False
