import os 
import shutil

path = input("Enter Your Path...")
files = os.listdir(path)       

for i in files:
    FileName, Extention = os.path.splitext(i)
    Extention_1 = Extention[1:]
    folder_path = os.path.join(path, Extention_1)  # Use os.path.join to create the folder path
    
    if os.path.exists(folder_path):
        shutil.move(os.path.join(path, i), os.path.join(folder_path, i))  # Correct the destination path
    else:
        os.makedirs(folder_path)
        shutil.move(os.path.join(path, i), os.path.join(folder_path, i))  # Correct the destination path
