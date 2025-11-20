a = int(input("Enter a number: "))

# If even, reduce by 1 to nearest odd
if a % 2 == 0:
    limit = a - 1
else:
    limit = a

result = []

# Generate odd numbers 1, 3, 5, ... <= limit
for num in range(1, limit + 1, 2):
    result.append(num)

print(result)

