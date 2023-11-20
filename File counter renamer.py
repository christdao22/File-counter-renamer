import os

def rename_files_in_folders(base_path, name_base, name_ctr):
    files = os.listdir(base_path)
    for file in files:
        folder_path = os.path.join(base_path, str(file))
        if os.path.exists(folder_path):
            if os.path.isfile(folder_path):
                new_filename = f'{name_base}{name_ctr}{os.path.splitext(file)[1]}'
                new_file_path = os.path.join(base_path, new_filename)
                # Rename the file
                os.rename(folder_path, new_file_path)
                print(f"Renamed: {folder_path} to {new_file_path}")
                name_ctr+=1

# pwede ra ni machange ang name
name_base = '';
name_ctr = 560;

# Specify the base folder
base_folder_path = "C:/Users/Deped/Desktop/test/"
rename_files_in_folders(base_folder_path, name_base, name_ctr)