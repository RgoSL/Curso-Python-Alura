# Décimo Exercício do Curso de Laços

# Estrutura de Controle do Tipo Loop
while True: # Este Tipo de Definição do While faz com que o Bloco Seja Infinito, Executando Tudo Dele sem Parar. O Comando Break Finaliza o Programa

# Variáveis que Guardam o Valor dos Dados Desejados Para a Conta
    Senha = input("Digite sua senha : ")
    Nickname = input("Digite seu nome de usuário : ")

# Len é uma Função Padrão do Próprio Python Para Medir o Comprimento dos Elemento
    if len(Senha) < 8:
        print("A senha deve ter no mínimo 8 caracteres.")
        continue
    
    if len(Nickname) < 5:
        print("O nome de usuário deve ter no mínimo 5 caracteres.")
        continue

    print("Cadastro realizado com sucesso!")
    break