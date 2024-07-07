def perform_operation(num1, num2, operation):
    if operation == "add":
        return num1 + num2
    if operation == "subtract":
        return num1 - num2
    if operation == "divide":
        try:
            
            return num1 / num2
        except ZeroDivisionError as e:
            return e
    
    if operation == "multiply":
        return num1 * num2
    
        














    # match operation:
    #     case "add":
    #         return num1 + num2
    #     case "subtract":
    #         return num1 - num2
    #     case "divide":
    #         return num1 / num2
    #     case "multiply":
    #         return num1 * num2
        