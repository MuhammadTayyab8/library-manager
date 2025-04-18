import json

class BooksCollection:
    """class to manage Books Collection data"""
    def __init__(self):
        self.book_list = []
        self.storage_file = "books_data.json"
        self.read_from_files()

    def read_from_files(self):
        """Method to read Books Collection data and store it to book_list"""
        try:
            with open(self.storage_file, "r") as file:
                 self.book_list = json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            self.book_list = []

    def save_to_file(self):
        """Method to save Books Collection in books_data.json file"""
        with open(self.storage_file, "w") as file:
            json.dump(self.book_list, file, indent=4)

    def create_new_book(self):
        """Method to create new Book"""
        print("Create New Book! \n")
        book_title = input("Enter Book Title: ").strip()
        book_author = input("Enter Author Name: ").strip()
        book_year = input("Enter Boos Year: ")
        is_book_read = input("Is You Read This Book? (yes / no): ").strip().lower() == "yes"

        new_book = {
            "title" : book_title,
            "author" : book_author,
            "year": book_year,
            "read" : is_book_read
        }

        self.book_list.append(new_book)
        self.save_to_file()
        print("Book Added Successfully! \n")

    def delete_book(self):
        """Method to delete Book"""
        print("Delete Book! \n")
        book_title = input("Enter a Book Title: ")
        for book in self.book_list:
            if book["title"].lower() == book_title.lower():
                self.book_list.remove(book)
                self.save_to_file()
                print("Book Deleted Successfully! \n")
                return
        print("Book Not Found! \n")

    def find_books(self):
        """Method to find Book by title and author name"""
        print("Find Book by Title and Author Name! \n")
        print("Find A Book")
        search_text = input("Enter Search Term: ")
        found_books = [
            book
            for book in self.book_list
            if search_text in book["title"].strip().lower()
            or search_text in book["author"].strip().lower()
        ]

        if found_books:
            print("Book Matched: \n")
            for index, book in enumerate(found_books, 1):
                reading_status = "Read" if book["read"] else "Unread"
                print(f"{index}. {book['title']} by {book['author']} ({book['year']}) - {reading_status}")
        else:
            print("No matching books found.\n")


    def update_book(self):
        """Method to update Book data"""
        print("Update Book! \n")
        book_title = input("Enter Book Title: ")
        for book in self.book_list:
            if book["title"].lower() == book_title.lower():
                print("Leave blank to keep existing value.")
                book["title"] = input(f"New title ({book['title']}): ") or book["title"]
                book["author"] = (
                    input(f"New author ({book['author']}): ") or book["author"]
                )
                book["year"] = input(f"New year ({book['year']}): ") or book["year"]
                book["read"] = (
                    input("Have you read this book? (yes/no): ").strip().lower()
                    == "yes"
                )
                self.save_to_file()
                print("Book updated successfully!\n")
                return
        print("Book not found!\n")

    def show_all_books(self):
        """Method to show all Books"""
        print("Show all Books! \n")
        if not self.book_list:
            print("Collection is empty.\n")
            return
        print("Books Collection: ")
        for index, book in enumerate(self.book_list, 1):
            reading_status = "Read" if book["read"] else "Unread"
            print(
                f"{index}. {book['title']} by {book['author']} ({book['year']}) - {reading_status}"
            )
        print()


    def show_progress(self):
        """Method to show libraray progress"""
        print("Library Progress! \n")
        total_book = len(self.book_list)
        completed_books = sum(1 for book in self.book_list if book["read"])
        completion_rate = (
            (completed_books / total_book * 100) if total_book > 0 else 0
        )
        print(f"Total books in collection: {total_book}")
        print(f"Reading progress: {completion_rate:.2f}%\n")

    def start_application(self):
        """Method to start the application"""
        while True:
            print("Welcome to Your Book Collection Manager!")
            print("1. Add a new book")
            print("2. Remove a book")
            print("3. Search for books")
            print("4. Update book details")
            print("5. View all books")
            print("6. View reading progress")
            print("7. Exit")
            user_choice = input("Please choose an option (1-7): ")

            if user_choice == "1":
                self.create_new_book()
            elif user_choice == "2":
                self.delete_book()
            elif user_choice == "3":
                self.find_books()
            elif user_choice == "4":
                self.update_book()
            elif user_choice == "5":
                self.show_all_books()
            elif user_choice == "6":
                self.show_progress()
            elif user_choice == "7":
                self.save_to_file()
                print("Thank you for using Book Collection Manager. Goodbye! \n")
                break
            else:
                print("Invalid choice. Please try again.\n")


if __name__ == "__main__":
    book_manager = BooksCollection()
    book_manager.start_application()