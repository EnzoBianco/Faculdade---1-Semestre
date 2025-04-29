import os
from colorama import Fore, Style, init
import time
init(autoreset=True)

titulo = '''
===========================
VERIFICAR MÚLTIPLO DE 5
===========================
'''

while True:
    os.system("cls")
    print(f"{Fore.CYAN}{titulo}{Style.RESET_ALL}")
    print(f"{Fore.GREEN}[1] - Verificar número{Style.RESET_ALL}")
    print(f"{Fore.RED}[2] - Sair do programa{Style.RESET_ALL}")

    try:
        opcao = int(input("Selecione a opção (1 ou 2): "))
        if opcao == 1:
            while True:
                os.system("cls")
                print(f"{Fore.CYAN}{titulo}{Style.RESET_ALL}")
                try:
                    numero = int(input("Digite um número inteiro positivo: "))
                    if numero < 0:
                        print(f"{Fore.RED}Número negativo! Digite apenas valores positivos.{Style.RESET_ALL}")
                        time.sleep(2)
                        continue
                    if numero % 5 == 0:
                        print(f"{Fore.GREEN}O número {numero} é múltiplo de 5.{Style.RESET_ALL}")
                    else:
                        print(f"{Fore.YELLOW}O número {numero} NÃO é múltiplo de 5.{Style.RESET_ALL}")
                except ValueError:
                    print(f"{Fore.RED}Erro: Digite apenas números inteiros!{Style.RESET_ALL}")
                    time.sleep(2)
                    continue

                continuar = input("Deseja fazer outro cálculo? (s/n): ").lower()
                if continuar == 'n':
                    break
                elif continuar == 's':
                    continue
                else:
                    print(f"{Fore.RED}Opção Inválida!{Style.RESET_ALL}")
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
