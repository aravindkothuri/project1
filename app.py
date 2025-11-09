def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

num = 5
print(f"The factorial of {num} is: {factorial(num)}")

code-2
number = int(input("Enter a number: "))
if number % 2 == 0:
    print(f"{number} is an even number.")
else:
    print(f"{number} is an odd number.")
