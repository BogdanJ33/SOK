from django.http import HttpResponse
from django.shortcuts import render
from django.apps.registry import apps
from django.utils.safestring import mark_safe


def index(request):
    return render(request, 'index.html')



def parse_and_visualize(request):
    if request.method == 'POST':
        uploaded_file = request.POST.get('file')
        uploaded_file = uploaded_file[12:]
        print(uploaded_file)



        parser = apps.get_app_config('core').pluginXml
        pluginVisualization = apps.get_app_config('core').pluginVisualization

        parsed_data = parser[0].parse("../XMLFiles/" + uploaded_file)  # Koristi ime fajla
        print(parsed_data)
        parser[0].print_node(parsed_data)

        nodes, links = parser[0].getNodeList(parsed_data)
        print(links)

        visualization_html = pluginVisualization[0].visualize(nodes, links)
        visualization_html = mark_safe(visualization_html)

        return render(request, 'index.html', {'visualization_html': visualization_html, 'nodes': nodes, 'links': links})
    return render(request, 'index.html')






