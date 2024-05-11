import unittest

from htmlnode import HTMLNode

class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = HTMLNode(tag="p", value="This is a text node")
        node2 = HTMLNode(tag="p", value="This is a text node")
        self.assertEqual(node, node2)

        node = HTMLNode(tag="a", value="This is a text node", props={"href": "https://www.boot.dev"})
        node2 = HTMLNode(tag="a", value="This is a text node", props={"href": "https://www.boot.dev"})
        self.assertEqual(node, node2)
    
    def test_not_eq(self):
        node = HTMLNode(tag="a", value="This is a text node", props={"href": "https://www.boot.dev"})
        node2 = HTMLNode(tag="p", value="This is a text node")
        self.assertNotEqual(node, node2)

        node = HTMLNode(tag="a", value="This is a text node", props={"href": "https://www.boot.dev"})
        node2 = HTMLNode(tag="a", value="This is a text node", props={"href": "https://some.different.link"})
        self.assertNotEqual(node, node2)
        

if __name__ == "__main__":
    unittest.main()