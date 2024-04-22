import requests
import os
from dotenv import load_dotenv
import json
import re
def analizing_keys(text, question, pdf_name):
    API_KEY = os.getenv('API_KEY')
    API_URL = os.getenv('API_URL')
    MODEL = os.getenv('MODEL')
    
    
    headers = {
        'Authorization': f'Bearer {API_KEY}',
        'Content-Type': 'application/json',
    }
    #aca jugar con los modelos 
    data = {
        'model': MODEL,
        'messages': [
            {"role": "system", "content": "You are a helpful IA assistant. You are an expert extracting information from documents. You will receive a text and a question about the text to answer. Always you must be respond using the provided text as source data"},
            {"role": "user", "content": f"answer the question: {question} using this text {text}"}
        ]
    }

    response = requests.post(API_URL, headers=headers, json=data)
    
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
        r_1_ = analizing_keys(pdf_text1, key,pdf_name)

        response_json_[key] = {
            "R": r_1_,
            "start_page": start_page,
            "end_page": end_page,
            "pdf_name":pdf_name,
            "raw_text_1": pdf_text1
        }

    return response_json_