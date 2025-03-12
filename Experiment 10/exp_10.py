def factorial(n):
    """
    Calculate the factorial of a given number using a for loop.
    """
    if n < 0:
        return "Factorial is not defined for negative numbers."
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

# Example usage
num = int(input("Enter a number: "))
print(f"Factorial of {num} is {factorial(num)}")