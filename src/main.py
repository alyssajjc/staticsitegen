from src.copy_static import copy_src_to_dest
from src.generate_webpage import generate_pages_recursive
import sys


def main():
    if len(sys.argv) <= 1:
        basepath = "/"
    else:
        basepath = sys.argv[1]
    copy_src_to_dest("static", "docs")
    generate_pages_recursive("content", "template.html", "docs", basepath)
main()