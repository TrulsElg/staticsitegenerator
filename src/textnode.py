text_type_text="text"
text_type_bold="bold"
text_type_italic="italic"
text_type_code="code"

def split_nodes_delimiter(old_nodes: list, delimiter: str, text_type: str):

    new_nodes = list()
    for node in old_nodes:
        if node.text_type != text_type_text:
            new_nodes.append(node)
            continue

        delim_splits = node.text.split(delimiter)
        if len(delim_splits) % 2 == 0:
            raise ValueError("Invalid markdown, formatted section not closed")
        
        for index, section in enumerate(delim_splits):
            if index % 2 == 0:
                node_type = text_type_text
            else:
                node_type = text_type
            new_nodes.append(TextNode(text=section, text_type=node_type))
    
    return new_nodes
        


class TextNode:
    def __init__(self, text, text_type, url=None) -> None:
        self.text = text
        self.text_type = text_type
        self.url = url
    
    def __eq__(self, value: object) -> bool:
        return self.text==value.text and self.text_type==value.text_type and self.url==value.url
    
    def __repr__(self) -> str:
        return f"TextNode({self.text}, {self.text_type}, {self.url})"

def main():
    pass

if __name__ == "__main__":
    main()