# M0_C10 - Library Catalog (Advanced)
Repository with prompt and code for Module 1, Challenge 10: Library Catalog (Advanced).

## Prompt
Starting with the example library catalog program we did together as the base, you will modify the program to accommodate some new features the local library is asking for.

### Requirements
- The catalog now keeps track of the authors of books.
- Each author may have more than one book associated with them, and each book will have a count describing the number of available copies in the catalog.
- You must add the following command:
  - `Add`: Adds a book to the catalog if it doesn't exist. See examples below.
- You must modify the following commands:
  - `Show`: Must now also print the author's name as part of the output. The authors must be printed alphabetically by first name. See examples below.
- The library starts with the following catalog:

Book Title                    | Author                  | Available Copies
------------------------------|-------------------------|-----------------
The Grapes of Wrath           | John Steinbeck          | 5
Of Mice and Men               | John Steinbeck          | 3
The Art of War                | Sun Tzu                 | 3
Twilight                      | Stephanie Meyer         | 2
Breaking Dawn                 | Stephanie Meyer         | 1
Cracking the Coding Interview | Gayle Laakmann McDowell | 7
Clean Code                    | Robert Martin           | 3
The Da Vinci Code             | Dan Brown               | 4

How you implement the structures and track the catalog is completely up to you. The tests only check for input & output.

See the examples below for usage.

## Example 1: Rent/Show
```
$ python3 library_catalog.py
Show, Add, Rent, Return, Exit
What would you like to do? Show
  Dan Brown:
    The Da Vinci Code: 4
  Gayle Laakmann McDowell:
    Cracking the Coding Interview: 7
  John Steinbeck:
    The Grapes of Wrath: 5
    Of Mice and Men: 3
  Robert Martin:
    Clean Code: 3
  Stephanie Meyer:
    Twilight: 2
    Breaking Dawn: 1
  Sun Tzu:
    The Art of War: 3

Show, Add, Rent, Return, Exit
What would you like to do? Rent
  Which book? The Grapes of Wrath
    Checked out The Grapes of Wrath
Show, Add, Rent, Return, Exit
What would you like to do? Show
  Dan Brown:
    The Da Vinci Code: 4
  Gayle Laakmann McDowell:
    Cracking the Coding Interview: 7
  John Steinbeck:
    The Grapes of Wrath: 4
    Of Mice and Men: 3
  Robert Martin:
    Clean Code: 3
  Stephanie Meyer:
    Twilight: 2
    Breaking Dawn: 1
  Sun Tzu:
    The Art of War: 3
```

## Example 2: Return/Show
```
Show, Add, Rent, Return, Exit
What would you like to do? Show
  Dan Brown:
    The Da Vinci Code: 4
  Gayle Laakmann McDowell:
    Cracking the Coding Interview: 7
  John Steinbeck:
    The Grapes of Wrath: 4
    Of Mice and Men: 3
  Robert Martin:
    Clean Code: 3
  Stephanie Meyer:
    Twilight: 2
    Breaking Dawn: 1
  Sun Tzu:
    The Art of War: 3
Show, Add, Rent, Return, Exit
What would you like to do? Return
  Which book? Breaking Dawn 
    Returned Breaking Dawn
Show, Add, Rent, Return, Exit
What would you like to do? Show
  Dan Brown:
    The Da Vinci Code: 4
  Gayle Laakmann McDowell:
    Cracking the Coding Interview: 7
  John Steinbeck:
    The Grapes of Wrath: 4
    Of Mice and Men: 3
  Robert Martin:
    Clean Code: 3
  Stephanie Meyer:
    Twilight: 2
    Breaking Dawn: 2
  Sun Tzu:
    The Art of War: 3
```

## Example 3: Add/Show
```
Show, Add, Rent, Return, Exit
What would you like to do? Add
  Title: The Docker Book
  Author: James Turnbull
  # Copies: 10
    Book added
Show, Add, Rent, Return, Exit
What would you like to do? Show
  Dan Brown:
    The Da Vinci Code: 4
  Gayle Laakmann McDowell:
    Cracking the Coding Interview: 7
  James Turnbull:
    The Docker Book: 10
  John Steinbeck:
    The Grapes of Wrath: 4
    Of Mice and Men: 3
  Robert Martin:
    Clean Code: 3
  Stephanie Meyer:
    Twilight: 2
    Breaking Dawn: 2
  Sun Tzu:
    The Art of War: 3
```

## Notes and Hints
- Make use of everything you've learned so far.
- **Remember indentation levels.**
- Remember to browse and read the tests (or execute them) to check what all is being tested!

## Knowledge Tested
- Conditionals
- Loops
- Nested Data Structures
- Type Conversion
- Reading Tests

## Instructions
1. Fork this repository to your own account.
2. Clone the forked repository to your local computer.
3. Inside `library_catalog.py`, you will implement your changes.  You'll be starting from the example problem code as a base.
4. While you're writing and/or when you're done, you can execute the provided tests to verify your program works by running `python3 test_library_catalog.py`. All tests are passing if you see `OK` in the output. You may also test manually.
