# Advanced OS Scripting Solutions

## 📌 Overview
This repository contains a collection of robust automation and system management scripts designed to optimize file handling, data processing, and administrative workflows. The solutions leverage Bash scripting and Python programming to implement efficient automation processes for file management, queue handling, and data validation. These scripts are designed to enhance operational efficiency, ensuring scalability and reliability in system administration tasks.

## 📁 Project Structure
```
Advanced-OS-Scripting-Solutions/
│── Task_1_File_Management/        # Bash script for file management & backup
│── Task_2_Library_System/         # Python script for smart library system
│── Task_3_Exam_Submission/        # Python script for assignment submission
│   ├── Submissions/               # Folder for submitted assignments
│   ├── exam_submission.py         # Main Python script
│   ├── submission_log.txt         # Submission log file
│── README.md                      # Project documentation
```

## 📝 Task Descriptions
### **🔹 Task 1: University File Management & Automated Backup System** (Bash)
- Implements a **menu-driven file management system**.
- Features **file listing, renaming, moving, deleting, and automated backup**.
- **Backup size monitoring** warns when exceeding **500MB**.
- **Logs all operations** in `backup_log.txt`.

### **🔹 Task 2: Christ Church University Library Smart Borrowing System** (Python)
- Allows students to **request books from a library system**.
- Supports **FIFO and priority-based book request processing**.
- **Prevents duplicate requests** and logs transactions in `library_log.txt`.
- Ensures **a smooth book borrowing experience** with data persistence.

### **🔹 Task 3: University Examination Submission & Similarity Detection** (Python)
- Implements an **automated assignment submission system**.
- **Validates file type** (`.pdf`, `.docx`) and **checks file size** (≤ 5MB).
- **Detects duplicate submissions** and prevents resubmission.
- Features **plagiarism detection** using **text similarity analysis**.
- Logs all submissions in `submission_log.txt`.

## ✅ **Key Achievements**
✔ **Fully implemented all task requirements**.
✔ **Successfully passed all test cases** with expected outputs.
✔ **Advanced features** like **backup automation, priority book requests, and plagiarism detection** were implemented.

## 🚀 How to Run the Scripts

## 📥 Prerequisites
Before running the scripts, ensure you have Python 3 installed. You also need to install the required Python libraries:
```bash
pip install python-docx PyPDF2 fuzzywuzzy
```
### **Task 1: File Management (Bash)**
```bash
cd Task_1_File_Management
bash file_management.sh
```

### **Task 2: Library System (Python)**
```bash
cd Task_2_Library_System
python library_system.py
```

### **Task 3: Exam Submission System (Python)**
```bash
cd Task_3_Exam_Submission
python exam_submission.py
```

## 📌 Technologies Used
- **Bash Scripting** (for Task 1 automation)
- **Python 3** (for Task 2 and Task 3 logic)
- **PyPDF2, python-docx, fuzzywuzzy** (for Task 3 text similarity detection)

## 📌 Additional Notes
- Ensure the `Submissions/` folder exists inside `Task_3_Exam_Submission/` before running the exam submission script.
- All logs and processed data are saved automatically in their respective directories.
- For any issues, refer to the logs (`backup_log.txt`, `library_log.txt`, `submission_log.txt`).

## 📄 References
1. Python Software Foundation. (2024). *Python Documentation*. Retrieved from https://docs.python.org/3/
2. GNU Bash Manual. (2024). *Bash Scripting Guide*. Retrieved from https://www.gnu.org/software/bash/manual/bash.html
3. The Linux Documentation Project. (2024). *Advanced Bash-Scripting Guide*. Retrieved from http://tldp.org/LDP/abs/html/

## 📄 Author & Acknowledgments
**Developed by:** Shayan Bagheri 
For **Advanced Operating Systems (U14553) - Assessment 1**  
