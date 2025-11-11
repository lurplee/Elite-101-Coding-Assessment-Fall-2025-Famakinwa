from library_books import library_books
from datetime import datetime, timedelta
import time
import os 
# Used Python Documentation to help review https://docs.python.org/3/tutorial/classes.html
# Learned how to clear screen after each option using https://www.geeksforgeeks.org/python/clear-screen-python/



books =[]


class MyBook:
    def __init__(self, id,title, author, genre,available, due_date,checkouts):
        self.id = id
        self.title = title
        self.author = author
        self.genre = genre
        self.available = available
        self.due_date = due_date
        self.checkouts = checkouts

    def view_book(self):
        return(f"\nBook ID: {self.id}\nTitle: {self.title}\nAuthor: {self.author}\n")
        
    def view_available_book(self):
        if self.available == True:
            return(f"\nBook ID: {self.id}\nTitle: {self.title}\nAuthor: {self.author}\n")
        

    def return_book(self,user_id):
        if self.id == user_id:
            if self.available == True:
                return(f"{self.title.upper()} by {self.author.upper()} was already returned!")
            else:
                self.available = True
                return(f"Thanks for returning {self.title.upper()} by {self.author.upper()}!")
            
    def search_book(self, search_field, search_term):
        if search_field.lower() == "author":
            if self.author == search_term.title():
                return("SUCCESS")

        if search_field.lower() == "genre":
            if self.genre == search_term.title():
                return("SUCCESS")

        else:
            return(None)
        
    def view_overdue_book(self):
         if self.due_date != None and datetime.strptime(self.due_date,"%Y-%m-%d") < datetime.now() and self.available == False:
             return("SUCCESS")

    def checkout_book(self, bookID):
        if bookID == self.id and self.available:
                    
                    print(f"{self.title.upper()} by {self.author.upper()} is AVAILABLE")

                    verify_checkout = input(f"Check Out {self.title.upper()}? [Y/N]: ").upper()
                    if verify_checkout == "Y":
                        self.checkouts += 1
                        self.due_date = (datetime.now() + timedelta(days=14)).strftime("%Y-%m-%d")
                        self.available = False
                        print(f"Thanks for Checking Out {self.title.upper()}!\nDue Date: {self.due_date}")
                    
        elif bookID ==self.id and not self.available:
            print(f"Sorry, {self.title.upper()} is NOT AVAILABLE at the moment")

                
        else:
            return(None)


                
for book_dict in library_books:
    book = MyBook(book_dict["id"], book_dict["title"], book_dict["author"], book_dict["genre"], book_dict["available"], book_dict["due_date"], book_dict["checkouts"])
    books.append(book)







class Library:
    def __init__(self):
        self.book = book

    def menu_return(self):
        input(self.divider("Press ENTER to Return to HOME",True))
        print("\x1b[H\x1b[2J", end="") #Adapted from https://github.com/orgs/pybricks/discussions/1074
        self.main_menu()

    def main_menu(self):
        menu_choice =""
        print(f"{self.header("MAIN MENU")}\n[1] View Books\n[2] Search Books\n[3] Checkout Book\n[4] Return Book\n[5] View Overdue Books")

        while menu_choice != None:
            try:
                menu_choice =int(input("Choice: "))
                if menu_choice not in [1,2,3,4,5]:
                    print("Invalid Choice. Please Try Again.")
                    raise Exception("Invalid Choice")
                    

                if menu_choice == 1:
                    print(self.header("VIEW ALL AVAILABLE BOOKS"))
                    self.view_available_books()
                    self.menu_return()
                if menu_choice ==2:
                    print(self.header("SEARCH ALL BOOKS"))
                    self.search_books()
                    self.menu_return()
                if menu_choice ==3:
                    print(self.header("CHECKOUT BOOK"))
                    self.book_checkout()
                    self.menu_return()
                if menu_choice ==4:
                    print(self.header("RETURN BOOK"))
                    self.book_return()
                    self.menu_return()
                if menu_choice ==5:
                    print(self.header("VIEW OVERDUE BOOKS"))
                    self.view_overdue_books()
                    self.menu_return()
            except:
                print(f"{self.header("MAIN MENU")}\n[1] View Books\n[2] Search Books\n[3] Checkout Book\n[4] Return Book\n[5] View Overdue Books")
                print("Invalid Response. Please Choose a New Choice")



    #Adding additional function to format outputs
    def header(self, header_message):
        return (f"-------------------------------\n{header_message.upper()}\n-------------------------------\n")

    def divider(self, content,lines):
        if lines:
            return(f"===========================\n{content}\n===========================\n")
        else:
            return(f"\n{content}\n")

