from  .ontologia_clean import CLASES, RELACIONES

XMLS = ["res1_clean"]
MODELO = "phi3"
PROMPT = f"""
    You must extract entities from the text that I will provide below following these rules:

    1. Extract only the relevant entities within the AI field.
    2. Each entity must not contain more than 3 individual words.
    3. Return exclusively these entities, without additional explanations, only a list of words.
    4. Do not include line breaks (/n). The entities must be separated by ;
    5. The output must follow EXACTLY this format: ENTITY1;ENTITY2;ENTITY3;ENTITY4...
    6. These entities must be able to fit into one of the 5 types listed below, which are accompanied by their explanation and some examples:
    {CLASES}
Text to analyze:

"""
# print(PROMPT)