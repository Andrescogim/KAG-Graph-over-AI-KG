from datetime import datetime as dt
import pandas as pd

class GuardarResultados:
    def __init__(self):
        pass

    def guardar_resultados(out_df):
        """Guarda resultados de extraccion en csv"""

        path = "C:/Users/andre/OneDrive/Escritorio/TFM/KAG/AI-KG/Project/KAG-Graph-over-AI-KG/outputs/resultados/"
        
        ahora = dt.now()
        fecha_hora = ahora.strftime("%Y-%m-%d_%H-%M")
        out_name = f"OUTPUT_{fecha_hora}.csv"
        out_file = f"{path}{out_name}"

        out_df.to_csv(out_file, index=False)



    def guardar_registro(xmls, modelo_LLM, prompt):
        """
            Guarda registro de ejecucion.
            En un txt se guarda:
            - Fecha y hora de ejecucion
            - Datasets utilizados
            - LLM Utilizado
            - Prompt utilizado
        """

        path = "C:/Users/andre/OneDrive/Escritorio/TFM/KAG/AI-KG/Project/KAG-Graph-over-AI-KG/outputs/registro/"
        
        ahora = dt.now()
        fecha_hora = ahora.strftime("%Y-%m-%d_%H-%M")
        out_name = f"Registro_{fecha_hora}.txt"
        out_file = f"{path}{out_name}"

        with open(out_file, "w", encoding="utf-8") as f:
            f.write(f"fecha_ejecucion: {fecha_hora}\n\n")
            f.write(f"xml_utilizados: {xmls}\n\n")
            f.write(f"modelo_utilizado: {modelo_LLM}\n\n")
            f.write(f'prompt_utilizado: \n"{prompt}"')
