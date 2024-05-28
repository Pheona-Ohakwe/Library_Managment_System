from book import Book
from user import User
from genre import Genre
from author import Author
import re
import random

class Library:

    def __init__(self):
        self.books = {} 
        self.current_loans = {}
        self.users = {}
        self.genres = []
        self.authors = {}

    def add_book(self):
        isbn = input('Enter the last 10 digits of the isbn in this form "##-####-##-#": ')
        verified_isbn = re.match (r"\d{2}-\d{5}-\d{1}", isbn)
        if verified_isbn:
            print("Valid ISBN")
            title = input("Enter book title: ").upper()
            author_first_name = input("Enter book author first name: ").title()
            author_last_name = input("Enter the book author last name: ").title()
            author_name = author_first_name + "  " + author_last_name
            biography = input("Enter short bio about author: ").lower()
            publication_date = input('Enter book publication date in this form "##-#####-##-##": (2 digit month, 2 digit day, 4 digit year):')
            verified_pub_date = re.match(r"\d{2}-\d{2}-\d{4}", publication_date)
            if verified_pub_date:
                print("Valid publication date")
                genre_name = input("Enter the genre name you would like to add: ").title()
                genre_category = input('Enter the genre category: Some examples are "Fiction", "Sci-Fi, "Romance", "Comedy", "Mystery", "Thriller":').title()
                print()
            else:
                print("Invalid publication date")
                self.add_book()
        else:
            print ("INVALID ISBN")
            self.add_book()
        author = Author(author_name, biography)
        self.authors[author_name] = biography
        genre = Genre(genre_name, genre_category)
        self.genres.append(genre)
        book = Book(isbn, title, author, publication_date, genre_name, genre_category)
        self.books[isbn] = book
        print(f"Book added successfully: \n{book}")

    def checkout_book(self):
        user = input('To checkout a book you must have a Library ID; Do you have a Library ID? Enter "yes" or "no" ').lower()
        if user == "no":
            print("Creating a Library ID")
            self.add_user()
        elif user == "yes":
            print("Membership confirmed")
            isbn = input('Enter the ISBN of the book to borrow. In this form "##-#####-##-#": ')
            verified_isbn = re.match(r"\d{2}-\d{5}-\d{2}-\d{1}", isbn)
            if verified_isbn:
                print("Valid ISBN")
                library_id = input("Enter your 6 digit library ID: ")
                if library_id.isdigit():
                    user_id = int(library_id)
                    if isbn in self.books:
                        book = self.books[isbn]
                        print()
                        print(f"Book found:{book}")        
                        if book.is_available():
                            print("Book is available for checkout")
                            print()
                            if user:
                                book.set_is_available(False)
                                self.current_rented_books[isbn] = user_id
                                user = self.users.get(user_id)
                                if user:
                                    user.add_borrowed_books(book)
                                    print(f"Book '{book.title}' checked out to {user.name}")
                                    print()
                        else:
                            print("That user couldn't be found")
                    else:
                      print("That book is unavailable")
                else:
                    print("No book found that by that ISBN")
            else:
                print("Invalid ISBN")
        else: 
            print("Invalid input")
        

def return_book(self):
        isbn = input('Enter the ISBN of the book to borrow. In this form "##-#####-##-#":')
        verified_isbn = re.match(r"\d{2}-\d{5}-\d{2}-\d{1}", isbn)
        if verified_isbn:
            print("Valid ISBN")
            if isbn in self.books and isbn in self.current_rented_books:
               title = self.books[isbn].get_title()
               self.books[isbn].return_book()
               del self.current_rented_books[isbn]
               print(f"Book '{title}' was returned")
               print()
            else:
               print("No book found by that information" )
        else:
            print("Invalid ISBN")

def search_for_book(self):
    isbn = input('Enter the ISBN of the book to borrow. In this form "##-#####-##-#": ')
    verified_isbn = re.match(r"\d{2}-\d{5}-\d{2}-\d{1}", isbn)
    if verified_isbn:
        print("Valid ISBN")
        book = self.books.get(isbn)
        if book:
            print()
            print("Here is the book that matched the ISBN you entered:")
            print(book)
            print()
        else:
            print("The ISBN did not match any of the books in the library.")
            self.search_for_book()
    else:
        print("Invalid ISBN")
        self.search_for_book()

def display_books(self):
    print()
    print("Here is a list of all the books in the library:")
    for isbn, book in self.books.items():
        print(book)
        print()

def add_user(self):
    user_name = input(" Input first and last name: ").title()
    print()
    if user_name not in self.users:
        random_num = 5000
        library_id = random.randrange(111111, 999999, random_num)
        user = User(user_name, library_id)
        self.users[library_id] = user
        print(f"{user.name} was added as a new user. Your library ID is {library_id}")
        print()
    else:
        print("The library id you entered does not match any of the user's.")
        self.add_user()

def view_user_details(self):
    library_id =input("Enter the six digit library ID of the user you would like to view details on: ")
    user = self.users.get(int(library_id))
    if user:
        print("Here are the user's details: ")
        print(user)
        print()
    else:
        print("The library id you entered does not match any of the user's.")
        self.view_user_details()

def display_users(self):
    print("Here are all the details of all users.")
    for user in self.users.values():
        print(user)

def borrowed_books(self):
        library_id = input("Enter book author first name")
        library_id = int(library_id)
        user = self.users.get(library_id)
        if user:
            print(f"Here is a list of borrowed books by {user.name}: ")
            for book in user.borrowed_books:
                print(book.title)
        else:
            print("The library id you entered does not match any of the users.")
            self.borrowed_books()

def add_author(self):
        author_first_name = input ("Enter author's first name: ").title()
        author_last_name = input ("Enter the last name of the author's last name: ").title()
        author = author_first_name + "  " + author_last_name
        biography = input("Enter a short bio about the author: ").lower()
        author = Author(author, biography)
        self.authors[author] = biography
        print()
        print(f'"{author}" was added!')

def view_author_details(self):
        author_first_name = input ("Enter author's first name: ").title()
        author_last_name = input ("Enter the last name of the author's last name: ").title()
        author = author_first_name + "  " + author_last_name
        for key, value in self.authors.items():
            if key == author:
                print()
                print(f'Author: {author}, Biography: {value}')
                break
            else:
                print("The name you entered does not match any of these authors.")
                self.view_author_details()

def display_authors(self):
     print("Here are the details of all the Authors: ")
     for author in self.authors:
        print(author)

def add_genre(self):
    genre_name = input("Enter the genre name you would like t add: ").title()
    genre_category = input('Enter the genre category: Some examples are: "Fiction", "Sci-Fi, "Romance", "Comedy", "Mystery", "Thriller":').title()
    genre = Genre(genre_name, genre_category)
    self.genres.append(genre)
    print()
    print(f'"{genre_name}" was added as a new genre and assigned to the category of "{genre_category}".')

def view_genre_details(self):
    print("Here is a list of genre's with the assigned category names: ")
    for genre in self.genres:
        print(f"Genre: {Genre.genre_name}. |  Category: {Genre.genre_category}")

def display_genres(self):
    print("Here is the list of genres: ")
    for genre in self.genres:
        print(genre.genre_name)
     