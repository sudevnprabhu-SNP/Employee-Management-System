    # Employee Management System

    A beginner Python console application demonstrating dictionaries, functions, input validation, and basic employee record handling.

    ## Features

    - Add an employee with ID, name, age, department, and salary
- View employee records in a formatted table
- Search for an employee by ID
- Reject duplicate employee IDs
- Basic checks for age and positive salary

    ## Requirements

    Uses only the Python standard library; no third-party packages are required.

    - Recommended Python version: Python 3.10 or newer.
    - See [`requirements.txt`](requirements.txt).

    ## Run locally

    1. Install Python 3.
    2. Clone this repository or download it as a ZIP.
    3. Open a terminal in the repository root.
    4. Run:

       ```bash
       python3 src/python_1.py
       ```

    ## Sample usage

    Run the script and select Add Employee, View All Employee, Search for Employee, or Exit from the menu. One sample employee is included.

    ## Project structure

    ```text
    Employee-Management-System/
    ├── src/
    │   └── python_1.py
    ├── docs/
    │   └── screenshots/
    ├── README.md
    ├── requirements.txt
    └── LICENSE
    ```

    ## Screenshots

    Add terminal screenshots here after running the program. Suggested screenshots: main menu, employee table, and search result. No screenshots are included because none were provided.

    ## Data and persistence

    The program starts with sample records defined in the source code. Records are maintained in memory during the current run; they are not saved to a database or file.

    ## Limitations

    - The current version supports create, read, and search operations; update and delete operations are not implemented.
- Records are stored in memory and are lost when the program exits.
- Salary is handled as an integer without currency configuration or payroll calculations.
- This is a learning exercise, not a production HR or payroll system.

    ## License

    This project is distributed under the MIT License. See [`LICENSE`](LICENSE). The license applies to the original project code and documentation authored for this repository; any third-party materials retain their own terms.
