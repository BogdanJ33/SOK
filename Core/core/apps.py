import pkg_resources
from django.apps import AppConfig

class CoreConfig(AppConfig):
    pluginXml = []
    pluginVisualization = []
    name = 'core'

    def ready(self):
        self.pluginXml = load_plugins("xml_parser")
        self.pluginVisualization = load_plugins("visualizer")
        print("parser", len(self.pluginXml))
        print("visual", len(self.pluginVisualization))

def load_plugins(group_tag):
    plugins = []
    for ep in pkg_resources.iter_entry_points(group=group_tag):
        p = ep.load()
        plugin = p()
        plugins.append(plugin)
    return plugins