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



    def guardar_registro(files, modelo_LLM, prompt, opciones_LLM, n_abs, t_ejecucion, ratio_validas):
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
            f.write(f"archivos_utilizados: {files}\n\n")
            f.write(f"Nº abstracts procesados: {n_abs}\n\n")
            f.write(f"Respuestas con formato valido: {ratio_validas*100}%\n\n")
            f.write(f"tº ejecucion: {t_ejecucion}\n\n")
            f.write(f"modelo_utilizado: {modelo_LLM}\n\n")
            f.write(f"parametros LLM: {opciones_LLM}\n\n")
            f.write(f'prompt_utilizado: \n"{prompt}"')


    def guardar_metricas(metric_df):
        """Guarda resultados de extraccion en csv"""

        path = "C:/Users/andre/OneDrive/Escritorio/TFM/KAG/AI-KG/Project/KAG-Graph-over-AI-KG/outputs/metricas/"
        
        ahora = dt.now()
        fecha_hora = ahora.strftime("%Y-%m-%d_%H-%M")
        out_name = f"Metricas_{fecha_hora}.csv"
        out_file = f"{path}{out_name}"

        metric_df.to_csv(out_file, index=False)