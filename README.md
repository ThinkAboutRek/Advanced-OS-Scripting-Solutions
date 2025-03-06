# 📂 Advanced Operating Systems Scripting Solutions

## 🔥 University File Management, Library Queue System & Exam Submission Automation

Welcome to the **Advanced Operating Systems Scripting Solutions** repository! 🚀 This project showcases three advanced automation scripts written in **Bash** and **Python**. They are designed to tackle real-world system administration problems related to file management, queue processing, and submission validation, ultimately improving system efficiency, data handling, and workflow automation.

---

## Table of Contents
- [Project Overview](#project-overview)
  - [1️⃣ University File Management & Backup System (Bash)](#1-university-file-management--backup-system-bash)
  - [2️⃣ Christ Church University Library Smart Borrowing System (Python)](#2-christ-church-university-library-smart-borrowing-system-python)
  - [3️⃣ University Examination Submission & Similarity Detection (Bash & Python)](#3-university-examination-submission--similarity-detection-bash--python)
- [Installation & Usage](#installation--usage)
- [Features & Highlights](#features--highlights)
- [Testing & Validation](#testing--validation)
- [License](#license)
- [Contributing](#contributing)
- [Acknowledgments](#acknowledgments)

---

## Project Overview

This repository contains three major automation scripts, each addressing a different real-world scenario:

### 1️⃣ University File Management & Backup System (Bash)
An **automated file management system** for handling essential file operations and backups.

- **Operations:**  
  - List, Move, Rename, Delete, and Restore files  
  - Automated backups with timestamped filenames  
  - Log all file operations for auditing
- **Safety Measures:**  
  - Prevent accidental overwrites  
  - Confirmation prompts on deletion and exit
- **File:** `file_management.sh`

#### Directory Structure
```
Task_1_File_Management/
├── Backup/                   # Directory where backups are stored
├── Test_folder/              # Directory for testing file operations
├── Trash/                    # Directory for deleted files
├── file_log.txt              # Log file tracking file activities
├── file_management.sh        # Bash script for file management & backup
├── Test files                # Test files for testing 

```

---

### 2️⃣ Christ Church University Library Smart Borrowing System (Python)
A **queue-based book borrowing system** that efficiently manages student book requests.

- **Features:**  
  - Supports both FIFO and Priority scheduling  
  - Dynamic processing and logging of book requests  
  - Stock management to track available copies  
  - Robust error handling and edge-case prevention
- **File:** `library_queue.py`

#### Directory Structure
```
Task_2_Library_Queue/
├── book_requests.txt         # Stores book requests as a JSON queue
├── borrowed_books.txt        # Stores borrowed books as a JSON queue
├── library_log.txt           # Log file tracking book borrowing transactions
├── library_system.py         # Python script for managing book queues
```

---

### 3️⃣ University Examination Submission & Similarity Detection (Bash & Python)
An **automated assignment submission system** that validates student submissions and detects potential plagiarism.

- **File Validation:**  
  - Accepts only `.pdf` and `.docx` files (max 5MB)  
  - Rejects duplicate submissions (based on filename and content)
- **Plagiarism Detection (Bonus):**  
  - Uses Python to extract text from both `.docx` (using `python-docx`) and `.pdf` files (using `PyPDF2`)  
  - Flags files with over 90% similarity
- **Files:**  
  - Bash submission system: `exam_submission.sh`  
  - Python similarity checker: `similarity_check.py`  
  - Log file: `submission_log.txt`

#### Directory Structure
```
Task_3_Exam_Submission/
├── Submissions/              # Directory where submitted files are stored
├── plagiarism_detection.py   # Python script for plagiarism detection
├── submission_log.txt        # Log file for tracking submissions
├── submission_system.sh      # Bash script for assignment submission
```

---

## Installation & Usage

### Prerequisites
Ensure your system has:
- **Bash** (Linux/macOS) or **Git Bash** (Windows)
- **Python 3.x**
- Required Python modules:
  ```
  pip install python-docx PyPDF2
  ```

### Running Each Script

#### University File Management & Backup System (Bash)
```bash
chmod +x file_manager.sh  
./file_manager.sh
```

#### Library Queue System (Python)
```bash
python library_system.p
```

#### To run automated tests for the Library Queue System, execute:
```bash
python library_system.py test
```

#### Exam Submission & Similarity Detection

**Bash Submission System:**
```bash
chmod +x submission_system.sh  
./submission_system.sh
```

**Plagiarism Detection (Python):**
```bash
python plagiarism_detection.py
```

---

## Features & Highlights

| Feature                    | File Management | Library Queue System | Exam Submission |
|----------------------------|-----------------|----------------------|-----------------|
| **File Operations**        | ✅ Yes         | ❌ No                | ✅ Yes         |
| **Automated Backups**      | ✅ Yes         | ❌ No                | ❌ No          |
| **Queue Processing**       | ❌ No          | ✅ Yes               | ❌ No          |
| **Duplicate Prevention**   | ❌ No          | ✅ Yes               | ✅ Yes         |
| **Logging System**         | ✅ Yes         | ✅ Yes               | ✅ Yes         |
| **Plagiarism Detection**   | ❌ No          | ❌ No                | ✅ Yes         |

---

## Testing & Validation

### Testing Overview
Each script has been rigorously tested to ensure:
- **Correct functionality** under multiple conditions
- **Robust error handling** for edge cases
- **Accurate logging & tracking** of operations
- **Cross-platform compatibility** on Linux/macOS and Windows (using Git Bash)

---

## License

This project is open-source and available under the **MIT License**.

---

## Contributing

Contributions, feature requests, and improvements are welcome! Please submit a pull request or open an issue if you have suggestions.

---

## Acknowledgments

- **Advanced Operating Systems (AOS) Module** – for the project inspiration.
- **Bash & Python Scripting Best Practices** – for guidance on robust automation.
- **Community Contributions** – thank you to all contributors for their support and feedback.

---

🚀 **Developed with precision, efficiency, and automation in mind.** Happy scripting! 😃