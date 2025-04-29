import os
from colorama import Fore, Style, init
import time
init(autoreset=True)

titulo = '''
=====================================
Cálculo de desconto a partir da idade
=====================================
'''

while True:
    os.system("cls")
    print(f"{Fore.CYAN}{titulo}{Style.RESET_ALL}")
    print(f"{Fore.GREEN}[1] - Calcular Desconto{Style.RESET_ALL}")
    print(f"{Fore.RED}[2] - Sair do Programa{Style.RESET_ALL}")

    try:
        opção = int(input("Selecione a opção desejada(1 ou 2): "))
        if opção == 1:
            while True:
                os.system("cls")
                print(f"{Fore.CYAN}{titulo}{Style.RESET_ALL}")
                idade = int(input("Digite sua idade: "))

                try:
                    if idade < 0 or idade > 120:
                        print(f"{Fore.RED}Idade Inválida!{Style.RESET_ALL}")
                        time.sleep(2)
                        continue
                except ValueError:
                    print(f"{Fore.RED}Por favor, digite apenas números!{Style.RESET_ALL}")
                    time.sleep(2)
                    continue
                if idade <= 16 or idade >= 60:
                    print(f"{Fore.GREEN}Você possui direito a desconto em nossa loja.{Style.RESET_ALL}")
                else:
                    print(f"{Fore.BLUE}Infelizmente você não possui direito a desconto em nossa loja.{Style.RESET_ALL}")
                continuar = input(f"{Fore.GREEN}Digite 's' para usar o programa novamente ou 'n' para sair:{Style.RESET_ALL} ")
                if continuar == "s":
                    continue
                if continuar == "n":
                    print("Saindo do programa...")
                    time.sleep(2)
                    break
                if continuar != "s" and continuar != "n":
                    print(f"{Fore.RED}Opção inválida!{Style.RESET_ALL}")
                    time.sleep(2)
                    break
                
        if opção == 2:
            try:
                print("Saindo do programa...")
                time.sleep(2)
                break
            except ValueError: 
                print("Ocorreu um erro inesperado!")
                continue
        if opção != 1 and opção != 2:
            print(f"{Fore.RED}Opção inválida!{Style.RESET_ALL}")
            time.sleep(2)
            continue
    except ValueError:
        print(f"{Fore.RED}Erro: Por favor, digite apenas números!{Style.RESET_ALL}")
        time.sleep(2)

