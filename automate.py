import os
import shutil

# File type categories
FILE_TYPES = {
    "Images": [".jpg", ".jpeg", ".png", ".gif"],
    "Documents": [".pdf", ".docx", ".txt", ".pptx", ".xlsx"],
    "Audio": [".mp3", ".wav"],
    "Videos": [".mp4", ".mkv", ".avi"],
    "Archives": [".zip", ".rar"],
}

# Get folder path from user
folder_path = input("Enter folder path: ")

# Check if folder exists
if not os.path.exists(folder_path):
    print("Folder does not exist!")
    exit()

# Organize files
for file_name in os.listdir(folder_path):

    file_path = os.path.join(folder_path, file_name)

    # Skip folders
    if os.path.isdir(file_path):
        continue

    # Get extension
    _, extension = os.path.splitext(file_name)
    extension = extension.lower()

    destination_folder = "Others"

    # Detect file type
    for folder, extensions in FILE_TYPES.items():
        if extension in extensions:
            destination_folder = folder
            break

    destination_path = os.path.join(folder_path, destination_folder)

    # Create folder if not exists
    os.makedirs(destination_path, exist_ok=True)

    # Handle duplicate filenames
    new_file_name = file_name
    counter = 1

    while os.path.exists(os.path.join(destination_path, new_file_name)):
        name, ext = os.path.splitext(file_name)
        new_file_name = f"{name}_{counter}{ext}"
        counter += 1

    # Move file
    shutil.move(
        file_path,
        os.path.join(destination_path, new_file_name)
    )

    print(f"Moved: {file_name} -> {destination_folder}")

print("\nFolder organized successfully!")