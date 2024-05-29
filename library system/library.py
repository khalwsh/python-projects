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

class Book:
    """
    Represents a book in the library.

    Attributes:
    id (int): The unique identifier for the book.
    name (str): The name of the book.
    quantity (int): The quantity of the book available in the library.
    borrowed (int): The number of copies currently borrowed.
    users (list): List of users who have borrowed this book.
    """
    def __init__(self , id , name , quantity ):
        """
        Initializes a Book instance.

        Parameters:
        id (int): The unique identifier for the book.
        name (str): The name of the book.
        quantity (int): The quantity of the book available in the library.
        """
        self.id = id
        self.name = name
        self.quantity = quantity
        self.borrowed = 0
        self.users = []
    
    def __str__(self):
        """
        Returns a string representation of the book.

        Returns:
        str: A string containing the book's details.
        """
        return f"book name: {self.name} , id: {self.id} , quantity: {self.quantity}\n"
    
    def can_be_borrowed(self):
        """
        Checks if the book can be borrowed.

        Returns:
        bool: True if the book can be borrowed, False otherwise.
        """
        return self.quantity > self.borrowed
    
    def returned (self , user):
        """
        Handles the returning of a book by a user.

        Parameters:
        user (User): The user returning the book.
        """
        if self.borrowed != 0:
            self.borrowed -= 1
            self.quantity += 1
            idx = 0
            i = 0
            for u in self.users:
                if u.id == user.id:
                    idx = i
                i+= 1
            self.users.pop(idx)
            
    def same_prefix(self , prefix):
        """
        Checks if the book's name starts with a given prefix.

        Parameters:
        prefix (str): The prefix to check.

        Returns:
        bool: True if the book's name starts with the prefix, False otherwise.
        """
        if self.name.find(prefix) == 0:
            return True
        return False
    
    def borrow(self , User):
        """
        Handles the borrowing of the book by a user.

        Parameters:
        User (User): The user borrowing the book.

        Returns:
        bool: True if the book was successfully borrowed, False otherwise.
        """
        if self.can_be_borrowed():
            self.users.append(User)
            self.quantity-=1
            self.borrowed+=1
            return True
        return False
        
class user:
    """
    Represents a user in the library.

    Attributes:
    id (int): The unique identifier for the user.
    name (str): The name of the user.
    borrowed (list): List of books borrowed by the user.
    """
    def __init__(self , id , name):
        """
        Initializes a User instance.

        Parameters:
        id (int): The unique identifier for the user.
        name (str): The name of the user.
        """
        self.id = id
        self.name = name
        self.borrowed = []
    
    def __str__(self):
        """
        Returns a string representation of the user.

        Returns:
        str: A string containing the user's details.
        """
        return f"user name: {self.name} , id: {self.id}\n"

    def borrow(self , book):
       """
       Handles borrowing of a book by the user.

       Parameters:
       book (Book): The book to be borrowed.
       """
       if book.borrow(self):
           self.borrowed.append(book)  
    def returned(self , book):
        """
        Handles the returning of a borrowed book by the user.

        Parameters:
        book (Book): The book to be returned.
        """
        idx = 0
        i = 0
        for b in self.borrowed:
            if b.id == book.id:
                idx = i
            i+= 1
        self.borrowed.pop(idx)
             

