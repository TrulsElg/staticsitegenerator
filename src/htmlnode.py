class HTMLNode():
    def __init__(self, tag: str = None, value: str = None, children: list = None, props:dict = None) -> None:
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props


    def to_html(self):
        raise NotImplementedError()
    

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


if __name__ == "__main__":
    pass
