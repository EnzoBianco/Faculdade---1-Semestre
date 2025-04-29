import os
from colorama import Fore, Style, init
import time
init(autoreset=True)

título = '''
  _____  _       _                       _            _       _                                                  _       _       _               
 |  __ \(_)     (_)                     | |          | |     (_)                                                (_)     | |     (_)              
 | |  | |___   ___ ___  __ _  ___     __| | ___    __| | ___  _ ___   _ __  _   _ _ __ ___   ___ _ __ ___  ___   _ _ __ | |_ ___ _ _ __ ___  ___ 
 | |  | | \ \ / / / __|/ _` |/ _ \   / _` |/ _ \  / _` |/ _ \| / __| | '_ \| | | | '_ ` _ \ / _ \ '__/ _ \/ __| | | '_ \| __/ _ \ | '__/ _ \/ __|
 | |__| | |\ V /| \__ \ (_| | (_) | | (_| |  __/ | (_| | (_) | \__ \ | | | | |_| | | | | | |  __/ | | (_) \__ \ | | | | | ||  __/ | | | (_) \__ \
 |_____/|_| \_/ |_|___/\__,_|\___/   \__,_|\___|  \__,_|\___/|_|___/ |_| |_|\__,_|_| |_| |_|\___|_|  \___/|___/ |_|_| |_|\__\___|_|_|  \___/|___/
                                                                                                                                                                                                                                                                                                
'''

while True:
    os.system("cls")
    print(f"{Fore.CYAN}{título}{Style.RESET_ALL}")
    print(f"{Fore.GREEN}[1] - Iniciar o cáculo{Style.RESET_ALL}")
    print(f"{Fore.RED}[2] - Sair do programa{Style.RESET_ALL}")

    try:
        opção = int(input(f"{Fore.YELLOW}Escolha uma opção(1 ou 2):{Style.RESET_ALL} "))
        if opção == 1:
            while True:
                os.system("cls")
                print(f"{Fore.CYAN}{título}{Style.RESET_ALL}")
                numerador = float(input("Digite o numerador: "))
                denominador = float(input("Digite o denominador: "))
                try:
                    if denominador == 0:
                        print(f"{Fore.RED}Denominador não pode ser zero!{Style.RESET_ALL}")
                        time.sleep(2)
                        continue
                except ValueError:
                    print(f"\n{Fore.RED}Erro: Por favor, digite apenas números!{Style.RESET_ALL}")
                    time.sleep(2)
                    continue
                resultado = numerador / denominador
                print(f"O resultado da divisão é: {resultado:.1f}")
                input(f"{Fore.GREEN}Pressione ENTER para uma nova divisão.{Style.RESET_ALL}")
        if opção == 2:
            try:
                print(f"{Fore.GREEN}Saindo do programa...{Style.RESET_ALL}")
                time.sleep(2)
                continue
            except ValueError:
                print(f"{Fore.RED}Erro: Ocorreu um erro inesperado!{Style.RESET_ALL}")
                time.sleep(2)
                break
        
    except ValueError:
        print(f"{Fore.RED}Erro: Por favor, digite apenas números!{Style.RESET_ALL}")
        time.sleep(2)

