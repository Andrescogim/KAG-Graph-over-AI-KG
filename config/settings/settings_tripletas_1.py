from  .ontologia_clean import CLASES, RELACIONES

COMENTARIOS = """
- Prompt simple
- Explicacion simple de que son las tripletas.
- Formato JSON CON format.
- Restricciones a campos vacios y nº de palabras
- Con 1 ejemplo
--------------------------------------------------------------------
"""
CSVS_ABS = ["subset_1000_abstracts"]
CSVS_RELS_ENTIS= "subset_1000_rels_entis"
N_ABS = 10  # Nº de abstracts a procesar - para pruebas 
LLM_OPTIONS = {
    'temperature': 0,
    'num_ctx': 1024,
    'num_predict': 600,
    'format': 1,
}
MODELO = "phi3"
# MODELO = "gemma:2b"
# MODELO = "gemma:7b"
PROMPT = f"""
[INSTRUCTIONS]
    Extract triplets of words (subject,relation,object) from the text following these rules:

    - Extract only the relevant triplets within the AI field.
    - Subject and object are entities (of AI- Relations are verbs connecting these entities.
    - Return exclusively a list of triplets, without additional explanations.
    - The output must be exclusive a list of triplets in JSON format.
    - No component of the triplet can be empty. Each element must be concise, with a maximum of 5 words; if there are more, keep only the most relevant words.
[EXAMPLE]

{{"tripletas": [{{"subject": "neural network", "relation": "uses method", "object": "object recognition"}}]}}


[Text to analyze]:

"""
# PROMPT = f"""
# [INSTRUCTIONS]
#     Extract triplets of words (subject,relation,object) from the text following these rules:

#     1. Extract only the relevant triplets within the AI field.
#     2. Each component of the triplet must not contain more than 3 individual words.
#     3. Return exclusively a list of triplets, without additional explanations.
#     4. Do not include any line breaks (/n).
#     5. The output must be exclusive in JSON format.
        
# [Text to analyze]:

# """
# PROMPT = f"""
#     You must extract triplets of words in a subject-predicate format (subject,predicate,object) from the text following these rules:

#     1. Extract only the relevant triplets within the AI field.
#     2. Each componentof the triplet must contain 3 individual words maximum.
#     3. Return exclusively a list of triplets, without additional explanations.
#     4. Do not include any line breaks (/n). The triplets must be inside parenthesis and separated by ;
#     5. The output must follow EXACTLY this format: (subject_1;predicate_1;object_1;);(subject_2;predicate_2;object_2;)...
#     6. These entities must be able to fit into one of the 5 types listed below, which are accompanied by their explanation and some examples:
#     {CLASES}
# Text to analyze:

# """
