# Exercise 5-4
import sys

limit = int(sys.argv[1]) if len(sys.argv) > 1 else 100

not_prime = {1,}

print(1)

for num in range(2, limit + 1):
    if num not in not_prime:
        print(num)
        for i in range(num, limit + 1, num): not_prime.add(i)
