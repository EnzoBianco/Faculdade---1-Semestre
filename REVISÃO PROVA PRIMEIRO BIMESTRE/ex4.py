import os
from colorama import Fore, Style, init
import time
init(autoreset=True)


titulo = '''
====================
NUMEROS CONSECUTIVOS
====================
'''

while True:
    os.system("cls")
    print(f"{Fore.CYAN}{titulo}{Style.RESET_ALL}")
    print(f"{Fore.GREEN}[1] - Verificar números consecutivos{Style.RESET_ALL}")
    print(f"{Fore.RED}[2] - Sair do programa{Style.RESET_ALL}")

    try:
        opção = int(input("Selecione a opção desejada(1 ou 2): "))
        if opção == 1:
            while True:
                os.system("cls")
                print(f"{Fore.CYAN}{titulo}{Style.RESET_ALL}")
                primeiro_numero = int(input("Digite o primeiro número: "))
                segundo_numero = int(input("Digite o segundo número: "))
                terceiro_numero = int(input("Digite o terceiro número: "))
                
                try:
                    if primeiro_numero < 0 or segundo_numero < 0 or terceiro_numero < 0:
                        print(f"{Fore.RED}Número inválido!{Style.RESET_ALL}")
                        time.sleep(2)
                        continue
                except ValueError:
                    print(f"{Fore.RED}Por favor, digite apenas números!{Style.RESET_ALL}")
                    time.sleep(2)
                    continue
                if primeiro_numero == segundo_numero - 1 and segundo_numero == terceiro_numero - 1 or primeiro_numero == segundo_numero + 1 and segundo_numero == terceiro_numero + 1:
                    print(f"{Fore.GREEN}Os números digitados são consecutivos.{Style.RESET_ALL}")
                else:
                    print(f"{Fore.RED}Os números digitados não são consecutivos.{Style.RESET_ALL}")

                continuar = input("Digite 's' para continuar ou 'n' para sair do programa: ") 
                if continuar == "s":
                    continue
                elif continuar == "n":
                    print(f"{Fore.GREEN}Saindo do programa...{Style.RESET_ALL}")
                    time.sleep(2)
                    break
                else:
                    print(f"{Fore.RED}Opção inválida!{Style.RESET_ALL}")
                    time.sleep(2)
                    continue
        if opção == 2:
            try:
                print("Saindo do programa...")
                time.sleep(2)
                break
            except ValueError:
                print(f"{Fore.RED}Erro: Ocorreu um erro inesperado!{Style.RESET_ALL}")
                time.sleep(2)
                continue
        if opção != 1 or opção != 2:
            print(f"{Fore.RED}Opção inválida!{Style.RESET_ALL}")
            time.sleep(2)
            continue
    except ValueError:
        print(f"{Fore.RED}Erro: Por favor, digite apenas números!{Style.RESET_ALL}")
        time.sleep(2)
    