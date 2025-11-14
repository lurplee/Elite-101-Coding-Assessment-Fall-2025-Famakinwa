
# Psuedocode for each feature (From previously-created Google Doc)

## VIEW AVAILABLE BOOKS

* Create a list to hold all books
* Iterate through the list to print books where available == True, if not do not print anything

## RETURN

* Prompt user for book ID
* Verify that book ID is correct
* If book is not available, then return the book and print a success message
* If book is available, print that book has already been returned

## CHECKOUT

* Prompt user for book ID
* Verify that book ID is correct
* If book is available, then checkout the book and print a success message
* If book is not available, print that the book is not currently available
* POSSIBLY - add a confirm feature

## SEARCH BOOK

* Ask user if they would like to search by genre or author
* Ask user for their desired search term
* Iterate over books to print only books that match the search term
* FOR PARTIAL SEARCH: just check if search term is in the books rather than an exact match

## VIEW OVERDUE BOOKS

* Print all books if the checkout_date > datetime.now() (current date)

## MODIFY BOOKS: EDIT

* Ask for desired book to modify, based on book ID
* Verify that book ID exists, if not reprompt user
* Ask user if they want to modify -> Genre, Author, Title
* Implement change to book and print success message

## MODIFY BOOKS: ADD

* Prompt user for the new book's genre, title, and author -> Store values
* Create new book object with these entered values and append the object to books list
* Print the user's new book using view_books or something similar

## MODIFY BOOKS: REMOVE

* Ask for book ID and verify that it exists (if not, reprompt)
* Remove the book with said bookID from book list



## EXIT

* Use quit() or exit()

## MAIN MENU

* List menu items
* Use try-except for exception handling
* Include header for each item before each method is called