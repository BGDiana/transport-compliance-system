
import csv
from datetime import datetime
from drivers import licence_exists

def record_vehicle_check():
    print("\n--- RECORD VEHICLE CHECK ---")

    registration = input("Vehicle registration: ").strip().upper()

    if not registration:
        print("Error: Vehicle registration cannot be empty.")
        return

    licence = input("Driver's licence number: ").strip().upper()

    if not licence_exists(licence):
        print("Error: Driver not registered.")
        return

    date_input = input("Inspection date (DD/MM/YYYY): ").strip()

    try:
        inspection_date = datetime.strptime(
            date_input, "%d/%m/%Y"
        ).strftime("%Y-%m-%d")
    except ValueError:
        print("Error: Invalid date.")
        return

    print("\nInspection result:")
    print("1. No defects reported")
    print("2. Defect reported")

    result = input("Choose 1 or 2: ").strip()

    if result == "1":
        status = "No defects reported"
        description = "None"

    elif result == "2":
        status = "Defect reported"
        description = input("Describe the defect: ").strip()

        if not description:
            print("Error: Defect description is required.")
            return

    else:
        print("Error: Invalid inspection result.")
        return

    with open("vehicle_checks.csv", "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([
            registration,
            licence,
            inspection_date,
            status,
            description
        ])

    print("Vehicle check recorded successfully.")
    
def view_vehicle_checks():
    print("\n--- VEHICLE CHECK RECORDS ---")

    try:
        with open("vehicle_checks.csv", "r", newline="") as file:
            reader = csv.reader(file)

            records_found = False

            for record in reader:
                if len(record) != 5:
                    continue

                registration, licence, date, status, description = record

                print("\n-----------------------------")
                print(f"Vehicle: {registration}")
                print(f"Driver Licence: {licence}")
                print(f"Inspection Date: {date}")
                print(f"Result: {status}")
                print(f"Defect Details: {description}")

                records_found = True

            if not records_found:
                print("No vehicle checks recorded.")

    except FileNotFoundError:
        print("No vehicle checks recorded.")
        
def view_reported_defects():
    print("\n--- REPORTED VEHICLE DEFECTS ---")

    try:
        with open("vehicle_checks.csv", "r", newline="") as file:
            reader = csv.reader(file)

            defects_found = False

            for record in reader:
                if len(record) != 5:
                    continue

                registration, licence, date, status, description = record

                if status == "Defect reported":
                    print("\n-----------------------------")
                    print(f"Vehicle: {registration}")
                    print(f"Driver Licence: {licence}")
                    print(f"Inspection Date: {date}")
                    print(f"Defect: {description}")

                    defects_found = True

            if not defects_found:
                print("No reported defects found.")

    except FileNotFoundError:
        print("No vehicle checks recorded.")



def vehicle_checks_management():
    while True:
        print("\n--- VEHICLE CHECKS MANAGEMENT ---")
        print("1. Record Vehicle Check")
        print("2. View Vehicle Checks")
        print("3. View Reported Defects")
        print("4. Return to Main Menu")

        choice = input("\nEnter your choice (1-4): ")

        if choice == "1":
            record_vehicle_check()

        elif choice == "2":
            view_vehicle_checks()

        elif choice == "3":
            view_reported_defects()

        elif choice == "4":
            break

        else:
            print("Invalid choice. Please enter 1-4.")
