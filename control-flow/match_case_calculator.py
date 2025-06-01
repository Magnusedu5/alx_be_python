num1 = float(input("Enter the first number:"))
num2 = float(input("Enter the second number:"))
arith_op = input("Choose the operation (+, -, *, /):")

match arith_op:
    case '+':
        result = num1 + num2
        print('The result is', result)
    case '-':
        result = num1 - num2
        print('The result is', result)
    case '*':
        result = num1 * num2
        print('The result is', result)
    case '/':
        if num2 == 0:
            print("Error, number cannot be divided by 0")
        else:
            result = num1 / num2
            print('The result is', result)
        