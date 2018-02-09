import os

my_path = 'C:/Users/TLC/Desktop/Python Web Development/Part 1/book1-exercises-master/chp09/practice_files/little pics'

for current_folder, subfolders, file_names in os.walk(my_path):
    for file_name in file_names:
        if file_name.lower().endswith('.jpg'):
            current_path = os.path.join(current_folder,file_name)
            if os.path.getsize(current_path) < 2000:
                os.remove(current_path)
