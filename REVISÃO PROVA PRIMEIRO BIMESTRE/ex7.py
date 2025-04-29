import os
from colorama import Fore, Style, init
import time
init(autoreset=True)

titulo = '''
=======================
CÁLCULO DE POTÊNCIA
=======================
'''

while True:
    os.system("cls")
    print(f"{Fore.CYAN}{titulo}{Style.RESET_ALL}")
    print(f"{Fore.GREEN}[1] - Calcular Potência{Style.RESET_ALL}")
    print(f"{Fore.RED}[2] - Sair do Programa{Style.RESET_ALL}")

    try:
        opcao = int(input("Selecione a opção desejada (1 ou 2): "))
        if opcao == 1:
            while True:
                os.system("cls")
                print(f"{Fore.CYAN}{titulo}{Style.RESET_ALL}")
                try:
                    base = float(input("Digite a base: "))
                    expoente = float(input("Digite o expoente: "))
                    if base == 0 and expoente == 0:
                        print(f"{Fore.RED}Erro: base e expoente não podem ser zero ao mesmo tempo.{Style.RESET_ALL}")
                        time.sleep(2)
                        continue
                    resultado = base ** expoente
                    print(f"Resultado: {base} ^ {expoente} = {resultado:.2f}")
                except ValueError:
                    print(f"{Fore.RED}Erro: digite apenas números válidos.{Style.RESET_ALL}")
                    time.sleep(2)
                    continue

                continuar = input("Deseja fazer outro cálculo? (s/n): ").lower()
                if continuar == 'n':
                    print(f"{Fore.GREEN}Saindo do programa...{Style.RESET_ALL}")
                    time.sleep(2)
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
        print(f"{Fore.RED}Erro: Digite uma opção válida!{Style.RESET_ALL}")
        time.sleep(2)
