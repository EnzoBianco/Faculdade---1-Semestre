import os
import time

titulo = '''
====================================
Calculadora com tratamento de erros
====================================
'''

while True:

    print(titulo)
    print("[1] - Fazer um cálculo")
    print("[2] - Sair do programa")

    try:
        opção = int(input("Selecione uma das opções acima (1 ou 2): "))

        if opção == 1:
            while True:
                os.system("cls")
                print(titulo)
                try:
                    N1 = float(input("Digite o primeiro número: "))
                    if not N1:
                        print("O campo não pode ficar vazio!")
                        print("Voltando...")
                        time.sleep(5)
                        continue
                    N2 = float(input("Digite o segundo número: "))
                    if not N2:
                        print("O campo não pode ficar vazio!")
                        print("Voltando...")
                        time.sleep(5)
                        continue
                    operador = input("Digite o operador matemático (Por exemplo: '+' (adição), '-' (subtração), '*' (multiplicação), '/' (divisão)): ").strip()
                    if operador == "+":
                        resultado = N1 + N2
                    elif operador == "-":
                        resultado = N1 - N2
                    elif operador == "*":
                        resultado = N1 * N2
                    elif operador == "/" or operador == "%" or operador == "//":
                        if N2 == 0 or N1 == 0:
                            print("Erro: Esta divisão não é permitida, pois o denominador ou numerador é igual a 0!")
                            print("Voltando...")
                            time.sleep(5)
                            continue
                        elif operador == "/":
                            resultado = N1 / N2
                        elif operador == "%":
                            resultado = N1 % N2
                        elif operador == "//":
                            resultado = N1 // N2
                    elif operador == "**":
                        resultado = N1 ** N2
                    else:
                        print("Operador inválido!")
                        print("Voltando...")
                        time.sleep(5)
                        continue
                except ValueError:
                    print("Erro: Por favor, digite apenas números!")
                    print("Voltando...")
                    time.sleep(5)
                    continue
                print(f"O resultado de {N1} {operador} {N2} é: {resultado}.")
                while True:
                    continuar = input("Deseja realizar outro cálculo? (s/n): ").strip().lower()
                    if continuar == "s":
                        print("Ok, vamos realizar outro cálculo...")
                        time.sleep(4)
                        break
                    elif continuar == "n":
                        print("Voltando ao menu principal...")
                        time.sleep(4)
                        break
                    else:
                        print("Opção inválida!")
                        print("Por favor, digite 's' para sim, e realizar outro cálculo, ou 'n' para não, e voltar ao menu principal.")
                        time.sleep(2)
                if continuar == "n":
                    break
        elif opção == 2:
            print("Saindo do programa...")
            time.sleep(3)
            break
        else:
            print("Opção inválida!")
            print("Por favor, digite uma opção válida!")
            print("Voltando ao menu inicial...")
            time.sleep(5)
            continue
    except ValueError:
        print("Erro: Por favor, digite apenas números!")
        print("Voltando ao menu inicial...")
        time.sleep(5)
        continue

