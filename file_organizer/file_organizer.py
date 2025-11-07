import os
import shutil

def organize_folder(folder_path):
    # File type categories
    file_types = {
        "Images": [".png", ".jpg", ".jpeg", ".gif"],
        "Documents": [".pdf", ".docx", ".txt", ".pptx"],
        "Music": [".mp3", ".wav"],
        "Videos": [".mp4", ".mov"],
        "Code": [".py", ".js", ".html", ".css"]
    }

    # Loop through files in the folder
    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)

        # Skip folders
        if os.path.isdir(file_path):
            continue

        file_ext = os.path.splitext(filename)[1]

        # Find matching folder for the file
        for folder_name, extensions in file_types.items():
            if file_ext.lower() in extensions:
                target_folder = os.path.join(folder_path, folder_name)

                # Create folder if not exists
                os.makedirs(target_folder, exist_ok=True)

                # Move the file
                shutil.move(file_path, target_folder)
                print(f"Moved: {filename} → {folder_name}")
                break

if __name__ == "__main__":
    path = input("Enter the folder path to organize: ")
    organize_folder(path)
    print("\n✅ File organization complete!")
