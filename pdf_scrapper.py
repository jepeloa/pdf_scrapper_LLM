import requests
import json
import re
import PyPDF2 
import sqlite3



#ver la libreria unestructured, creo que es mejor dado lo sensible de los datos







def analizing_keys(text, question):
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
        return response_json['choices'][0]['message']['content']
    else:
        return "fail, wrong response"

def key_responses(pdf_text1, page, keys):
    response_json_ = {}

    for key in keys:
        #para agregar mas keys a la salida se puede hacer aca, si se analiza usando paginas o rangos tal ves estaria bueno tenerlo, despues cuando hacemos RAG de esto va a servir
        print(key)
        r_1_ = analizing_keys(pdf_text1, key)

        response_json_[key] = {
            "R_1": r_1_,
            "raw_text_1": pdf_text1,
            "page": page
        }

    return response_json_
#ver aca esto, se puede intentar utilizar lo que venian usando con chromadb o analizar pagina a pagina

initial_page=0

start_page=str(0)
end_page=str(3)

pdf_a, pdf_b=fetch_pdf_content(start_page,end_page)
print("text document A between pages: " + start_page + " y " + end_page)
print(pdf_a)
print("text document B between pages: " + start_page + " y " + end_page)
print(pdf_b)


# Ejemplo de uso
keys_ = ["what is the Sum insured?", "what is the name of the person insured"]
text1 = pdf_a
text2 = pdf_b

resultados = key_responses(text1, text2, keys_)
print("structured_json_output: ")
print(resultados)

for question, answers in resultados.items():
    print(f'Pregunta: {question}')
    print(f'Respuesta R_1: {answers["R_1"]}')
    print(f'Respuesta R_2: {answers["R_2"]}')
    print()
