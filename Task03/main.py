import logging
import os
from src.organizer import FileOrganizer

# Configure logging
log_dir = "logs"
if not os.path.exists(log_dir):
    os.makedirs(log_dir)

logging.basicConfig(
    filename=os.path.join(log_dir, 'file_organizer.log'),
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
)

# Path to the directory you want to organize
directory_to_organize = "C:/Users/PMLS/Desktop/FilesToOrganize"

def main():
    organizer = FileOrganizer(directory_to_organize)
    
    while True:
        print("\n--- File Organizer Menu ---")
        print("1. Organize Files")
        print("2. Resize Images")
        print("3. Delete Files")
        print("4. Count Files")
        print("5. List Files")
        print("6. Check Disk Usage")
        print("7. Disk Cleaner")
        print("8. System Maintenance")
        print("9. System Report")
        print("10. Exit")
        
        choice = input("Enter your choice (1-10): ")
        
        if choice == '1':
            organizer.organize_files()
            print("Files organized successfully.")
        elif choice == '2':
            width = int(input("Enter the width: "))
            height = int(input("Enter the height: "))
            organizer.resize_images(width, height)
            print(f"Images resized to {width}x{height}.")
        elif choice == '3':
            extension = input("Enter the file extension to delete (e.g., .tmp): ")
            organizer.delete_files(extension_criteria=extension)
            print(f"Files with extension {extension} deleted.")
        elif choice == '4':
            file_count = organizer.count_files()
            print(f"Number of files: {file_count}")
        elif choice == '5':
            files = organizer.list_files()
            print(f"Files: {files}")
        elif choice == '6':
            disk_usage = organizer.check_disk_usage()
            print(f"Disk usage: {disk_usage}")
        elif choice == '7':
            organizer.disk_cleaner()
            print("Disk cleaned successfully.")
        elif choice == '8':
            organizer.system_maintenance()
            print("System maintenance completed.")
        elif choice == '9':
            report = organizer.system_report()
            print(f"System report: {report}")
        elif choice == '10':
            print("Exiting...")
            break
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()