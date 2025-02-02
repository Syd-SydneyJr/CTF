import itertools

# Generate all combinations of 5-digit numbers
combinations = list(itertools.product(range(10), repeat=5))

# Convert each combination to a string and write to file
with open('combinations.txt', 'w') as f:
    for c in combinations:
        number = ''.join(map(str, c))
        f.write(number + '\n')

