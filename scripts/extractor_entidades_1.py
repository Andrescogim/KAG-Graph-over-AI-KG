import sys
from pathlib import Path
import pandas as pd
import time

current_file = Path(__file__).resolve()
root_dir = current_file.parent.parent
sys.path.append(str(root_dir))

from config.settings.settings_2 import XMLS, MODELO, PROMPT
from src.xml_handler.LecturaXML import LecturaXML
from src.LLM_interaction.LLM_interaction import LlamadaLLM
from src.output_save.output_save import GuardarResultados



def main(xmls, modelo, prompt):
    """ 
    Extraccion de entidades a partir de los xml
    """
    output_df = pd.DataFrame(columns=["xml_source", "id", "entidades"])
    n_abs = 0
    t_lectura = 0
    t0 = time.time()

    for xml in xmls:
        print("-"*60)
        print(f"COMIENZA la extraccion para el archivo: {xml}.xml")
        
        t0_lectura = time.time()
        xml_raw = LecturaXML(xml)       
        abstracts = xml_raw.get_abs()
        
        tfin_lectura = time.time()
        t_lectura += (tfin_lectura - t0_lectura)
        
        print(f"Abstracts del archivo: {xml}.xml EXTRAIDOS")
        print(f"Nº de Abstracts: {len(abstracts)}")
        abstracts = abstracts[0:50] # PARA PRUEBAS
        n_abs += len(abstracts)

        for i, abs in enumerate(abstracts, start=1):
            abs_id = abs[0]
            abstract = abs[1]            
            prompt_final = f"{prompt}{abstract}"
            respuesta = LlamadaLLM.generate(modelo, prompt_final)
            output_df.loc[len(output_df)] = [xml, abs_id, respuesta]
            if i%10 == 0:
                print(f"Extraccion completa del abstract: {i}")
        print(f"FINALIZA la extraccion para el archivo: {xml}.xml")

    tfin = time.time()
    tprocesado = tfin - t0 - t_lectura
    print("GUARDANDO RESULTADOS...")
    GuardarResultados.guardar_resultados(output_df)
    print("GUARDANDO REGISTROS...")
    GuardarResultados.guardar_registro(xmls, modelo, prompt, n_abs, tprocesado)
    print("FINALIZA EXTRACCION")
    print(":)")


if __name__ == "__main__":
    main(XMLS, MODELO, PROMPT)