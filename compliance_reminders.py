
import csv
from datetime import datetime, date

def add_compliance_reminder():
    print("\n--- ADD COMPLIANCE REMINDER ---")

    print("1. Vehicle MOT")
    print("2. Vehicle Insurance")
    print("3. Vehicle Maintenance")
    print("4. Driver Licence")

    choice = input("Select reminder type (1-4): ").strip()

    reminder_types = {
        "1": "Vehicle MOT",
        "2": "Vehicle Insurance",
        "3": "Vehicle Maintenance",
        "4": "Driver Licence"
    }

    if choice not in reminder_types:
        print("Error: Invalid reminder type.")
        return

    reminder_type = reminder_types[choice]

    reference = input(
        "Enter vehicle registration or driver licence number: "
    ).strip().upper()

    if not reference:
        print("Error: Reference cannot be empty.")
        return

    date_input = input("Enter due date (DD/MM/YYYY): ").strip()

    try:
        due_date = datetime.strptime(
            date_input, "%d/%m/%Y"
        ).strftime("%Y-%m-%d")
    except ValueError:
        print("Error: Invalid date.")
        return

    with open("compliance_reminders.csv", "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([
            reminder_type,
            reference,
            due_date
        ])

    print("Compliance reminder saved successfully.")

def view_compliance_reminders():
    print("\n--- ALL COMPLIANCE REMINDERS ---")

    try:
        with open("compliance_reminders.csv", "r", newline="") as file:
            reader = csv.reader(file)
            records_found = False

            for record in reader:
                if len(record) != 3:
                    continue

                reminder_type, reference, due_date = record

                print("\n-----------------------------")
                print(f"Reminder Type: {reminder_type}")
                print(f"Vehicle / Driver: {reference}")
                print(f"Due Date: {due_date}")

                records_found = True

            if not records_found:
                print("No compliance reminders found.")

    except FileNotFoundError:
        print("No compliance reminders found.")

def check_upcoming_reminders():
    print("\n--- UPCOMING AND OVERDUE REMINDERS ---")

    today = date.today()
    reminders_found = False

    try:
        with open("compliance_reminders.csv", "r", newline="") as file:
            reader = csv.reader(file)

            for record in reader:
                if len(record) != 3:
                    continue

                reminder_type, reference, due_date = record

                try:
                    deadline = datetime.strptime(
                        due_date, "%Y-%m-%d"
                    ).date()
                except ValueError:
                    print("Warning: Invalid reminder date skipped.")
                    continue

                days_remaining = (deadline - today).days

                if days_remaining < 0:
                    status = "OVERDUE"

                elif days_remaining == 0:
                    status = "DUE TODAY"

                elif days_remaining <= 30:
                    status = "UPCOMING"

                else:
                    continue

                print("\n-----------------------------")
                print(f"Reminder Type: {reminder_type}")
                print(f"Vehicle / Driver: {reference}")
                print(f"Due Date: {due_date}")
                print(f"Days Remaining: {days_remaining}")
                print(f"Status: {status}")

                reminders_found = True

        if not reminders_found:
            print("No upcoming or overdue reminders found.")

    except FileNotFoundError:
        print("No compliance reminders found.")

def compliance_reminders_management():
    while True:
        print("\n--- COMPLIANCE REMINDERS ---")
        print("1. Add Compliance Reminder")
        print("2. View All Reminders")
        print("3. View Upcoming and Overdue Reminders")
        print("4. Return to Main Menu")

        choice = input("\nEnter your choice (1-4): ").strip()

        if choice == "1":
            add_compliance_reminder()

        elif choice == "2":
            view_compliance_reminders()

        elif choice == "3":
            check_upcoming_reminders()

            

        elif choice == "4":
            break

        else:
            print("Invalid choice. Please enter 1-4.")


