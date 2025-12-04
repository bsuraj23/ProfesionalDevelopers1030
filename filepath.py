# wordcount.py
from pathlib import Path

# Get Desktop path in a cross-platform way
desktop = Path.home() / "Desktop"
file_path = desktop / "myfile.txt"  # change name if your file is different

# Print full path
print("File Path:", file_path)

# Check file exists
if not file_path.exists():
    print("ERROR: File not found. Please put 'myfile.txt' on your Desktop.")
    exit(1)

# Read file and count words
with file_path.open("r", encoding="utf-8") as f:
    content = f.read()

words = content.split()
word_count = len(words)

print("Word Count:", word_count)
