import PyPDF2 
import re
def fetch_pdf_content(pdf_file, start: int = 0, end: int = 0) -> str:

    #hardcoding aca, ver despues de definir bien esto
   
    with open(pdf_file, 'rb') as pdf_a:
       
        reader_1 = PyPDF2.PdfReader(pdf_a)
        start = max(0, start)
        end = min(len(reader_1.pages) - 1, end)
        text_a = '\n'.join(page.extract_text() for page in reader_1.pages[start:end+1] if page.extract_text())
        processed_text = re.sub(r'\s+', ' ', text_a).strip()
    return processed_text