# -------- Level 1 --------
# TODO: Create a function to view all books that are currently available
# Output should include book ID, title, and author

    def view_available_books(self):
        for book in books:
            if book.view_available_book() != None:
                print(self.divider(book.view_available_book(), True))

# Added extra methods to view specific books by book ID & access attributes within library_books

# -------- Level 2 --------
# TODO: Create a function to search books by author OR genre
# Search should be case-insensitive
# Return a list of matching books
    def search_books(self):
        selected_books =[]
        search_choice = 0
        while search_choice not in [1,2]:
            search_choice = int(input("Search by:\n[1] AUTHOR\n[2] GENRE\n"))

        if search_choice == 1:
            user_search_field = "author"
        if search_choice == 2:
            user_search_field = "genre"

        print(f"Searching by {user_search_field.upper()}...")
        time.sleep(0.5)
        user_search_term = input(f"{user_search_field.title()} Name: ").title()


        print(self.divider(f"Searching for books with {user_search_field.upper()} name {user_search_term.upper()}...",True))
        
        for book in books:
            if book.search_book(user_search_field, user_search_term) != None:
                selected_books.append(book)
        
        if len(selected_books) >0:
            for selected_book in selected_books:
                selected_book.view_book()
        else:
            print("NO RESULTS")





# -------- Level 3 --------
# TODO: Create a function to checkout a book by ID
# If the book is available:
#   - Mark it unavailable
#   - Set the due_date to 2 weeks from today
#   - Increment the checkouts counter
# If it is not available:
#   - Print a message saying it's already checked out


    def book_checkout(self):
        bookID = input("Book ID: ").upper()        
        
        # while bookID not in books: 
        #     print("Book ID not Found. Please Try Again.")
        #     bookID = input("Book ID: ").upper()

        for book in books:
            if book.checkout_book(bookID) != None:
                print(book.checkout_book(bookID))



# -------- Level 4 --------
# TODO: Create a function to return a book by ID
# Set its availability to True and clear the due_date
    def book_return(self):
        user_id = input("Book ID: ").upper()

        for book in books:
            if book.return_book(user_id) != None:
                print(book.return_book(user_id))
        

# TODO: Create a function to list all overdue books
# A book is overdue if its due_date is before today AND it is still checked out

    def view_overdue_books(self):
        overdue_books =[]
        for book in books:
            if book.view_overdue_book() != None:
                overdue_books.append(book)
        
        for overdue_book in overdue_books:
            print(self.divider(overdue_book.view_book(),True))



# -------- Level 5 --------
# TODO: Convert your data into a Book class with methods like checkout() and return_book()
# TODO: Add a simple menu that allows the user to choose different options like view, search, checkout, return, etc.

# -------- Optional Advanced Features --------
# You can implement these to move into Tier 4:
# - Add a new book (via input) to the catalog DO
# - Sort and display the top 3 most checked-out books
# - Partial title/author search DO
# - Save/load catalog to file (CSV or JSON)
# - Anything else you want to build on top of the system!

if __name__ == "__main__":
    myLibrary = Library()
    myLibrary.main_menu()
    pass
