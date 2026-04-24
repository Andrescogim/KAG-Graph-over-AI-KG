from  .ontologia_clean import CLASES, RELACIONES

CSVS_ABS = ["subset_1000_abstracts"]
CSVS_RELS_ENTIS= "subset_1000_rels_entis"
LLM_OPTIONS = {
    'temperature': 0,
    'num_ctx': 4096,
    'num_predict': 200,
}
MODELO = "phi3"
# MODELO = "gemma:2b"
# MODELO = "gemma:7b"
# PROMPT = f"""
#     You must extract entities from the text that I will provide below following these rules:

#     1. Extract only the relevant entities within the AI field.
#     2. Each entity must not contain more than 3 individual words.
#     3. Return exclusively these entities, without additional explanations, only a list of words.
#     4. Do not include any line breaks (/n). The entities must be separated by ;
#     5. The output must follow EXACTLY this format: ENTITY1;ENTITY2;ENTITY3;ENTITY4...
#     6. These entities must be able to fit into one of the 5 types listed below, which are accompanied by their explanation and some examples:
#     {CLASES}
# Text to analyze:

# """
PROMPT = f"""
    You must extract entities from the text that I will provide below following these rules:

    1. Extract only the relevant entities within the AI field.
    2. Each entity must not contain more than 3 individual words.
    3. Return exclusively these entities, without additional explanations, only a list of words.
    4. Do not include any line breaks (/n). The entities must be separated by ;
    5. The output must follow EXACTLY this format: ENTITY1;ENTITY2;ENTITY3;ENTITY4...

Text to analyze:

"""
# print(PROMPT)