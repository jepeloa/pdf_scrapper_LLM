import requests
import json
import re
def analizing_keys(text, question, pdf_name):
    api_key = 'sk-proj-C08uRJpe3ww9h06tC4ntT3BlbkFJ3A0Nuoep2iQSWYBLe0pS'
    headers = {
        'Authorization': f'Bearer {api_key}',
        'Content-Type': 'application/json',
    }
    #aca jugar con los modelos 
    data = {
        'model': 'gpt-4-turbo',
        'messages': [
            {"role": "system", "content": "You are a helpful IA assistant. You are an expert extracting information from documents. You will receive a text and a question about the text to answer. Always you must be respond using the provided text as source data"},
            {"role": "user", "content": f"answer the question: {question} using this text {text}"}
        ]
    }

    response = requests.post('https://api.openai.com/v1/chat/completions', headers=headers, json=data)
    
    if response.status_code == 200:
        response_json = response.json()
        # Asumimos que la última respuesta del modelo es la respuesta a la pregunta
        return response_json['choices'][0]['message']['content'], pdf_name
    else:
        return "fail, wrong response"

def key_responses(pdf_text1, keys, pdf_name, start_page, end_page):
    response_json_ = {}

    for key in keys:
        #para agregar mas keys a la salida se puede hacer aca, si se analiza usando paginas o rangos tal ves estaria bueno tenerlo, despues cuando hacemos RAG de esto va a servir
        print(key)
        r_1_ = analizing_keys(pdf_text1, key)

        response_json_[key] = {
            "R_1": r_1_,
            "raw_text_1": pdf_text1,
            "start_page": start_page,
            "end_page": end_page,
            "pdf_name":pdf_name
        }

    return response_json_