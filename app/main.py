import json_LLM_key_analizer
import pdf_reader
from fastapi import FastAPI
from pydantic import BaseModel
from typing import List
import db
#example request:{
#  "items": [
#    "a brief resume of the text. Schema {'key':answer'}", "five different tags. Schema {'tag1':'tag','tag2','tag','tag3':'tag3','tag4':'tag','tag5':'tag5'}"
#  ]
#}
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

@app.post("/process_pdf/")
def procesar_lista(item_list: ItemList):
    #keys_ = ["What is the language of the text?", "Create a brief resume of the text","Create a list of 5 tags that are representative of the text"] 
    pdf_file='./pdfs/3.pdf'
    number_of_pages=pdf_reader.obtain_number_of_pages(pdf_file)
    #quiero obtener la longitud de paginas del pdf

    print(f"The total number of pages are: {number_of_pages}")
    print("Starting the analisys of the document")
    keys_= item_list.items
    for i in range(0,number_of_pages):
        print(f"analizing page {i}")
        start_page=i
        end_page=i+1
        output=json_LLM_key_analizer.json_LLM_key_analizer(keys_, pdf_file, start_page, end_page)
        db.connect_fetch(output,keys_)
    
    return output



