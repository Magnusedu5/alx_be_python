def safe_divide(numerator, denominator):
    try:
        a = float(numerator)
        b = float(denominator)

        result = a / b
        return result
    
    except ZeroDivisionError:
        print(f"Cannot divide by zero")
        
    except ValueError:
        print(f"Invalid Value")
