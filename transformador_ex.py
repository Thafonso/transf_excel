import re # Regex - lógica de análise de texto
import pandas as pd
from io import StringIO # Transforma o texto em arquivo
import os 

def extrair_tabelas_texto(texto):
    busca_regex = re.compile(r"((?:\|.+\|(?:\n|\r))+)", re.MULTILINE) # Esse padrao vai ser aplicado em multiplas linhas
    tabelas = busca_regex.findall(texto)
    return tabelas


def transformacao_markdown_excel(texto, num_pagina): 
    # Identificação das tabelas que estão no texto
    list_texto_tabelas = extrair_tabelas_texto(texto)
    if len(list_texto_tabelas) > 0:
        # ler e salvar a tabela em excel
        for i, texto_tabelas in  enumerate(list_texto_tabelas):
            tabela = pd.read_csv(StringIO(texto_tabelas), sep="|", encoding="utf-8", engine="python")
            tabela = tabela.dropna(how="all", axis=1)
            tabela = tabela.dropna(how="all", axis=0)
            tabela.to_excel(f"leitura_PDFs/Tabelas/Pagina{num_pagina}Tabela{i+1}.xlsx", index=False)
            

# pegando lista de arquivos de uma pasta

past_pag = "leitura_PDFs/Docs"
lista_paginas = os.listdir(past_pag)

for i, pagina in enumerate(lista_paginas):
    with open(f"leitura_PDFs/Docs/{pagina}", "r", encoding="utf-8") as arquivo:
        texto = arquivo.read()

    num_pagina = i + 1
    transformacao_markdown_excel(texto, num_pagina)