task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ").lower()
time_bound = input("Is it time-bound? (yes/no): ").lower()

match priority:
    case "high":
        if time_bound == 'yes':
            print(f"Reminder: '{task}' is a high priority task that requires immediate attention today!")
        elif time_bound == 'no':
            print(f"Reminder: '{task}' is a high priority task. Complete as soon as you can.")
        else:
            print(f"Invalid Response") 
    case "medium":
        if time_bound == 'yes':
            print(f"Reminder: '{task}' has a deadline. Complete it before the deadline.")
        elif time_bound == 'no':
            print(f"Reminder: '{task}' has no deadline but is quite impertant. Complete as soon as you can.")
        else:
            print(f"Invalid Response") 
    case "low":
        if time_bound == 'yes':
            print(f"Reminder: '{task}' is a low priority task but has a deadline. Complete before the deadline.")
        elif time_bound == 'no':
            print(f"Reminder: '{task}' is a low priority task. Consider completing it when you have free time.")
        else:
            print(f"Invalid Response") 
