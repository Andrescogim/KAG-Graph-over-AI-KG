import xml.etree.ElementTree as ET

class LecturaXML:
    def __init__(self, ruta):
        self.tree = ET.parse(ruta)
        self.root = self.tree.getroot()

    def get_abs(self):
        
        """Extrae tuplas: (id, abstracts) del XML"""
        
        abs = []
        for text in self.root.findall(".//text"):
            text_id = text.get("id")
            abs_elem = text.find("abs")

            if abs_elem is not None:
                abs.append((text_id, abs_elem.text))

        return abs