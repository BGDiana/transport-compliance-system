
import csv



def add_driver():
    print("\n--- ADD NEW DRIVER ---")

    name = input("Enter driver's full name: ")
    licence = input("Enter driving licence number: ")
    phone = input("Enter phone number: ")

    with open("drivers.csv", "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([name, licence, phone])

    print("\nDriver saved successfully!")
    print("Name:", name)
    print("Licence:", licence)
    print("Phone:", phone)


def view_drivers():
    print("\n--- REGISTERED DRIVERS ---")

    try:
        with open("drivers.csv", "r", newline="") as file:
            reader = csv.reader(file)

            drivers = list(reader)

            if not drivers:
                print("No drivers registered yet.")
                return

            for number, driver in enumerate(drivers, start=1):
                if len(driver) != 3:
                    print("Skipping an invalid driver record.")
                    continue

                print(f"\nDriver {number}")
                print("Name:", driver[0])
                print("Licence:", driver[1])
                print("Phone:", driver[2])

    except FileNotFoundError:
        print("No drivers registered yet.")


def driver_management():
    while True:
        print("\n--- DRIVER MANAGEMENT ---")
        print("1. Add New Driver")
        print("2. View All Drivers")
        print("3. Return to Main Menu")

        choice = input("\nEnter your choice (1-3): ")

        if choice == "1":
            add_driver()

        elif choice == "2":
            view_drivers()

        elif choice == "3":
            break

        else:
            print("Invalid choice. Please enter 1-3.")


def main():
    while True:
        print("\n================================")
        print("   TRANSPORT COMPLIANCE SYSTEM")
        print("================================")
        print("1. Driver Management")
        print("2. Driving Hours")
        print("3. Vehicle Checks")
        print("4. Incident Logging")
        print("5. Compliance Reminders")
        print("6. Exit")

        choice = input("\nEnter your choice (1-6): ")

        if choice == "1":
            driver_management()

        elif choice == "2":
            print("Driving Hours selected")

        elif choice == "3":
            print("Vehicle Checks selected")

        elif choice == "4":
            print("Incident Logging selected")

        elif choice == "5":
            print("Compliance Reminders selected")

        elif choice == "6":
            print("Exiting the application. Goodbye!")
            break

        else:
            print("Invalid choice. Please enter 1-6.")


main()

