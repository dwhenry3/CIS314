import random

numbers = [random.randint(1,16) for _ in range(100)]
numbers.sort()

#Method 1
counter = {}
for number in numbers:
    if number in counter:
        counter[number] += 1
    else:
        counter[number] = 1

print(counter)

from collections import Counter
#Method 2
print(Counter(numbers).keys())
print(Counter(numbers).values())

#Method 3
counts = Counter(numbers)
for number, count in sorted(counter.items()):
    print(f"Number {number}: {count} times")