import os
from difflib import SequenceMatcher
from docx import Document
import PyPDF2

# Define the submission directory
SUBMISSION_DIR = "Submissions"

def get_text_from_docx(file_path):
    """Extract text from a .docx file."""
    try:
        doc = Document(file_path)
        return "\n".join([para.text for para in doc.paragraphs])
    except Exception as e:
        print(f"Error reading {file_path}: {e}")
        return ""

def get_text_from_pdf(file_path):
    """Extract text from a PDF file using PyPDF2."""
    try:
        with open(file_path, "rb") as f:
            reader = PyPDF2.PdfReader(f)
            text = ""
            for page in reader.pages:
                page_text = page.extract_text()
                if page_text:
                    text += page_text
            return text
    except Exception as e:
        print(f"Error reading {file_path}: {e}")
        return ""

def check_similarity(text1, text2):
    """Check similarity percentage between two text documents."""
    return SequenceMatcher(None, text1, text2).ratio() * 100

def detect_plagiarism():
    """Compare all submitted assignments for plagiarism, checking both .docx and .pdf files."""
    # Get all submission files with .docx or .pdf extension
    files = [f for f in os.listdir(SUBMISSION_DIR) if f.endswith('.docx') or f.endswith('.pdf')]

    if len(files) < 2:
        print("Not enough files to check similarity.")
        return

    print("\n===== Plagiarism Detection Report =====")
    flagged_files = []

    for i in range(len(files)):
        for j in range(i + 1, len(files)):
            file1 = os.path.join(SUBMISSION_DIR, files[i])
            file2 = os.path.join(SUBMISSION_DIR, files[j])

            # Extract text based on file extension
            if files[i].endswith('.docx'):
                text1 = get_text_from_docx(file1)
            elif files[i].endswith('.pdf'):
                text1 = get_text_from_pdf(file1)
            else:
                text1 = ""

            if files[j].endswith('.docx'):
                text2 = get_text_from_docx(file2)
            elif files[j].endswith('.pdf'):
                text2 = get_text_from_pdf(file2)
            else:
                text2 = ""

            similarity_score = check_similarity(text1, text2)
            if similarity_score > 90:
                print(f"⚠️  High similarity detected: {files[i]} & {files[j]} - {similarity_score:.2f}%")
                flagged_files.append((files[i], files[j], similarity_score))

    if not flagged_files:
        print("✅ No plagiarism detected.")

if __name__ == "__main__":
    detect_plagiarism()
