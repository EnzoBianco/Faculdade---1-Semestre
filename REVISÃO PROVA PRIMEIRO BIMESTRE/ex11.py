import os
import time
import locale 
locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')
titulo = '''
=========================
Entrada de número inteiro
=========================
'''

while True:

    print(titulo)
    print("[1] - Conferir se um determinado número é inteiro")
    print("[2] - Sair do programa")

    try:

        opção = int(input("Selecione uma opção para continuar(1 ou 2): "))

        if opção == 1:
            while True:
                os.system("cls")
                print(titulo)
                try:
                    numero = locale.atof(input("Digite um número qualquer: "))
                    if numero == "":
                        print("ERRO: É necessário digitar um número!")
                        time.sleep(2)
                        continue
                except ValueError:
                    print("ERRO: Digite apenas números!")
                    time.sleep(2)
                    continue
                if numero.is_integer():
                    print(f"O número {numero} é um inteiro!")
                    print("Voltando ao Início...")
                    time.sleep(2)
                    break
                else:
                    print(f"O número {numero} não é um inteiro!")
                    print("Voltando ao Início...")
                    time.sleep(2)
                    break
        else:
            print("Saindo do Programa...")
            time.sleep(2)
            break
    except ValueError:
        print("Digite umas das opções disponíveis(1 ou 2)")
        time.sleep(3)
        continue

          