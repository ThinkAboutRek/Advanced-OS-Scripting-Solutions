#!/bin/bash

# 🟢 Global Variables
BACKUP_DIR="Backup"
TRASH_DIR="Trash"  # Folder for deleted files (soft delete)
LOG_FILE="backup_log.txt"
ERROR_LOG="error_log.txt"
MAX_BACKUP_SIZE=$((500 * 1024 * 1024))  # 500MB in bytes

# Ensure required directories exist
mkdir -p "$BACKUP_DIR" "$TRASH_DIR"

# ✅ Function to log actions
log_action() {
    echo "$(date '+%Y-%m-%d %H:%M:%S') - $1" >> "$LOG_FILE"
}

# ✅ Function to log errors
log_error() {
    echo "$(date '+%Y-%m-%d %H:%M:%S') - ERROR: $1" >> "$ERROR_LOG"
}

# ✅ Fixed Function to List Files with Clean Formatting
list_files() {
    echo -e "\n📂 Available files in current directory:\n"
    echo "1. Sort by Name"
    echo "2. Sort by Size (Largest First)"
    echo "3. Sort by Last Modified Date (Newest First)"
    read -p "Choose sorting option (1-3): " sort_option

    echo -e "\n--------------------------------------------------"
    printf "%-25s %-10s %-20s\n" "Filename" "Size" "Last Modified"
    echo "--------------------------------------------------"

    case $sort_option in
        1) find . -maxdepth 1 -type f -printf "%f %s %TY-%Tm-%Td %TH:%TM:%TS\n" | sort | awk '{printf "%-25s %-10s %-20s\n", $1, $2 " bytes", $3 " " $4}' ;;
        2) find . -maxdepth 1 -type f -printf "%f %s %TY-%Tm-%Td %TH:%TM:%TS\n" | sort -k2,2nr | awk '{printf "%-25s %-10s %-20s\n", $1, $2 " bytes", $3 " " $4}' ;;
        3) find . -maxdepth 1 -type f -printf "%f %s %TY-%Tm-%Td %TH:%TM:%TS\n" | sort -k3,3r -k4,4r | awk '{printf "%-25s %-10s %-20s\n", $1, $2 " bytes", $3 " " $4}' ;;
        *) echo "❌ Invalid option!" ;;
    esac

    echo "--------------------------------------------------"
}

# ✅ Function to move files with validation
move_file() {
    read -p "Enter file name to move: " file
    read -p "Enter destination directory: " dest

    if [ ! -f "$file" ]; then
        echo "❌ Error: File does not exist!"
        log_error "Move failed: File '$file' not found"
        return
    fi

    if [ ! -d "$dest" ]; then
        echo "❌ Error: Destination directory does not exist!"
        log_error "Move failed: Destination '$dest' not found"
        return
    fi

    mv "$file" "$dest/"
    echo "✅ File moved successfully!"
    log_action "Moved file '$file' to '$dest/'"
}

# ✅ Function to rename files with overwrite protection
rename_file() {
    read -p "Enter file to rename: " old_name
    read -p "Enter new name: " new_name

    if [ ! -f "$old_name" ]; then
        echo "❌ Error: File does not exist!"
        log_error "Rename failed: '$old_name' not found"
        return
    fi

    if [ -f "$new_name" ]; then
        read -p "⚠️ File '$new_name' already exists! Overwrite? (Y/N): " confirm
        if [[ "$confirm" =~ ^[Nn]$ ]]; then
            echo "🚫 Rename cancelled."
            return
        fi
    fi

    mv "$old_name" "$new_name"
    echo "✅ File renamed successfully!"
    log_action "Renamed '$old_name' to '$new_name'"
}

# ✅ Function to delete files with recovery option
delete_file() {
    read -p "Enter file to delete: " file
    if [ ! -f "$file" ]; then
        echo "❌ Error: File does not exist!"
        log_error "Delete failed: '$file' not found"
        return
    fi

    echo "📄 File Preview:"
    if file "$file" | grep -q text; then
        head -n 5 "$file"
    else
        echo "(Binary file - preview unavailable)"
    fi
    
    read -p "Move to Trash or Delete permanently? (T/P): " choice
    if [[ "$choice" == "T" || "$choice" == "t" ]]; then
        mv "$file" "$TRASH_DIR/"
        echo "♻️ File moved to Trash!"
        log_action "Moved '$file' to Trash"
    else
        rm "$file"
        echo "⚠️ File permanently deleted!"
        log_action "Deleted file '$file'"
    fi
}

# ✅ Function to restore files from Trash
restore_file() {
    read -p "Enter file to restore: " file
    if [ ! -f "$TRASH_DIR/$file" ]; then
        echo "❌ Error: File not found in Trash!"
        return
    fi

    mv "$TRASH_DIR/$file" ./
    echo "✅ File restored successfully!"
    log_action "Restored file '$file' from Trash"
}

# ✅ Fixed Backup Function (No GPG, No Encryption)
backup_files() {
    read -p "Enter file(s) to backup (separated by space): " files
    timestamp=$(date '+%Y%m%d_%H%M%S')

    for file in $files; do
        if [ -f "$file" ]; then
            cp "$file" "$BACKUP_DIR/${file}_v$timestamp"
            echo "📦 Backup created: $file → $BACKUP_DIR/${file}_v$timestamp"
            log_action "Backed up '$file' as '${file}_v$timestamp'"
        else
            echo "❌ Error: File '$file' does not exist!"
            log_error "Backup failed: '$file' not found"
        fi
    done

    # ✅ Automatic Cleanup if Backup Exceeds 500MB
    backup_size=$(du -sb "$BACKUP_DIR" | awk '{print $1}')
    if (( backup_size > MAX_BACKUP_SIZE )); then
        oldest_file=$(ls -t "$BACKUP_DIR" | tail -1)
        rm "$BACKUP_DIR/$oldest_file"
        log_action "Backup size exceeded. Deleted oldest backup: $oldest_file"
        echo "⚠️ Backup directory exceeded 500MB. Oldest backup deleted!"
    fi
}

# ✅ Function to view logs
view_logs() {
    echo -e "\n📜 Recent Logs:"
    tail -n 10 "$LOG_FILE"
}

# ✅ Function to exit script safely
exit_script() {
    read -p "Are you sure you want to exit? (Y/N): " confirm
    if [[ "$confirm" =~ ^[Yy]$ ]]; then
        echo "👋 Goodbye!"
        log_action "User exited script"
        exit 0
    fi
}

# ✅ Menu-driven system with enhanced UI
while true; do
    echo "------------------------------------"
    echo "  📁 University File Management System  "
    echo "------------------------------------"
    echo "1. List files"
    echo "2. Move file"
    echo "3. Rename file"
    echo "4. Delete file"
    echo "5. Restore file"
    echo "6. Backup files"
    echo "7. View logs"
    echo "8. Exit"
    echo "------------------------------------"
    read -p "Choose an option (1-8): " choice

    case $choice in
        1) list_files ;;
        2) move_file ;;
        3) rename_file ;;
        4) delete_file ;;
        5) restore_file ;;
        6) backup_files ;;
        7) view_logs ;;
        8) exit_script ;;
        *) echo "❌ Invalid option! Please enter a number between 1-8." ;;
    esac
done
