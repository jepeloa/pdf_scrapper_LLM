import json_LLM_key_analizer

from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

app = FastAPI()

class ItemList(BaseModel):
    items: List[str]

def texto(items: List[str]):
    # Aquí va la lógica de la función 'texto'
    # Por ejemplo, podríamos simplemente imprimir los elementos recibidos
    #for item in items:
    #    print(item)
    print(items)
    return {"message": "Función texto ejecutada"}

@app.post("/procesar-lista/")
def procesar_lista(item_list: ItemList):
    #keys_ = ["What is the language of the text?", "Create a brief resume of the text","Create a list of 5 tags that are representative of the text"]
    pdf_file='./pdfs/1.pdf'
    keys_= item_list.items
    start_page=1
    end_page=2
    output=json_LLM_key_analizer.json_LLM_key_analizer(keys_, pdf_file, start_page, end_page)
    for question, answers in output.items():
        print(f'Pregunta: {question}')
        print(f'Respuesta R_1: {answers["R"]}')
        print()
    return output



