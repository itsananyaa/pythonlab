# Define the structure of the database using lists and tuples
# Each book is represented as a tuple with (title, author, publication year)
database = []

# Function to add a book to the database
def add_book(title, author, year):
    book = (title, author, year)
    database.append(book)
    print(f"Book '{title}' by {author} added to the database.")

# Function to display all books in the database
def display_books():
    if not database:
        print("The database is empty.")
    else:
        print("Books in the database:")
        for book in database:
            print(f"Title: {book[0]}, Author: {book[1]}, Year: {book[2]}")

# Example usage
add_book("The Great Gatsby", "F. Scott Fitzgerald", 1925)
add_book("To Kill a Mockingbird", "Harper Lee", 1960)
add_book("1984", "George Orwell", 1949)

display_books()
