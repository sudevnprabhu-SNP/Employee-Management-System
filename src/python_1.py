#Employee Management System (EMS)
# Objective - Create a simplified Employee Management System (EMS). 
# This project will cover control structures, functions, and 
# object-oriented programming concepts to manage employee data.

employees = {
    101: {
        "name":"Satya",
        "age":27,
        "department":"HR",
        "salary":50000
    }
}

def main_menu():
    print("\n========= MENU =========")
    print("1. Add Employee")
    print("2. View All Employee")
    print("3. Search for Employee")
    print("4. Exit")

    try:
        menu_selected = int(input("Select the index from the menu: "))
        return menu_selected

    except ValueError:
        print("Invalid input! Please enter only numbers.")
     

def add_employee(emp_id,emp_name,emp_age,emp_dep, emp_salary):
    if emp_id in employees:
        print("The ID already exists, please enter a new ID")
    else:
        employees[emp_id] = {"name" : emp_name, "age":emp_age, "department":emp_dep, "salary": emp_salary}
        print("Employee was added successfully")

def view_employee():
    if not employees:
        print("No employees available.")
    else:
        print("==============================================================================")
        print(f"{'Employee ID':<15}{'Name':<15}{'Age':<10}{'Department':<20}{'Salary':<10}")
        print("==============================================================================")
        for employee_id in sorted(employees):
            emp = employees[employee_id]
            print(
                f"{employee_id:<15}"
                f"{emp['name']:<15}"
                f"{emp['age']:<10}"
                f"{emp['department']:<20}"
                f"{emp['salary']:<10}"
            )

def search_employee(emp_id):
    if emp_id in employees:
       print("==============================")
       print("Employee Id.        : ", emp_id)
       print("Employee Name       : ", employees[emp_id]["name"])
       print("Employee Age        : ", employees[emp_id]["age"])
       print("Employee Department : ", employees[emp_id]["department"])
       print("Employee Salary     : ", employees[emp_id]["salary"])
       print("==============================")
    else:
        print("Employee not found.")


while True:
    menu_selected = main_menu()

    if menu_selected == 1:
        try:
            emp_id = int(input("Enter the new employee id: "))
            emp_name = input("Enter the employee name: ")
            emp_age = int(input("Enter the employee age: "))
            emp_dep = input("Enter the employee department: ")
            emp_salary = int(input("Enter the employee Salary: "))
            if emp_age < 18 or emp_age > 70:
                print("Invalid Age")
            elif emp_salary <= 0:
                print("Invalid Salary")
            else:
                add_employee(emp_id,emp_name,emp_age,emp_dep,emp_salary)
        
        except ValueError:
            print("Invalid input! Please enter only numbers.")
        

    elif menu_selected == 2:
        view_employee()
    
    elif menu_selected == 3:
        try:
            emp_id = int(input("Enter the new employee id: "))
            search_employee(emp_id)
        
        except ValueError:
            print("Invalid input! Please enter only numbers.")
       

    elif menu_selected == 4:
        print("Thank you for using our Employee Management Application.")
        break

    else:
         print("Invalid Choice! Please try again.")