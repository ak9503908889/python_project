import math

# Function to calculate permutations
def permutations(n, k):
    return math.factorial(n) // math.factorial(n - k)

# Function to calculate combinations
def combinations(n, k):
    return math.factorial(n) // (math.factorial(k) * math.factorial(n - k))

# Input values
n = int(input("Enter the total number of objects (n): "))
k = int(input("Enter the number of objects to select (k): "))

# Calculate and print permutations and combinations
if n >= k >= 0:
    perm = permutations(n, k)
    comb = combinations(n, k)
    print(f"Permutations: {perm}")
    print(f"Combinations: {comb}")
else:
    print("Invalid input. Ensure n >= k >= 0.")