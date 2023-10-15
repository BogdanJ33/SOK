
import json

from core.models import Graph, Node
from django.template import Template, Context
import os.path

class SimpleVisualizer:
    def visualize(self, graph: Node):
        rawTemplate = '''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Prosta Vizualizacija</title>
    <script src="https://d3js.org/d3.v6.min.js"></script>
    <style>
        .node {
            fill: #ccc;
            stroke: #fff;
            stroke-width: 2px;
        }

        .link {
            stroke: #777;
            stroke-width: 2px;
        }
    </style>
</head>
<body>
    <svg width="600" height="400"></svg>

    <script>
        var nodes = [
            {id: 1, name: "Node 1"},
            {id: 2, name: "Node 2"},
            {id: 3, name: "Node 3"},
            {id: 4, name: "Node 4"}
        ];

        var links = [
            {source: 1, target: 2},
            {source: 1, target: 3},
            {source: 2, target: 4}
        ];

        var svg = d3.select("svg"),
            width = +svg.attr("width"),
            height = +svg.attr("height");

        var simulation = d3.forceSimulation(nodes)
            .force("link", d3.forceLink(links).id(d => d.id))
            .force("charge", d3.forceManyBody().strength(-200))
            .force("center", d3.forceCenter(width / 2, height / 2));

        var link = svg.selectAll(".link")
            .data(links)
            .enter().append("line")
            .attr("class", "link");

        var node = svg.selectAll(".node")
            .data(nodes)
            .enter().append("circle")
            .attr("class", "node")
            .attr("r", 10);

        simulation.on("tick", () => {
            link.attr("x1", d => d.source.x)
                .attr("y1", d => d.source.y)
                .attr("x2", d => d.target.x)
                .attr("y2", d => d.target.y);

            node.attr("cx", d => d.x)
                .attr("cy", d => d.y);
        });
    </script>
</body>
</html>'''
        template = Template(rawTemplate)
        context = Context({"graph": graph})
        return rawTemplate

