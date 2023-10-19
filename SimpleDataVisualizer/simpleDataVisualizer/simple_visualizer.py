
import json

from core.models import Graph, Node
from django.template import Template, Context
import os.path

from django.template.loader import render_to_string


class SimpleVisualizer:

    def convert_to_D3(self, node):
        d3_json = {"name": node.name}

        if node.attributes:
            d3_json["attributes"] = node.attributes

        if node.children:
            d3_json["children"] = [self.visualize(child) for child in node.children]

        return d3_json

    def visualize(self, graph_data):
        context = {'nodes': graph_data
        }
        return render_to_string('visualizer.html', context)

