from textnode import *
import shutil
import os

def main():
    test_node = TextNode("Anchor text", "link", "https://www.google.com")
    print(test_node)
    copy_src_to_dest("static", "public")

def copy_src_to_dest(source, dest):
    if not os.path.exists(dest) or os.path.exists(source):
        raise Exception("Source or destination directory does not exist")
    # delete all contents of dest
    shutil.rmtree(dest)
    # copy all files from source to dest
    copy_src(source, dest)

def copy_src(source, dest):
    if not os.path.exists(source):
        raise Exception("Destination does not exist")

    if os.path.isdir(source):
        target_path = os.path.join(dest, source)
        os.mkdir(target_path)
        for file in os.listdir(source):
            copy_src(os.path.join(source, file), dest)

    if os.path.isfile(dest):
        target_path = os.path.join(dest, source)
        shutil.copy(target_path, dest)

main()