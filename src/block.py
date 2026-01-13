from enum import Enum
import re

class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    UNORDERED_LIST = "unordered_list"
    ORDERED_LIST = "ordered_list"

def markdown_to_blocks(markdown):
    lines = markdown.split("\n")
    blocks = []
    current_block = []
    inside_code = False

    for line in lines:
        is_fence = line.strip().startswith("```")
        if is_fence:
            if not inside_code:
                # starting a code block
                inside_code = True
                if current_block:
                    blocks.append("\n".join(current_block).strip())
                    current_block = []
                current_block.append(line)
            else:
                # ending a code block
                current_block.append(line)
                blocks.append("\n".join(current_block).strip())
                current_block = []
                inside_code = False
            continue

        if inside_code:
            current_block.append(line)
            continue

        if line.strip() != "":
            current_block.append(line)
        elif current_block != []:
            blocks.append("\n".join(current_block).strip())
            current_block = []
    if current_block != []:
        blocks.append("\n".join(current_block).strip())
    return blocks

def block_to_block_type(block):
    match = re.match(r"#{1,6} ", block)
    if match is not None:
        return BlockType.HEADING
    if block.startswith("```\n") and block.endswith("```"):
        return BlockType.CODE
    lines = block.split("\n")
    quote_possible = True
    unordered_possible = True
    ordered_possible = True
    for line in lines:
        line_match = re.match(r"[0-9]+.", line)
        if not line.startswith("> "):
            quote_possible = False
        if not line.startswith("- "):
            unordered_possible = False
        if line_match is None:
            ordered_possible = False
    if quote_possible:
        return BlockType.QUOTE
    if unordered_possible:
        return BlockType.UNORDERED_LIST
    if ordered_possible:
        return BlockType.ORDERED_LIST
    return BlockType.PARAGRAPH