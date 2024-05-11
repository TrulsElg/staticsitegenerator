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
        for prop in self.props:
            string += f' {prop}="{self.props[prop]}"'
        return string
    

    def __repr__(self) -> str:
        return f"HTMLNode({self.tag}, {self.value}, {self.children}, {self.props})"
    

    def __eq__(self, value: object) -> bool:
        return self.tag==value.tag and self.value==value.value and self.children==value.children and self.props==value.props


if __name__ == "__main__":
    pass
