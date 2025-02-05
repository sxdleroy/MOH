# Move a file from one folder to another folder
import shutil

# Source file path & Destination folder path
source_file = "/home/leroy/Desktop/Test/Payslip.pdf"
destination_folder = "/home/leroy/Desktop/Test/Backup"

# Move file
shutil.move(source_file, destination_folder)

# Print message
print("File moved successfully")