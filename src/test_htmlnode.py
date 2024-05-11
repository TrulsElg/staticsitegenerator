import unittest

from htmlnode import HTMLNode, LeafNode

class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = HTMLNode(tag="p", value="This is a text node")
        node2 = HTMLNode(tag="p", value="This is a text node")
        self.assertEqual(node, node2)

        node = HTMLNode(tag="a", value="This is a text node", props={"href": "https://www.boot.dev"})
        node2 = HTMLNode(tag="a", value="This is a text node", props={"href": "https://www.boot.dev"})
        self.assertEqual(node, node2)

        lnode = LeafNode("p", "This is a paragraph of text.")
        rendered_text = "<p>This is a paragraph of text.</p>"
        self.assertEqual(lnode.to_html(), rendered_text)

        lnode = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
        rendered_text = '<a href="https://www.google.com">Click me!</a>'
        self.assertEqual(lnode.to_html(), rendered_text)
    
    def test_not_eq(self):
        node = HTMLNode(tag="a", value="This is a text node", props={"href": "https://www.boot.dev"})
        node2 = HTMLNode(tag="p", value="This is a text node")
        self.assertNotEqual(node, node2)

        node = HTMLNode(tag="a", value="This is a text node", props={"href": "https://www.boot.dev"})
        node2 = HTMLNode(tag="a", value="This is a text node", props={"href": "https://some.different.link"})
        self.assertNotEqual(node, node2)

        lnode = LeafNode("a", "Click here!", {"href": "https://www.google.com"})
        rendered_text = '<a href="https://www.google.com">Click me!</a>'
        self.assertNotEqual(lnode.to_html(), rendered_text)

        lnode = LeafNode("a", "Click me!", {"href": "https://www.google.no"})
        rendered_text = '<a href="https://www.google.com">Click me!</a>'
        self.assertNotEqual(lnode.to_html(), rendered_text)
        

if __name__ == "__main__":
    unittest.main()