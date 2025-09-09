def display_menu():
    print("=== Welcome to the Library System ===")
    print("1. Add a new book")
    print("2. Display all books")
    print("3. Search for a book")
    print("4. Remove a book")
    print("5. Exit")

library_db = {"Titles": [], "Authors": [], "Years": []}

while True:
    display_menu()
    try:
        choice = int(input("Select an option (1-5): "))
        if choice == 1:
            book_title = input("Enter the book title: ")
            book_author = input("Enter the author's name: ")
            try:
                publish_year = int(input("Enter the year of publication: "))
            except ValueError:
                print("Invalid year. Please enter a valid number.")
                continue
            library_db["Titles"].append(book_title)
            library_db["Authors"].append(book_author)
            library_db["Years"].append(publish_year)
            print("Book added successfully!")
        elif choice == 2:
            if not library_db["Titles"]:
                print("No books available in the library.")
            else:
                for i in range(len(library_db["Titles"])):
                    print(f"{i+1}. Title: {library_db['Titles'][i]} | Author: {library_db['Authors'][i]} | Year: {library_db['Years'][i]}")
        elif choice == 3:
            search_title = input("Enter the book title to search: ")
            if search_title in library_db["Titles"]:
                idx = library_db["Titles"].index(search_title)
                print(f"Title: {library_db['Titles'][idx]} | Author: {library_db['Authors'][idx]} | Year: {library_db['Years'][idx]}")
            else:
                print("Book not found in the library.")
        elif choice == 4:
            delete_title = input("Enter the title of the book to delete: ")
            if delete_title in library_db["Titles"]:
                idx = library_db["Titles"].index(delete_title)
                library_db["Titles"].pop(idx)
                library_db["Authors"].pop(idx)
                library_db["Years"].pop(idx)
                print("Book removed successfully!")
            else:
                print("Book not found in the library.")
        elif choice == 5:
            print("Exiting the Library System.")
            break
        else:
            print("Please choose a valid option (1 to 5).")
    except ValueError:
        print("Invalid input. Please enter a number (1 to 5).")
