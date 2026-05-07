import pandas as pd
import time


from src.csv_handler.csv_handler import LecturaCSV
from src.LLM_interaction import LLM_interaction_functions as LLM_inter



def lectura_abstracts(csv, n_abs = None):
    abstracts = LecturaCSV.lectura_abs(csv)
    if n_abs is not None:
        abstracts = abstracts.head(n_abs)
    return abstracts



def extraer_tripletas(csv, abstracts, modelo, prompt, opciones_LLM, output_df):
    """ 
    Extraccion de tripletas a partir de los abstracts de los csv
    """

    for index, row in abstracts.iterrows():
        abs_id = row["id"]
        abstract = row["abs"]        
        prompt_final = f"{prompt}{abstract}"
        respuesta = LLM_inter.generate(modelo, prompt_final, opciones_LLM)
        output_df.loc[len(output_df)] = [csv, abs_id, respuesta]
        print(f"Extraccion completa del abstract: {index+1}")
        # CON structured_output + model_validate_json -- DEMASIADO ESTRICTO
        # respuesta = LLM_inter.generate(modelo, prompt_final, opciones_LLM)
        # tripletas = LLM_inter.TripletasList.model_validate_json(respuesta)
        # output_df.loc[len(output_df)] = [csv, abs_id, tripletas]
        
        # if index%10 == 0:
        #     os.system("ollama stop phi3")
        #     LlamadaLLM.reset(modelo)
        #     time.sleep(3)
        #     print(f"Extraccion completa del abstract: {index}")
        
    return output_df



def extractor_tripletas(csvs, modelo, prompt, opciones_LLM, n_abs):

    """ 
    Bucle lectura + extraccion
    """
    output_df = pd.DataFrame(columns=["csv_source", "id", "entidades"])

    for csv in csvs:
        
        print("-"*60)
        print(f"COMIENZA la extraccion para el archivo: {csv}.csv")
        
        abstracts = lectura_abstracts(csv, n_abs)
        
        print(f"Abstracts del archivo: {csv}.csv LEIDOS")
        
        output_df = extraer_tripletas(csv, abstracts, modelo, prompt, opciones_LLM, output_df)

        print(f"FINALIZA la extraccion de tripletas para el archivo: {csv}.csv")
        
    return output_df