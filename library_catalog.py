# Module 0, Challenge 10: Library Catalog (Advanced)

catalog = {
    "Grapes of Wrath": 5,
    "The Art of War": 3,
    "Twilight": 2
}

def get_catalog():
    for book, num in catalog.items():
        print(f"  {book}: {num}")

def rent_book(book):
    if book in catalog:
        available = catalog.get(book)
        if available:
            catalog[book] -= 1
            print(f"    Checked out {book}")
        else:
            print("    Book not available.")
    else:
        print("    No such book in this library.")

def return_book(book):
    if book in catalog:
        catalog[book] += 1
    else:
        print("    Book does not belong to this library.")

if __name__ == '__main__':
    while True:
        print("Show, Rent, Return, Exit")
        command = input("What would you like to do? ")

        if command == "Show":
            get_catalog()
        elif command == "Rent":
            get_catalog()
            book = input("  Which book? ")
            rent_book(book)
        elif command == "Return":
            book = input("  Which book are you returning? ")
            return_book(book)
        elif command == "Exit":
            print("  Thank you for coming today.")
            break
        else:
            print("  Invalid command.")
