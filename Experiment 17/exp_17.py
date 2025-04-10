import re  # Importing regex module

# Function to extract data from text
def extract_data(filename):
    with open(filename, 'r') as file:  # Open file in read mode
        text = file.read()  # Read the entire file content

    # Regular expressions for different data types
    email_pattern = r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}"  # Email pattern
    phone_pattern = r"\b\d{10}\b"  # 10-digit phone number pattern
    date_pattern = r"\b\d{2}/\d{2}/\d{4}\b"  # Date format MM/DD/YYYY

    # Extracting data using regex
    emails = re.findall(email_pattern, text)
    phones = re.findall(phone_pattern, text)
    dates = re.findall(date_pattern, text)

    # Printing extracted data
    print("Extracted Emails:", emails)
    print("Extracted Phone Numbers:", phones)
    print("Extracted Dates:", dates)

# Call function with file name
extract_data("data.txt")  # Ensure you have a 'data.txt' file with sample data
