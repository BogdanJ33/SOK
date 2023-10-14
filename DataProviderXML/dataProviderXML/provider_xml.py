from lxml import etree

class ProviderXML:
    def __init__(self):
        self.data = {}

    def parse(self, file_path):
        with open(file_path, 'rb') as f:
            tree = etree.parse(f)
        root = tree.getroot()

        for element in root.iter():
            self.data[element.tag] = element.text

        return self.data

#parser = ProviderXML()
#parsed_data = parser.parse('../../XMLFiles/languages.xml')
#print(parsed_data)
