#!/bin/bash

# University Examination Submission & Similarity Detection System
# Bash Script for File Submission and Validation

# Define the submission directory and log file
SUBMISSION_DIR="Submissions"
LOG_FILE="submission_log.txt"

# Ensure the submission directory exists
mkdir -p "$SUBMISSION_DIR"

# Function to submit an assignment
submit_assignment() {
    read -p "Enter Student ID: " student_id
    read -p "Enter the file path: " file_path

    if [[ ! -f "$file_path" ]]; then
        echo -e "\n❌ Error: File does not exist.\n"
        return
    fi

    filename=$(basename "$file_path")
    file_ext="${filename##*.}"
    file_size=$(stat -c%s "$file_path")

    # Validate file format
    if [[ "$file_ext" != "pdf" && "$file_ext" != "docx" ]]; then
        echo -e "\n❌ Error: Only .pdf and .docx files are allowed.\n"
        return
    fi

    # Validate file size (Max 5MB)
    if (( file_size > 5242880 )); then
        echo -e "\n❌ Error: File size exceeds 5MB limit.\n"
        return
    fi

    # Check for duplicate submission
    for file in "$SUBMISSION_DIR"/*; do
        if cmp -s "$file_path" "$file"; then
            echo -e "\n⚠️  Error: Duplicate submission detected! File already exists.\n"
            return
        fi
    done

    # Move file to submission directory
    cp "$file_path" "$SUBMISSION_DIR/$filename"
    echo "$student_id | $filename | $(date)" >> "$LOG_FILE"
    echo -e "\n✅ Submission successful!\n"
}

# Function to check if a file has been submitted
check_submission() {
    read -p "Enter the filename to check: " check_file
    if grep -q "$check_file" "$LOG_FILE"; then
        echo -e "\n✅ File '$check_file' has been submitted.\n"
    else
        echo -e "\n❌ File '$check_file' not found in submissions.\n"
    fi
}

# Function to list all submissions
list_submissions() {
    if [[ -s "$LOG_FILE" ]]; then
        echo -e "\n📄 List of All Submitted Assignments:\n"
        cat "$LOG_FILE"
        echo ""
    else
        echo -e "\n❌ No submissions found.\n"
    fi
}

# Function to exit with confirmation
confirm_exit() {
    while true; do
        read -p "⚠️  Are you sure you want to exit? (Y/N): " confirm
        case "$confirm" in
            [Yy]) 
                echo -e "\n👋 Exiting... Goodbye!\n"
                exit 0
                ;;
            [Nn]) 
                echo -e "\nReturning to main menu...\n"
                return
                ;;
            *) 
                echo -e "\n❌ Invalid choice. Please enter 'y' or 'n'.\n"
                ;;
        esac
    done
}

# Main Menu
while true; do
    echo -e "\n=============================================="
    echo -e " 📂 University Examination Submission System "
    echo -e "=============================================="
    echo -e " 1️⃣  Submit an Assignment"
    echo -e " 2️⃣  Check Existing Submission"
    echo -e " 3️⃣  List All Submissions"
    echo -e " 4️⃣  Exit"
    echo -e "==============================================\n"
    
    read -p "🔹 Enter your choice: " choice

    case $choice in
        1) submit_assignment ;;
        2) check_submission ;;
        3) list_submissions ;;
        4) confirm_exit ;;
        *) echo -e "\n❌ Invalid choice, please try again.\n" ;;
    esac
done
