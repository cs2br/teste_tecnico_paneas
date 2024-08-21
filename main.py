import string
from collections import Counter

def analisar_texto(texto: str) -> dict:
    # Converter o texto para minúsculas e remover pontuações
    texto = texto.lower()
    texto = texto.translate(str.maketrans('', '', string.punctuation))
    
    # Dividir o texto em palavras
    palavras = texto.split()
    
    # Verificar se o texto está vazio ou contém apenas espaços
    if not palavras:
        return {
            "contagem_palavras_unicas": 0,
            "frequencia_palavras": {},
            "palavra_mais_frequente": None,
            "max_ocorrencias_palavra_mais_frequente": 0,
            "tamanho_medio_palavras": 0
        }
    
    # Contagem de palavras únicas
    palavras_unicas = set(palavras)
    contagem_palavras_unicas = len(palavras_unicas)
    
    # Frequência de cada palavra
    frequencia_palavras = Counter(palavras)
    
    # Palavra mais frequente
    palavra_mais_frequente, max_ocorrencias = frequencia_palavras.most_common(1)[0] if frequencia_palavras else (None, 0)
    
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
    texto1 = "A MÁQUINA está pré-configurada, mas é necessário reconfigurar, porque a máquina precisa estar corretamente configurada; é essencial verificar a máquina antes de iniciar o processo."
    resultado1 = analisar_texto(texto1)
    print(resultado1)

    texto2 = "Python é incrível. python é fácil de aprender, e PYTHON é poderoso."
    resultado2 = analisar_texto(texto2)
    print(resultado2)

    texto3 = ""
    resultado3 = analisar_texto(texto3)
    print(resultado3)

    texto4 = "Palavra"
    resultado4 = analisar_texto(texto4)
    print(resultado4)

# Executa os testes
testes()