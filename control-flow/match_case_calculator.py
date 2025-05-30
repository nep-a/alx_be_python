#asks the user to enter a number
number1 = int(input("Enter first number: "))
number2 = int(input("Enter second number: "))
#choosing an operator
operator = input("Choose an operator '- + / *': ")
#perfoming calculations
match operator:
    case '-':
        if operator == '-':
            result = number1 - number2
        print("The result is ", result)
    case '+':
        if operator == '+':
            result = number1 + number2
        print("The result is ", result)
    case '*':
        if operator == '*':
            result = number1 * number2
        print("The result is ", result)
    case '/':
        if operator == '/':
            result = number1 / number2
        print("The result is ", result)