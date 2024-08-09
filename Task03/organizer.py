import os
import shutil
import logging
from PIL import Image
import psutil
import platform
import tempfile

class FileOrganizer:
    def __init__(self, directory):
        self.directory = directory
        self.supported_image_formats = ('.png', '.jpg', '.jpeg', '.bmp', '.gif')

    def organize_files(self):
        for filename in os.listdir(self.directory):
            file_path = os.path.join(self.directory, filename)
            if os.path.isfile(file_path):
                _, ext = os.path.splitext(filename)
                ext = ext[1:].upper()  # Remove dot and convert to upper case
                dest_dir = os.path.join(self.directory, ext)
                if not os.path.exists(dest_dir):
                    os.makedirs(dest_dir)
                shutil.move(file_path, os.path.join(dest_dir, filename))

    def resize_images(self, width, height):
        for root, _, files in os.walk(self.directory):
            for file in files:
                if file.lower().endswith(self.supported_image_formats):
                    file_path = os.path.join(root, file)
                    try:
                        with Image.open(file_path) as img:
                            img = img.resize((width, height))
                            img.save(file_path)
                            logging.info(f"Resized image {file_path} to {width}x{height}.")
                    except Exception as e:
                        logging.error(f"Error resizing image {file}: {e}")

    def delete_files(self, extension_criteria=".tmp"):
        for root, _, files in os.walk(self.directory):
            for file in files:
                if file.lower().endswith(extension_criteria.lower()):
                    file_path = os.path.join(root, file)
                    try:
                        os.remove(file_path)
                        logging.info(f"Deleted file {file_path}.")
                    except Exception as e:
                        logging.error(f"Error deleting file {file}: {e}")

    def count_files(self):
        count = 0
        for _, _, files in os.walk(self.directory):
            count += len(files)
        return count

    def list_files(self):
        file_list = []
        for root, _, files in os.walk(self.directory):
            for file in files:
                file_list.append(os.path.join(root, file))
        return file_list

    def check_disk_usage(self):
        usage = shutil.disk_usage(self.directory)
        return {
            'total': usage.total,
            'used': usage.used,
            'free': usage.free
        }

    def disk_cleaner(self):
        temp_dir = tempfile.gettempdir()
        for root, _, files in os.walk(temp_dir):
            for file in files:
                file_path = os.path.join(root, file)
                try:
                    os.remove(file_path)
                    logging.info(f"Deleted temp file {file_path}.")
                except Exception as e:
                    logging.error(f"Error deleting temp file {file}: {e}")

    def system_maintenance(self):
        os_type = platform.system()
        if os_type == "Windows":
            os.system("cleanmgr /sagerun:1")
        elif os_type == "Linux":
            os.system("sudo apt-get autoremove -y")
            os.system("sudo apt-get autoclean -y")
        elif os_type == "Darwin":  # macOS
            os.system("sudo rm -rf /Library/Caches/*")
            os.system("sudo rm -rf ~/Library/Caches/*")
        logging.info("System maintenance completed.")

    def system_report(self):
        return {
            'OS': platform.system(),
            'Processor': platform.processor(),
            'Memory': psutil.virtual_memory().total,
            'Disk Usage': self.check_disk_usage()
        }