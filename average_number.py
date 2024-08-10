scores = [22.4, 56.9, 98.7, 45.6, 78.8, 67.74]

# Average = sum/number

# Simple way
print(sum(scores) / len(scores))

# Other Way!
accumulator = 0

for number in (scores):
    accumulator = accumulator + number

print(accumulator / len(scores))