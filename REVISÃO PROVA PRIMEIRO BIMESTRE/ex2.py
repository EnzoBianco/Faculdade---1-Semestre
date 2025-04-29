import os
from colorama import Fore, Style, init
import time
init(autoreset=True)

título = '''
=============
Par ou Ímpar
=============
'''

while True:
    os.system("cls")
    print(f"{Fore.CYAN}{título}{Style.RESET_ALL}")
    print(f"{Fore.GREEN}[1] - Verificar se o número é par ou ímpar{Style.RESET_ALL}")
    print(f"{Fore.RED}[2] - Sair do programa{Style.RESET_ALL}")

    try:
        opção = int(input("Selecione a opção desejada(1 ou 2): "))
        if opção == 1:
            while True:
                os.system("cls")
                print(f"{Fore.CYAN}{título}{Style.RESET_ALL}")
                número_digitado = int(input("Digite um número qualquer: "))

                try: 
                    if número_digitado < 0:
                        print(f"{Fore.RED}Número inválido!{Style.RESET_ALL}")
                        time.sleep(2)
                        continue
                except ValueError:
                    print(f'{Fore.RED}Erro: Por favor, digite apenas números!{Style.RESET_ALL}')
                    time.sleep(2)
                    continue
                if número_digitado % 2 == 0:
                    print(f"{Fore.GREEN}O número {número_digitado} é par.{Style.RESET_ALL}")
                else:
                    print(f"{Fore.RED}O número {número_digitado} é ímpar.{Style.RESET_ALL}")
        if opção == 2:
            try:
                print(f"{Fore.GREEN}Saindo do programa...{Style.RESET_ALL}")
                time.sleep(2)
                continue
            except ValueError:
                print(f"{Fore.RED}Erro: Ocorreu um erro inesperado!{Style.RESET_ALL}")
                time.sleep(2)
                break
        if opção != 1 or opção != 2:
            print(f"{Fore.RED}Opção inválida!{Style.RESET_ALL}")
            time.sleep(2)
            continue
    except ValueError:
        print(f"{Fore.RED}Erro: Por favor, digite apenas números!{Style.RESET_ALL}")
        time.sleep(2)

