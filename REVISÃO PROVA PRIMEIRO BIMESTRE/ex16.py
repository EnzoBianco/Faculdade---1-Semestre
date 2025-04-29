import os
import time

titulo = '''
==========================
Cálculo de Média Semestral
==========================
'''

while True:
    print(titulo)
    print("[1] - Calcular a média semestral")
    print("[2] - Sair do programa")

    try:
        opção = int(input("Selecione uma das opções acima(1 ou 2): "))
        if opção == 1:
            while True:
                os.system("cls")
                print(titulo)
                try:
                    M1 = float(input("Digite a nota da primeira média: "))
                    M2 = float(input("Digite a nota da segunda média: "))
                    if M1 > 10:
                        print("M1 não pode ser maior do que 10.")
                        print("Por favor, digite uma nota válida!")
                        time.sleep(5)
                        continue
                    elif M1 < 0:
                        print("M1 não pode ser menor do que 0.")
                        print("Por favor, digite uma nota válida!")
                        time.sleep(5)
                        continue
                    elif M2 > 10:
                        print("M2 não pode ser maior do que 10.")
                        print("Por favor, digite uma nota válida!")
                        time.sleep(5)
                        continue
                    elif M2 < 0:
                        print("M2 não pode ser menor do que 0.")
                        print("Por favor, digite uma nota válida!")
                        time.sleep(5)
                        continue
                    elif M1 == "" or M2 == "":
                        print("O campo não pode ficar vazio!")
                        print("Por favor, digite uma nota válida!")
                        time.sleep(5)
                        continue
                except ValueError:
                    print("Ocorreu um ERRO!")
                    time.sleep(3)
                    continue
                media_semestral = (M1 + (M2 * 2)) / 3
                if media_semestral < 3:
                    print(f"Sua média semestral é {media_semestral:.2f}. Você está Reprovado!")
                    time.sleep(4)
                    break
                elif media_semestral > 5:
                    print(f"Sua média semestral é {media_semestral:.2f}. Você está Aprovado!")
                    time.sleep(4)
                    break
                else:
                    print(f"Sua média semestral é {media_semestral:.2f}. Você está de Recuperação!")
                    time.sleep(4)
                    break
        elif opção == 2:
            print("Saindo do programa...")
            time.sleep(3)
            break
        else:
            print("Opção inválida!")
            print("Selecione uma das opções disponíveis(1 ou 2)")
            time.sleep(3)
            continue
    except ValueError:
        print("Opção inválida!")
        print("Selecione uma das opções disponíveis(1 ou 2)")
        time.sleep(3)
        continue