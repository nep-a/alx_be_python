def perform_operation(num1,num2,operation):
    if operation == "add":
        num1 + num2
    elif operation == "Divide":
        num1 / num2
    elif operation == "multiply":
        num1 * num2
    elif operation == "substract":
        num1 - num2
    else:
        return "Error on operator"