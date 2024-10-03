import os 
import shutil

file_types = {
    'Images': ['.jpg', '.png', '.gif', '.tif', '.bmp', '.eps'],
    'Documents': ['.txt', '.rtf', '.docx', '.csv', '.doc', '.wps'],
    'Video': ['.mp4', '.avi', '.mkv', '.mov', '.wmv'],
    'Audio': ['.mp3', '.wav', '.aac', '.flac', '.ogg'],
    'Archives': ['.zip', '.rar', '.tar', '.gz', '.7z'],
    'Code': ['.py', '.java', '.c', '.cpp', '.js', '.html', '.css'],
}

def organize_files(directory):
    if not os.path.exists(directory):
        print(f"The directory {directory} does not exist.")
        return
    for filename in os.listdir(directory):
        file_extension = os.path.splitext(filename)[1].lower()

        for folder_name, extensions in file_types.items():
            if file_extension in extensions:
                folder_path = os.path.join(directory, folder_name)

                if not os.path.exists(folder_path):
                    os.makedirs(folder_path)

                shutil.move(os.path.join(directory, filename), os.path.join(folder_path, filename))
                print(f"Moved{filename} to {folder_name}")
                break
            print("Your files have been orgainzed sucessfully") 
               
directory = input("Enter the directory that you want to organize: " )
organize_files(directory)