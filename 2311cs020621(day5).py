n = int(input("Enter a positive integer: "))
print("Using for loop:")
for i in range(1, n + 1):
    print(i)
sum_numbers = 0
i = 1
while i <= n:
    sum_numbers += i
    i += 1
print(f"The sum of numbers from 1 to {n} is: {sum_numbers}")
