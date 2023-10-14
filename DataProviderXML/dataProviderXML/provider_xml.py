
import json
import xml.etree.ElementTree as ET
import os
from core.models import Graph, Node

class ProviderXML:
    def __init__(self):
        self.nodes_dict = {}

    def parse_element(self, element):
        attrib = {}
        for key, value in element.attrib.items():
            attrib[key] = value

        attrib["name"] = element.tag
        if element.text and element.text.strip() != "":
            attrib["text"] = element.text.strip()

        node = Node(**attrib)

        children = []
        for child in element:
            child_node = self.parse_element(child)
            children.append(child_node)

        node.children = children

        return node

    def print_node(self, node, indent=0):
        print("  " * indent + node.name)
        for child in node.children:
            self.print_node(child, indent + 1)

    def parse(self, file_path):
        tree = ET.parse(file_path)
        root = tree.getroot()

        return self.parse_element(root)


#parser = ProviderXML()
#parsed_data = parser.parse('../../XMLFiles/languages.xml')
#print(parsed_data)
