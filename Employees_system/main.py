class Employee:
    """
    A class to represent an employee.
    
    Attributes:
    name (str): The name of the employee.
    age (int): The age of the employee.
    salary (int): The salary of the employee.
    """

    def __init__(self, name, age, salary):
        """
        Initialize a new Employee instance.
        
        Parameters:
        name (str): The name of the employee.
        age (int): The age of the employee.
        salary (int): The salary of the employee.
        """
        self.name = name
        self.age = age
        self.salary = salary

    def print_employee(self):
        """
        Return a formatted string with the employee's details.
        
        Returns:
        str: A string describing the employee.
        """
        return f"{self.name} has age {self.age} and salary {self.salary}"

    def update_salary(self, new_salary):
        """
        Update the employee's salary.
        
        Parameters:
        new_salary (int): The new salary for the employee.
        """
        self.salary = new_salary


class EmployeeManager:
    """
    A class to manage a list of employees.
    
    Attributes:
    employees (list): A list to store employee instances.
    """

    def __init__(self):
        """
        Initialize a new EmployeeManager instance.
        """
        self.employees = list()

    def handle(self, choice):
        """
        Handle the user's menu choice.
        
        Parameters:
        choice (int): The user's menu choice.
        """
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
        """
        Add a new employee to the list.
        """
        emp = Employee("x", 2, 3)
        emp.name = input("Enter Employee name: ")
        emp.age = int(input("Enter Employee age: "))
        emp.salary = int(input("Enter Employee salary:"))
        self.employees.append(emp)

    def print_all_employees(self):
        """
        Print the details of all employees.
        """
        for emp in self.employees:
            print("Employee: ", emp.print_employee())

    def delete_by_age_range(self):
        """
        Delete employees within a specified age range.
        """
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
        """
        Update the salary of an employee by their name.
        
        Returns:
        bool: True if the employee was found and updated, False otherwise.
        """
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


class FrontendManager:
    """
    A class to manage the user interface for the EmployeeManager.
    
    Attributes:
    manager (EmployeeManager): An instance of EmployeeManager.
    """

    def __init__(self):
        """
        Initialize a new FrontendManager instance.
        """
        self.manager = EmployeeManager()

    def print_menu(self):
        """
        Print the main menu and handle user input.
        """
        print("1) Add new employee")
        print("2) Print all employees")
        print("3) Delete by age range")
        print("4) Update salary by name")
        print("5) End the program")
        choice = input()
        for i in choice:
            if not i.isdigit():
                print("Invalid input. Try again!")
                self.print_menu()
                return
        if len(choice) != 1:
            print("Invalid input. Try again!")
            self.print_menu()
            return
        choice = int(choice)
        if not 1 <= choice <= 5:
            print("Invalid input. Try again!")
            self.print_menu()
            return
        self.manager.handle(choice)
        self.print_menu()


if __name__ == '__main__':
    front_manager = FrontendManager()  # Create an instance of FrontendManager
    front_manager.print_menu()  # Call the print_menu method on the instance
