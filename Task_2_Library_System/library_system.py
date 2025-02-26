import os
import json

# File paths
BOOK_REQUESTS_FILE = "book_requests.txt"
LIBRARY_LOG_FILE = "library_log.txt"
BORROWED_BOOKS_FILE = "borrowed_books.txt"

# Sample books available in the library
AVAILABLE_BOOKS = {
    "1": "The Great Gatsby",
    "2": "1984",
    "3": "To Kill a Mockingbird",
    "4": "Pride and Prejudice",
    "5": "The Catcher in the Rye"
}

# Ensure necessary files exist
for file in [BOOK_REQUESTS_FILE, LIBRARY_LOG_FILE, BORROWED_BOOKS_FILE]:
    if not os.path.exists(file):
        with open(file, "w", encoding="utf-8") as f:
            f.write("[]") if "book_requests" in file or "borrowed_books" in file else f.write("")

# Function to log actions (fixes Unicode error)
def log_action(action):
    with open(LIBRARY_LOG_FILE, "a", encoding="utf-8") as log_file:
        log_file.write(f"{action}\n")

# Function to load book requests (Fix: Always return valid JSON)
def load_requests():
    try:
        with open(BOOK_REQUESTS_FILE, "r", encoding="utf-8") as file:
            content = file.read().strip()
            return json.loads(content) if content else []
    except (json.JSONDecodeError, FileNotFoundError):
        return []

# Function to save book requests
def save_requests(requests):
    with open(BOOK_REQUESTS_FILE, "w", encoding="utf-8") as file:
        json.dump(requests, file, indent=4)

# Function to load borrowed books
def load_borrowed_books():
    try:
        with open(BORROWED_BOOKS_FILE, "r", encoding="utf-8") as file:
            content = file.read().strip()
            return json.loads(content) if content else []
    except (json.JSONDecodeError, FileNotFoundError):
        return []

# Function to save borrowed books
def save_borrowed_books(borrowed_books):
    with open(BORROWED_BOOKS_FILE, "w", encoding="utf-8") as file:
        json.dump(borrowed_books, file, indent=4)

# Function to view available books
def view_books():
    print("\n📚 Available Books:")
    for key, title in AVAILABLE_BOOKS.items():
        print(f"{key}. {title}")

# Function to request a book (Fix: Prevent duplicate requests)
def request_book():
    view_books()
    book_id = input("\nEnter the book number you want to request: ").strip()

    if book_id not in AVAILABLE_BOOKS:
        print("❌ Invalid book selection. Try again.")
        return

    student_name = input("Enter your name: ").strip()
    if not student_name:
        print("❌ Name cannot be empty.")
        return

    while True:
        priority = input("Enter priority (1-10, or leave blank for default 5): ").strip()
        if priority.isdigit() and 1 <= int(priority) <= 10:
            priority = int(priority)
            break
        elif priority == "":
            priority = 5  # Default priority
            break
        else:
            print("❌ Invalid priority. Enter a number between 1 and 10.")

    requests = load_requests()

    # Prevent duplicate requests from the same student
    for request in requests:
        if request["student"].lower() == student_name.lower() and request["book"] == AVAILABLE_BOOKS[book_id]:
            print("⚠ You have already requested this book!")
            return

    requests.append({"student": student_name, "book": AVAILABLE_BOOKS[book_id], "priority": priority})
    save_requests(requests)

    log_action(f"📖 Book requested: {AVAILABLE_BOOKS[book_id]} by {student_name} (Priority: {priority})")
    print("✅ Book request added successfully.")

# Function to process book requests (Fix: Ensure FIFO and Priority work correctly)
def process_requests():
    requests = load_requests()

    if not requests:
        print("⚠ No book requests to process.")
        return

    print("\n📌 Choose processing method:")
    print("1️⃣ FIFO (First Come, First Serve)")
    print("2️⃣ Priority-based (Highest Priority First)")

    choice = input("Enter option: ").strip()

    if choice == "2":
        requests.sort(key=lambda x: x["priority"], reverse=True)

    processed_request = requests.pop(0)
    save_requests(requests)

    # Store borrowed books
    borrowed_books = load_borrowed_books()
    borrowed_books.append(processed_request)
    save_borrowed_books(borrowed_books)

    log_action(f"✅ Book loaned: {processed_request['book']} to {processed_request['student']} (Priority: {processed_request['priority']})")
    print(f"📚 {processed_request['student']} has borrowed '{processed_request['book']}'.")

# Function to list borrowed books
def list_borrowed_books():
    borrowed_books = load_borrowed_books()
    if not borrowed_books:
        print("⚠ No books have been borrowed yet.")
        return

    print("\n📋 Borrowed Books:")
    for entry in borrowed_books:
        print(f"📖 {entry['book']} - Borrowed by: {entry['student']} (Priority: {entry['priority']})")

# Function to exit system
def exit_system():
    confirm = input("Are you sure you want to exit? (Y/N): ").strip().lower()
    if confirm == "y":
        log_action("🛑 System exited.")
        print("👋 Goodbye!")
        exit(0)
    else:
        print("🚫 Exit cancelled.")

# Main menu loop
while True:
    print("\n🔹 Library Smart Borrowing System 🔹")
    print("1️⃣  View Available Books")
    print("2️⃣  Request a Book")
    print("3️⃣  Process Book Requests")
    print("4️⃣  List Borrowed Books")
    print("5️⃣  Exit")

    option = input("Choose an option: ").strip()

    if option == "1":
        view_books()
    elif option == "2":
        request_book()
    elif option == "3":
        process_requests()
    elif option == "4":
        list_borrowed_books()
    elif option == "5":
        exit_system()
    else:
        print("❌ Invalid choice! Please try again.")
