from library_books import library_books
from datetime import datetime, timedelta
import time
# Used Python Documentation to help review https://docs.python.org/3/tutorial/classes.html



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

    def return_book(self,user_id):
        if self.id == user_id:
            if self.available == True:
                print(f"{self.title.upper()} was already returned!")
            else:
                print(f"Book Returned! {self.id}")
        else: 
            return("")
            
            
for book_dict in library_books:
    book = MyBook(book_dict["id"], book_dict["title"], book_dict["author"], book_dict["genre"], book_dict["available"], book_dict["due_date"], book_dict["checkouts"])
    books.append(book)







class Library:
    def __init__(self):
        self.book = book

    def main_menu(self):
        menu_choice =""

        print(f"{self.header("MAIN MENU")}\n[1] View Books\n[2] Search Books\n[3] Checkout Book\n[4] Return Book\n[5] View Overdue Books")
        while menu_choice not in [1,2,3,4,5] or type(menu_choice) != int :
            menu_choice = int(input("Choice: "))


        if menu_choice == 1:
            print(self.header("VIEW ALL BOOKS"))
            self.view_books()
            self.main_menu()
        if menu_choice ==2:
            print(self.header("SEARCH ALL BOOKS"))
            self.search_books()
            self.main_menu()
        if menu_choice ==3:
            print(self.header("CHECKOUT BOOK"))
            self.book_checkout()
            self.main_menu()
        if menu_choice ==4:
            print(self.header("RETURN BOOK"))
            self.book_return()
            self.main_menu()
        if menu_choice ==5:
            print(self.header("VIEW OVERDUE BOOKS"))
            self.view_overdue_books()
            self.main_menu()


    #Adding additional function to format outputs
    def header(self, header_message):
        return (f"-------------------------------\n{header_message.upper()}\n-------------------------------\n")

    def divider(self, content,lines):
        if lines:
            return(f"-------------------------------\n{content}\n-------------------------------\n")
        else:
            return(f"\n{content}\n")

# -------- Level 1 --------
# TODO: Create a function to view all books that are currently available
# Output should include book ID, title, and author

    def view_books(self):
        for book in library_books:
            print(self.divider((f"Book ID: {book.get("id")}\nTitle: {book.get("title")}\nAuthor: {book.get("author")}"), False))

# Added extra methods to view specific books by book ID & access attributes within library_books

    def view_books_by_id(self,bookID):
        for book in BookObjList:
            if book.book_id == bookID:
                print(self.divider((f"Book ID: {book.get("id")}\nTitle: {book.get("title")}\nAuthor: {book.get("author")}\nCheckout Status: {book.get("available")}"),False))

    def book_detail(self,id,attribute):
        for book in library_books:
            if book.get("id") == id:
                return(book.get(attribute))


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
            search_filter = "author"
        if search_choice == 2:
            search_filter = "genre"

        print(f"Searching by {search_filter.upper()}...")
        time.sleep(0.5)
        search_term = input(f"{search_filter.title()} Name: ").title()

        for book in library_books:
            if search_term == book.get(search_filter):
                selected_books.append(book)

#Edit this line to be cooler
        print(self.divider(f"Searching for books with {search_filter.upper()} name {search_term.upper()}...",True))
        
        if len(selected_books) >0:
            for selected_book in selected_books:
                print(self.divider((f"Book ID: {selected_book.get("id")}\nTitle: {selected_book.get("title")}\nAuthor: {selected_book.get("author")}"),False))
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
        bookID_check = input("Book ID: ").upper()

        if bookID_check in self.bookID_list:
            if self.book_detail(bookID_check, "available") == True:
                print(f"{self.book_detail(bookID_check, "title")} is AVAILABLE")
                verify_checkout = input(f"Check Out {self.book_detail(bookID_check,"title")}? [Y/N]: ").upper()

                if verify_checkout == "Y":
                    for book in library_books:
                        if bookID_check in book.get("id"):
                            book["available"] = False
                            book["checkouts"] += 1
                            book["due_date"] = (datetime.now() + timedelta(days=14)).strftime("%Y-%m-%d")

                    print(self.divider(f"Thanks for Checking Out {self.book_detail(bookID_check, "title").upper()}\nDue Date: {book["due_date"]}", True))


                else:
                    print(f"Sorry, {self.book_detail(bookID_check, "title")} is NOT AVAILABLE")
                
        else:
            print("Book Not Found.")




# -------- Level 4 --------
# TODO: Create a function to return a book by ID
# Set its availability to True and clear the due_date
    def book_return(self):
        user_id = input("Book ID: ").upper()
        for book in books:
            print(book.return_book(user_id))
        
        # for book in library_books:
        #     if return_bookID == book.get("id") and book.get("available") == False:
        #         selected_book = book
        #         selected_book["available"] == True
        #         selected_book["due_date"] = None
        #         print(f"Returned {selected_book.get("title").upper()}!")
        #     if book.get("available") == True:
        #         print("Already returned!")
# TODO: Create a function to list all overdue books
# A book is overdue if its due_date is before today AND it is still checked out

    def view_overdue_books(self):
        overdue_books =[]
        for book in library_books:
            if book["due_date"] != None and datetime.strptime(book["due_date"],"%Y-%m-%d") < datetime.now() and book["available"] == False:
                overdue_books.append(book)
        print(overdue_books)




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
    myLibrary.book_return()
    pass
