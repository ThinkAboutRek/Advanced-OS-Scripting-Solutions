#!/usr/bin/env python3
import os
import shutil
import sys
import time

# Define constants
SUBMISSION_DIR = "Submissions"
LOG_FILE = "submission_log.txt"
MAX_SIZE = 5 * 1024 * 1024  # 5MB

def ensure_directory():
    if not os.path.exists(SUBMISSION_DIR):
        os.makedirs(SUBMISSION_DIR)

def log_action(message):
    with open(LOG_FILE, "a") as log_file:
        log_file.write(f"{time.strftime('%Y-%m-%d %H:%M:%S')} - {message}\n")

def submit_assignment():
    student_id = input("Enter Student ID: ").strip()
    file_path = input("Enter the file path: ").strip()

    if not os.path.isfile(file_path):
        print("\n❌ Error: File does not exist.\n")
        return

    filename = os.path.basename(file_path)
    file_ext = filename.split('.')[-1].lower()

    # Validate file format
    if file_ext not in ["pdf", "docx"]:
        print("\n❌ Error: Only .pdf and .docx files are allowed.\n")
        return

    # Validate file size
    file_size = os.path.getsize(file_path)
    if file_size > MAX_SIZE:
        print("\n❌ Error: File size exceeds 5MB limit.\n")
        return

    dest_path = os.path.join(SUBMISSION_DIR, filename)

    # Check for duplicate submission by filename first
    if os.path.exists(dest_path):
        with open(file_path, "rb") as f1, open(dest_path, "rb") as f2:
            if f1.read() == f2.read():
                print(f"\n⚠️ Duplicate submission detected! File '{filename}' already exists with identical content.\n")
                log_action(f"Duplicate submission attempt: Student ID {student_id} tried to submit duplicate file '{filename}'")
                return

    # Additionally, check all files in the submission directory with the same name
    for file in os.listdir(SUBMISSION_DIR):
        if file == filename:
            existing_path = os.path.join(SUBMISSION_DIR, file)
            with open(file_path, "rb") as f1, open(existing_path, "rb") as f2:
                if f1.read() == f2.read():
                    print(f"\n⚠️ Duplicate submission detected! File '{filename}' already exists with identical content.\n")
                    log_action(f"Duplicate submission attempt: Student ID {student_id} tried to submit duplicate file '{filename}'")
                    return

    # Copy file to submission directory
    shutil.copy2(file_path, dest_path)
    log_action(f"{student_id} | {filename} | {time.strftime('%Y-%m-%d %H:%M:%S')}")
    print("\n✅ Submission successful!\n")

def check_submission():
    # Read user input and normalize case for comparison.
    check_file = input("Enter the filename to check: ").strip().lower()
    found = False

    if os.path.exists(LOG_FILE):
        with open(LOG_FILE, "r") as f:
            for line in f:
                # We're expecting log lines for successful submissions to be in the format:
                # "YYYY-MM-DD HH:MM:SS - student_id | filename | timestamp"
                if '|' in line:
                    parts = line.split('|')
                    if len(parts) >= 2:
                        logged_filename = parts[1].strip().lower()
                        if logged_filename == check_file:
                            found = True
                            break
    if found:
        print(f"\n✅ File '{check_file}' has been submitted.\n")
    else:
        print(f"\n❌ File '{check_file}' not found in submissions.\n")

def list_submissions():
    if os.path.exists(LOG_FILE) and os.path.getsize(LOG_FILE) > 0:
        print("\n📄 List of All Submitted Assignments:\n")
        with open(LOG_FILE, "r") as f:
            print(f.read())
    else:
        print("\n❌ No submissions found.\n")

def exit_script():
    confirm = input("Are you sure you want to exit? (Y/N): ").strip().lower()
    if confirm == "y":
        print("\n👋 Exiting... Goodbye!\n")
        sys.exit(0)
    else:
        print("\nReturning to main menu...\n")

def main():
    ensure_directory()
    while True:
        print("\n==============================================")
        print(" 📂 University Examination Submission System ")
        print("==============================================")
        print(" 1️⃣  Submit an Assignment")
        print(" 2️⃣  Check Existing Submission")
        print(" 3️⃣  List All Submissions")
        print(" 4️⃣  Exit")
        print("==============================================\n")
        choice = input("🔹 Enter your choice: ").strip()
        if choice == "1":
            submit_assignment()
        elif choice == "2":
            check_submission()
        elif choice == "3":
            list_submissions()
        elif choice == "4":
            exit_script()
        else:
            print("\n❌ Invalid choice, please try again.\n")

if __name__ == "__main__":
    main()
