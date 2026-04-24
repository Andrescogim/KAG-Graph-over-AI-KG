import pandas as pd
from src.metricas.metricas import precision_recall_f1

class ComprobarOutput:
    PATH = "C:/Users/andre/OneDrive/Escritorio/TFM/KAG/AI-KG/Project/KAG-Graph-over-AI-KG/data/processed/csv/"

    def entidades_validas(respuesta):
        
        """Comprueba si el formato de entidades es valido (por encima)"""
        
        if "\n" in respuesta:
            return False
        if ":" in respuesta:
            return False
        if ";" not in respuesta:
            return False
        if len(respuesta) > 1000:
            return False

        return True

    def comprobar_entidades(out_df):
        
        """Comprueba si el formato de entidades es valido (por encima)"""
        
        df_metric = pd.DataFrame()
        df_metric['id'] = out_df['id']
        df_metric['formato_valido'] = out_df["entidades"].apply(ComprobarOutput.entidades_validas)
            

        return df_metric


    # def metricas_generales(n_abs, n_validas, ):
    def metricas_generales(df_metricas):
        
        """Calculo de metricas"""
        
        # Respuestas con formato valido
        ratio_validas = df_metricas["formato_valido"].sum() / df_metricas["formato_valido"].count()

        return ratio_validas


    def metricas_entidades(resultados, entis, df_metricas):
        
        """Calculo de metricas de entidades"""
    
        resultados['entidades'] = resultados['entidades'].astype(str).str.split(';')
        resultados['entidades'] = resultados['entidades'].apply(lambda x: [s.lower() for s in x])
        resultados['entidades'] = resultados['entidades'].apply(lambda s: {elem.strip().replace(' ', '_') for elem in s})
        # resultados['entidades'] = resultados['entidades'].apply(set)
        
        
        entis['entidades_lst'] = entis['entidades'].str.replace("(", "").str.replace(")", "").str.replace("'", "").str.split(',')
        entis['entidades_lst'] = entis['entidades_lst'].apply(lambda x: [s.strip() for s in x])
        # entis = entis.groupby("id", as_index=False)['entidades_lst'].agg(lambda x: set(sum(x, [])))
        entis = entis.groupby("id", as_index=False)['entidades_lst'].agg(lambda x: sum(x, []))

        entidades_validas = df_metricas[df_metricas["formato_valido"] == True]["id"]
        resultados_validos = resultados[resultados["id"].isin(entidades_validas)]
        
        # for i, row in resultados.iterrows():
        # Respuestas con formato valido
        for i, row in resultados_validos.iterrows():
            id = row["id"]
            pred = row["entidades"]
            true = entis.loc[entis["id"] == id, 'entidades_lst'].values[0]
            precision, recall, f1, comunes, solo_pred, solo_true = precision_recall_f1(pred, true)
            metricas = {
                "precision": precision,
                "recall": recall,
                "f1": f1,
                "comunes": str(comunes),
                "solo_pred": str(solo_pred),
                "solo_true": str(solo_true)
            }
            for col, val in metricas.items():
                df_metricas.loc[df_metricas["id"] == id, col] = val

        return df_metricas