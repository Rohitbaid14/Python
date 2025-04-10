import pdb  # Import Python Debugger

def buggy_function():
    a = 10
    b = 0# Intentional error: Division by zero
    pdb.set_trace()  # Set a breakpoint
    result = a / b  # This line will cause an error
    print("Result:", result)
buggy_function()
