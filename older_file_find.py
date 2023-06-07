import os
import time

def find_older_files(directory, days):
    current_time = time.time()
    seven_days_ago = current_time - (days * 24 * 60 * 60)

    for root, dirs, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            if os.path.isfile(file_path):
                modified_time = os.path.getmtime(file_path)
                if modified_time < seven_days_ago:
                    print("Found file:", file_path)

# Usage example
directory = "/home/shiwi"
days = 7
find_older_files(directory, days)
