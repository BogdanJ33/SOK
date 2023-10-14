from django.http import HttpResponse
from django.shortcuts import render
from django.apps.registry import apps
def index(request):
    return render(request, 'index.html')



def parse_and_visualize(request):
    parser = apps.get_app_config('core').pluginXml
    pluginVisualization = apps.get_app_config('core').pluginVisualization
    parsed_data = parser[0].parse("../XMLFiles/langualges.xml")
    parser[0].print_node(parsed_data)
    return HttpResponse(parsed_data)

