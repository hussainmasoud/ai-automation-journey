import os
import shutil
print("Files in notes folder:", os.listdir("notes"))

# Folder containing your notes
NOTES_FOLDER = "notes"

# Categories and the keywords to detect them
CATEGORIES = {
    "Work": ["meeting", "client", "project", "task"],
    "Personal": ["diary", "life", "thoughts", "memory"],
    "Ideas": ["idea", "plan", "concept", "brainstorm"],
    "Study": ["lesson", "class", "notes", "revision"],
}

def organize_notes():
    # Create category folders if they don't exist
    for category in CATEGORIES.keys():
        os.makedirs(os.path.join(NOTES_FOLDER, category), exist_ok=True)

    # Loop through all files in notes folder
    for filename in os.listdir(NOTES_FOLDER):
        file_path = os.path.join(NOTES_FOLDER, filename)

        # Only process .txt files
        if not filename.endswith(".txt"):
            continue

        # Read file content
        with open(file_path, "r", encoding="utf-8") as file:
            content = file.read().lower()

        # Determine which category the note belongs to
        moved = False
        for category, keywords in CATEGORIES.items():
            if any(keyword in content for keyword in keywords):
                shutil.move(file_path, os.path.join(NOTES_FOLDER, category, filename))
                print(f"Moved '{filename}' → {category} ✅")
                moved = True
                break

        # If no keyword matches, move to Misc
        if not moved:
            misc_folder = os.path.join(NOTES_FOLDER, "Misc")
            os.makedirs(misc_folder, exist_ok=True)
            shutil.move(file_path, os.path.join(misc_folder, filename))
            print(f"Moved '{filename}' → Misc 🔄")

if __name__ == "__main__":
    organize_notes()
