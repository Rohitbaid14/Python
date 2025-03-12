def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, num):
        if num % i == 0:
            return False
    return True

# Main program
number = int(input("Enter a number: "))

# Call the function and display result
if is_prime(number):
    print(number, "is a prime number.")
else:
    print(number, "is not a prime number.")

