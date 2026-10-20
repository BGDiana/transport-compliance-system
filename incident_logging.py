
import csv
from datetime import datetime
from drivers import licence_exists

def record_incident():
    print("\n--- RECORD NEW INCIDENT ---")

    licence = input("Driver's licence number: ").strip().upper()

    if not licence_exists(licence):
        print("Error: Driver not registered.")
        return

    registration = input("Vehicle registration: ").strip().upper()

    if not registration:
        print("Error: Vehicle registration cannot be empty.")
        return

    date_input = input("Incident date (DD/MM/YYYY): ").strip()

    try:
        incident_date = datetime.strptime(
            date_input, "%d/%m/%Y"
        ).strftime("%Y-%m-%d")
    except ValueError:
        print("Error: Invalid incident date.")
        return

    description = input("Describe the incident: ").strip()

    if not description:
        print("Error: Incident description cannot be empty.")
        return

    incident_id = 1

    try:
        with open("incidents.csv", "r", newline="") as file:
            reader = csv.reader(file)

            for record in reader:
                if len(record) == 6:
                    try:
                        incident_id = max(
                            incident_id, int(record[0]) + 1
                        )
                    except ValueError:
                        continue

    except FileNotFoundError:
        pass

    with open("incidents.csv", "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([
            incident_id,
            incident_date,
            registration,
            licence,
            description,
            "Open"
        ])

    print(f"Incident {incident_id} recorded successfully.")

def view_all_incidents():
    print("\n--- ALL RECORDED INCIDENTS ---")

    try:
        with open("incidents.csv", "r", newline="") as file:
            reader = csv.reader(file)
            incidents_found = False

            for record in reader:
                if len(record) != 6:
                    continue

                incident_id, date, registration, licence, description, status = record

                print("\n-----------------------------")
                print(f"Incident ID: {incident_id}")
                print(f"Date: {date}")
                print(f"Vehicle: {registration}")
                print(f"Driver Licence: {licence}")
                print(f"Description: {description}")
                print(f"Status: {status}")

                incidents_found = True

            if not incidents_found:
                print("No incidents recorded.")

    except FileNotFoundError:
        print("No incidents recorded.")

def view_open_incidents():
    print("\n--- OPEN INCIDENTS ---")

    try:
        with open("incidents.csv", "r", newline="") as file:
            reader = csv.reader(file)
            open_incidents_found = False

            for record in reader:
                if len(record) != 6:
                    continue

                incident_id, date, registration, licence, description, status = record

                if status.strip().lower() == "open":
                    print("\n-----------------------------")
                    print(f"Incident ID: {incident_id}")
                    print(f"Date: {date}")
                    print(f"Vehicle: {registration}")
                    print(f"Driver Licence: {licence}")
                    print(f"Description: {description}")
                    print(f"Status: {status}")

                    open_incidents_found = True

            if not open_incidents_found:
                print("No open incidents found.")

    except FileNotFoundError:
        print("No incidents recorded.")

def close_incident():
    print("\n--- CLOSE INCIDENT ---")

    incident_id = input("Enter incident ID to close: ").strip()

    if not incident_id.isdigit():
        print("Error: Enter a valid incident ID.")
        return

    try:
        with open("incidents.csv", "r", newline="") as file:
            reader = csv.reader(file)
            records = list(reader)

    except FileNotFoundError:
        print("No incidents recorded.")
        return

    incident_found = False

    for record in records:
        if len(record) != 6:
            continue

        if record[0] == incident_id:
            incident_found = True

            if record[5].strip().lower() == "closed":
                print("This incident is already closed.")
                return

            print(f"\nIncident: {record[4]}")
            confirmation = input(
                "Confirm this incident has been resolved? (yes/no): "
            ).strip().lower()

            if confirmation != "yes":
                print("Incident closure cancelled.")
                return

            record[5] = "Closed"
            break

    if not incident_found:
        print("Error: Incident ID not found.")
        return

    with open("incidents.csv", "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerows(records)

    print(f"Incident {incident_id} closed successfully.")

def incident_logging_management():
    while True:
        print("\n--- INCIDENT LOGGING ---")
        print("1. Record New Incident")
        print("2. View All Incidents")
        print("3. View Open Incidents")
        print("4. Close Incident")
        print("5. Return to Main Menu")

        choice = input("\nEnter your choice (1-5): ").strip()

        if choice == "1":
            record_incident()

        elif choice == "2":
            view_all_incidents()

        elif choice == "3":
            view_open_incidents()

        elif choice == "4":
            close_incident()    

        elif choice == "5":
            break

        else:
            print("Invalid choice. Please enter 1-5.")
