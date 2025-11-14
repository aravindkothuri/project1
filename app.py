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

code-3 
num1 = 10
num2 = 25
sum_of_numbers = num1 + num2
print(f"The sum of {num1} and {num2} is: {sum_of_numbers}")
      
code-4
a = 5
b = 10
print(f"Before swapping: a = {a}, b = {b}")
a, b = b, a  # Pythonic way to swap variables
print(f"After swapping: a = {a}, b = {b}")


