import sys

MAX_EMPLOYEES = 100
USERNAME = "admin"
PASSWORD = "password"


class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary


def main():
    employees = []
    num_employees = 0

    login_attempts = 0
    while True:
        print("Login")
        username = input("Username: ")
        password = input("Password: ")
        login_attempts += 1

        if username == USERNAME and password == PASSWORD:
            print("Login successful.")
            break
        else:
            print("Invalid username or password. Please try again.")

        if login_attempts == 3:
            print("Maximum login attempts reached. Exiting program...")
            sys.exit()

    while True:
        print("\nPayroll Management System")
        print("1. Add Employee")
        print("2. Delete Employee")
        print("3. View Employee Details")
        print("4. View Payroll")
        print("5. Exit")
        option = input("Enter your option: ")

        if option == "1":
            if num_employees == MAX_EMPLOYEES:
                print("Error: Maximum number of employees reached.")
                continue

            name = input(f"Enter name of employee {num_employees + 1}: ")
            salary = float(input("Enter salary: "))
            employees.append(Employee(name, salary))
            num_employees += 1
            print("Employee added successfully.")

        elif option == "2":
            emp_index = int(input("Enter index of employee to delete: "))
            if emp_index < 0 or emp_index >= num_employees:
                print("Error: Invalid employee index.")
                continue

            employees.pop(emp_index)
            num_employees -= 1
            print("Employee deleted successfully.")

        elif option == "3":
            emp_index = int(input("Enter index of employee to view details: "))
            if emp_index < 0 or emp_index >= num_employees:
                print("Error: Invalid employee index.")
                continue

            emp = employees[emp_index]
            print(f"Name: {emp.name}")
            print(f"Salary: {emp.salary:.2f}")

        elif option == "4":
            total_payroll = 0.0
            print("\nPayroll:")
            print("{:<20} {:<10}".format("Name", "Salary"))
            print("--------------------------------------------------")
            for emp in employees:
                print("{:<20} {:<10.2f}".format(emp.name, emp.salary))
                total_payroll += emp.salary

            print("--------------------------------------------------")
            print(f"Total payroll: {total_payroll:.2f}")

        elif option == "5":
            print("Exiting program...")
            sys.exit()

        else:
            print("Error: Invalid option.")


if __name__ == "__main__":
    main()