class BackEndManager:
    """
    Manages the backend operations of the library.

    Attributes:
    books (list): List of books in the library.
    users (list): List of users in the library.
    """
    def __init__(self):
        """
        Initializes a BackEndManager instance.
        """
        self.books = []
        self.users = []
        
    def Add_book(self):
        """
        Adds a new book to the library.
        """
        id = valid_int("Enter book id:"  , 1 , 10000000000)
        name = input("Enter book name: ")
        quantity = valid_int("Enter book quantity: " , 1 , 1000000)
        book = Book(id , name , quantity)
        found = False
        for B in self.books:
            if book.name == B.name or book.id == B.id:
                Found = True
                B.quantity += book.quantity
                break
        if not found:
            self.books.append(book)
            
    def print_library_book(self):
        """
        Prints all books in the library.
        """
        for book in self.books:
            print(book)
    def print_books_by_prefix(self):
        """
        Prints books that have names starting with a given prefix.
        """
        prefix = input("Enter book prefix: ")
        printed = False
        for book in self.books:
            if book.same_prefix(prefix):
                print(book)
                printed = True
        if not printed:
            print("no such a book in the system")
                
    def Add_user(self):
        """
        Adds a new user to the library.
        """
        name = input("Enter user name: ")
        id = valid_int("Enter userd id: " ,1 , 10000000000)
        User = user(id  , name)
        found = False
        for u in self.users:
            if self.user_exist:
                print("user already exits")
                found = True
        if not found:
            self.users.append(User)
        
    def user_exist(self , user):
        """
        Checks if a user exists in the library.

        Parameters:
        user (User): The user to check.

        Returns:
        int: The index of the user if found, -1 otherwise.
        """
        i = 0
        for u in self.users:
            if u.id == user.id:
                return i
            i += 1
        return -1
    
    def book_exist(self , book):
        """
        Checks if a book exists in the library.

        Parameters:
        book (Book): The book to check.

        Returns:
        int: The index of the book if found, -1 otherwise.
        """
        i = 0
        for b in self.books:
            if b.id == book.id or b.name == book.name:
                return i
            i += 1
        return -1
    
    def Borrow_book(self):
        """
        Handles the borrowing process of a book by a user.
        """
        user_name = input("Enter user name: ")
        user_id = valid_int("Enter user id: ", 1 , 10000000000)
        User = user(user_id , user_name)
        book_name = input("Enter book name: ")
        book_id = valid_int("Enter book id: ", 1 , 10000000000)
        book = Book(book_id , book_name , 0)
        book_idx = self.book_exist(book)
        user_idx = self.user_exist(User)
        if book_idx != -1 and user_idx != -1 and self.books[book_idx].can_be_borrowed():
            self.users[user_idx].borrow(self.books[book_idx])
            print("borrowed successfully")
        else:
            print("failed to borrow")
    
    def Return_book(self):
        """
        Handles the returning process of a book by a user.
        """
        user_name = input("Enter user name: ")
        user_id = valid_int("Enter user id: ", 1 , 10000000000)
        User = user(user_id , user_name)
        book_name = input("Enter book name: ")
        book_id = valid_int("Enter book id: ", 1 , 10000000000)
        book = Book(book_id , book_name , 0)
        book_idx = self.book_exist(book)
        user_idx = self.user_exist(User)
        if book_idx != -1 and user_idx != -1 :
            self.users[user_idx].returned(self.books[book_idx])
            self.books[book_idx].returned(self.users[user_idx])
            print("returned successfully")
        else:
            print("failed to return")
    
    def print_users_borrowed_book(self):
        """
        Prints the list of users who borrowed books.
        """
        for u in self.users:
            if len(u.borrowed) != 0:
               print(u , end = ' ')
               print("borrowed " , end= '')
               for j in u.borrowed:
                   print(j , end = ' ')
               print()
    
    def print_users(self):
        """
        Prints the list of users in the library.
        """
        for user in self.users:
            print(user)

class FrontEndManager:
    """
    Manages the frontend operations of the library.
    """
    def __init__(self):
        """
        Initializes a FrontEndManager instance.
        """
        self.Manager = BackEndManager()
        
    def print_menu(self):
        """
        Prints the menu of available operations.
        """
        print(''' 
1) Add book 
2) print library books 
3) print books by prefix
4) Add user
5) Borrow book
6) Return book
7) print users borrowed book
8) print users
9) exit system
              ''')  
    
    def run(self):
        """
        Runs the library management system.
        """
        while True:
            self.print_menu()
            choice = valid_int("Enter your choice (from 1 to 9): ", 1, 9)
            if choice == 1:
                self.Manager.Add_book()
            elif choice == 2:
                self.Manager.print_library_book()
            elif choice == 3:
                self.Manager.print_books_by_prefix()
            elif choice == 4:
                self.Manager.Add_user()
            elif choice == 5:
                self.Manager.Borrow_book()
            elif choice == 6:
                self.Manager.Return_book()
            elif choice == 7:
                self.Manager.print_users_borrowed_book()
            elif choice == 8:
                self.Manager.print_users()
            else:
                exit()

App = FrontEndManager()
App.run()
