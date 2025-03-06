import os
import json
import datetime

# File paths
BOOK_REQUESTS_FILE = "book_requests.txt"
LIBRARY_LOG_FILE = "library_log.txt"
BORROWED_BOOKS_FILE = "borrowed_books.txt"

# Books with stock management
AVAILABLE_BOOKS = {
    "1": {"title": "The Great Gatsby", "stock": 3},
    "2": {"title": "1984", "stock": 2},
    "3": {"title": "To Kill a Mockingbird", "stock": 1},
    "4": {"title": "Pride and Prejudice", "stock": 5},
    "5": {"title": "The Catcher in the Rye", "stock": 4}
}

# Ensure necessary files exist
for file in [BOOK_REQUESTS_FILE, LIBRARY_LOG_FILE, BORROWED_BOOKS_FILE]:
    if not os.path.exists(file):
        with open(file, "w", encoding="utf-8") as f:
            f.write("[]")

# Function to log actions with timestamp
def log_action(action):
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(LIBRARY_LOG_FILE, "a", encoding="utf-8") as log_file:
        log_file.write(f"[{timestamp}] {action}\n")

# Function to load book requests
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
    for key, info in AVAILABLE_BOOKS.items():
        print(f"{key}. {info['title']} - {info['stock']} copies available")

# Function to request a book
def request_book():
    view_books()
    book_id = input("\nEnter the book number you want to request: ").strip()

    if book_id not in AVAILABLE_BOOKS:
        print("❌ Invalid book selection. Try again.")
        return

    book_title = AVAILABLE_BOOKS[book_id]["title"]
    book_stock = AVAILABLE_BOOKS[book_id]["stock"]

    # Show stock count before requesting
    print(f"✅ {book_stock} copies left of '{book_title}'.")

    if book_stock == 0:
        print(f"⚠ Sorry, '{book_title}' is out of stock.")
        return

    student_name = input("Enter your name: ").strip()
    if not student_name:
        print("❌ Name cannot be empty.")
        return

    # Check if the student has already borrowed this book
    borrowed_books = load_borrowed_books()
    if any(b["student"].lower() == student_name.lower() and b["book"] == book_title for b in borrowed_books):
        print(f"⚠ You have already borrowed '{book_title}'. You cannot request it again.")
        return  # Stops them immediately

    requests = load_requests()

    # Check if the student already has a request for this book
    for request in requests:
        if request["student"].lower() == student_name.lower() and request["book"] == book_title:
            print(f"⚠ You have already requested '{book_title}'.")
            change_priority = input("Would you like to change priority? (Y/N): ").strip().lower()
            if change_priority == "y":
                while True:
                    new_priority = input("Enter new priority (1-10): ").strip()
                    if new_priority.isdigit() and 1 <= int(new_priority) <= 10:
                        request["priority"] = int(new_priority)
                        save_requests(requests)
                        log_action(f"🔄 Priority updated: '{book_title}' for {student_name} (Priority: {new_priority})")
                        print(f"✅ Priority updated to {new_priority}.")
                        return
                    else:
                        print("❌ Invalid priority. Enter a number between 1 and 10.")
            else:
                return

    # Get priority
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

    # Add request to queue with timestamp for FIFO ordering
    requests.append({
        "student": student_name,
        "book": book_title,
        "priority": priority,
        "timestamp": datetime.datetime.now().isoformat()
    })
    
    save_requests(requests)

    log_action(f"📖 Book requested: {book_title} by {student_name} (Priority: {priority})")
    print("✅ Book request added successfully.")

# Function to process book requests (FIFO & Priority with stock reduction)
def process_requests():
    requests = load_requests()

    if not requests:
        print("⚠ No book requests to process.")
        return

    print("\n📌 Choose processing method:")
    print("1️⃣ FIFO (First Come, First Serve)")
    print("2️⃣ Priority-based (Highest Priority First)")

    choice = input("Enter option: ").strip()

    if choice == "1":
        # FIFO: sort requests by timestamp (oldest first)
        requests.sort(key=lambda x: x["timestamp"])
    elif choice == "2":
        # Priority Mode: sort requests based on priority (highest first)
        requests.sort(key=lambda x: x["priority"], reverse=True)
    else:
        print("❌ Invalid option.")
        return

    # Process the first request in the sorted list
    processed_request = requests.pop(0)
    save_requests(requests)  # Update request queue immediately

    # Reduce stock when book is borrowed
    for key, info in AVAILABLE_BOOKS.items():
        if info["title"] == processed_request["book"]:
            if info["stock"] > 0:
                info["stock"] -= 1
            else:
                print(f"⚠ '{processed_request['book']}' is out of stock. Request cannot be processed.")
                return  

    # Store borrowed books
    borrowed_books = load_borrowed_books()

    # Check if the student already borrowed this book
    if any(b["student"].lower() == processed_request["student"].lower() and b["book"] == processed_request["book"] for b in borrowed_books):
        print(f"⚠ {processed_request['student']} has already borrowed '{processed_request['book']}'.")
        return  

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
    print("\n==============================================")
    print(" 📚 Library Smart Borrowing System ")
    print("==============================================")
    print(" 1️⃣  View Available Books")
    print(" 2️⃣  Request a Book")
    print(" 3️⃣  Process Book Requests")
    print(" 4️⃣  List Borrowed Books")
    print(" 5️⃣  Exit")
    print("==============================================\n")
    
    option = input("🔹 Enter your choice: ").strip()

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
        print("\n❌ Invalid choice, please try again.\n")
