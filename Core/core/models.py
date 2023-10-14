from django.db import models

class Node:
    def __init__(self, attributes):
        self.attributes = attributes
        self.neighbors = []

    def add_neighbor(self, node):
        self.neighbors.append(node)

class Graph:
    def __init__(self):
        self.nodes = []

    def add_node(self, node):
        self.nodes.append(node)