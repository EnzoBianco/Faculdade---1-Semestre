import os
from colorama import Fore, Style, init
import time
init(autoreset=True)

titulo = '''
===========================
Verificar números repetidos
===========================
'''

while True:
    os.system("cls")
    print(f"{Fore.CYAN}{titulo}{Style.RESET_ALL}")
    print(f"{Fore.GREEN}[1] - Verificar números repetidos{Style.RESET_ALL}")
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
                quarto_numero = int(input("Digite o quarto número: "))

                try:
                    if primeiro_numero < 0 or segundo_numero < 0 or terceiro_numero < 0 or quarto_numero < 0:
                        print(f"{Fore.RED}Número inválido!{Style.RESET_ALL}")
                        time.sleep(2)
                        continue
                except ValueError:
                    print(f"{Fore.RED}Por favor, digite apenas números!{Style.RESET_ALL}")
                    time.sleep(2)
                    continue
                if primeiro_numero == segundo_numero or primeiro_numero == terceiro_numero or primeiro_numero == quarto_numero or segundo_numero == terceiro_numero or segundo_numero == quarto_numero or terceiro_numero == quarto_numero:
                    print(f"{Fore.GREEN}Existem sim números repetidos na sequência digitada.{Style.RESET_ALL}")
                else:
                    print(f"{Fore.RED}Não existem números repetidos na sequência digitada.{Style.RESET_ALL}")

                input(f"{Fore.GREEN}Pressione ENTER para verificar novamente.{Style.RESET_ALL}")


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
        continue