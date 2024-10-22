import os
from datetime import datetime

# Add whatever directory hosts the files you want to rename
directory = "files"

# Make a list of those files
filenames = os.listdir(directory)

# Make a reference to the current path and create a new filename for the new file path. I used the date in this example.
for filename in filenames:
    filepath = os.path.join(directory, filename)
    print(filepath)
    date = datetime.now().strftime("%Y-%m-%d")
    new_filename = f"{filename[:-4]}-{date}.txt"
    new_filepath = os.path.join(directory, new_filename)
    # Do the actual rename
    os.rename(filepath, new_filepath)
    print(f"Renamed {filepath} to {new_filepath}")

print("File renaming completed.")
