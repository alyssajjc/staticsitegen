def markdown_to_blocks(markdown):
    lines = markdown.split("\n")
    blocks = []
    current_block = []
    for line in lines:
        if line != "":
            current_block.append(line)
        elif current_block != []:
            blocks.append("\n".join(current_block).strip())
            current_block = []
    if current_block != []:
        blocks.append("\n".join(current_block).strip())
    return blocks