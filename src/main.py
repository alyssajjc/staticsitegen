from src.copy_static import copy_src_to_dest
from src.generate_webpage import generate_page, generate_pages_recursive


def main():
    copy_src_to_dest("static", "public")
    generate_pages_recursive("content", "template.html", "public")
main()