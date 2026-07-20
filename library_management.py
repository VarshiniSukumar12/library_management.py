library = []

while True:
    print("\n===== LIBRARY MANAGEMENT SYSTEM =====")
    print("1. Add Book")
    print("2. View Books")
    print("3. Search Book")
    print("4. Issue Book")
    print("5. Return Book")
    print("6. Delete Book")
    print("7. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        book = input("Enter Book Name: ")
        author = input("Enter Author Name: ")
        library.append({"book": book, "author": author, "issued": False})
        print("Book added successfully!")

    elif choice == "2":
        if not library:
            print("No books available.")
        else:
            print("\nBook List:")
            for i, b in enumerate(library, start=1):
                status = "Issued" if b["issued"] else "Available"
                print(f"{i}. {b['book']} - {b['author']} ({status})")

    elif choice == "3":
        search = input("Enter Book Name: ")
        found = False
        for b in library:
            if b["book"].lower() == search.lower():
                status = "Issued" if b["issued"] else "Available"
                print(f"Book: {b['book']}")
                print(f"Author: {b['author']}")
                print(f"Status: {status}")
                found = True
                break
        if not found:
            print("Book not found.")

    elif choice == "4":
        book = input("Enter Book Name to Issue: ")
        for b in library:
            if b["book"].lower() == book.lower():
                if not b["issued"]:
                    b["issued"] = True
                    print("Book issued successfully!")
                else:
                    print("Book is already issued.")
                break
        else:
            print("Book not found.")

    elif choice == "5":
        book = input("Enter Book Name to Return: ")
        for b in library:
            if b["book"].lower() == book.lower():
                if b["issued"]:
                    b["issued"] = False
                    print("Book returned successfully!")
                else:
                    print("Book was not issued.")
                break
        else:
            print("Book not found.")

    elif choice == "6":
        book = input("Enter Book Name to Delete: ")
        for b in library:
            if b["book"].lower() == book.lower():
                library.remove(b)
                print("Book deleted successfully!")
                break
        else:
            print("Book not found.")

    elif choice == "7":
        print("Thank you for using Library Management System!")
        break

    else:
        print("Invalid choice! Please try again.")