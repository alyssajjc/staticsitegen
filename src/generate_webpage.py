import os

from src.markdown_to_html import markdown_to_html_node

def extract_title(markdown):
    lines = markdown.split("\n")
    for line in lines:
        if line.startswith("# "):
            line = line[1:]
            line = line.strip()
            return line
    raise Exception("No title found")

def generate_page(from_path, template_path, dest_path):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")
    with open(from_path, "r") as f:
        markdown = f.read()
    with open(template_path, "r") as t:
        template_file = t.read()
    markdown_html = markdown_to_html_node(markdown).to_html()
    title = extract_title(markdown)
    page = template_file.replace("{{ Title }}", title).replace("{{ Content }}", markdown_html)
    os.makedirs(os.path.dirname(dest_path), exist_ok=True)
    with open(dest_path, "w") as f:
        f.write(page)

def generate_pages_recursive(dir_path_content, template_path, dest_dir_path):
    for file in os.listdir(dir_path_content):
        full_path = os.path.join(dir_path_content, file)
        full_dest_path = os.path.join(dest_dir_path, file)
        if os.path.isdir(full_path):
            os.mkdir(full_dest_path)
            generate_pages_recursive(full_path, template_path, full_dest_path)
        elif os.path.isfile(full_path):
            generate_page(full_path, template_path, os.path.join(dest_dir_path, file[:-3] + ".html"))