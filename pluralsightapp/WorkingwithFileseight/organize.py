import os
import shutil

# Define the directory you want to organize (your Desktop)
desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")
print('desktop path:', desktop_path)

# Define the folders and their corresponding file extensions
folders = {
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".tiff", ".svg"],
    "Documents": [".doc", ".docx", ".pdf", ".txt", ".ppt", ".pptx", ".xls", ".xlsx"],
    "Archives": [".zip", ".rar", ".7z", ".tar", ".gz"],
    "Videos": [".mp4", ".mov", ".avi", ".mkv", ".flv"],
    "Music": [".mp3", ".wav", ".aac", ".flac"],
    "Scripts": [".py", ".sh", ".bat", ".js", ".html", ".css"]
}

# Create the folders on the desktop if they don't exist
for folder_name in folders:
    folder_path = os.path.join(desktop_path, folder_name)
    print('folder_path:', folder_path)
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)

# Move the files to the appropriate folders
for filename in os.listdir(desktop_path):
    original_file_path = os.path.join(desktop_path, filename)
    # Check if it's a file and not a directory
    if os.path.isfile(original_file_path):
        # Move the file to the corresponding folder based on its extension
        file_ext = os.path.splitext(filename)[1].lower()
        for folder_name, extensions in folders.items():
            if file_ext in extensions:
                destination_path = os.path.join(desktop_path, folder_name, filename)
                print(original_file_path, destination_path)
                #shutil.move(original_file_path, destination_path)
                print(f"Moved: {filename} -> {folder_name}")
                break

print("Desktop organized successfully!")

