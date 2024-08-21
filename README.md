# Descrição:
Você deve escrever um programa em Python que analisa um texto fornecido e retorna as seguintes informações:
Contagem de Palavras: Quantas palavras únicas existem no texto.
Frequência de Palavras: A frequência de cada palavra no texto.
Palavra Mais Frequente: A palavra que aparece mais vezes no texto e o número de ocorrências.
Tamanho Médio das Palavras: O tamanho médio das palavras no texto.

# Requisitos:
O texto será uma string com múltiplas palavras, separadas por espaços, e pode conter pontuações (pontos, vírgulas, etc.).
O texto deve ser tratado de forma case-insensitive, ou seja, "Python" e "python" devem ser considerados a mesma palavra.
Pontuações devem ser removidas para a contagem de palavras.
O programa deve ser capaz de lidar com textos de tamanho variável, desde uma única palavra até parágrafos inteiros.

Exemplo de Input:
texto = "Python é incrível. Python é fácil de aprender, e Python é poderoso."

resultado = analisar_texto(texto)
print(resultado)

# Exemplo de Output:
{
    'contagem_palavras': 7,
    'frequencia_palavras': {
        'python': 3,
        'é': 3,
        'incrível': 1,
        'fácil': 1,
        'de': 1,
        'aprender': 1,
        'poderoso': 1
    },
    'palavra_mais_frequente': ('python', 3),
    'tamanho_medio_palavras': 6.14
}

# Instruções:
Implemente a função analisar_texto(texto: str) -> dict que realiza as análises descritas acima.
Inclua testes para verificar a corretude da sua implementação.
Considere edge cases, como textos vazios ou com apenas uma palavra.

# Critérios de Avaliação:
Corretude: O programa deve produzir a saída correta para uma variedade de inputs.
Código Limpo: O código deve ser bem organizado e seguir boas práticas de programação.
Eficiência: O programa deve ser eficiente em termos de tempo e espaço, especialmente para textos maiores.
