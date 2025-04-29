import os
import time
from colorama import init, Style, Fore
import locale
locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')
init(autoreset=True)

titulo = '''
=============================
Simulador de Caixa Eletrônico
=============================
'''

while True:

    print(f"{Fore.BLUE}{titulo}{Style.RESET_ALL}")
    print(f"{Fore.YELLOW}Bem-vindo ao Simulador de Caixa Eletrônico!{Style.RESET_ALL}\n")
    print(f"{Fore.GREEN}[1]{Style.RESET_ALL} - Sacar Dinheiro")
    print(f"{Fore.CYAN}[2]{Style.RESET_ALL} - Depositar Dinheiro")
    print(f"{Fore.RED}[3]{Style.RESET_ALL} - Sair/Fechar o Programa")

    try:
        opção = int(input("Selecione uma das opções acima(1, 2 ou 3): "))

        if opção == 1:
            while True:
                os.system("cls")
                print(f"{Fore.BLUE}{titulo}{Style.RESET_ALL}")
                print(f"{Fore.YELLOW}Bem-vindo ao Simulador de Caixa Eletrônico!{Style.RESET_ALL}\n")
                try:
                    valor_a_sacar = locale.atof(input("Digite o valor que deseja sacar: "))
                    if valor_a_sacar <= 0:
                        print(f"O valor a se sacar deve ser {Style.BRIGHT}maior{Style.RESET_ALL} do que {Fore.YELLOW}R$0,00{Style.RESET_ALL}.")
                        print(f"Por favor, digite um {Style.BRIGHT}valor válido!{Style.RESET_ALL}")
                        print("Voltando(Aguarde 5 segundos)...")
                        time.sleep(5)
                        continue
                    elif valor_a_sacar < 5:
                        print(f"O valor a se sacar deve ser {Style.BRIGHT}maior{Style.RESET_ALL} do que {Fore.YELLOW}R$5,00{Style.RESET_ALL}.")
                        print(f"Por favor, digite um {Style.BRIGHT}valor válido!{Style.RESET_ALL}")
                        print("Voltando(Aguarde 5 segundos)...")
                        time.sleep(5)
                        continue
                    elif valor_a_sacar > 1000:
                        print(f"O valor a se sacar deve ser {Style.BRIGHT}menor{Style.RESET_ALL} do que {Fore.YELLOW}R$1000,00{Style.RESET_ALL}.")
                        print(f"Por favor, digite um {Style.BRIGHT}valor válido!{Style.RESET_ALL}")
                        print("Voltando(Aguarde 5 segundos)...")
                        time.sleep(5)
                        continue
                    elif valor_a_sacar % 5 != 0:
                        print(f"O valor a se sacar deve ser {Style.BRIGHT}múltiplo{Style.RESET_ALL} de {Fore.YELLOW}R$5,00{Style.RESET_ALL}.")
                        print(f"Por favor, digite um {Style.BRIGHT}valor válido!{Style.RESET_ALL}")
                        print("Voltando(Aguarde 5 segundos)...")
                        time.sleep(5)
                        continue
                    elif valor_a_sacar == "":
                        print(f"O campo {Style.BRIGHT}não pode ficar vazio!{Style.RESET_ALL}")
                        print(f"Por favor, digite um {Style.BRIGHT}valor válido!{Style.RESET_ALL}")
                        print("Voltando(Aguarde 5 segundos)...")
                        time.sleep(5)
                        continue
                except ValueError:
                    print(F"Ocorreu um {Fore.RED}ERRO!{Style.RESET_ALL}")
                    print("Voltando(Aguarde 3 segundos)...")
                    time.sleep(3)
                    continue
                print(f"Você sacou {Fore.RED}R${valor_a_sacar:.2f} com sucesso!{Style.RESET_ALL}")
                print("Voltando(Aguarde 5 segundos)...")
                time.sleep(7)
                break
        elif opção == 2:
            while True:
                os.system("cls")
                print(f"{Fore.BLUE}{titulo}{Style.RESET_ALL}")
                print(f"{Fore.YELLOW}Bem-vindo ao Simulador de Caixa Eletrônico!{Style.RESET_ALL}\n")
                try:
                    valor_a_depositar = locale.atof(input("Digite o valor que deseja depositar: "))
                    if valor_a_depositar <= 0:
                        print(f"O valor a se depositar deve ser {Style.BRIGHT}maior{Style.RESET_ALL} do que {Fore.YELLOW}R$0,00{Style.RESET_ALL}.")
                        print(f"Por favor, digite um {Style.BRIGHT}valor válido!{Style.RESET_ALL}")
                        print("Voltando(Aguarde 5 segundos)...")
                        time.sleep(5)
                        continue
                    elif valor_a_depositar < 5:
                        print(f"O valor a se depositar deve ser {Style.BRIGHT}maior{Style.RESET_ALL} do que R$ 5,00{Style.RESET_ALL}.")
                        print(f"Por favor, digite um {Style.BRIGHT}valor válido!{Style.RESET_ALL}")
                        print("Voltando(Aguarde 5 segundos)...")
                        time.sleep(5)
                        continue
                    elif valor_a_depositar > 1000:
                        print(f"O valor a se depositar deve ser {Style.BRIGHT}menor{Style.RESET_ALL} do que {Fore.YELLOW}R$1000,00{Style.RESET_ALL}.")
                        print(f"Por favor, digite um {Style.BRIGHT}valor válido!{Style.RESET_ALL}")
                        print("Voltando(Aguarde 5 segundos)...")
                        time.sleep(5)
                        continue
                    elif valor_a_depositar == "":
                        print(f"O campo {Style.BRIGHT}não pode ficar vazio!{Style.RESET_ALL}")
                        print(f"Por favor, digite um {Style.BRIGHT}valor válido!{Style.RESET_ALL}")
                        print("Voltando(Aguarde 5 segundos)...")
                        time.sleep(5)
                        continue
                except ValueError:
                    print(f"Ocorreu um {Fore.RED}ERRO!{Style.RESET_ALL}")
                    print("Voltando(Aguarde 3 segundos)...")
                    time.sleep(3)
                    continue
                print(f"Você depositou {Fore.GREEN}R${valor_a_depositar:.2f} com sucesso!{Style.RESET_ALL}")
                print("Voltando(Aguarde 5 segundos)...")
                time.sleep(7)
                break
        elif opção == 3:
            print("Saindo do programa(Aguarde 3 segundos)...")
            time.sleep(3)
            break
        else:
            print(f"{Fore.RED}OPÇÃO INVÁLIDA!{Style.RESET_ALL}")
            print(f"Por favor, digite uma {Style.BRIGHT}opção válida!{Style.RESET_ALL}")
            print("Voltando ao menu inicial(Aguarde 5 segundos)...")
            time.sleep(5)
            continue
    except ValueError:
        print(f"Ocorreu um {Fore.RED}ERRO!{Style.RESET_ALL}")
        print("Voltando ao menu inicial(Aguarde 3 segundos)...")
        time.sleep(3)
        continue