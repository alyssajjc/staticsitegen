from src.copy_static import copy_src_to_dest
from src.generate_webpage import generate_page

def main():
    copy_src_to_dest("static", "public")
    generate_page("content/index.md", "template.html", "public/index.html")
main()