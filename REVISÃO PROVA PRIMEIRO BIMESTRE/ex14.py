import os
import time
from datetime import datetime, timedelta
from colorama import Fore, Style, init
init(autoreset = True)

titulo = '''
============================================
Calcular idade a partir do ano de nascimento
============================================
'''
while True:
    print(titulo)
    print(f"{Fore.GREEN}[1]{Style.RESET_ALL} - Calcular minha idade a partir do ano, mês e dia em que nasci.")
    print(f"{Fore.RED}[2]{Style.RESET_ALL} - Sair do programa.")

    try:
        opção = int(input("Selecione uma das opções acima(1 ou 2): "))
        if opção == 1:
            while True:
                os.system("cls")
                nascimento = input("Digite sua data de nascimento (dd/mm/aaaa): ")
                try:
                    data_nascimento = datetime.strptime(nascimento, "%d/%m/%Y")
                    data_atual = datetime.now()
                    if data_nascimento > data_atual:
                        print("ERRO: A data de nascimento não pode ser no futuro!")
                        time.sleep(5)
                        continue
                    anos = data_atual.year - data_nascimento.year
                    meses = data_atual.month - data_nascimento.month
                    dias = data_atual.day - data_nascimento.day

                    if meses < 0 or (meses == 0 and dias < 0):
                        anos -= 1
                        meses += 12
                    if dias < 0:
                        meses -= 1
                        ultimo_dia_mes_anterior = (datetime(data_atual.year, data_atual.month, 1) - timedelta(days=1)).day
                        dias += ultimo_dia_mes_anterior
                    if data_nascimento.day == data_atual.day and data_nascimento.month == data_atual.month:
                        print(f"Hoje é seu aniversário! Parabéns pelos {anos} anos!")
                        print("Voltando ao menu inicial...")
                        time.sleep(5)
                        break
                    print(f"Você tem {anos} anos, {meses} mês(es) e {dias} dia(s) de idade.")
                    print("Voltando ao menu inicial...")
                    time.sleep(5)
                    break
                except ValueError:
                    print("ERRO: Por favor, digite uma data válida no formato dd/mm/aaaa!")
                    time.sleep(5)
                    continue
        elif opção == 2:
            print("Saindo do programa...")
            time.sleep(5)
            break
        else:
            print("A opção informada é inválida!")
            print("Por favor, selecione uma das opções disponíveis (1 ou 2).")
            print("Voltando ao menu inicial...")
            time.sleep(5)
            continue
    except ValueError:
        print("ERRO: Por favor, digite apenas números!")
        time.sleep(5)
        continue