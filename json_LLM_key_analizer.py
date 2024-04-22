import pdf_reader
import LLM_key_analizer

def json_LLM_key_analizer(pdf_text, keys_, pdf_file, start_page, end_page):
    """
    Función que analiza las respuestas de las preguntas de las llaves en un documento PDF.

    Args:
        pdf_text (str): Texto del documento PDF.
        keys_ (list): Lista de las llaves a analizar.
        pdf_file (str): Ruta del archivo PDF.
        start_page (str): Página de inicio del documento PDF.
        end_page (str): Página de fin del documento PDF.

    Returns:
        dict: Diccionario con las respuestas de las llaves.
    """
    pdf_text=pdf_reader.fetch_pdf_content(pdf_file, start_page,end_page) #si escaneas de a una es i,i+1 start y end respectivamente
    results = LLM_key_analizer.key_responses(pdf_text, keys_, pdf_file, start_page, end_page)
    return results

pdf_file=""
initial_page=0

start_page=str(0)
end_page=str(3)


print("text document A between pages: " + start_page + " y " + end_page)
print(pdf_text)
keys_ = ["what is the Sum insured?", "what is the name of the person insured"]


# Ejemplo de uso



resultados = LLM_key_analizer.key_responses(pdf_text, keys_,pdf_file, start_page, end_page)
print("structured_json_output: ")
print(resultados)

for question, answers in resultados.items():
    print(f'Pregunta: {question}')
    print(f'Respuesta R_1: {answers["R_1"]}')
    print(f'Respuesta R_2: {answers["R_2"]}')
    print()
