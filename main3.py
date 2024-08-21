import string 
from collections import Counter

def analisar_texto(texto: str) -> dict:
    # Converter o texto para minúsculas e remover pontuações
    texto = texto.lower()
    texto = texto.translate(str.maketrans('', '', string.punctuation))
    
    # Dividir o texto em palavras
    palavras = texto.split()
    
    # Contagem de palavras únicas
    palavras_unicas = set(palavras)
    contagem_palavras_unicas = len(palavras_unicas)
    
    # Frequência de cada palavra
    frequencia_palavras = Counter(palavras)
    
    # Palavra mais frequente
    if frequencia_palavras:
        palavra_mais_frequente, max_ocorrencias = frequencia_palavras.most_common(1)[0]
    else:
        palavra_mais_frequente, max_ocorrencias = None, 0
    
    # Tamanho médio das palavras
    tamanho_medio_palavras = sum(len(palavra) for palavra in palavras) / len(palavras) if palavras else 0
    
    # Resultado final
    resultado = {
        "contagem_palavras_unicas": contagem_palavras_unicas,
        "frequencia_palavras": frequencia_palavras,
        "palavra_mais_frequente": palavra_mais_frequente,
        "max_ocorrencias_palavra_mais_frequente": max_ocorrencias,
        "tamanho_medio_palavras": tamanho_medio_palavras
    }
    
    return resultado

# Testes para verificar a implementação
def testes():
    texto = "Python é incrível. Python é fácil de aprender, e Python é poderoso"
    resultado = analisar_texto(texto)
    print(resultado)

# Executa os testes
testes()
