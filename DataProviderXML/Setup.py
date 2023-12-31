from setuptools import setup, find_packages
setup(
    name="data-provider-xml",
    version="0.1",
    packages=find_packages(),
    entry_points = {
        'xml_parser':
            ['provider_xml=dataProviderXML.provider_xml:ProviderXML'],
    },
    zip_safe=True
)