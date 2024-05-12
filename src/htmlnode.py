from textnode import TextNode

def text_node_to_html_node(text_node: TextNode):
    supported_text_types = ["text", "bold", "italic", "code", "link", "image"]
    if text_node.text_type not in supported_text_types:
        raise ValueError("Text type not supported")
    
    if text_node.text_type == "text":
        return LeafNode(value=text_node.text)
    if text_node.text_type == "bold":
        return LeafNode(tag="b", value=text_node.text)
    if text_node.text_type == "italic":
        return LeafNode(tag="i", value=text_node.text)
    if text_node.text_type == "code":
        return LeafNode(tag="code", value=text_node.text)
    if text_node.text_type == "link":
        return LeafNode(tag="a", value=text_node.text, props={"href": text_node.url})
    if text_node.text_type == "image":
        return LeafNode(tag="img", props={"src": text_node.url, "alt": text_node.text})


class HTMLNode():
    def __init__(self, tag: str = None, value: str = None, children: list = None, props:dict = None) -> None:
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props


    def to_html(self):
        raise NotImplementedError("This method is not implemented in this base class")
    

    def props_to_html(self):
        string = ""
        if self.props:
            for prop in self.props:
                string += f' {prop}="{self.props[prop]}"'
        return string
    

    def __repr__(self) -> str:
        return f"HTMLNode({self.tag}, {self.value}, {self.children}, {self.props})"
    

    def __eq__(self, value: object) -> bool:
        return self.tag==value.tag and self.value==value.value and self.children==value.children and self.props==value.props


class LeafNode(HTMLNode):
    def __init__(self, tag: str, value: str, props: dict = None) -> None:
        super().__init__(tag=tag, value=value, children=None, props=props)
    

    def to_html(self):
        if self.value is None:
            raise ValueError("Invalid HTML: no value")
        if self.tag is None:
            return self.value
        return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"

    
    def __repr__(self):
        return f"LeafNode({self.tag}, {self.value}, {self.props})"


class ParentNode(HTMLNode):
    def __init__(self, tag: str, children: list, props: dict = None) -> None:
        super().__init__(tag, None, children, props)

    
    def to_html(self):
        if self.tag is None:
            raise ValueError("No tag set")
        if self.children is None:
            raise ValueError("No children set")
        
        child_strings = ""
        for child in self.children:
            child_strings += child.to_html()
        
        return f"<{self.tag}{self.props_to_html()}>{child_strings}</{self.tag}>"

if __name__ == "__main__":
    pass
