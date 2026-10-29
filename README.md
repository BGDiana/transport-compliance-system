# HGV Transport Compliance Management System

## Project Overview

A Python application developed for the PFD200 Professional Development module. It is an educational prototype for organising information relating to UK Heavy Goods Vehicle (HGV) transport operations.

The project includes a command-line application and a partially developed Tkinter graphical interface.

## Features

The command-line application supports:

- Driver registration and record viewing.
- Driving-hours recording and basic daily-hours checks.
- Vehicle safety checks and defect records.
- Incident logging and open/closed status management.
- Compliance reminders showing upcoming and overdue requirements.
- Saving and retrieving records using CSV files.

Input validation includes required-field checks, duplicate driving-licence prevention and UK telephone-format checks.

## Graphical Interface

The Tkinter interface provides:

- Dashboard and module navigation.
- Driver registration and record viewing.
- Driving-hours recording, viewing and screening.
- Security guidance and a dashboard reminder.

GUI actions for vehicle checks, incident logging and compliance reminders require further development. These functions are available through the command-line application.

## Security Awareness

The GUI includes a security briefing and dashboard reminder encouraging users to:

- Verify information against source records.
- Check recipients and file contents before sharing.
- Maintain protected backups.

These materials provide guidance rather than technical protection. Their effect on user behaviour has not yet been evaluated.

## Technologies Used

- Python 3.14
- Tkinter
- CSV file storage
- Visual Studio Code
- GitHub and GitHub Desktop
- Jira

## How to Run

1. Install Python 3.14 with Tkinter available.
2. Download or clone this repository.
3. Extract the ZIP file if downloaded.
4. Open a terminal in the project folder.

To run the command-line application:

```bash
python main.py
```

To run the graphical interface:

```bash
python guy.py
```

The application runs locally and does not require hosting.

## Testing

The `test_results.csv` file records test actions, expected outcomes, actual outcomes and pass/fail statuses.

Testing covers core functions, input validation and retention of CSV records after restarting the application.

## Project Management

Jira was used to organise development tasks and track progress. GitHub maintains the code history, with relevant commits referencing Jira issues.

## Limitations

- This is an educational prototype, not professionally validated transport compliance software.
- Driving-hours checks are simplified and do not assess every applicable rule or exception.
- CSV files can be accessed or edited outside the application.
- Authentication, role-based access and encryption are not implemented.
- Some graphical-interface functions remain unfinished.
- Demonstration records are fictional.

## Project Status

The core command-line application is implemented. The graphical interface is partially implemented and remains under development.