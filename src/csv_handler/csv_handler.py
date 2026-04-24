import pandas as pd

class LecturaCSV:
    PATH = "C:/Users/andre/OneDrive/Escritorio/TFM/KAG/AI-KG/Project/KAG-Graph-over-AI-KG/data/processed/csv/"

    def lectura_abs(file):
        
        """Extrae (id, abstracts) del csv a un df de pandas"""
        
        df = pd.read_csv(f"{LecturaCSV.PATH}{file}.csv")

        return df

    def get_rels_entis(file):
        
        """Extrae (relaciones, entidades, id, b_hlight) del csv a un df de pandas"""
        
        df = pd.read_csv(f"{LecturaCSV.PATH}{file}.csv")

        return df