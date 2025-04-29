import os
from colorama import Fore, Style, init
import time
init(autoreset=True)

titulo = '''
==============================
VERIFICAR DIREITO AO VOTO
==============================
'''

while True:
    os.system("cls")
    print(f"{Fore.CYAN}{titulo}{Style.RESET_ALL}")
    print(f"{Fore.GREEN}[1] - Verificar elegibilidade{Style.RESET_ALL}")
    print(f"{Fore.RED}[2] - Sair do programa{Style.RESET_ALL}")

    try:
        opcao = int(input("Escolha uma opção (1 ou 2): "))
        if opcao == 1:
            while True:
                os.system("cls")
                print(f"{Fore.CYAN}{titulo}{Style.RESET_ALL}")
                try:
                    idade = int(input("Digite sua idade: "))
                    if idade < 0 or idade > 120:
                        print(f"{Fore.RED}Idade inválida! Digite entre 0 e 120 anos.{Style.RESET_ALL}")
                        time.sleep(2)
                        continue

                    if idade >= 18:
                        print(f"{Fore.GREEN}Você está apto(a) a votar.{Style.RESET_ALL}")
                    else:
                        print(f"{Fore.YELLOW}Você ainda NÃO pode votar.{Style.RESET_ALL}")
                except ValueError:
                    print(f"{Fore.RED}Erro: Digite apenas números inteiros!{Style.RESET_ALL}")
                    time.sleep(2)
                    continue

                continuar = input("Deseja verificar outra idade? (s/n): ").lower()
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
