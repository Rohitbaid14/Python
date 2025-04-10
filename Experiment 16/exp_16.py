import re  # Importing the regular expressions module
 # Function to validate phone number
def validate_phone(phone):
    pattern = r"^\d{10}$"  # Regular expression: exactly 10 digits
    if re.match(pattern, phone):  # Check if the phone number matches the pattern
        return True
    else:
        return False
 # Function to validate email ID
def validate_email(email):
    pattern = r"^[a-zA-Z0-9_.]+@[a-zA-Z]+\.[a-zA-Z]{2,}$"  # Simple email regex
    if re.match(pattern, email):  # Check if the email matches the pattern
        return True
    else:
        return False
 # Taking user input
phone = input("Enter your phone number: ")
email = input("Enter your email ID: ")
 # Validating inputs
if validate_phone(phone):
    print("Phone number is valid.")
else:
    print("Invalid phone number. Please enter a 10-digit number.")
if validate_email(email):
    print("Email ID is valid.")
else:
    print("Invalid email ID. Please enter a correct format (e.g., example@mail.com).")
