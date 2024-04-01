class Employee:

    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary

    def print_employee(self):
        return f"{self.name} has age {self.age} and salary {self.salary}"

    def update_salary(self, new_salary):
        self.salary = new_salary


class EmployeeManager:

    def __init__(self):
        self.employees = list()

    def handle(self, choice):
        if choice == 1:
            self.add()
        elif choice == 2:
            self.print_all_employees()
        elif choice == 3:
            self.delete_by_age_range()
        elif choice == 4:
            x = self.update_salary_by()
            if not x:
                print("Error there is no such an Employee")
        else:
            exit(0)

    def add(self):
        emp = Employee("x", 2, 3)
        emp.name = input("Enter Employee name: ")
        emp.age = int(input("Enter Employee age: "))
        emp.salary = int(input("Enter Employee salary:"))
        self.employees.append(emp)

    def print_all_employees(self):
        for emp in self.employees:
            print("Employee: ", emp.print_employee())

    def delete_by_age_range(self):
        a, b = input("Enter range of ages to delete: ").split()
        a = int(a)
        b = int(b)
        if a > b:
            a, b = b, a
        for idx in range(len(self.employees) - 1, -1, -1):
            emp = self.employees[idx]
            if a <= emp.age <= b:
                print('\tDeleting', emp.name)
                self.employees.pop(idx)


    def update_salary_by(self):
        name = input("Enter Employee name: ")
        new_salary = int(input("Enter new salary: "))
        done = False
        for emp in self.employees:
            if emp.name == name:
                emp.update_salary(new_salary)
                done = True
        if done:
            return True
        return False


class FrontedManager:
    def __init__(self):
        self.manager = EmployeeManager()

    def print_menu(self):
        print("1) add new employee")
        print("2) print all employees")
        print("3) delete by age range")
        print("4) update Salary by name")
        print("5) End the program")
        choice = input()
        for i in choice:
            if not i.isdigit():
                print("invalid input Try again!")
                self.print_menu()
        if len(choice) != 1:
            print("invalid input Try again!")
            self.print_menu()
        choice = int(choice)
        if not 1 <= choice <= 5:
            print("invalid input Try again!")
            self.print_menu()
        self.manager.handle(choice)
        self.print_menu()


front_manager = FrontedManager()  # Create an instance of FrontedManager
front_manager.print_menu()  # Call the print_menu method on the instance
