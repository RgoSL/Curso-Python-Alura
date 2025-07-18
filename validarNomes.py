# Sétimo Exercício do Curso de Strings e Regex

# Importando o Módulo de Interação com as Regex do Python
import re 

# Variável que Captura o Nome a ser Validado
NomeCliente = input("Qual o nome do cliente?\n")

# Estrutura Condicional Utilizando o Método "fullmatch", Verificando se a String Inteira Segue Aquele Padrão
if re.fullmatch(r'[A-Z][a-z]*', NomeCliente): # Entre Parênteses Estão as Classes de Caracteres de Letras Maiúsculas e Minúsculas
    print("Este nome é válido.")

else:
    print("Esse é um nome inválido.")