from datetime import datetime, timedelta



def display_current_datetime():
    current_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print  (f"Current date and time:{current_date}")

display_current_datetime()


def calculate_future_date():
        user = int(input("Enter a date: "))
        future_date = timedelta(days=user).strftime("%Y-%m-%d %H:%M:%S")
        print(future_date)
calculate_future_date()