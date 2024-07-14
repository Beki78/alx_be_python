def safe_divide(numerator, denominator):
    try:
        float(numerator / denominator)
    except ZeroDivisionError as e:
        print(e)
    except TypeError as e:
        print("Please enter numeric values only")
    else:
        return print(numerator / denominator)
    
safe_divide(1.23, 0)
