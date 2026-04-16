XMLS = ["res1_clean"]
MODELO = "phi3"
PROMPT = """
    Tienes que extraer entidades del texto que te voy a pasar a continuación siguiendo estas reglas:
    1. Extrae solo las entidades relevantes con el campo de la IA.
    2. Cada entidad no puede contener más de 5 palabras individuales.
    3. Devuelve exclusivamente estas entidades, sin explicaciones adicionales, solo una lista de palabras.
    4. No pongas saltos de linea (/n). Las Entidades deben estar separadas por ;
    5. El output tiene que seguir EXACTAMENTE este formato: ENTIDAD1;ENTIDAD2;ENTIDAD3;ENTIDAD4...


    Texto a analizar: 

"""