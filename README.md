# 📂 Advanced Operating Systems Scripting Solutions

## 🔥 University File Management, Library Queue System & Exam Submission Automation

Welcome to the **Advanced Operating Systems Scripting Solutions** repository! 🚀 This project showcases three advanced **Bash & Python** automation scripts for **file management, queue processing, and submission validation**. These solutions are designed to improve system efficiency, enforce structured data handling, and automate administrative workflows.

---

## 📌 Project Overview
This repository contains **three major automation scripts**, each solving a real-world system administration problem:

### **1️⃣ University File Management & Backup System (Bash Only)**
📁 **Automated file management system** designed to handle:
- 📜 **File operations**: List, Move, Rename, Delete, Restore
- 🔄 **Automated backup system** with timestamped backups & storage monitoring
- 📝 **Logging system** that records all file changes
- ✅ **Menu-driven interface** with user-friendly navigation
- 🔒 **Safety measures**: Prevent accidental overwrites & unauthorized deletions

📂 **File:** `file_management.sh`

📂 **Directory Structure for Task 1:**
```
Task_1_File_Management/
├── file_management.sh        # Bash script for file operations & backup
├── backup/                   # Directory where backups are stored
├── file_log.txt               # Log file tracking all file activities
```

### **2️⃣ Christ Church University Library Smart Borrowing System (Python)**
📚 **Queue-based book borrowing system** that efficiently manages student book requests:
- 📌 **FIFO (First Come, First Serve) & Priority scheduling**
- 📖 **Dynamic book request processing** & tracking
- 🗂 **Book request log** for full transaction history
- 📊 **Error handling & edge case prevention**
- 🏆 **Extra features**: Stock management, enhanced logging

🐍 **File:** `library_queue.py`

📂 **Directory Structure for Task 2:**
```
Task_2_Library_Queue/
├── library_queue.py          # Python script for managing book queues
├── book_requests.txt         # Stores book requests in queue format
├── library_log.txt           # Log file tracking book borrowings
```

### **3️⃣ University Examination Submission & Similarity Detection (Bash & Python)**
📄 **Automated assignment submission system** that prevents duplicate submissions and plagiarism:
- 📝 **File validation**: Accepts only `.pdf` & `.docx` (Max 5MB)
- 🔍 **Duplicate detection**: Rejects identical files
- ⚠️ **Plagiarism detection**: Flags assignments with >90% similarity
- 📋 **Submission tracking**: Every submission is logged
- 🎨 **Enhanced UI & automated path conversion**

💡 **Files:**
- 🖥 **Bash Submission System**: `exam_submission.sh`
- 🧠 **Python Similarity Checker**: `similarity_check.py`
- 📄 **Log File**: `submission_log.txt`

📂 **Directory Structure for Task 3:**
```
Task_3_Exam_Submission/
├── exam_submission.sh        # Bash script for submission handling
├── similarity_check.py       # Python script for plagiarism detection
├── submission_log.txt        # Log file for tracking submissions
├── submissions/              # Directory where submitted files are stored
```

### **🔹 Important Note for Windows Users (Git Bash File Paths)**
For **file paths in Git Bash on Windows**, use the correct format:
✅ **Working Path Format:**
```
/c/Users/cdsa/Desktop/Test/TestA.docx
```
❌ **These formats will NOT work in Git Bash:**
```
C:\Users\cdsa\Desktop\Test\TestA.docx  # Incorrect (Windows-style)
/mnt/c/Users/cdsa/Desktop/Test/TestA.docx # Incorrect (Git Bash issue)
```
Always use `/c/` instead of `C:\` and replace backslashes (`\`) with forward slashes (`/`).

---

## ⚙️ Installation & Usage
### **🔹 Prerequisites**
Ensure your system has:
- **Bash (Linux/macOS)** or **Git Bash (Windows)**
- **Python 3.x**
- Required Python modules:
  ```sh
  pip install python-docx
  ```

### **🚀 Running Each Script**
#### **📁 File Management & Backup System (Bash Only)**
```sh
chmod +x file_management.sh
./file_management.sh
```
#### **📚 Library Queue System (Python)**
```sh
python library_queue.py
```
#### **📄 Exam Submission & Similarity Detection**
```sh
chmod +x exam_submission.sh
./exam_submission.sh
```
To run the **plagiarism detection system**:
```sh
python similarity_check.py
```

---

## 📊 Features & Highlights
| Feature | File Management | Library Queue System | Exam Submission |
|---------|----------------|----------------------|----------------|
| **File Operations** | ✅ Yes | ❌ No | ✅ Yes |
| **Automated Backups** | ✅ Yes | ❌ No | ❌ No |
| **Queue Processing** | ❌ No | ✅ Yes | ❌ No |
| **Duplicate Prevention** | ❌ No | ✅ Yes | ✅ Yes |
| **Logging System** | ✅ Yes | ✅ Yes | ✅ Yes |
| **Plagiarism Detection** | ❌ No | ❌ No | ✅ Yes |

---

## 🔍 Testing & Validation
Each script has been **thoroughly tested** to ensure:
- ✅ **Correct functionality** under multiple conditions
- ⚠️ **Error handling for edge cases**
- 📊 **Accurate logging & tracking**
- 🚀 **Performance optimization**

All tests were executed on **Linux/macOS & Windows (Git Bash).**

---

## 📜 License
This project is open-source and available under the **MIT License**.

---

## 🤝 Contributing
Contributions, feature requests, and improvements are welcome! Feel free to submit a pull request.

---

## 🏆 Acknowledgments
- **Advanced Operating Systems (AOS) module inspiration**
- **Bash scripting best practices**
- **Python automation techniques**

---

🚀 **Developed with precision, efficiency, and automation in mind.** Happy scripting! 😃
