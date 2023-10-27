
import json

from core.models import Graph, Node
from django.template import Template, Context
import os.path

from django.template.loader import render_to_string


class SimpleVisualizer:

    def visualize(self, graph_data, graph_data2):
        context = {'nodes': graph_data,
                   'links': graph_data2
        }
        return render_to_string('visualizer.html', context)

