import os
from colorama import Fore, Style, init
import time
from datetime import datetime
init(autoreset=True)

preços = {
    1: {1: 20.00, 2: 28.00, 3: 35.00, 4: 42.00, 5: 48.00, 6: 53.00},
    2: {1: 25.00, 2: 34.00, 3: 42.00, 4: 50.00, 5: 57.00, 6: 63.00}
}



COLONIA_DE_FERIAS  = """
  ██████╗ ██████╗ ██╗      ██████╗ ███╗   ██╗██╗ █████╗     ██████╗ ███████╗    
 ██╔════╝██╔═══██╗██║     ██╔═══██╗████╗  ██║██║██╔══██╗    ██╔══██╗██╔════╝    
 ██║     ██║   ██║██║     ██║   ██║██╔██╗ ██║██║███████║    ██║  ██║█████╗      
 ██║     ██║   ██║██║     ██║   ██║██║╚██╗██║██║██╔══██║    ██║  ██║██╔══╝      
 ╚██████╗╚██████╔╝███████╗╚██████╔╝██║ ╚████║██║██║  ██║    ██████╔╝███████╗    
  ╚═════╝ ╚═════╝ ╚══════╝ ╚═════╝ ╚═╝  ╚═══╝╚═╝╚═╝  ╚═╝    ╚═════╝ ╚══════╝    
                                                                                 
 ███████╗███████╗██████╗ ██╗ █████╗ ███████╗                                    
 ██╔════╝██╔════╝██╔══██╗██║██╔══██╗██╔════╝                                    
 █████╗  █████╗  ██████╔╝██║███████║███████╗                                    
 ██╔══╝  ██╔══╝  ██╔══██╗██║██╔══██║╚════██║                                    
 ██║     ███████╗██║  ██║██║██║  ██║███████║                                    
 ╚═╝     ╚══════╝╚═╝  ╚═╝╚═╝╚═╝  ╚═╝╚══════╝                                    
"""
executar_programa = True

