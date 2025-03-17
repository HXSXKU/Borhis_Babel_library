import string

# Defining an alphabet (Borges version includes 26 symbols(A-Z, " ", "." and "," )).
# You can change the alphabet anytime but keep in mind that your string will change their location in the 
# library because of different numeral system which depends on symbols count in alphabet.
ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZ ,."  # 29 символов

# Parameters
PAGE_CHARS = 40  # digits per row
LINES_PER_PAGE = 40  # rows per page
PAGES_PER_BOOK = 410  # pages per book

# Book total volume
BOOK_SIZE = PAGE_CHARS * LINES_PER_PAGE * PAGES_PER_BOOK

# Structure
BOOKS_PER_SHELF = 5  
SHELVES_PER_ROOM = 4  
ROOMS_PER_HALL = 10  
HALLS_PER_LIBRARY = 10  


def text_to_number(text, alphabet=ALPHABET):
    """Converting your string into l-numeral system, where l is equal to your alphabet symbol count"""
    base = len(alphabet)
    num = 0
    for char in text:
        num = num * base + alphabet.index(char)
    return num

def number_to_location(num):
    """Converting book number into library structure"""
    book_number = num // BOOK_SIZE  # The book where the string is
    page_offset = num % BOOK_SIZE   # inside book offset
    
    # unlimited dividing into shelves, rooms, halls, libraries
    shelf_number = book_number % BOOKS_PER_SHELF
    room_number = (book_number // BOOKS_PER_SHELF) % SHELVES_PER_ROOM
    hall_number = (book_number // (BOOKS_PER_SHELF * SHELVES_PER_ROOM)) % ROOMS_PER_HALL
    library_number = book_number // (BOOKS_PER_SHELF * SHELVES_PER_ROOM * ROOMS_PER_HALL)
    
    return {
        "library": library_number,
        "hall": hall_number,
        "room": room_number,
        "shelf": shelf_number,
        "book": book_number,
        "page_offset": page_offset
    }

def location_to_number(library, hall, room, shelf, book, page_offset):
    """Converting structure into book number """
    book_number = (
        library * (HALLS_PER_LIBRARY * ROOMS_PER_HALL * SHELVES_PER_ROOM * BOOKS_PER_SHELF) +
        hall * (ROOMS_PER_HALL * SHELVES_PER_ROOM * BOOKS_PER_SHELF) +
        room * (SHELVES_PER_ROOM * BOOKS_PER_SHELF) +
        shelf * BOOKS_PER_SHELF +
        book
    )
    return book_number * BOOK_SIZE + page_offset

def find_text_location(text):
    """Find location of your string in library"""
    text = text.upper().replace(" ", ".")  # just make sure it is uppercase in case u dont use double registry alphabet
    num = text_to_number(text)
    return number_to_location(num)

def find_text_by_location(library, hall, room, shelf, book, page_offset, length):
    """Find a given string in library by its coordinates"""
    num = location_to_number(library, hall, room, shelf, book, page_offset)
    return number_to_text(num, length)

def number_to_text(num, length, alphabet=ALPHABET):
    """Converting number back to string"""
    base = len(alphabet)
    text = ""
    for _ in range(length):
        text = alphabet[num % base] + text
        num //= base
    return text

while True:
    print("\nВыберите действие:")
    print("1 - Найти местоположение текста")
    print("2 - Найти текст по номеру")
    print("exit - Выйти из программы")
    
    choice = input("Choose an option (type 'exit to leave programme'): ").strip().lower()
    
    if choice == "exit":
        break
    
    if choice == "1":
        text = input("String to find in library: ").strip()
        location = find_text_location(text)
        print(f'String "{text}" Is located in : {location}')
    
    elif choice == "2":
        try:
            library = int(input("Number of library: "))
            hall = int(input("Hall number: "))
            room = int(input("Room number: "))
            shelf = int(input("shelf number: "))
            book = int(input("Book number: "))
            page_offset = int(input("Offset number: "))
            length = int(input("String length: "))
            restored_text = find_text_by_location(library, hall, room, shelf, book, page_offset, length)
            print(f'String found on this coordinates: "{restored_text}"')
        except ValueError:
            print("Insert apropriate numeric parameters.")
    else:
        print("Invalid input try again.")   
    