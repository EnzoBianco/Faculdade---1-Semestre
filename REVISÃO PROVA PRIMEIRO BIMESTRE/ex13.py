import os
import time
import math
import locale
from colorama import Fore, Style, init
locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')
init(autoreset=True)

titulo = '''
=====================================
Arredondamento de número quebrado
=====================================
'''                 

while True:
    print(f"{Fore.BLUE}{titulo}{Style.RESET_ALL}")
    print(f"{Fore.GREEN}[1]{Style.RESET_ALL} - Calcular o arredondamento de um número quebrado")
    print(f"{Fore.RED}[2]{Style.RESET_ALL} - Sair do programa")

    try:
        opção = int(input("Selecione a opção desejada(1 ou 2): "))

        if opção == 1:
            while True:
                os.system("cls")
                print(titulo)
                try:
                    numero = locale.atof(input("Digite um número quebrado qualquer: "))
                    if numero == "":
                        print("O campo não pode ficar vazio.")
                        print("Por favor, digite um número!")
                        time.sleep(3)
                        continue
                    if numero.is_integer():
                        print("ERRO: O número digitado não se trata de um número quebrado, mas de um número inteiro.")
                        print("Por favor, digite um número quebrado.")
                        time.sleep(3)
                        continue
                except ValueError:
                    print("ERRO: Digite apenas números!")
                    time.sleep(2)
                    continue
                parte_decimal = numero - int(numero)
                parte_decimal = round(numero - math.floor(numero), 2)
                
                if 0.01 <= parte_decimal <= 0.49:
                    print(f"O número {numero} arredondado é igual a {math.floor(numero)}")
                    print("Voltando a tela inicial...")
                    time.sleep(5)
                    break
                elif 0.50 <= parte_decimal <= 0.99:
                    print(f"O número {numero} arredondado é igual a {math.ceil(numero)}")
                    print("Voltando a tela inicial...")
                    time.sleep(5)
                    break
                else:
                    print("ERRO: O número digitado não é um número quebrado.")
                    print("Por favor, digite um número quebrado.")
                    time.sleep(3)
                    continue
                
        elif opção == 2:
            print("Saindo do programa...")
            time.sleep(3)
            break
        else:
            print("Opção inválida! Selecione uma das opções disponíveis (1 ou 2)")
            print("Voltando...")
            time.sleep(3)
            continue
    except ValueError:
        print("Digite apenas números!")
        time.sleep(3)
        continue