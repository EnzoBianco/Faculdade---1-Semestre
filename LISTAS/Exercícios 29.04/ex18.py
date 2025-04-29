# Exercício 18: 
# Enumerar elementos (enumerate). Mostre a posição dos nomes que possuem mais de 6 letras.

Minha_Lista = ["Ana", "Carlos", "Beatriz", "Eduardo", "Sérgio"]
for indice, nome in enumerate(Minha_Lista):
    if len(nome) > 6:
        print(f"O nome '{nome}' na posição {indice} possui mais de 6 letras!")