
import csv


from drivers import driver_management
from driving_hours import driving_hours_management

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
            driving_hours_management()

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