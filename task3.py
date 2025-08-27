# ⚙️ Task Automation Script
# Move all .jpg files from one folder to another
# Developed by Faisal Saleem for CodeAlpha Internship

import os
import shutil

# Define source and destination folders
source_folder = "source_folder"
destination_folder = "destination_folder"

# Agar destination folder exist nahi karta to bana do
if not os.path.exists(destination_folder):
    os.makedirs(destination_folder)

# Counter for moved files
count = 0

# Source folder ke andar files check karo
if os.path.exists(source_folder):
    for file_name in os.listdir(source_folder):
        if file_name.lower().endswith(".jpg"):
            # Full file paths
            src_path = os.path.join(source_folder, file_name)
            dest_path = os.path.join(destination_folder, file_name)

            # Move file
            shutil.move(src_path, dest_path)
            count += 1
            print(f"Moved: {file_name}")

    print(f"\n✅ Task Completed! {count} .jpg files moved to '{destination_folder}' folder.")
else:
    print("❌ Source folder not found! Please make sure 'source_folder' exists in your project directory.")
