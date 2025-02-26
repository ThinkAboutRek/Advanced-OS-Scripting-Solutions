import os
import sys
import shutil  # Added for cross-drive file movement
import hashlib
import json
from datetime import datetime
from fuzzywuzzy import fuzz
from PyPDF2 import PdfReader
from docx import Document

# File paths
SUBMISSION_FOLDER = "Submissions"
LOG_FILE = "submission_log.txt"

# Ensure necessary folders exist
if not os.path.exists(SUBMISSION_FOLDER):
    os.makedirs(SUBMISSION_FOLDER)

# Function to log actions
def log_action(action):
    with open(LOG_FILE, "a", encoding="utf-8") as log_file:
        log_file.write(f"{action}\n")

# Function to calculate file hash (for duplicate detection)
def get_file_hash(filepath):
    hasher = hashlib.md5()
    with open(filepath, "rb") as f:
        buf = f.read()
        hasher.update(buf)
    return hasher.hexdigest()

# Function to extract text from PDFs and DOCX for plagiarism check
def extract_text_from_file(filepath):
    _, ext = os.path.splitext(filepath)
    
    if ext.lower() == ".pdf":
        try:
            with open(filepath, "rb") as f:
                reader = PdfReader(f)
                text = "\n".join([page.extract_text() or "" for page in reader.pages])
            return text.strip()
        except Exception as e:
            print(f"❌ Error reading PDF: {e}")
            return ""
    
    elif ext.lower() == ".docx":
        try:
            doc = Document(filepath)
            text = "\n".join([para.text for para in doc.paragraphs])
            return text.strip()
        except Exception as e:
            print(f"❌ Error reading DOCX: {e}")
            return ""

    return ""

# Function to check similarity between submissions
def check_similarity(new_text, existing_texts):
    for stored_text in existing_texts:
        similarity = fuzz.ratio(new_text, stored_text)
        if similarity > 90:
            return True, similarity
    return False, 0

# Function to check for duplicate files
def is_duplicate_submission(filepath):
    new_file_hash = get_file_hash(filepath)

    if os.path.exists(LOG_FILE):
        with open(LOG_FILE, "r", encoding="utf-8") as log_file:
            logs = log_file.readlines()
            for log in logs:
                if new_file_hash in log:
                    return True

    return False

# Function to submit an assignment
def submit_assignment():
    student_name = input("Enter your name: ").strip()
    if not student_name:
        print("❌ Name cannot be empty.")
        return

    file_path = input("Enter the file path of your assignment: ").strip().replace("\\", "/")  # Fix Windows paths
    if not os.path.exists(file_path):
        print("❌ File does not exist.")
        return
    
    _, ext = os.path.splitext(file_path)
    if ext.lower() not in [".pdf", ".docx"]:
        print("❌ Invalid file type. Only .pdf and .docx are allowed.")
        return

    file_size = os.path.getsize(file_path) / (1024 * 1024)
    if file_size > 5:
        print("❌ File too large. Maximum allowed size is 5MB.")
        return

    # Check for duplicate files
    if is_duplicate_submission(file_path):
        print("⚠ This file has already been submitted!")
        return

    # Move file to submissions folder (Fix: Use shutil.move for cross-drive movement)
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    new_filename = f"{student_name}_{timestamp}{ext}"
    new_filepath = os.path.join(SUBMISSION_FOLDER, new_filename)

    try:
        shutil.move(file_path, new_filepath)  # Fixed for cross-drive moves
    except Exception as e:
        print(f"❌ Error moving file: {e}")
        return

    # Extract text for plagiarism check
    new_text = extract_text_from_file(new_filepath)
    existing_texts = [extract_text_from_file(os.path.join(SUBMISSION_FOLDER, f)) for f in os.listdir(SUBMISSION_FOLDER)]
    
    # Check for plagiarism
    is_plagiarized, similarity = check_similarity(new_text, existing_texts)
    if is_plagiarized:
        print(f"⚠ Warning: Submission flagged for potential plagiarism ({similarity}% similarity).")

    # Log submission
    log_action(f"{datetime.now()} - {student_name} submitted {new_filename} - Hash: {get_file_hash(new_filepath)}")
    print("✅ Assignment submitted successfully.")

# Function to list all submitted assignments
def list_submissions():
    submissions = os.listdir(SUBMISSION_FOLDER)
    if not submissions:
        print("📂 No assignments submitted yet.")
        return
    
    print("\n📜 Submitted Assignments:")
    for file in submissions:
        print(f"- {file}")

# Function to check for duplicate submissions
def check_duplicate():
    file_path = input("Enter the file path to check for duplicates: ").strip().replace("\\", "/")
    if not os.path.exists(file_path):
        print("❌ File does not exist.")
        return
    
    if is_duplicate_submission(file_path):
        print("⚠ This file is a duplicate of an existing submission.")
    else:
        print("✅ No duplicate found.")

# Function to exit with confirmation
def exit_system():
    confirm = input("Are you sure you want to exit? (Y/N): ").strip().lower()
    if confirm == "y":
        log_action("🛑 System exited.")
        print("👋 Goodbye!")
        sys.exit()
    else:
        print("🚫 Exit cancelled.")

# Function to display menu options
def display_menu():
    print("\n📄 University Exam Submission System 📄")
    print("1️⃣  Submit an Assignment")
    print("2️⃣  Check for Duplicate Submissions")
    print("3️⃣  List All Submitted Assignments")
    print("4️⃣  Exit")
    return input("Choose an option: ").strip()

# Main menu loop
while True:
    choice = display_menu()
    
    if choice == "1":
        submit_assignment()
    elif choice == "2":
        check_duplicate()
    elif choice == "3":
        list_submissions()
    elif choice == "4":
        exit_system()
    else:
        print("❌ Invalid choice! Please try again.")
