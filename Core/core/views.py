from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.apps.registry import apps
from django.urls import reverse
from django.utils.safestring import mark_safe
context = {}
context["visualization_html"] = ""
def index(request):

    # Clear the session value after retrieving it
    return render(request, 'index.html', context)



def parse_and_visualize(request):
    if request.method == 'POST':
        uploaded_file = request.POST.get('file')
        uploaded_file = uploaded_file[12:]
        parser = apps.get_app_config('core').pluginXml
        pluginVisualization = apps.get_app_config('core').pluginVisualization
        # parsed_data = parser[0].parse("../XMLFiles/movies.xml")
        parsed_data = parser[0].parse("../XMLFiles/" + uploaded_file)  # Koristi ime fajla
        nodes, links = parser[0].getNodeList(parsed_data)
        visualization_html = pluginVisualization[0].visualize(nodes, links)
        visualization_html = mark_safe(visualization_html)
        global context
        context["visualization_html"] = visualization_html
        return HttpResponseRedirect(reverse("index"))



def visualize(request, visualization_html):
    return render(request, 'index.html', {'visualization_html': visualization_html})






