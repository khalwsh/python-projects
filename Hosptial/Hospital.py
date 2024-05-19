def valid_int(msg, start, end):
    """
    Prompt the user to enter an integer within a specified range.

    Parameters:
    msg (str): The message to display to the user.
    start (int): The start of the valid range (inclusive).
    end (int): The end of the valid range (inclusive).

    Returns:
    int: A valid integer within the specified range.
    """
    x = 0
    try:
        x = int(input(msg))
    except ValueError:  # Catching specific exception
        return valid_int(msg, start, end)
    if x >= start and x <= end:
        return x
    return valid_int(msg, start, end)  # Return the function call

class Patient:
    """
    This class represents a patient.

    Attributes:
    name (str): The name of the patient.
    status (int): The status of the patient (0: normal, 1: urgent, 2: super urgent).
    specialization (int): The specialization of the patient.
    """
    
    def __init__(self, name, status, specialization):
        """
        Initialize a new patient.

        Parameters:
        name (str): The name of the patient.
        status (int): The status of the patient.
        specialization (int): The specialization of the patient.
        """
        self.name = name
        self.status = status
        self.specialization = specialization
        
    def __str__(self):
        """
        Return a string representation of the patient.

        Returns:
        str: A string describing the patient.
        """
        return f"name: {self.name} \nstatus: {self.status} \nspecialization: {self.specialization}\n"
    
    def __repr__(self):
        """
        Return a string representation of the patient for debugging.

        Returns:
        str: A string describing the patient.
        """
        return f"Patient({self.name}, {self.status}, {self.specialization})"

class HospitalManager:
    """
    This class manages the hospital's patient records.
    
    Attributes:
    specialization_cnt (int): The number of specializations.
    max_patients_per_specialization (int): The maximum number of patients per specialization.
    CurrentPatients (list): A list of lists holding current patients for each specialization.
    """
    
    def __init__(self, specialization_cnt, max_patients_per_specialization):
        """
        Initialize a new HospitalManager.

        Parameters:
        specialization_cnt (int): The number of specializations.
        max_patients_per_specialization (int): The maximum number of patients per specialization.
        """
        self.specialization_cnt = specialization_cnt
        self.max_patients_per_specialization = max_patients_per_specialization
        self.CurrentPatients = [[] for _ in range(self.specialization_cnt)]
            
    def can_take_more_patient(self, specialization):
        """
        Check if more patients can be added to a specialization.

        Parameters:
        specialization (int): The specialization to check.

        Returns:
        bool: True if more patients can be added, False otherwise.
        """
        return len(self.CurrentPatients[specialization - 1]) < self.max_patients_per_specialization
    
    def add_patient(self):
        """
        Add a new patient to the hospital.
        """
        name = input("Enter patient Name: ")
        specialization = valid_int("Enter specialization [1 , 20] : ", 1, 20)
        status = valid_int("Enter status  (0 normal , 1 urgent , 2 super urgent)", 0, 2)
        patient = Patient(name, status, specialization)
        
        if self.can_take_more_patient(patient.specialization):
            print(patient)
            print("added to the system successfully")
            self.CurrentPatients[patient.specialization - 1].append(patient)
        else:
            print(f"can't accept more patients with specialization: {patient.specialization}")
    
    def next_patient(self, specialization):
        """
        Get the next patient for a given specialization.

        Parameters:
        specialization (int): The specialization to get the next patient for.
        """
        if len(self.CurrentPatients[specialization - 1]) == 0:
            print(f"no patients of this specialization: {specialization}")
        else:
            current = self.CurrentPatients[specialization - 1][0]
            for patient in self.CurrentPatients[specialization - 1]:
                if patient.status > current.status:
                    current = patient
            print(current)
            print("you can see the Dr. now")
            for i in range(len(self.CurrentPatients[specialization - 1]) - 1, -1, -1):
                if current == self.CurrentPatients[specialization - 1][i]:
                    del self.CurrentPatients[specialization - 1][i]
                    break

    def print_patient_info(self):
        """
        Print information about all patients.
        """
        for specialization in self.CurrentPatients:
            for patient in specialization:
                print(patient)
    
    def remove_patient(self, specialization, name):
        """
        Remove a patient from the hospital.

        Parameters:
        specialization (int): The specialization of the patient to remove.
        name (str): The name of the patient to remove.
        """
        done = False
        x = Patient(name, 0, specialization) 
        for i in range(len(self.CurrentPatients[specialization - 1]) - 1, -1, -1):
            if name == self.CurrentPatients[specialization - 1][i].name and specialization == self.CurrentPatients[specialization - 1][i].specialization:
                del self.CurrentPatients[specialization - 1][i]
                done = True
                break
        if done:
            print(x)
            print("deleted successfully")
        else:
            print(x)
            print("not found")
            
class FrontendManager:
    """
    This class manages the user interface for the hospital system.
    
    Attributes:
    specialization_cnt (int): The number of specializations.
    Manager (HospitalManager): The hospital manager instance.
    """
    
    def __init__(self, specialization_cnt=20):
        """
        Initialize a new FrontendManager.

        Parameters:
        specialization_cnt (int): The number of specializations. Default is 20.
        """
        self.specialization_cnt = specialization_cnt
        self.Manager = HospitalManager(specialization_cnt, 10)
    
    def print_menu(self):
        """
        Print the main menu.

        Returns:
        str: The menu string.
        """
        menu = """
            1) Add new patient
            2) Print all patients
            3) Get next patient
            4) Remove a leaving patient
            5) End of program
            Enter your choice (from 1 to 5): 
            """
        return menu     

    def add_dummy_data(self):
        """
        Add dummy data to the hospital system.
        """
        pass
    
    def run(self):
        """
        Run the main program loop.
        """
        while True:
            menu = self.print_menu()
            choice = valid_int(menu, 1, 5)
            
            if choice == 1:
                self.Manager.add_patient()
            elif choice == 2:
                self.Manager.print_patient_info()
            elif choice == 3:
                specialization = valid_int("Enter specialization: ", 1, 20)
                self.Manager.next_patient(specialization)
            elif choice == 4:
                name = input("Enter patient name to remove: ")
                specialization = valid_int("Enter specialization: ", 1, 20)
                self.Manager.remove_patient(specialization, name)
            elif choice == 5:
                print("Ending program.")
                break
    
if __name__ == '__main__':
    app = FrontendManager()
    app.run()
