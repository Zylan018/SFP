import os
import shutil

def organize_files(source_directory):
    """
    Organizes files in the specified source directory into subfolders
    based on their file extensions.
    """
    if not os.path.isdir(source_directory):
        print(f"Error: Directory '{source_directory}' not found.")
        return

    # Define file categories and their corresponding extensions
    file_categories = {
        "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".tiff", ".webp"],
        "Documents": [".pdf", ".doc", ".docx", ".txt", ".odt", ".rtf", ".xls", ".xlsx", ".ppt", ".pptx"],
        "Videos": [".mp4", ".mov", ".avi", ".mkv", ".flv", ".wmv"],
        "Audio": [".mp3", ".wav", ".ogg", ".aac", ".flac"],
        "Archives": [".zip", ".rar", ".7z", ".tar", ".gz"],
        "Executables": [".exe", ".msi", ".dmg"],
        "Code": [".py", ".js", ".html", ".css", ".java", ".cpp", ".c", ".php"]
    }

    # Create category folders if they don't exist
    for category in file_categories:
        category_path = os.path.join(source_directory, category)
        os.makedirs(category_path, exist_ok=True)

    # Create an "Others" folder for uncategorized files
    others_path = os.path.join(source_directory, "Others")
    os.makedirs(others_path, exist_ok=True)

    # Iterate through files in the source directory
    for filename in os.listdir(source_directory):
        file_path = os.path.join(source_directory, filename)

        # Skip directories and the script itself
        if os.path.isdir(file_path) or filename == os.path.basename(__file__):
            continue

        file_extension = os.path.splitext(filename)[1].lower()
        moved = False

        for category, extensions in file_categories.items():
            if file_extension in extensions:
                destination_folder = os.path.join(source_directory, category)
                shutil.move(file_path, os.path.join(destination_folder, filename))
                print(f"Moved '{filename}' to '{category}' folder.")
                moved = True
                break
        
        if not moved:
            # Move uncategorized files to the "Others" folder
            shutil.move(file_path, os.path.join(others_path, filename))
            print(f"Moved '{filename}' to 'Others' folder.")

if __name__ == "__main__":
    # Specify the directory to organize (e.g., your Downloads folder)
    target_directory = input("Enter the path of the directory to organize: ")
    organize_files(target_directory)
    print("File organization complete!")