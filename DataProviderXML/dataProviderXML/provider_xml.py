
import json
import xml.etree.ElementTree as ET
import os
from core.models import Graph, Node

class ProviderXML:
    def __init__(self):
        self.nodes_dict = {}

    def parse_element(self, element, parent=None):
        attrib = {}
        for key, value in element.attrib.items():
            attrib[key] = value

        attrib["name"] = element.tag
        if element.text and element.text.strip() != "":
            attrib["text"] = element.text.strip()

        node = Node(**attrib, parent=parent)

        children = []
        for child in element:
            child_node = self.parse_element(child, parent=node)
            children.append(child_node)

        node.children = children

        return node

    def print_node(self, node, indent=0):
        if node.text is not None:
            print("  " * indent + node.text)
        for child in node.children:
            self.print_node(child, indent + 1)

    def getNodeList(self, node):
        nodes = []
        edges = []

        # Add information about the current node
        nodes.append({"name": node.name})  # Changed this line

        for child in node.children:
            edge = {"source": node.name, "target": child.name}  # Changed this line
            edges.append(edge)

            # Recursively call getNodeList on the child node
            child_nodes, child_edges = self.getNodeList(child)

            # Extend the nodes and edges lists with the child's information
            nodes.extend(child_nodes)
            edges.extend(child_edges)

        return nodes, edges


    def parse(self, file_path):
        tree = ET.parse(file_path)
        root = tree.getroot()

        return self.parse_element(root)


#parser = ProviderXML()
#parsed_data = parser.parse('../../XMLFiles/languages.xml')
#print(parsed_data)
