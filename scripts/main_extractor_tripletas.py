import sys
import os
from pathlib import Path
import pandas as pd
import time

current_file = Path(__file__).resolve()
root_dir = current_file.parent.parent
sys.path.append(str(root_dir))

from config.settings.settings_tripletas_1 import CSVS_ABS, CSVS_RELS_ENTIS, MODELO, PROMPT, LLM_OPTIONS, COMENTARIOS, N_ABS

from extractor_tripletas import extractor_tripletas
from src.output_save.output_save import GuardarResultados
from src.output_check.output_check import ComprobarOutput



def main(csvs, modelo, prompt, opciones_LLM, comentarios, n_abs):
    """ 
    Extraccion de tripletas a partir de los csv
    main - separado del bucle de iteracion y procesado
    """
    
    t0 = time.time()

    output_df = extractor_tripletas(csvs, modelo, prompt, opciones_LLM, n_abs)

    tfin = time.time()
    
    # METRICAS
    # De momento fuera del bucle
    # df_metric = ComprobarOutput.comprobar_entidades(output_df)
    # ratio_validas = ComprobarOutput.metricas_generales(df_metric)
    # rels_entis = LecturaCSV.get_rels_entis(CSVS_RELS_ENTIS)
    # df_metric = ComprobarOutput.metricas_entidades(output_df, rels_entis, df_metric)
    
    
    tprocesado = tfin - t0
    print("GUARDANDO RESULTADOS...")
    GuardarResultados.guardar_resultados(output_df)
    print("GUARDANDO REGISTROS...")
    GuardarResultados.guardar_registro(comentarios, csvs, modelo, prompt, opciones_LLM, n_abs, tprocesado, ratio_validas="NA")
    # print("GUARDANDO METRICAS...")
    # GuardarResultados.guardar_metricas(df_metric)
    print("FINALIZA EXTRACCION")
    print(":)")


if __name__ == "__main__":
    main(CSVS_ABS, MODELO, PROMPT, LLM_OPTIONS, COMENTARIOS, N_ABS)