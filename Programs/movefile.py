import shutil

source_file = "/home/leroy/Desktop/Test/Payslip.pdf"
destination_folder = "/home/leroy/Desktop/Test/Backup"

shutil.move(source_file, destination_folder)

print("File moved successfully"