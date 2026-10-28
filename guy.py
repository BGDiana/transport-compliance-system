
import tkinter as tk
from tkinter import ttk, messagebox
import csv
from pathlib import Path
from datetime import datetime

# Application settings
APP_TITLE = "Transport Compliance System"
WINDOW_SIZE = "1100x700"

# Colours
NAVY = "#124438"
BLUE = "#12AC67"
LIGHT = "#F3F6FA"
WHITE = "#FFFFFF"
TEXT = "#042606"


class TransportComplianceGUI:
    def __init__(self, root):
        self.root = root
        self.root.title(APP_TITLE)
        self.root.geometry(WINDOW_SIZE)
        self.root.minsize(850, 550)
        self.root.configure(bg=LIGHT)

        self.create_layout()
        self.show_dashboard()

    def create_layout(self):
        # Sidebar
        self.sidebar = tk.Frame(
            self.root, bg=NAVY, width=240
        )
        self.sidebar.pack(side="left", fill="y")
        self.sidebar.pack_propagate(False)

        tk.Label(
            self.sidebar,
            text="TRANSPORT\nCOMPLIANCE",
            bg=NAVY,
            fg=WHITE,
            font=("Arial", 17, "bold"),
            justify="left"
        ).pack(padx=20, pady=(30, 35), anchor="w")

        menu_items = [
            ("Dashboard", self.show_dashboard),
            ("Driver Management", self.show_drivers),
            ("Driving Hours", self.show_hours),
            ("Vehicle Checks", self.show_vehicles),
            ("Incident Logging", self.show_incidents),
            ("Compliance Reminders", self.show_reminders),
            ("Security Guidance", self.show_security_guidance),
        ]

        for label, command in menu_items:
            tk.Button(
                self.sidebar,
                text=label,
                command=command,
                bg=NAVY,
                fg=WHITE,
                activebackground=BLUE,
                activeforeground=WHITE,
                relief="flat",
                anchor="w",
                padx=20,
                pady=12,
                font=("Arial", 11),
                cursor="hand2"
            ).pack(fill="x", padx=8, pady=2)

        tk.Button(
            self.sidebar,
            text="Exit Application",
            command=self.confirm_exit,
            bg="#B42318",
            fg=WHITE,
            relief="flat",
            padx=20,
            pady=12,
            cursor="hand2"
        ).pack(side="bottom", fill="x", padx=12, pady=25)

        # Main content area
        self.content = tk.Frame(
            self.root, bg=LIGHT
        )
        self.content.pack(
            side="right", fill="both", expand=True
        )

    def clear_content(self):
        for widget in self.content.winfo_children():
            widget.destroy()

    def page_heading(self, title, subtitle):
        tk.Label(
            self.content,
            text=title,
            bg=LIGHT,
            fg=NAVY,
            font=("Arial", 24, "bold")
        ).pack(anchor="w", padx=35, pady=(35, 8))

        tk.Label(
            self.content,
            text=subtitle,
            bg=LIGHT,
            fg=TEXT,
            font=("Arial", 11)
        ).pack(anchor="w", padx=35, pady=(0, 25))

    def create_card(self, parent, title, description, command):
        card = tk.Frame(
            parent,
            bg=WHITE,
            highlightbackground="#D9E2EC",
            highlightthickness=1
        )
        card.pack(fill="x", pady=7)

        tk.Label(
            card,
            text=title,
            bg=WHITE,
            fg=NAVY,
            font=("Arial", 14, "bold")
        ).pack(anchor="w", padx=20, pady=(15, 5))

        tk.Label(
            card,
            text=description,
            bg=WHITE,
            fg=TEXT,
            font=("Arial", 10)
        ).pack(anchor="w", padx=20)

        tk.Button(
            card,
            text="Open Module",
            command=command,
            bg=BLUE,
            fg=WHITE,
            relief="flat",
            padx=15,
            pady=8,
            cursor="hand2"
        ).pack(anchor="w", padx=20, pady=15)

    def show_dashboard(self):
        self.clear_content()
        self.page_heading(
            "Management Dashboard",
            "Select a module to manage transport compliance."
        )
        tk.Label(
            self.content,
            text=(
                "SECURITY REMINDER\n"
                "Verify entries against source records. "
                "Check recipients before sharing personal information. "
                "Back up updated CSV files to an approved secure location."
            ),
            bg=LIGHT,
            fg=NAVY,
            font=("Arial", 11),
            justify="left",
            wraplength=480
        ).pack(anchor="w", padx=35, pady=(0, 10))

        area = tk.Frame(self.content, bg=LIGHT)
        area.pack(
            fill="both", expand=True,
            padx=35, pady=5
        )

        modules = [
            (
                "Driver Management",
                "Register drivers and review driver records.",
                self.show_drivers
            ),
            (
                "Driving Hours",
                "Record driving hours and review warnings.",
                self.show_hours
            ),
            (
                "Vehicle Checks",
                "Record inspections and vehicle defects.",
                self.show_vehicles
            ),
            (
                "Incident Logging",
                "Record incidents and manage their status.",
                self.show_incidents
            ),
            (
                "Compliance Reminders",
                "Track MOT, insurance and maintenance dates.",
                self.show_reminders
            )
        ]

        for title, description, command in modules:
            self.create_card(
                area, title, description, command
            )

    def module_page(self, title, subtitle, actions):
        self.clear_content()
        self.page_heading(title, subtitle)

        panel = tk.Frame(
            self.content, bg=WHITE,
            highlightbackground="#D9E2EC",
            highlightthickness=1
        )
        panel.pack(
            fill="x", padx=35, pady=10
        )

        for action in actions:
            tk.Button(
                panel,
                text=action,
                command=lambda name=action: self.placeholder(name),
                bg=BLUE,
                fg=WHITE,
                relief="flat",
                padx=15,
                pady=12,
                font=("Arial", 11),
                cursor="hand2"
            ).pack(
                fill="x", padx=25, pady=8
            )

    def placeholder(self, action):
        messagebox.showinfo(
            "Under Development",
            f"{action}\n\n"
            "This action will be connected to "
            "the existing Python module."
        )

    def show_drivers(self):
        self.clear_content()
        self.page_heading(
            "Driver Management",
            "Register drivers and view existing records."
        )

        panel = tk.Frame(self.content, bg=LIGHT)
        panel.pack(fill="both", expand=True, padx=35)

        tk.Button(
            panel,
            text="Add New Driver",
            command=self.show_add_driver,
            bg=BLUE,
            fg=WHITE,
            relief="flat",
            padx=20,
            pady=12,
            cursor="hand2"
        ).pack(fill="x", pady=8)

        tk.Button(
            panel,
            text="View Registered Drivers",
            command=self.show_driver_table,
            bg=BLUE,
            fg=WHITE,
            relief="flat",
            padx=20,
            pady=12,
            cursor="hand2"
        ).pack(fill="x", pady=8)

    def show_add_driver(self):
        self.clear_content()
        self.page_heading(
            "Add New Driver",
            "Enter driver information below."
        )

        form = tk.Frame(self.content, bg=WHITE)
        form.pack(fill="x", padx=35, pady=10)

        fields = [
            ("Full Name", "name"),
            ("Driving Licence Number", "licence"),
            ("Phone Number", "phone")
        ]

        entries = {}

        for label_text, key in fields:
            tk.Label(
                form,
                text=label_text,
                bg=WHITE,
                fg=NAVY,
                font=("Arial", 11)
            ).pack(anchor="w", padx=25, pady=(15, 3))

            entry = ttk.Entry(form, font=("Arial", 11))
            entry.pack(fill="x", padx=25, pady=(0, 5))
            entries[key] = entry

        def save_driver():
            name = entries["name"].get().strip()
            licence = entries["licence"].get().strip().upper()
            phone = entries["phone"].get().strip()

            if not name:
                messagebox.showerror(
                    "Validation Error",
                    "Driver name cannot be empty."
                )
                return

            if not licence:
                messagebox.showerror(
                    "Validation Error",
                    "Driving licence number cannot be empty."
                )
                return

            if not phone.isdigit():
                messagebox.showerror(
                    "Validation Error",
                    "Phone number must contain only digits."
                )
                return

            if len(phone) != 11 or not phone.startswith("0"):
                messagebox.showerror(
                    "Validation Error",
                    "Enter an 11-digit UK phone number starting with 0."
                )
                return

            csv_path = Path(__file__).resolve().parent / "drivers.csv"

            try:
                with csv_path.open("r", newline="", encoding="utf-8") as file:
                    reader = csv.reader(file)

                    for driver in reader:
                        if len(driver) >= 2:
                            if driver[1].strip().upper() == licence:
                                messagebox.showerror(
                                    "Duplicate Licence",
                                    "This driving licence is already registered."
                                )
                                return

            except FileNotFoundError:
                pass
            except OSError as error:
                messagebox.showerror(
                    "File Error",
                    f"Could not read driver records:\n{error}"
                )
                return

            try:
                with csv_path.open("a", newline="", encoding="utf-8") as file:
                    writer = csv.writer(file)
                    writer.writerow([name, licence, phone])

            except OSError as error:
                messagebox.showerror(
                    "File Error",
                    f"Could not save driver:\n{error}"
                )
                return

            messagebox.showinfo(
                "Success",
                "Driver registered successfully."
            )

            self.show_driver_table()

        tk.Button(
            form,
            text="Save Driver",
            command=save_driver,
            bg=BLUE,
            fg=WHITE,
            relief="flat",
            padx=20,
            pady=10,
            cursor="hand2"
        ).pack(pady=20)

        tk.Button(
            self.content,
            text="Back to Driver Management",
            command=self.show_drivers
        ).pack(pady=10)

    def show_driver_table(self):
        self.clear_content()
        self.page_heading(
            "Registered Drivers",
            "Driver records stored in drivers.csv"
        )

        table_frame = tk.Frame(self.content, bg=LIGHT)
        table_frame.pack(
            fill="both",
            expand=True,
            padx=35,
            pady=10
        )

        columns = ("name", "licence", "phone")

        table = ttk.Treeview(
            table_frame,
            columns=columns,
            show="headings"
        )

        table.heading("name", text="Driver Name")
        table.heading("licence", text="Licence Number")
        table.heading("phone", text="Phone Number")

        table.column("name", width=200)
        table.column("licence", width=180)
        table.column("phone", width=150)

        scrollbar = ttk.Scrollbar(
            table_frame,
            orient="vertical",
            command=table.yview
        )

        table.configure(yscrollcommand=scrollbar.set)

        scrollbar.pack(side="right", fill="y")
        table.pack(side="left", fill="both", expand=True)

        csv_path = Path(__file__).resolve().parent / "drivers.csv"

        try:
            with csv_path.open("r", newline="", encoding="utf-8") as file:
                reader = csv.reader(file)

                for driver in reader:
                    if len(driver) == 3:
                        table.insert(
                            "",
                            "end",
                            values=driver
                        )

        except FileNotFoundError:
            pass
        except OSError as error:
            messagebox.showerror(
                "File Error",
                f"Could not load drivers:\n{error}"
            )

        tk.Button(
            self.content,
            text="Back to Driver Management",
            command=self.show_drivers
        ).pack(pady=15)


    def hours_csv_path(self):
         return Path(__file__).resolve().parent / "driving_hours.csv"

    def registered_licence_exists(self, licence):
        licence = licence.strip().upper()
        csv_path = Path(__file__).resolve().parent / "drivers.csv"

        with csv_path.open("r", newline="", encoding="utf-8") as file:
            reader = csv.reader(file)
            return any(
                len(row) >= 2 and row[1].strip().upper() == licence
                for row in reader
            )

    def show_hours(self):
        self.clear_content()
        self.page_heading(
            "Driving Hours",
            "Record driving hours and review daily totals."
        )

        panel = tk.Frame(self.content, bg=LIGHT)
        panel.pack(fill="x", padx=35, pady=10)

        actions = [
            ("Record Driving Hours", self.show_record_hours),
            ("View Driving Hours", self.show_hours_table),
            ("Check Compliance", self.show_hours_compliance)
        ]

        for label, command in actions:
            tk.Button(
                panel,
                text=label,
                command=command,
                bg=BLUE,
                fg=WHITE,
                relief="flat",
                padx=20,
                pady=12,
                cursor="hand2"
            ).pack(fill="x", padx=20, pady=10)

    def show_record_hours(self):
        self.clear_content()
        self.page_heading(
            "Record Driving Hours",
            "Enter a registered driver's hours."
        )

        form = tk.Frame(self.content, bg=WHITE)
        form.pack(fill="x", padx=35, pady=10)

        entries = {}

        fields = [
            ("Driving Licence Number", "licence"),
            ("Driving Date (DD/MM/YYYY)", "date"),
            ("Driving Hours", "hours")
        ]

        for label_text, key in fields:
            tk.Label(
                form,
                text=label_text,
                bg=WHITE,
                fg=NAVY,
                font=("Arial", 11)
            ).pack(anchor="w", padx=25, pady=(15, 3))

            entry = ttk.Entry(form, font=("Arial", 11))
            entry.pack(fill="x", padx=25, pady=(0, 5))
            entries[key] = entry

        def save_hours():
            licence = entries["licence"].get().strip().upper()
            date_text = entries["date"].get().strip()
            hours_text = entries["hours"].get().strip()

            if not licence:
                messagebox.showerror(
                    "Validation Error",
                    "Licence number cannot be empty."
                )
                return

            try:
                exists = self.registered_licence_exists(licence)
            except FileNotFoundError:
                exists = False
            except OSError as error:
                messagebox.showerror("File Error", str(error))
                return

            if not exists:
                messagebox.showerror(
                    "Unregistered Driver",
                    "Please register this driver first."
                )
                return

            try:
                date = datetime.strptime(
                    date_text, "%d/%m/%Y"
                ).strftime("%Y-%m-%d")
            except ValueError:
                messagebox.showerror(
                    "Invalid Date",
                    "Enter a valid date in DD/MM/YYYY format."
                )
                return

            try:
                hours = float(hours_text)
            except ValueError:
                messagebox.showerror(
                    "Invalid Hours",
                    "Enter a valid number of hours."
                )
                return

            if not 0 < hours <= 24:
                messagebox.showerror(
                    "Invalid Hours",
                    "Hours must be greater than 0 and no more than 24."
                )
                return

            try:
                with self.hours_csv_path().open(
                    "a", newline="", encoding="utf-8"
                ) as file:
                    writer = csv.writer(file)
                    writer.writerow([licence, date, hours])
            except OSError as error:
                messagebox.showerror(
                    "File Error",
                    f"Could not save driving hours:\n{error}"
                )
                return

            messagebox.showinfo(
                "Success",
                "Driving hours recorded successfully."
            )
            self.show_hours_table()

        tk.Button(
            form,
            text="Save Driving Hours",
            command=save_hours,
            bg=BLUE,
            fg=WHITE,
            relief="flat",
            padx=20,
            pady=10
        ).pack(pady=20)

        tk.Button(
            self.content,
            text="Back to Driving Hours",
            command=self.show_hours
        ).pack(pady=10)

    def show_hours_table(self):
        self.clear_content()
        self.page_heading(
            "Driving Hours Records",
            "Previously recorded driving hours."
        )

        frame = tk.Frame(self.content, bg=LIGHT)
        frame.pack(
            fill="both", expand=True, padx=35, pady=10
        )

        columns = ("licence", "date", "hours")

        table = ttk.Treeview(
            frame, columns=columns, show="headings"
        )

        table.heading("licence", text="Licence Number")
        table.heading("date", text="Driving Date")
        table.heading("hours", text="Hours")

        for column in columns:
            table.column(column, width=160)

        scrollbar = ttk.Scrollbar(
            frame, orient="vertical", command=table.yview
        )
        table.configure(yscrollcommand=scrollbar.set)

        scrollbar.pack(side="right", fill="y")
        table.pack(side="left", fill="both", expand=True)

        try:
            with self.hours_csv_path().open(
                "r", newline="", encoding="utf-8"
            ) as file:
                for record in csv.reader(file):
                    if len(record) == 3:
                        table.insert("", "end", values=record)
        except FileNotFoundError:
            pass
        except OSError as error:
            messagebox.showerror("File Error", str(error))

        tk.Button(
            self.content,
            text="Back to Driving Hours",
            command=self.show_hours
        ).pack(pady=15)

    def show_hours_compliance(self):
        self.clear_content()
        self.page_heading(
            "Driving Hours Check",
            "Review recorded daily driving-hour totals."
        )

        panel = tk.Frame(self.content, bg=WHITE)
        panel.pack(fill="both", expand=True, padx=35, pady=10)

        tk.Label(
            panel,
            text="Driving Licence Number",
            bg=WHITE,
            fg=NAVY,
            font=("Arial", 11)
        ).pack(anchor="w", padx=20, pady=(20, 5))

        licence_entry = ttk.Entry(
            panel, font=("Arial", 11)
        )
        licence_entry.pack(fill="x", padx=20)

        results = tk.Text(
            panel,
            height=12,
            font=("Consolas", 11),
            wrap="word",
            state="disabled"
        )
        results.pack(
            fill="both", expand=True, padx=20, pady=15
        )

        def check_hours():
            licence = licence_entry.get().strip().upper()

            if not licence:
                messagebox.showerror(
                    "Validation Error",
                    "Enter a driving licence number."
                )
                return

            try:
                exists = self.registered_licence_exists(licence)
            except FileNotFoundError:
                exists = False
            except OSError as error:
                messagebox.showerror("File Error", str(error))
                return

            if not exists:
                messagebox.showerror(
                    "Unregistered Driver",
                    "Driver not registered."
                )
                return

            totals = {}
            skipped = 0

            try:
                with self.hours_csv_path().open(
                    "r", newline="", encoding="utf-8"
                ) as file:
                    for row in csv.reader(file):
                        if len(row) != 3:
                            skipped += 1
                            continue

                        row_licence, date, hours_text = row

                        if row_licence.strip().upper() != licence:
                            continue

                        try:
                            hours = float(hours_text)
                            if not 0 < hours <= 24:
                                raise ValueError
                        except ValueError:
                            skipped += 1
                            continue

                        totals[date] = totals.get(date, 0) + hours

            except FileNotFoundError:
                pass
            except OSError as error:
                messagebox.showerror("File Error", str(error))
                return

            lines = [f"Driver Licence: {licence}", ""]

            if not totals:
                lines.append("No driving records found.")

            for date, total in sorted(totals.items()):
                if total > 10:
                    status = "WARNING - Above 10 hours"
                elif total > 9:
                    status = "REVIEW - Above 9 hours"
                else:
                    status = "Within normal threshold"

                lines.append(
                    f"{date} | {total:.2f} hours | {status}"
                )

            if skipped:
                lines.append(
                    f"\nSkipped invalid records: {skipped}"
                )

            lines.append(
                "\nNote: Simplified daily-hours screening only."
            )

            results.configure(state="normal")
            results.delete("1.0", tk.END)
            results.insert(tk.END, "\n".join(lines))
            results.configure(state="disabled")

        tk.Button(
            panel,
            text="Check Driving Hours",
            command=check_hours,
            bg=BLUE,
            fg=WHITE,
            relief="flat",
            padx=20,
            pady=10
        ).pack(pady=(0, 15))

        tk.Button(
            self.content,
            text="Back to Driving Hours",
            command=self.show_hours
        ).pack(pady=10)
        
    def show_vehicles(self):
        self.module_page(
            "Vehicle Checks",
            "Manage vehicle inspections and defects.",
            [
                "Record Vehicle Check",
                "View Vehicle Checks",
                "View Vehicle Defects"
            ]
        )

    def show_incidents(self):
        self.module_page(
            "Incident Logging",
            "Record and manage transport incidents.",
            [
                "Record Incident",
                "View All Incidents",
                "View Open Incidents",
                "Close Incident"
            ]
        )

    def show_reminders(self):
        self.module_page(
            "Compliance Reminders",
            "Track upcoming and overdue requirements.",
            [
                "Add Reminder",
                "View Reminders"
            ]
        )
    
    def show_security_guidance(self):
        messagebox.showinfo(
            "Security Guidance for Transport Staff",
            "CHECK RECORDS\n"
            "Compare driver details, driving hours and dates with "
            "source records before saving. Correct any mistakes.\n\n"
            "SHARE SAFELY\n"
            "Check the recipient and file contents before sharing. "
            "Only share necessary information with authorised people. "
            "Never upload real driver records to GitHub.\n\n"
            "PROTECT BACKUPS\n"
            "After updating records, back up the CSV files to an "
            "organisation-approved, access-restricted location. "
            "Check that the backup can be opened.\n\n"
            "These reminders support safe working; they do not "
            "encrypt files or restrict access automatically.",
            parent=self.root
        )

    def confirm_exit(self):
        if messagebox.askyesno(
            "Exit",
            "Are you sure you want to exit?"
        ):
            self.root.destroy()


if __name__ == "__main__":
    root = tk.Tk()
    app = TransportComplianceGUI(root)
    root.mainloop()
