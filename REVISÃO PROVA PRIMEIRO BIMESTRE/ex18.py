import time

print("=== Sistema de Login ===")

# Etapa 1: Criação de nome de usuário e senha
while True:
    try:
        nome_usuario = input("Crie seu nome de usuário: ").strip()
        if not nome_usuario:
            print("O nome de usuário não pode estar vazio. Tente novamente.")
            continue
        senha = input("Crie sua senha: ").strip()
        if not senha:
            print("A senha não pode estar vazia. Tente novamente.")
            continue
        print("Usuário e senha criados com sucesso!")
        time.sleep(2)
        break
    except ValueError:
        print("Ocorreu um erro. Tente novamente.")
        continue

# Etapa 2: Login
while True:
    try:
        print("\n=== Login ===")
        tentativa_usuario = input("Digite seu nome de usuário: ").strip()
        if tentativa_usuario != nome_usuario:
            print("Nome de usuário incorreto. Tente novamente.")
            continue

        # Nome de usuário correto, agora verificar a senha
        tentativas_restantes = 3
        while tentativas_restantes > 0:
            tentativa_senha = input("Digite sua senha: ").strip()
            if tentativa_senha == senha:
                print("Login realizado com sucesso!")
                time.sleep(2)
                break  # Encerra o programa após login bem-sucedido
            else:
                tentativas_restantes -= 1
                if tentativas_restantes > 0:
                    print(f"Senha incorreta. Você ainda tem {tentativas_restantes} tentativa(s).")
                else:
                    print("Você excedeu o número de tentativas. Tente novamente mais tarde.")
                    time.sleep(2)
                    break  
    except ValueError:
        print("Ocorreu um erro. Tente novamente.")
        continue