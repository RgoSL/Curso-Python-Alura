# Segundo Exercício do Curso de Strings e Regex

# Variáveis que Recebem a Parte que Será Personalizada na Mensagem
NomeCliente = input("Qual seu nome?\n")
CidadeCliente = input("De qual cidade você está acessando?\n")

# Mensagem Salva em uma Variável Para Permitir Flexibilidade por Parte da Mesma
MsgPersonalizada = f"Olá {NomeCliente.capitalize()}! Seja bem-vinda(o) ao Sistema da Cidade de {CidadeCliente.capitalize()}."
# Utilizei o Método "capitalize" Para Corrigir o Nome Próprio que for Inserido

# Exibindo a Variável com a Saudação
print(MsgPersonalizada)