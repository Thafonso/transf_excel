import os 


os.environ["LLAMA_CLOUD_API_KEY"] = "llx-ycypqpI79txBluHprQBGCVEZckVblUOqHIikkZgXqx1An4n1"

from llama_parse import LlamaParse

documentos = LlamaParse(result_type="markdown", # md
                         parsing_instruction="this file contains text and tables, i'd like to get only the tables from text").load_data("leitura_PDFs/desempenho.pdf")

print(len(documentos))

for i, pagina in enumerate(documentos): # i = Indice - numerate = para numerar da pág - Lembrando que em Python começa no indice 0
    # Criando um arquivo de texto 
    with open(f"leitura_PDFs/Docs/pagina{i+1}.md", "w", encoding="utf-8") as arquivo:
        arquivo.write(pagina.text)
        


