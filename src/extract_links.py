import re


def extract_markdown_images(text: str):
    pattern = r"!\[(.*?)\]\((.*?)\)"
    matches = re.findall(pattern=pattern, string=text)
    return matches


def extract_markdown_links(text: str):
    pattern = r" \[(.*?)\]\((.*?)\)"
    matches = re.findall(pattern=pattern, string=text)
    return matches


if __name__ == "__main__":
    pass