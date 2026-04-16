import xml.etree.ElementTree as ET

class LecturaXML:
    def __init__(self, xml):
        path = "C:/Users/andre/OneDrive/Escritorio/TFM/KAG/AI-KG/Project/KAG-Graph-over-AI-KG/data/processed/xml/"
        file = f"{path}{xml}.xml"
        self.tree = ET.parse(file)
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