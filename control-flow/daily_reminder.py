task = input("Enter your task: ").lower()
priority = input("Priority (high/medium/low): ").lower()
time_bound = input("Is it time-bound? (yes/no): ").lower()

match priority:
    case "high":
        if time_bound == "yes":
            print("Reminder: 'Finish project report' is a high priority task that requires immediate attention today!")
    case "low":
        if time_bound == "no":
            print("Note: 'Read a book' is a low priority task. Consider completing it when you have free time.")
    case _:
        print("No specific action required for this priority level.")
