from src.block import markdown_to_blocks, block_to_block_type, BlockType
from src.textnode import TextType, text_node_to_html_node, TextNode
from src.htmlnode import HTMLNode, ParentNode
from src.split_nodes import text_to_textnodes
import re

def markdown_to_html_node(markdown):
    raw_blocks = markdown_to_blocks(markdown)
    blocks = []

    for block in raw_blocks:
        block_type = block_to_block_type(block)
        match block_type:
            case BlockType.CODE:
                block = block.removeprefix("```\n")
                block = block.removesuffix("```")
                lines = block.split("\n")
                if lines and lines[0].strip("") == "":
                    lines = lines[1:]
                if lines and lines[-1].strip("") == "":
                    lines = lines[:-1]
                common = min((leading_spaces(l) for l in lines if l.strip() != ""), default = 0)
                dedented = "\n".join(l[common:] for l in lines)

                code_node = TextNode(dedented, TextType.CODE)

                block_node = ParentNode("pre", children = [text_node_to_html_node(code_node)])
                blocks.append(block_node)

            case BlockType.PARAGRAPH:
                block_text = clean_lines(block)
                block_node = ParentNode("p", children = text_to_children(block_text))
                blocks.append(block_node)

            case BlockType.QUOTE:
                lines = block.split("\n")
                lines = [line.removeprefix(">") for line in lines]
                lines = [line.strip() for line in lines if line.strip() != "" and not line.strip().startswith("--")]
                block_text = " ".join(lines)
                block_node = ParentNode("blockquote", children = text_to_children(block_text))
                blocks.append(block_node)

            case BlockType.UNORDERED_LIST:
                block_node = ParentNode("ul", children = list_children(block))
                blocks.append(block_node)

            case BlockType.ORDERED_LIST:
                block_node = ParentNode("ol", children = ordered_list_children(block))
                blocks.append(block_node)

            case BlockType.HEADING:
                lines = block.split("\n")
                for line in lines:
                    if line.strip() == "":
                        continue
                    count, clean_text = clean_header(line)
                    block_node = ParentNode(f"h{count}", children = text_to_children(clean_text))
                    blocks.append(block_node)

            case _:
                block_node = ParentNode("div", children = text_to_children(block))
                blocks.append(block_node)

    parent_node = ParentNode("div", children = blocks)
    return parent_node

def clean_header(text):
    count = 0
    text = text.strip()
    while text.startswith("#"):
        count += 1
        text = text[1:]
    clean_text = text.lstrip(" ")
    return count, clean_text

def clean_lines(text):
    lines = text.split("\n")
    stripped_lines = [line.strip() for line in lines if line.strip() != ""]
    return " ".join(stripped_lines)

def text_to_children(text):
    text_nodes = text_to_textnodes(text)
    html_nodes = []
    for node in text_nodes:
        html_nodes.append(text_node_to_html_node(node))
    return html_nodes

def list_children(text):
    lines = text.split("\n")
    stripped_lines = [line.strip() for line in lines if line.strip() != ""]
    for line in stripped_lines:
        line = line.removeprefix("- ")
        yield ParentNode("li", children = text_to_children(line))

def ordered_list_children(text):
    lines = text.split("\n")
    stripped_lines = [line.strip() for line in lines if line.strip() != ""]
    for line in stripped_lines:
        line = line.removeprefix(re.match(r"[0-9]+. ", line).group(0))
        yield ParentNode("li", children = text_to_children(line))

def leading_spaces(text):
    return len(text) - len(text.lstrip(" "))