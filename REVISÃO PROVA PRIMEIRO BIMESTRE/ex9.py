import os
from colorama import Fore, Style, init
import time
init(autoreset=True)

titulo = '''
============================
VERIFICAR ORDEM CRESCENTE
============================
'''

while True:
    os.system("cls")
    print(f"{Fore.CYAN}{titulo}{Style.RESET_ALL}")
    print(f"{Fore.GREEN}[1] - Verificar sequência de números{Style.RESET_ALL}")
    print(f"{Fore.RED}[2] - Sair do programa{Style.RESET_ALL}")

    try:
        opcao = int(input("Escolha uma opção (1 ou 2): "))
        if opcao == 1:
            while True:
                os.system("cls")
                print(f"{Fore.CYAN}{titulo}{Style.RESET_ALL}")
                try:
                    n1 = int(input("Digite o primeiro número: "))
                    n2 = int(input("Digite o segundo número: "))
                    n3 = int(input("Digite o terceiro número: "))

                    if n1 < 0 or n2 < 0 or n3 < 0:
                        print(f"{Fore.RED}Números negativos não são permitidos.{Style.RESET_ALL}")
                        time.sleep(2)
                        continue

                    if n1 < n2 < n3:
                        print(f"{Fore.GREEN}Os números estão em ordem crescente.{Style.RESET_ALL}")
                    else:
                        print(f"{Fore.YELLOW}Os números NÃO estão em ordem crescente.{Style.RESET_ALL}")
                except ValueError:
                    print(f"{Fore.RED}Erro: Digite apenas números inteiros!{Style.RESET_ALL}")
                    time.sleep(2)
                    continue

                continuar = input("Deseja verificar outra sequência? (s/n): ").lower()
                if continuar == 'n':
                    break
                elif continuar == 's':
                    continue
                else:
                    print(f"{Fore.RED}Opção inválida!{Style.RESET_ALL}")
                    time.sleep(2)
                    break
        elif opcao == 2:
            print("Saindo do programa...")
            time.sleep(2)
            break
        else:
            print(f"{Fore.RED}Opção inválida!{Style.RESET_ALL}")
            time.sleep(2)
    except ValueError:
        print(f"{Fore.RED}Erro: Digite apenas números válidos!{Style.RESET_ALL}")
        time.sleep(2)
