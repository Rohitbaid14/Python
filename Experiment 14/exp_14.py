def safe_division():
    try:
        num1 = float(input("Enter 1st number: "))
        num2 = float(input("Enter 2nd number: "))
        
        result = num1/num2
        print("Result: ",result)
        
    except ZeroDivisionError:
        print("Error:Number cannot be divided by zero")
    
    except ValueError:
        print("Error:Invalid input.Please enter numeric values.")
        
    except Exception as e:
        print("An unexpected error occurred:",e)
    
    finally:
        print("Execution completed.")
        
safe_division()