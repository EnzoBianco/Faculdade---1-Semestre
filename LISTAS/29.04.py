Minha_Lista = ["Ana", "Carlos", "Beatriz", "Eduardo", "Sérgio"]

# Exercício 1
# Acessar por índice, mostrando na tela o terceiro nome da lista:

print(Minha_Lista[2])
print("=" * 50)
# Exercício 2:
# Alteração de elemento, trocando o nome Carlos por Eulano Jr

Minha_Lista[1] = "Eulano Jr."
print("Lista Alterada/t", Minha_Lista)
print("=" * 50)

# Exercício 3:
# Acrescentar elemento (append), adicionando o nome Voslano ao final da lista

Minha_Lista.append ("Voslano")
print("Lista Alterada/t", Minha_Lista)
print("=" * 50)

# Exercício 4:
# Índice de elemento (index), descobrindo em que posição está o nome "Sérgio".
posição = Minha_Lista.index("Sérgio")
print(f"Sérgio está na posição: {posição}")
print("=" * 50)

# Exercício 5:
# Inserir elemento (insert). Insira "Sicrano 2" logo após "Beatriz".
i = Minha_Lista.index("Beatriz")
Minha_Lista.insert(i+1, "Sicrano 2")
print("Lista alterada\t", Minha_Lista)
print("=" * 50)

# Exercício 6:
# Remoção (del). Remova o segundo nome da lista.

del Minha_Lista[1]
print("Lista Alterada\t", Minha_Lista)
print("=" * 50)

# Exercício 7:
# Ordenar (sorted). Mostre os nomes em ordem decrescente.

print(sorted(Minha_Lista, reverse = True))
print("=" * 50)

# Exercício 8:
# Tamanho da lista (len). Mostre quantos nomes existem na lista.

print("Tamanho da Lista = ", len(Minha_Lista))
print("=" * 50)

# Exercício 9:
# Contar ocorrências (count). Conte quantas vezes o nome "Ana" aparece na lista.

print("Contagem de 'Ana' =  ", Minha_Lista.count("Ana"))
print("=" * 50)

# Exercício 10:
# Enumerar elementos (enumerate). Mostre todos os nomes da lista com sua respectiva posição.

for i, val in enumerate(Minha_Lista):
    print(f"Índice/Posição = {i} \t\t valor = {val}")
print("=" * 50)

# Exercício 11
# Acesso por índice e startswith. Verifique se o nome na quarta posição da lista começa com a letra 'E'. Mostre 'Sim' ou 'Não'.

if Minha_Lista[3].startswith("E"):
    print("Sim")
else:
    print("Não")
print("=" * 50)

# Exercício 12:
# Alteração de elemento. Se o nome da posição 0 for "Ana", substitua por "Anastácia".

if Minha_Lista[0] == "Ana":
    Minha_Lista[0] = "Anastácia"
    print("Lista alterada \t", Minha_Lista)
else:
    print(Minha_Lista)
print("=" * 50)

# Exercício 13:
# Acrescentar elemento (append). Peça ao usuário um nome. Se ele ainda não estiver na lista, adicione-o.

nome = input("Insira um nome qualquer: ")
if nome not in Minha_Lista:
    Minha_Lista.append(nome)
    print("Lista atualizada \t", Minha_Lista)
else:
    print(Minha_Lista)