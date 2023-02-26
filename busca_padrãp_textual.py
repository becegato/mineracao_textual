import re

def nomes():
    #Exemplo de texto a ser minerado.
    simple_string = """Amy tem 5 anos, e sua irmã Mary tem 2 anos. 
    Ruth e Peter, seus pais, têm 3 filhos."""

    # Defina o padrão de expressão regular para encontrar os nomes
    padrao = r'\b[A-Z][a-z]+\b'

    # Encontre todas as correspondências usando a função findall()
    lista_nomes = re.findall(padrao, simple_string)

    # Retorne a lista de nomes
    return lista_nomes
