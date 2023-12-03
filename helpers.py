import os

def make_folder_if_not_exist(folder_path):
     if not os.path.exists(folder_path):
        os.mkdir(folder_path)