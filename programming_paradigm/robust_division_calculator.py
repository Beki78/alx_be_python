def safe_divide(numerator, denominator):
    try:
        numur = float(numerator)
        deno = float(denominator)
        return print(numur / deno)
    except ZeroDivisionError as e:
        print("Error: Cannot divide by zero.")
    except ValueError as e:
        print("Error: Please enter numeric values only.")
 
        
    
safe_divide(1.23, 3)
