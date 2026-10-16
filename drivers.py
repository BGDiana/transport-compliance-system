
import csv
def licence_exists(licence):
    try:
        with open("drivers.csv", "r", newline="") as file:
            reader = csv.reader(file)

            for driver in reader:
                if len(driver) >= 2:
                    if driver[1].strip().upper() == licence:
                        return True

    except FileNotFoundError:
        return False

    return False


def add_driver():
    print("\n--- ADD NEW DRIVER ---")

    while True:
       name = input("Enter driver's full name: ").strip()

       if name:
           break
       else:
        print("Error: Driver name cannot be empty.")


    while True:
        licence = input("Enter driving licence number: ").strip().upper()

        if not licence:
         print("Error: Driving licence number cannot be empty.")

        elif licence_exists(licence):
         print("Error: This driving licence is already registered.")

        else:
           break

 
    while True:
        phone = input("Enter phone number: ").strip()

        if not phone:
         print("Error: Phone number cannot be empty.")

        elif not phone.isdigit():
         print("Error: Phone number must contain only digits.")

        elif len(phone) != 11:
         print("Error: Enter an 11-digit UK phone number.")

        elif not phone.startswith("0"):
         print("Error: UK national phone numbers must start with 0.")

        else:
            break


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