import os
import importlib.util

# Check if mutagen is installed
if importlib.util.find_spec("mutagen") is None:
    print("Mutagen library not found. Installing...")
    try:
        import pip
        pip.main(["install", "mutagen"])
        print("Mutagen library installed successfully.")
    except Exception as e:
        print("Failed to install mutagen library:", e)
        exit(1)

from mutagen.id3 import ID3

def rename_mp3_files(folder_path):
    for filename in os.listdir(folder_path):
        if filename.endswith(".mp3"):
            file_path = os.path.join(folder_path, filename)
            try:
                audio = ID3(file_path)
                title = audio["TIT2"].text[0]  # Get the title from the ID3 metadata
                new_filename = f"{title}.mp3"
                new_file_path = os.path.join(folder_path, new_filename)
                os.rename(file_path, new_file_path)
                print(f"Renamed {filename} to {new_filename}")
            except Exception as e:
                print(f"Failed to rename {filename}: {e}")

# Usage example
folder_path = "path/to/folder"
rename_mp3_files(folder_path)
