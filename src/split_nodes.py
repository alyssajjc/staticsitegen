from textnode import TextNode, TextType
from extract_links import extract_markdown_links, extract_markdown_images

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue
        inline_text = node.text.split(delimiter)
        if len(inline_text) % 2 == 0:
            raise Exception("mismatched delimiters")

        for i, part in enumerate(inline_text):
            if i % 2 == 0:
                if part:
                    new_nodes.append(TextNode(part, TextType.TEXT))
            elif i % 2 != 0:
                new_nodes.append(TextNode(part, text_type))
    return new_nodes

def split_nodes_link(old_nodes):
    new_nodes = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue
        links = extract_markdown_links(node.text)
        if len(links) == 0:
            new_nodes.append(node)
            continue
        current_text = node.text
        for link in links:
            sections = current_text.split(f"[{link[0]}]({link[1]})", 1)
            if sections[0] != "":
                new_nodes.append(TextNode(sections[0], TextType.TEXT))
            new_nodes.append(TextNode(link[0], TextType.LINK, link[1]))
            current_text = sections[1] if len(sections) > 1 else ""
        if current_text != "":
            new_nodes.append(TextNode(current_text, TextType.TEXT))
    return new_nodes

def split_nodes_image(old_nodes):
    new_nodes = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue
        images = extract_markdown_images(node.text)
        if len(images) == 0:
            new_nodes.append(node)
            continue
        current_text = node.text
        for image in images:
            sections = current_text.split(f"![{image[0]}]({image[1]})", 1)
            if sections[0] != "":
                new_nodes.append(TextNode(sections[0], TextType.TEXT))
            new_nodes.append(TextNode(image[0], TextType.IMAGE, image[1]))
            current_text = sections[1] if len(sections) > 1 else ""
        if current_text != "":
            new_nodes.append(TextNode(current_text, TextType.TEXT))
    return new_nodes

def text_to_textnodes(text):
    italics = split_nodes_delimiter([TextNode(text, TextType.TEXT)], "_", TextType.ITALIC)
    bolds = split_nodes_delimiter(italics, "**", TextType.BOLD)
    codes = split_nodes_delimiter(bolds, "`", TextType.CODE)
    links = split_nodes_link(codes)
    images = split_nodes_image(links)
    return images