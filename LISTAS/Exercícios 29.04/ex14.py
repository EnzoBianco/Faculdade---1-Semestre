Minha_Lista = ["Ana", "Carlos", "Beatriz", "Eduardo", "Sérgio"]

# Exercício 14:
# Índice de elemento (index). Mostre a posição do nome “Beatriz”. Se não estiver presente, mostre uma mensagem adequada.
if "Beatriz" in Minha_Lista:
    posição = Minha_Lista.index("Beatriz")
    print(f"O nome 'Beatriz' estána posição {posição} da lista!")
else:
    print("O nome 'Beatriz' não está presente na lista!")