from extract_links import extract_markdown_links, extract_markdown_images

text_type_text="text"
text_type_bold="bold"
text_type_italic="italic"
text_type_code="code"
text_type_image="image"
text_type_link="link"

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


def split_nodes_image(old_nodes: list):
    new_nodes = list()
    for node in old_nodes:
        images = extract_markdown_images(node.text)
        if images:
            non_image_sections = list()
            non_image_sections.extend(node.text.split(f"![{images[0][0]}]({images[0][1]})", 1))
            for image in images[1:]:
                text_to_split = non_image_sections.pop()
                non_image_sections.extend(text_to_split.split(f"![{image[0]}]({image[1]})", 1))

            image_nodes = list()
            for image in images:
                image_nodes.append(TextNode(text=image[0], text_type=text_type_image, url=image[1]))
            text_nodes = list()
            for text in non_image_sections:
                text_nodes.append(TextNode(text=text, text_type=text_type_text))
            
            print(image_nodes)
            print(text_nodes)
            l = list()
            for i in range(max(len(image_nodes), len(text_nodes))):
                if i+1 <= len(text_nodes):
                    l.append(text_nodes[i])
                if i+1 <= len(image_nodes):
                    l.append(image_nodes[i])
            
            l = [n for n in l if n.text]
            
            new_nodes.extend(l)

        else:
            new_nodes.append(node)

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