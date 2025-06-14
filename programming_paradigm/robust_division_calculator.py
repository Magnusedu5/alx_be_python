def safe_divide(numerator, denominator):
    try:
        a = float(numerator)
        b = float(denominator)

        result = a / b
        return f"The result of the division is {result}"
    
    except ZeroDivisionError:
        return f"Error: Cannot divide by zero."

    except ValueError:
        return f"Error: Please enter numeric values only."
