from django.http import HttpResponse
from django.shortcuts import render
from django.apps.registry import apps
from django.utils.safestring import mark_safe


def index(request):
    return render(request, 'index.html')



def parse_and_visualize(request):
    parser = apps.get_app_config('core').pluginXml
    pluginVisualization = apps.get_app_config('core').pluginVisualization

    parsed_data = parser[0].parse("../XMLFiles/langualges.xml")
    print(parsed_data)
    parser[0].print_node(parsed_data)

    nodes, edges = parser[0].getNodeList(parsed_data)
    print(nodes)

    visualization_html = pluginVisualization[0].visualize(nodes)
    visualization_html = mark_safe(visualization_html)

    return render(request, 'index.html', {'visualization_html': visualization_html, 'nodes': nodes})





