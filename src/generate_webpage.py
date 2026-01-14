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