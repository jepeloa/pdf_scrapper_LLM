import json_LLM_key_analizer

keys_ = ["What is the language of the text?", "Create a brief resume of the text","Create a list of 5 tags that are representative of the text"]
pdf_file='./pdfs/1.pdf'
start_page=1
end_page=2

output=json_LLM_key_analizer.json_LLM_key_analizer(keys_, pdf_file, start_page, end_page)
print("structured_json_output: ")
print(output)

for question, answers in output.items():
    print(f'Pregunta: {question}')
    print(f'Respuesta R_1: {answers["R"]}')
    print()
