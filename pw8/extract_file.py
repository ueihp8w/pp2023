import zipfile
import os

def extract():
    if os.path.isfile("./students.zip"):
        print("Extracting students.zip...")
        zip_name = "students.zip"
        with zipfile.ZipFile(zip_name, mode='r') as archive:
            archive.extractall()