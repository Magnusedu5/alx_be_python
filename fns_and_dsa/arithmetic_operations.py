def perform_operation(num1, num2, operation):
    if operation == 'add':
        return num1 + num2
    elif operation == 'subtract':
        return num1 - num2
    elif operation == 'multiply':
        return num1 * num2
    elif operation == 'divide':
        if num2 == 0:
            return "Can't perform this operation"
        else:
            return num1 / num2
    else:
        print("Error")

perform_operation(10, 0, 'divide')