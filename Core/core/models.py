from django.db import models

from django.db import models


class Node:
    def __init__(self, name, attributes=None, children=None, text=None, parent = None):
        self.name = name
        self.attributes = attributes or {}
        self.children = children or []
        self.text = text
        self.parent = parent

    def add_child(self, child):
        self.children.append(child)



    def __repr__(self):
        return f"Node({self.name}, {self.attributes}, {self.children}, {self.text})"


class Graph:
    def __init__(self, root=None):
        self.root = root

    def set_root(self, root):
        self.root = root

    def __repr__(self):
        return f"Graph({self.root})"
