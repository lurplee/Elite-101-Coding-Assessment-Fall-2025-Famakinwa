from library_books import library_books
from datetime import datetime, timedelta
import time
import csv
# Used Python Documentation to help review https://docs.python.org/3/tutorial/classes.html
# Learned how to clear screen after each option using https://www.geeksforgeeks.org/python/clear-screen-python/



books =[]


class MyBook:
    def __init__(self, id,title, author, genre,available, due_date,checkouts):
        #Intializing instance variables
        self.id = id
        self.title = title
        self.author = author
        self.genre = genre
        self.available = available
        self.due_date = due_date
        self.checkouts = checkouts
    
    #Divider method for formatting answers

    def divider(self, content,lines):
        if lines:
            return(f"{'='*(len(content)+3)}\n{content}\n{'='*(len(content)+3)}")
        else:
            return(f"\n{content}\n")
    
    #Viewing a single book
    def view_book(self):
        return(f"\nBook ID: {self.id}\nTitle: {self.title}\nAuthor: {self.author}\n")
    
    #Viewing a single book, based on bookID
    def view_specific_book(self,bookID):
        if self.id == bookID:
            return(f"\nBook ID: {self.id}\nTitle: {self.title}\nAuthor: {self.author}\nGenre: {self.genre}\n")
    # Viewing a book IF available
    def view_available_book(self):
        if self.available == True:
            return(f"\nBook ID: {self.id}\nTitle: {self.title}\nAuthor: {self.author}\n")
    

    # Returning a Book
    def return_book(self,entered_bookID):
        if self.id == entered_bookID:
            if self.available == True:
                print(f"{self.title.upper()} by {self.author.upper()} was already returned!")
            else:
                self.available = True
                print(f"Thanks for returning {self.title.upper()} by {self.author.upper()}!")
    # Searching for a book based on GENRE or AUTHOR    
    def search_book(self, search_field, search_term):
        if search_field.lower() == "author":
            #Adding "in" instead of "==" allows for partial search
            if search_term.lower() in self.author.lower():
                return("SUCCESS") #return needed due to conditional in search_books() in Library Class

        if search_field.lower() == "genre":
            if search_term.lower() in self.genre.lower():
                return("SUCCESS")  #return needed due to conditional in search_books() in Library Class

        else:
            return(None)
    
    # View a Book IF overdue
    def view_overdue_book(self):
         if self.due_date != None and datetime.strptime(self.due_date,"%Y-%m-%d") < datetime.now() and self.available == False:
             return("SUCCESS") #return needed due to conditional in search_books() in Library Class

    # Check out a book based on AVAILABILITY and ID
    def checkout_book(self, bookID):
        if bookID == self.id and self.available:
                    
                    print(f"{self.title.upper()} by {self.author.upper()} is AVAILABLE")

                    verify_checkout = input(f"Check Out {self.title.upper()}? [Y/N]: ").upper()
                    if verify_checkout == "Y":
                        self.checkouts += 1
                        self.due_date = (datetime.now() + timedelta(days=14)).strftime("%Y-%m-%d")
                        self.available = False
                        print(self.divider(f"Thanks for Checking Out {self.title.upper()}!\nDue Date: {self.due_date}",True))
                    
        elif bookID ==self.id and not self.available:
            print(f"Sorry, {self.title.upper()} is NOT AVAILABLE at the moment")

                
        else:
            return(None)

    # Edit Book's Author, Genre, or Title
    def edit_book(self,bookID):
        if bookID == self.id:
            change_choice =1
            original_info=""
            edited_info=""
            edit_category=""

            while True:
                try:

                    change_choice =int(input("\n[1] Author\n[2] Title\n[3] Genre\n[4] EXIT\n"))
                    if change_choice not in [1,2,3,4]:
                        raise Exception("Invalid Choice")
                    

                    if change_choice == 1:
                        print(self.divider("EDITING AUTHOR",True))
                        edit_category = "Author"
                        original_info = self.author
                        edited_info = input(f"CURRENT AUTHOR: {original_info}\nNEW AUTHOR: ")
                        self.author = edited_info
                        print(self.divider(f"Edited {self.title.upper()}'s {edit_category} from {original_info} to {edited_info}",True))


                    elif change_choice ==2:
                        edit_category = "Title"
                        print(self.divider("EDITING TITLE",True))
                        original_info = self.title
                        edited_info = input(f"CURRENT TITLE: {original_info}\nNEW TITLE: ")
                        self.title = edited_info
                        print(self.divider(f"Edited {self.title.upper()}'s {edit_category} from {original_info} to {edited_info}",True))

                    elif change_choice ==3:
                        edit_category ="Genre"
                        print(self.divider("EDITING GENRE",True))
                        original_info = self.genre
                        edited_info = input(f"CURRENT GENRE: {original_info}\nNEW GENRE: ")
                        self.author = edited_info
                        print(self.divider(f"Edited {self.title.upper()}'s {edit_category} from {original_info} to {edited_info}",True))

                    else:
                        self.divider("EXITING..",True)
                        time.sleep(0.3)
                    break
             
                except:
                    print("Invalid Response. Please Choose a New Choice")