while executar_programa:
    # Limpar a tela do terminal
   
    
    # Exibir o título do sistema em ASCII art
    print(f"{Fore.BLUE}{COLONIA_DE_FERIAS}{Style.RESET_ALL}")
    print(f"{Fore.YELLOW}Sistema de Reservas para Funcionários{Style.RESET_ALL}")
    print(f"\n{Fore.LIGHTMAGENTA_EX}MENU PRINCIPAL:{Style.RESET_ALL}")
   
    # Capturar opção do usuário
    print(f" {Fore.GREEN}[1]{Style.RESET_ALL} - Fazer nova reserva")
    print(f" {Fore.RED}[2]{Style.RESET_ALL} - Sair")
    print(" " + "-" * 40)

    try:
        opção = int(input("\n Selecione uma opção: "))
    # Capturar opção do usuário
        if opção == 1:
            fazer_reserva = True
            
            while fazer_reserva:
                # Limpar a tela e exibir título
                os.system('cls' if os.name == 'nt' else 'clear')
                print(f"{Fore.BLUE}{COLONIA_DE_FERIAS}{Style.RESET_ALL}")
                print(f"{Fore.CYAN}Sistema de Reservas para Funcionários{Style.RESET_ALL}")
                print(f"{Fore.YELLOW}= * 40{Style.RESET_ALL}")

        # Exibir tabela de preços
                print(f"\n{Style.BRIGHT}TABELA DE PREÇOS:{Style.RESET_ALL}")
                print(" " + "-" * 40)
                print(f" {Style.BRIGHT}{'Pessoas':<10}{'Tipo 1 (R$)':<15}{'Tipo 2 (R$)':<15}{Style.RESET_ALL}")
                
                for pessoas in range(1, 7):
                    print(f" {pessoas:<10}{preços[1][pessoas]:.2f}{'':>7}{preços[2][pessoas]:.2f}")
                
                print(" " + "-" * 40)
                
                # Coleta de dados
                print(f"\n{Style.BRIGHT}NOVA RESERVA:{Style.RESET_ALL}")
                print(" " + "-" * 40)
                
                # Nome do funcionário
                nome = input("Nome do funcionário: ").strip()
                if not nome:
                    print(f"{Fore.RED}Erro: O nome não pode estar vazio!{Style.RESET_ALL}")
                    time.sleep(2)
                    continue
                
                # Quantidade de pessoas
                try:
                    quantidade_pessoas = int(input("Quantidade de pessoas (1-6): "))
                    if quantidade_pessoas < 1 or quantidade_pessoas > 6:
                        print(f"\n{Fore.RED}Erro: Quantidade de pessoas inválida! O limite é de 1 a 6 pessoas.{Style.RESET_ALL}")
                        time.sleep(2)
                        continue
                except ValueError:
                    print(f"\n{Fore.RED}Erro: Por favor, digite apenas números!{Style.RESET_ALL}")
                    time.sleep(2)
                    continue
                
                # Tipo de apartamento
                try:
                    tipo_apto = int(input("Tipo de apartamento (1 ou 2): "))
                    if tipo_apto not in [1, 2]:
                        print(f"\n{Fore.RED}Erro: Tipo de apartamento inválido! Escolha 1 ou 2.{Style.RESET_ALL}")
                        time.sleep(2)
                        continue
                except ValueError:
                    print(f"\n{Fore.RED}Erro: Por favor, digite apenas números!{Style.RESET_ALL}")
                    time.sleep(2)
                    continue
                
                # Quantidade de dias
                try:
                    dias = int(input("Quantidade de dias: "))
                    if dias < 1:
                        print(f"\n{Fore.RED}Erro: Quantidade de dias inválida! Deve ser pelo menos 1 dia.{Style.RESET_ALL}")
                        time.sleep(2)
                        continue
                except ValueError:
                    print(f"\n{Fore.RED}Erro: Por favor, digite apenas números!{Style.RESET_ALL}")
                    time.sleep(2)
                    continue
                
                # Cálculo do valor total
                diaria = preços[tipo_apto][quantidade_pessoas]
                valor_total = diaria * quantidade_pessoas * dias
                
                # Exibição do relatório
                os.system('cls' if os.name == 'nt' else 'clear')
                print(f"{Fore.BLUE}{COLONIA_DE_FERIAS}{Style.RESET_ALL}")
                print(f"{Fore.GREEN}Sistema de Reservas para Funcionários{Style.RESET_ALL}")
                print(f"{Fore.GREEN} " + "=" * 40 + Style.RESET_ALL)
                
                
                print(f"\n {Style.BRIGHT}RELATÓRIO DE RESERVA{Style.RESET_ALL}")
                print(" " + "=" * 40)
                print(f" {Style.BRIGHT}Data da reserva:{Style.RESET_ALL} {datetime.now().strftime('%d/%m/%Y %H:%M:%S')}")
                print(f" {Style.BRIGHT}Nome do funcionário:{Style.RESET_ALL} {nome}")
                print(f" {Style.BRIGHT}Tipo de apartamento:{Style.RESET_ALL} {tipo_apto}")
                print(f" {Style.BRIGHT}Quantidade de pessoas:{Style.RESET_ALL} {quantidade_pessoas}")
                print(f" {Style.BRIGHT}Dias de estadia:{Style.RESET_ALL} {dias}")
                print(" " + "-" * 40)
                
                diaria_por_pessoa = preços[tipo_apto][quantidade_pessoas]
                print(f" {Style.BRIGHT}Valor da diária por pessoa:{Style.RESET_ALL} R$ {diaria_por_pessoa:.2f}")
                print(f" {Style.BRIGHT}Valor da diária total:{Style.RESET_ALL} R$ {diaria_por_pessoa * quantidade_pessoas:.2f}")
                print(f" {Fore.GREEN + Style.BRIGHT}VALOR TOTAL DA ESTADIA: R$ {valor_total:.2f}{Style.RESET_ALL}")
                print(" " + "=" * 40)
                
                input("\n Pressione ENTER para voltar ao menu principal...")
                
                fazer_reserva = False
                
        # Opção 2: Sair do sistema
        else:
            os.system('cls' if os.name == 'nt' else 'clear')
            print(f"{Fore.BLUE}{COLONIA_DE_FERIAS}{Style.RESET_ALL}")
            print(f"{Fore.BLUE}Sistema de Reservas para Funcionários{Style.RESET_ALL}")
            print(f"{Fore.GREEN} =" * 40 + Style.RESET_ALL)
            
            print(f"\n{Fore.YELLOW}Obrigado por utilizar o Sistema de Reservas da Colônia de Férias!{Style.RESET_ALL}")
            print(f"{Fore.YELLOW}Encerrando o programa...{Style.RESET_ALL}")
            time.sleep(2)
            executar_programa = False

    except ValueError:
        print(f"{Fore.RED}Erro: Por favor, digite apenas números!{Style.RESET_ALL}")
        time.sleep(2)
