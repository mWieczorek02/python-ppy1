import os
from pathlib import Path

if __name__ == "__main__":
    downloads_path = str(Path.home() / "Downloads")
    files = os.listdir(downloads_path)
    for file in files:
        if os.path.isdir(file):
            print(f"{file}: directory")
        if os.path.isfile(file):
            print(f"{file}: file")

