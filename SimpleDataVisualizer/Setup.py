from setuptools import setup, find_packages
setup(
    name="simple-data-visualizer",
    version="0.1",
    packages=find_packages(),
    entry_points = {
        'visualizer':
            ['simple_visualizer=simpleDataVisualizer.simple_visualizer:SimpleVisualizer'],
    },
    zip_safe=True
)