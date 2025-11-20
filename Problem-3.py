a = int(input("Enter a number: "))
if a % 2 == 0:
    count = a - 1
else:
    count = a
result = []
value = 1
for i in range(count):
    result.append(value)
    value += 2
print(result)


