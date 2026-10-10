# 👥 Employee Management System

**A Python console application for creating, viewing, and searching employee records.**

A beginner-friendly software project that demonstrates Python programming fundamentals through a simple employee record management system.

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.10%2B-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python 3.10+">
  <img src="https://img.shields.io/badge/Dependencies-None-2ea44f?style=for-the-badge" alt="No third-party dependencies">
  <img src="https://img.shields.io/badge/Interface-CLI-555555?style=for-the-badge" alt="Command-line interface">
  <img src="https://img.shields.io/badge/Project-Learning%20Project-orange?style=for-the-badge" alt="Learning project">
</p>

---

## 📌 Overview

The **Employee Management System** is a menu-driven Python application for handling basic employee information through an interactive terminal.

Users can add employee records, display them in a formatted table, and search for employees using their IDs. The application also includes basic validation to help prevent duplicate IDs and invalid age or salary values.

The project provides hands-on experience with Python functions, dictionaries, conditional logic, and structured data presentation.

## ✨ Features

| Feature | Description |
|---|---|
| ➕ Add Employees | Register employees with an ID, name, age, department, and salary |
| 📋 View Records | Display employee information in a formatted table |
| 🔎 Search Employees | Find an employee using their ID |
| 🛡️ Duplicate Detection | Reject duplicate employee IDs |
| ✅ Input Validation | Apply basic checks to employee age and positive salary |
| 🧑‍💼 Sample Record | Explore the application using a preloaded employee record |

## 🛠️ Built With

- **Language:** Python
- **Interface:** Interactive command-line menu
- **Data structure:** Python dictionaries
- **Dependencies:** Python standard library only

No third-party packages or database installation are required.

## 🚀 Getting Started

### Prerequisites

- Python 3.10 or newer recommended
- A terminal or command prompt
- Git, if you want to clone the repository

### 1. Clone the repository

```bash id="f7tq2m"
git clone https://github.com/sudevnprabhu-SNP/Employee-Management-System.git
```

### 2. Navigate to the project directory

```bash id="h9zq4v"
cd Employee-Management-System
```

### 3. Run the application

```bash id="b6w2kj"
python3 src/python_1.py
```

If `python3` is not recognized on Windows, try:

```bash id="m3r8vx"
python src/python_1.py
```

Follow the numbered menu to explore the available operations.

## 🧪 Example Workflow

A typical session involves:

1. Starting the application.
2. Adding an employee with the required details.
3. Viewing all employee records.
4. Searching for a specific employee by ID.
5. Exiting the application.

One sample employee is included to demonstrate how records are displayed.

## 📁 Project Structure

```text id="p5k3nw"
Employee-Management-System/
├── src/
│   └── python_1.py
├── docs/
│   └── screenshots/
├── README.md
├── requirements.txt
└── LICENSE
```

## 🖥️ Screenshots

Screenshots can be added to demonstrate the application interface.

Recommended screenshots:

- Main menu
- Employee records displayed in a formatted table
- Successful employee search
- Input validation for a duplicate employee ID

*Screenshots are not included yet. Add genuine terminal captures after running the application.*

## 💾 Data and Persistence

The application starts with a sample employee record. Employee information is stored in memory while the program is running.

**Important:** Records added during a session are lost when the application exits. No database or file-based persistence is currently implemented.

## ⚠️ Limitations

- **Limited operations:** The current version supports adding, viewing, and searching records. Updating and deleting employee records are not implemented.
- **Temporary storage:** Employee records are not saved between sessions.
- **Basic salary handling:** Salary is represented as an integer, without configurable currency, deductions, or payroll calculations.
- **Console-based interface:** No graphical interface is currently provided.
- **Basic validation:** Input checks are intended for learning and may need further improvement.

This is an educational programming project, not a production human-resources or payroll management system.

## 🎯 Learning Objectives

This project demonstrates practical use of:

- Python dictionaries and functions
- Loops and conditional statements
- User input and validation
- Duplicate record detection
- Searching records using unique identifiers
- Formatting tabular output
- Structuring a beginner Python project for GitHub

## 🔮 Future Improvements

Potential extensions include:

- Updating and deleting employee records
- Saving data using SQLite
- Adding department-based search and filtering
- Generating employee summary reports
- Improving validation and adding automated tests
- Building a graphical interface

These are possible future enhancements, not features currently available.

## 📄 License

Distributed under the MIT License. See [`LICENSE`](LICENSE) for details.

Use this license only if you have the rights to license the code and documentation in this repository. Third-party materials, if added, remain subject to their own terms.

---

<p align="center">
  <i>Built with Python • Focused on Employee Record Management • Created as a Learning Project</i>
</p>