#Creates a list of objects based on dictonaries in list library_books
                
for book_dict in library_books:
    book = MyBook(book_dict["id"], book_dict["title"], book_dict["author"], book_dict["genre"], book_dict["available"], book_dict["due_date"], book_dict["checkouts"])
    books.append(book)






#LIBRARY CLASS -> used to iterate over book in books for functions requiring multiple books
class Library:
    def __init__(self):
        self.book = book
    
    # Returning to Menu after each Action
    def menu_return(self):
        input(self.divider("Press ENTER to Return to HOME",True)+"\n")
        print("\x1b[H\x1b[2J", end="") #Adapted from https://github.com/orgs/pybricks/discussions/1074
        self.main_menu()

    # Creating a Main Menu
    def main_menu(self):
        menu_choice =""
        print(f"{self.header("WELCOME TO LIBRARY MANAGER")}\n[1] View Available Books\n[2] Search Books\n[3] Checkout Book\n[4] Return Book\n[5] View Overdue Books\n[6] Modify Book List\n[7] Download Catalog as CSV\n[8] EXIT")

        while True:
            try:
                menu_choice =int(input("Choice: "))
                if menu_choice not in [1,2,3,4,5,6,7,8]:
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
                if menu_choice ==6:
                    self.modify_book_list()
                    self.menu_return()
                if menu_choice ==7:
                    self.download_catalog()
                    self.menu_return()
                if menu_choice ==8:
                    print(self.header("Thank you for using Library Manager. Goodbye!"))
                    return(False)
            except:
                print(f"{self.header("WELCOME TO LIBRARY MANAGER")}\n[1] View Available Books\n[2] Search Books\n[3] Checkout Book\n[4] Return Book\n[5] View Overdue Books\n[6] Modify Book List\n[7] Download Catalog as CSV\n[8] EXIT")
                print("Invalid Response. Please Choose a New Choice")



    #Adding additional function to format outputs
    def header(self, header_message):
        return (f"{'-'*(len(header_message)+3)}\n{header_message.upper()}\n{'-'*(len(header_message)+3)}\n")

    def divider(self, content,lines):
        if lines:
            return(f"===============================================\n{content}\n===============================================")
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

        # Prompts user to choose to search by author or genre
        search_choice = int(input("Search by:\n[1] AUTHOR\n[2] GENRE\n"))

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
                print(selected_book.view_book()+f"Genre: {selected_book.genre}\n")
        else:
            print("NO RESULTS")



    # Forces user to input a valid book ID before proceeding

    def verify_id(self,entered_bookID):
        book_found = False
        while entered_bookID and book_found == False:
  
            for book in books: 
                if entered_bookID == book.id:
                    book_found = True
                    break

            if not book_found:
                print("Book ID not Found. Please Try Again.")
                entered_bookID = input("Book ID: ").upper()
            else:
                break

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
        self.verify_id(bookID)      



        # Runs checkout_book Function from myBook Class for each book

        for book in books:
            if book.checkout_book(bookID) != None:
                print(book.checkout_book(bookID))



# -------- Level 4 --------
# TODO: Create a function to return a book by ID
# Set its availability to True and clear the due_date
    def book_return(self):
        bookID = input("Book ID: ").upper()
        self.verify_id(bookID)  


         # Runs return_book Function from myBook Class for each book
        for book in books:
            if book.return_book(bookID) != None:
                print(book.return_book(bookID))
        

