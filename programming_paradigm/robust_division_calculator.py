def safe_divide(numerator, denominator):
    try:
        a = float(numerator)
        b = float(denominator)

        result = a / b
        print(f"The result of the division is {result}")
    
    except ZeroDivisionError:
        print(f"Error: Cannot divide by zero.")

    except ValueError:
        print(f"Error: Please enter numeric values only.")
