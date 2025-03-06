import os
from difflib import SequenceMatcher
from docx import Document  # Import python-docx to read .docx files

# Define the submission directory
SUBMISSION_DIR = "submissions"

def get_text_from_docx(file_path):
    """Extract text from a .docx file."""
    try:
        doc = Document(file_path)
        return "\n".join([para.text for para in doc.paragraphs])
    except Exception as e:
        print(f"Error reading {file_path}: {e}")
        return ""

def check_similarity(text1, text2):
    """Check similarity percentage between two text documents."""
    return SequenceMatcher(None, text1, text2).ratio() * 100

def detect_plagiarism():
    """Compare all submitted assignments for plagiarism."""
    files = [f for f in os.listdir(SUBMISSION_DIR) if f.endswith('.docx')]

    if len(files) < 2:
        print("Not enough files to check similarity.")
        return

    print("\n===== Plagiarism Detection Report =====")
    flagged_files = []

    for i in range(len(files)):
        for j in range(i + 1, len(files)):
            file1 = os.path.join(SUBMISSION_DIR, files[i])
            file2 = os.path.join(SUBMISSION_DIR, files[j])

            text1 = get_text_from_docx(file1)
            text2 = get_text_from_docx(file2)

            similarity_score = check_similarity(text1, text2)
            if similarity_score > 90:
                print(f"⚠️ High similarity detected: {files[i]} & {files[j]} - {similarity_score:.2f}%")
                flagged_files.append((files[i], files[j], similarity_score))

    if not flagged_files:
        print("✅ No plagiarism detected.")

if __name__ == "__main__":
    detect_plagiarism()
