Minha_Lista = ["Ana", "Carlos", "Beatriz", "Eduardo", "Sérgio"]

# Exercício 13:
# Acrescentar elemento (append). Peça ao usuário um nome. Se ele ainda não estiver na lista, adicione-o.

nome = input("Insira um nome qualquer: ")
if nome not in Minha_Lista:
    Minha_Lista.append(nome)
    print("Lista atualizada \t", Minha_Lista)
else:
    print(Minha_Lista)