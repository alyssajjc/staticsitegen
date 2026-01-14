import os
import shutil

def copy_src_to_dest(source, dest):
    if not os.path.exists(source):
        raise Exception("Source directory does not exist")
    # delete all contents of dest
    if os.path.exists(dest):
        shutil.rmtree(dest)
    os.mkdir("public")
    # copy all files from source to dest
    for file in os.listdir(source):
        copy_src(source, dest, file)

def copy_src(source, dest, filename):
    full_path = os.path.join(source, filename)
    if not os.path.exists(full_path):
        raise Exception("Source does not exist")

    if os.path.isdir(full_path):
        target_path = os.path.join(dest, filename)
        os.mkdir(target_path)
        print(f"Creating directory {target_path}")
        for file in os.listdir(full_path):
            copy_src(full_path, target_path, file)

    if os.path.isfile(full_path):
        print(f"Copying {filename} to {dest}")
        shutil.copy(full_path, dest)