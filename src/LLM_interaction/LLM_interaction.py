import ollama

class LlamadaLLM:
    def __init__(self, modelo):
        pass

    def modelos_disponibles():
        """Muestra los modelos disponibles"""
        
        for model in ollama.list().models:
            print(f"Modelo: {model.model} ; N_Parametros = {model.details.parameter_size}")



    def chat(modelo, prompt):

        response = ollama.chat(
            model = modelo,
            messages = [{
                'role': 'user',
                'content': prompt,
                }],
            options = {
                'temperature': 0
            },
        )
        return response.message.content



    def generate(modelo, prompt):

        response = ollama.generate(
            model = modelo,
            prompt = prompt,
            options = {
                'temperature': 0
            },
        )
        return response.response