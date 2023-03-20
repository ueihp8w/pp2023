import zipfile
import os

def compress():
    zip_name = "students.zip"
    txt_files = [f for f in os.listdir('.') if f.endswith('.txt')]
    with zipfile.ZipFile(zip_name, mode='w') as archive:
        for file in txt_files:
            archive.write(file)
