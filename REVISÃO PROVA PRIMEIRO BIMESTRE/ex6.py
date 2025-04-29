import os
from colorama import Fore, Style, init
import time
init(autoreset=True)

preços = {
    1: {1: 20.00, 2: 28.00, 3: 35.00, 4: 42.00, 5: 48.00, 6: 53.00},
    2: {1: 25.00, 2: 34.00, 3: 42.00, 4: 50.00, 5: 57.00, 6: 63.00}
}


titulo = '''
==============================================
COLÔNIA DE FÉRIAS PARA FUNCIONÁRIOS DA EMPRESA
==============================================
'''

while True:
    os.system("cls")
    print(f"{Fore.RED}{titulo}{Style.RESET_ALL}")
    print(f"{Fore.GREEN}[1] - Reserve suas férias{Style.RESET_ALL}")
    print(f"{Fore.BLUE}[2] - Sair do programa{Style.RESET_ALL}")

    try:
        opção = int(input("Selecione a opção desejada(1 ou 2): "))
        if opção == 1:
            while True:
                os.system("cls")
                print(f"{Fore.RED}{titulo}{Style.RESET_ALL}")
                apartamento = input("Selecione o tipo de apartemento(1 ou 2): ")
                pessoas = int(input("Digite o número de pessoas(1 até 6): "))
                dias = int(input("Digite o número de dias(1 até 6): "))
                try:
                    if apartamento not in ["1", "2"]:
                        print(f"{Fore.RED}Tipo de apartamento inválido!{Style.RESET_ALL}")
                        time.sleep(2)
                        continue
                    if pessoas < 1 or pessoas > 6:
                        print(f"{Fore.RED}Número de pessoas inválido!{Style.RESET_ALL}")
                        time.sleep(2)
                        continue
                    if dias < 1 or dias > 6:
                        print(f"{Fore.RED}Número de dias inválido!{Style.RESET_ALL}")
                        time.sleep(2)
                        continue
                except ValueError:
                    print(f"{Fore.RED}Por favor, digite apenas números!{Style.RESET_ALL}")
                    time.sleep(2)
                    continue
                if apartamento in ["1", "2"]:
                    apartamento = int(apartamento)  # Converter para inteiro para acessar o dicionário
                    valor_total = preços[apartamento][pessoas] * dias
                    print(f"Valor total de R$ {valor_total:.2f}")
                continuar = input(f"{Fore.GREEN}Digite 's' para reservar novamente ou 'n' para sair:{Style.RESET_ALL} ")
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
                reserva = False
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
        continue


