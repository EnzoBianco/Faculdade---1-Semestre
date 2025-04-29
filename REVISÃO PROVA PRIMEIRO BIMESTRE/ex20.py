import os
import time

titulo = '''
========================================
Conversor de nota numérica para conceito
========================================
'''
while True:
    
    print(titulo)
    print("[1] - Converter")
    print("[2] - Sair do programa")

    try:
        opção = int(input("Selecione uma das opções acima (1 ou 2): "))

        if opção == 1:
            while True:
                os.system("cls")
                print(titulo)

                try:
                    nota = float(input("Digite a nota (De 0 a 10): "))
                    if not nota:
                        print("O campo não pode ficar vazio!")
                        print("Voltando...")
                        time.sleep(5)
                        continue
                    if nota < 0 or nota > 10:
                        print("Nota inválida!")
                        print("Voltando...")
                        time.sleep(5)
                        continue
                    elif nota == 9 or nota == 10:
                        conceito = "A"
                    elif nota == 8 or nota == 7:
                        conceito = "B"
                    elif nota == 6 or nota == 5:
                        conceito = "C"
                    else:
                        conceito = "D"
                    print(f"Nota: {nota} - Conceito: {conceito}")
                except ValueError:
                    print("Erro: Por favor, digite apenas números!")
                    print("Voltando...")
                    time.sleep(5)
                    continue
        if opção == 2:
            print("Saindo do programa...")
            time.sleep(2)
            break
        else:
            print("Opção inválida!")
            print("Voltando...")
            time.sleep(5)
            continue
    except ValueError:
        print("Erro: Por favor, digite apenas números!")
        print("Voltando...")
        time.sleep(5)
        continue