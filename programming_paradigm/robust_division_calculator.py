def safe_divide(numerator, denominator):
    try:
        numur = float(numerator)
        deno = float(denominator)
        return f"The result of the division is {numur / deno}"
    except ZeroDivisionError:
        return "Error: Cannot divide by zero."
    except ValueError:
        return "Error: Please enter numeric values only."
 

