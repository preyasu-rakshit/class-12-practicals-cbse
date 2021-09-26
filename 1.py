#Write a Python Program Using Function to find the factorial of a number.

def factorial(n):
    if n == 1:
        return n
    elif n < 1:
        return "Invalid input, please enter natural numbers only."
    else:
        return n*factorial(n - 1)

print(factorial(3))
#Output : 6
print(factorial(4))
#Output : 24