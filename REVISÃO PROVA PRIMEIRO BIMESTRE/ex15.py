import os
from colorama import Fore, Style, init
import time
init(autoreset=True)

titulo = '''
=============================================
Converter temperatura Fahrenheit para Celsius
=============================================
'''

while True:

    print(f"{Fore.BLUE}{titulo}{Style.RESET_ALL}")
    print(f"{Fore.GREEN}[1]{Style.RESET_ALL} - Converter temperatura Fahrenheit para Celsius")
    print(f"{Fore.RED}[2]{Style.RESET_ALL} - Sair do programa")

    try:
        opção = int(input(f"Selecione uma das opções acima ({Fore.GREEN}[1]{Style.RESET_ALL} ou {Fore.RED}[2]{Style.RESET_ALL}): "))
        
        if opção == 1:
            while True:
                os.system("cls")
                print(titulo)
                try:
                    temperatura_em_Fahrenheit = (input("Digite a temperatura na escala Fahrenheit: "))
                    if not temperatura_em_Fahrenheit:
                        print("O campo não pode ficar vazio!")
                        print("Voltando...")
                        time.sleep(5)
                        continue
                    temperatura_em_Fahrenheit = float(temperatura_em_Fahrenheit)
                except ValueError:
                    print("ERRO: Digite apenas números!")
                    print("Voltando...")
                    time.sleep(5)
                    continue
                temperatura_em_Celsius = (temperatura_em_Fahrenheit - 32) * 5 / 9
                print(f"A tempertura de {temperatura_em_Fahrenheit}°F é igual a {temperatura_em_Celsius:.1f}°C.")
                while True:
                    continuar = input("Deseja converter outra temperatura? (s/n): ").strip().lower()
                    if continuar == "s":
                        print("Ok, vamos converter outra temperatura...")
                        time.sleep(4)
                        break
                    elif continuar == "n":
                        print("Voltando ao menu principal...")
                        time.sleep(4)
                        break
                    else:
                        print("Opção inválida!")
                        print("Por favor, digite 's' para sim, e converter outra temperatura, ou 'n' para não, e voltar ao menu principal.")
                        time.sleep(2)
                if continuar == "n":
                    break
        elif opção == 2:
            print("Saindo do programa...")
            time.sleep(3)
            break
        else:
            print("A opção digitada é inválida!")
            print(f"Por favor, selecione uma das opções disponíveis ({Fore.GREEN}[1]{Style.RESET_ALL} ou {Fore.RED}[2]{Style.RESET_ALL}).")
            time.sleep(5)
            continue
    except ValueError:
        print("Opção inválida!")
        print("Por favor, selecione uma das opções disponíveis (1 ou 2).")
        time.sleep(5)
        continue