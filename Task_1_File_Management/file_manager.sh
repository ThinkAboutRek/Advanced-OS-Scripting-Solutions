#!/bin/bash

# Backup directory and log file paths
BACKUP_DIR="Backup"
LOG_FILE="backup_log.txt"

# Ensure the Backup directory exists
mkdir -p "$BACKUP_DIR"

# Function to log actions
log_action() {
    echo "$(date '+%Y-%m-%d %H:%M:%S') - $1" >> "$LOG_FILE"
}

# Function to list files with better readability
list_files() {
    echo "Listing all files in the current directory:"
    ls -lh --color=auto | awk '{print $9, $5, $6, $7, $8}' | column -t
}

# Function to move a file with validation
move_file() {
    read -p "Enter the file name to move: " file
    read -p "Enter the destination directory: " dest

    if [ ! -f "$file" ]; then
        echo "Error: '$file' does not exist!"
        return
    fi

    if [ ! -d "$dest" ]; then
        read -p "Destination folder does not exist. Create it? (Y/N): " create_dest
        if [[ "$create_dest" == "Y" || "$create_dest" == "y" ]]; then
            mkdir -p "$dest"
        else
            echo "Move operation cancelled."
            return
        fi
    fi

    mv "$file" "$dest/"
    if [ $? -eq 0 ]; then
        echo "File moved successfully to $dest/"
        log_action "Moved file '$file' to '$dest/'"
    else
        echo "Error: Failed to move file."
    fi
}

# Function to rename a file with overwrite protection
rename_file() {
    read -p "Enter the file to rename: " old_name
    read -p "Enter the new name: " new_name

    if [ ! -f "$old_name" ]; then
        echo "Error: '$old_name' does not exist!"
        return
    fi

    if [ -f "$new_name" ]; then
        read -p "File '$new_name' already exists. Overwrite? (Y/N): " confirm
        if [[ "$confirm" != "Y" && "$confirm" != "y" ]]; then
            echo "Rename operation cancelled."
            return
        fi
    fi

    mv "$old_name" "$new_name"
    echo "File renamed successfully."
    log_action "Renamed '$old_name' to '$new_name'"
}

# Function to delete a file with confirmation
delete_file() {
    read -p "Enter the file to delete: " file
    if [ ! -f "$file" ]; then
        echo "Error: '$file' does not exist!"
        return
    fi

    read -p "Are you sure? (Y/N): " confirm
    if [[ "$confirm" == "Y" || "$confirm" == "y" ]]; then
        rm "$file"
        echo "File deleted."
        log_action "Deleted file '$file'"
    else
        echo "Deletion cancelled."
    fi
}

# Function to create a backup with full path details
backup_file() {
    read -p "Enter the file to back up: " file
    if [ ! -f "$file" ]; then
        echo "Error: '$file' does not exist!"
        return
    fi

    timestamp=$(date '+%Y%m%d_%H%M%S')
    file_name=$(basename "$file")
    file_path=$(dirname "$file")
    backup_file="$BACKUP_DIR/${file_path//\//_}_$file_name_$timestamp"

    cp "$file" "$backup_file"
    if [ $? -eq 0 ]; then
        echo "File backed up successfully: $backup_file"
        log_action "Backed up '$file' as '$backup_file'"
    else
        echo "Backup failed!"
    fi
}

# Function to check backup folder size and warn if >500MB
check_backup_size() {
    size=$(du -sh "$BACKUP_DIR" | awk '{print $1}')
    echo "Backup folder size: $size"

    max_size=500  # 500MB limit
    current_size=$(du -sm "$BACKUP_DIR" | awk '{print $1}')

    if (( current_size > max_size )); then
        echo "Warning: Backup size exceeds 500MB!"
        log_action "WARNING: Backup size exceeded 500MB"
    fi
}

# Function to exit with confirmation and log user action
exit_script() {
    read -p "Are you sure you want to exit? (Y/N): " confirm
    if [[ "$confirm" == "Y" || "$confirm" == "y" ]]; then
        echo "Goodbye!"
        log_action "User exited script"
        exit 0
    else
        echo "Exit cancelled."
    fi
}

# Menu-driven system with better UI and handling
while true; do
    echo "------------------------------------"
    echo "  University File Management System "
    echo "------------------------------------"
    echo "1. List files"
    echo "2. Move file"
    echo "3. Rename file"
    echo "4. Delete file"
    echo "5. Backup file"
    echo "6. Check backup size"
    echo "7. Exit"
    echo "------------------------------------"
    read -p "Choose an option (1-7): " choice

    case $choice in
        1) list_files ;;
        2) move_file ;;
        3) rename_file ;;
        4) delete_file ;;
        5) backup_file ;;
        6) check_backup_size ;;
        7) exit_script ;;
        *) echo "Invalid option, please enter a number between 1-7." ;;
    esac
done  
