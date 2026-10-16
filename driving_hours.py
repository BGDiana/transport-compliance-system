
import csv
from datetime import datetime
from drivers import licence_exists


def record_driving_hours():
    print("\n--- RECORD DRIVING HOURS ---")

    
    while True:
        licence = input("Enter driver's licence number: ").strip().upper()

        if not licence:
          print("Error: Licence number cannot be empty.")

        elif not licence_exists(licence):
          print("Error: Driver not registered.")
          print("Please register the driver in Driver Management first.")

        else:
          break


    while True:
        date = input("Enter driving date (DD/MM/YYYY): ").strip()

        try:
            valid_date = datetime.strptime(date, "%d/%m/%Y")
            date = valid_date.strftime("%Y-%m-%d")
            break
        except ValueError:
            print("Error: Enter a valid date (DD/MM/YYYY).")

    while True:
        hours = input("Enter driving hours: ").strip()

        try:
            hours = float(hours)

            if hours <= 0 or hours > 24:
                print("Error: Hours must be between 0 and 24.")
            else:
                break

        except ValueError:
            print("Error: Please enter a valid number.")

    with open("driving_hours.csv", "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([licence, date, hours])

    print("\nDriving hours recorded successfully!")

def view_driving_hours():
    print("\n--- DRIVING HOURS RECORDS ---")

    try:
        with open("driving_hours.csv", "r", newline="") as file:
            reader = csv.reader(file)
            records = list(reader)

            if not records:
                print("No driving hours recorded yet.")
                return

            for number, record in enumerate(records, start=1):
                if len(record) != 3:
                    print("Skipping an invalid record.")
                    continue

                print(f"\nRecord {number}")
                print("Driver Licence:", record[0])
                print("Date:", record[1])
                print("Driving Hours:", record[2])

    except FileNotFoundError:
        print("No driving hours recorded yet.")

def check_compliance():
    print("\n--- DRIVING HOURS COMPLIANCE CHECK ---")

    licence = input("Enter driver's licence number: ").strip().upper()

    if not licence_exists(licence):
        print("Error: Driver not registered.")
        return

    daily_totals = {}

    try:
        with open("driving_hours.csv", "r", newline="") as file:
            reader = csv.reader(file)

            for record in reader:
                if len(record) != 3:
                    continue

                record_licence, date, hours = record

                if record_licence.strip().upper() == licence:
                    try:
                        hours = float(hours)
                    except ValueError:
                        print("Warning: Invalid hours record skipped.")
                        continue

                    if not 0 < hours <= 24:
                        print("Warning: Invalid hours record skipped.")
                        continue

                    daily_totals[date] = daily_totals.get(date, 0) + hours

    except FileNotFoundError:
        print("No driving records found.")
        return

    if not daily_totals:
        print("No driving records found for this driver.")
        return

    for date, total in sorted(daily_totals.items()):
        print(f"\nDate: {date}")
        print(f"Total driving hours: {total:.2f}")

        if total > 10:
            print("WARNING: Exceeds the 10-hour daily driving limit.")

        elif total > 9:
            print("REVIEW: Daily driving extension required.")

        else:
            print("Within the normal 9-hour daily driving limit.")

def driving_hours_management():
    while True:
        print("\n--- DRIVING HOURS MANAGEMENT ---")
        print("1. Record Driving Hours")
        print("2. View Driving Hours")
        print("3. Check Compliance")
        print("4. Return to Main Menu")

        choice = input("\nEnter your choice (1-4): ")

        if choice == "1":
            record_driving_hours()


        elif choice == "2":
            view_driving_hours()

        elif choice == "3":
            check_compliance()

        elif choice == "4":
            break

        else:
            print("Invalid choice. Please enter 1-4.")
