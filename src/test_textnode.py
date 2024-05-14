import unittest

from textnode import TextNode, split_nodes_delimiter, text_type_bold, text_type_code, text_type_italic, text_type_text

class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", "bold")
        node2 = TextNode("This is a text node", "bold")
        self.assertEqual(node, node2)

        node = TextNode("This is a text node", "bold", "https://www.boot.dev")
        node2 = TextNode("This is a text node", "bold", "https://www.boot.dev")
        self.assertEqual(node, node2)
    
    def test_not_eq(self):
        node = TextNode("This is a text node", "bold")
        node2 = TextNode("This is a text node", "italic")
        self.assertNotEqual(node, node2)

        node = TextNode("This is a text node", "bold", "https://www.boot.dev")
        node2 = TextNode("This is a text node", "bold")
        self.assertNotEqual(node, node2)
    
    def test_split_eq(self):
        node = TextNode("This is text with a `code block` word", text_type_text)
        new_nodes = split_nodes_delimiter([node], "`", text_type_code)
        exptected = [
                        TextNode("This is text with a ", text_type_text),
                        TextNode("code block", text_type_code),
                        TextNode(" word", text_type_text),
                    ]
        self.assertEqual(new_nodes, exptected)

        node = TextNode("This is text with a *code block* word", text_type_text)
        new_nodes = split_nodes_delimiter([node], "*", text_type_bold)
        exptected = [
                        TextNode("This is text with a ", text_type_text),
                        TextNode("code block", text_type_bold),
                        TextNode(" word", text_type_text),
                    ]
        self.assertEqual(new_nodes, exptected)
        

if __name__ == "__main__":
    unittest.main()