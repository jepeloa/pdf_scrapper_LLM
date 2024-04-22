import pdf_reader
import LLM_key_analizer


def json_LLM_key_analizer(keys_, pdf_file, start_page, end_page):
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



# Ejemplo de uso