# TODO: Create a function to list all overdue books
# A book is overdue if its due_date is before today AND it is still checked out

    def view_overdue_books(self):
        overdue_books =[]
        for book in books:
            if book.view_overdue_book() != None:
                overdue_books.append(book)
        
        for overdue_book in overdue_books:
            print(self.divider(overdue_book.view_book()+ f"Due Date: {overdue_book.due_date}\n",True))



# -------- Level 5 --------
# TODO: Convert your data into a Book class with methods like checkout() and return_book()
# TODO: Add a simple menu that allows the user to choose different options like view, search, checkout, return, etc.



    # Modify, add, or remove a book
    def modify_book_list(self):

        modify_choice =1
        while True:
            try:
                print(self.header("MODIFY BOOK"))
                modify_choice =int(input("[1] Edit Book\n[2] Add Book\n[3] Remove Book\n[4] EXIT\n"))
                if modify_choice not in [1,2,3,4]:
                    raise Exception("Invalid Choice")
                

                if modify_choice ==1 or modify_choice ==3:
                    bookID = input("Book ID: ").upper()
                    self.verify_id(bookID)

                    print(self.header("Current Book Info"))
                    for book in books:
                        if bookID == book.id:
                            print(book.view_specific_book(bookID))

                    if modify_choice == 1:
                        print(self.header("EDIT BOOK BY"))
                        self.edit_books(bookID)
                    if modify_choice ==3:
                        print(self.header("REMOVED BOOK"))
                        self.remove_books(bookID)
                
                if modify_choice ==2:
                    print(self.header("ADD BOOK"))
                    print(self.add_books())
                else:
                    print(self.header("EXITING..."))
                    time.sleep(0.3)
                    break

         
            except:
                print("Invalid Choice - Please Try Again.")
        

        
    # Uses edit_book() function from myBook class
    def edit_books(self,bookID):
        for book in books:
            if book.edit_book(bookID) != None:
                book.edit_book(bookID)

    
    def add_books(self):
        #Necessary so that the new book's id is correct even if a book is removed
        for book in books:
            num=int(book.id[1])
            max_bookID =0
            if num > max_bookID:
                max_bookID = num
                
        new_bookID = f"B{max_bookID+1}"
        new_book_title = input("Book Title: ").title()
        new_book_author = input("Book Author: ").title()
        new_book_genre = input("Book Genre: ").title()

        # Creates new object from MyBook class based on user input
        new_book = MyBook(new_bookID, new_book_title, new_book_author, new_book_genre, True, None, 0)
        books.append(new_book)
        return(f"{self.header("BOOK CREATED")}\n{self.divider(new_book.view_book()+f"Genre: {new_book_genre}\n", True)}")

    def remove_books(self,bookID):
        for book in books:
            if book.id.upper() == bookID :
                print(self.divider(f"{book.title.upper()} has been removed!", True))
                books.remove(book)
    # Download Book Catalog as CSV - Used https://docs.python.org/3/library/csv.html for help
    def download_catalog(self):
        checked_out =""
        book_due_date =""
        file_name = f"{(datetime.now().strftime("%Y-%m-%d"))}_library_catalog.csv"
        with open(file_name, 'w', newline='') as csvfile:
            column_names = ["Book ID","Title", "Author", "Genre", "Checked Out", "Checkouts", "Due Date"]
            myWriter = csv.writer(csvfile)

            myWriter.writerow(column_names)
            for book in books:
                if book.available == False:
                    checked_out = "Yes"
                else:
                    checked_out="No"
                if book.due_date != None:
                    book_due_date =book.due_date
                else:
                    book_due_date = "None"
                myWriter.writerow([book.id, book.title,book.author, book.genre, checked_out, book.checkouts, book_due_date])
        print(self.header(f"CSV File, {file_name} Downloaded!"))


# -------- Optional Advanced Features --------
# You can implement these to move into Tier 4:
# - Add a new book (via input) to the catalog DONE
# - Sort and display the top 3 most checked-out books
# - Partial title/author search DONE
# - Save/load catalog to file (CSV or JSON) DONE
# - Anything else you want to build on top of the system!

if __name__ == "__main__":
    myLibrary = Library()
    myLibrary.main_menu()
    pass
