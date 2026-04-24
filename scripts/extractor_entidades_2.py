import sys
import os
from pathlib import Path
import pandas as pd
import time

current_file = Path(__file__).resolve()
root_dir = current_file.parent.parent
sys.path.append(str(root_dir))

from config.settings.settings_3 import CSVS_ABS, CSVS_RELS_ENTIS, MODELO, PROMPT, LLM_OPTIONS
from src.csv_handler.csv_handler import LecturaCSV
from src.LLM_interaction.LLM_interaction import LlamadaLLM
from src.output_save.output_save import GuardarResultados
from src.output_check.output_check import ComprobarOutput



def main(csvs, modelo, prompt, opciones_LLM):
    """ 
    Extraccion de entidades a partir de los csv
    """
    output_df = pd.DataFrame(columns=["csv_source", "id", "entidades"])
    n_abs = 0
    t_lectura = 0
    t0 = time.time()

    # for xml in xmls:
    for csv in csvs:
        print("-"*60)
        print(f"COMIENZA la extraccion para el archivo: {csv}.csv")
        
        t0_lectura = time.time()
        abstracts = LecturaCSV.lectura_abs(csv)       
        
        tfin_lectura = time.time()
        t_lectura += (tfin_lectura - t0_lectura)
        
        print(f"Abstracts del archivo: {csv}.csv EXTRAIDOS")
        print(f"Nº de Abstracts: {len(abstracts)}")
        # abstracts = abstracts[0:50] # PARA PRUEBAS
        abstracts = abstracts.head(200) # PARA PRUEBAS
        n_abs += len(abstracts)

        for index, row in abstracts.iterrows():
            abs_id = row["id"]
            abstract = row["abs"]        
            prompt_final = f"{prompt}{abstract}"
            respuesta = LlamadaLLM.generate(modelo, prompt_final, opciones_LLM)
            output_df.loc[len(output_df)] = [csv, abs_id, respuesta]
            # if index%10 == 0:
            #     os.system("ollama stop phi3")
            #     LlamadaLLM.reset(modelo)
            #     time.sleep(3)
            #     print(f"Extraccion completa del abstract: {index}")

            print(f"Extraccion completa del abstract: {index}")
        print(f"FINALIZA la extraccion para el archivo: {csv}.csv")

    # METRICAS
    # De momento fuera del bucle
    df_metric = ComprobarOutput.comprobar_entidades(output_df)
    ratio_validas = ComprobarOutput.metricas_generales(df_metric)
    rels_entis = LecturaCSV.get_rels_entis(CSVS_RELS_ENTIS)
    df_metric = ComprobarOutput.metricas_entidades(output_df, rels_entis, df_metric)
    
    tfin = time.time()
    tprocesado = tfin - t0 - t_lectura
    print("GUARDANDO RESULTADOS...")
    GuardarResultados.guardar_resultados(output_df)
    print("GUARDANDO REGISTROS...")
    GuardarResultados.guardar_registro(csvs, modelo, prompt, opciones_LLM, n_abs, tprocesado, ratio_validas)
    print("GUARDANDO METRICAS...")
    GuardarResultados.guardar_metricas(df_metric)
    print("FINALIZA EXTRACCION")
    print(":)")


if __name__ == "__main__":
    main(CSVS_ABS, MODELO, PROMPT, LLM_OPTIONS)