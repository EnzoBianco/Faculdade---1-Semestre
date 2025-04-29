import os
import locale
import math
import time 
locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')

titulo = '''
==============
Raíz Quadrada
==============
'''

while True:

    print(titulo)
    print("[1] - Fazer o cálculo da raíz quadrada de um número")
    print("[2] - Sair do programa")

    try:

        opção = int(input("Selecione uma opção(1 ou 2): "))

        if opção == 1:
            while True:
                os.system("cls")
                print(titulo)
                try:
                    numero = locale.atof(input("Digite um número qualquer para ver sua raíz quadrada: "))
                    if numero == "":
                        print("O campo não pode ficar vazio! Digite um número!")
                        time.sleep(3)
                        continue
                except ValueError:
                    print("ERRO: Digite apenas números!")
                    time.sleep(3)
                    continue
                raiz_quadrada = math.sqrt(numero)
                if numero < 0:
                    print("ERRO: Não existe raíz quadrada para um número negativo!")
                    print("Por favor, digite um número positivo!")
                    time.sleep(3)
                    continue    
                elif numero == 0:
                    print("A raíz de zero é zero!")
                else:
                    print(f"A raíz quadrada de {numero} é {raiz_quadrada:.2f}")
                    continuar = input("Deseja encontrar a raíz quadrada de outro número qualquer? (s/n): ").strip().lower()
                    if continuar == "s":
                        continue
                    elif continuar == "n":
                        print("Voltando ao início do programa...")
                        time.sleep(3)
                        break
                    else:
                        print("Opção Inválida!")
                        print("Voltando ao início do programa...")
                        time.sleep(3)
                        break
        elif opção == 2:
            print("Saindo do Programa...")
            time.sleep(3)
            break
        else:
            print("Opção inválida!")
            print("Digite uma das opiniões disponíneis(1 ou 2)")
            time.sleep(3)
            break
    except ValueError:
        print("Opção inválida!")
        print("Digite uma das opiniões disponíneais(1 ou 2)")
        time.sleep(3)
        continue
