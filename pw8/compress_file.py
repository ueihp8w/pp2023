import zipfile
import os

def compress():
    zip_name = "students.zip"
    txt_files = ["students", "courses", "marks"]
    with zipfile.ZipFile(zip_name, mode='w') as archive:
        for file in txt_files:
            archive.write(file)
