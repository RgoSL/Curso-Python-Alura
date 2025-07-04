# Sexto Exercício do Curso de Strings e Regex

# Importando o Módulo de Interação com as Regex do Python
import re

# Variável que Recebe o Texto Original
Texto = input("Texto a ser revisado : ")

# Variável que Recebe a Palavra que Desagrada o Autor(a)
PalavraErrada = input("Qual palavra deseja substituir?")

# Variável que Recebe a Substituição Desejada
NovaPalavra = input("Qual palavra deve substituir essa?")

# Variável que Armazena o Texto Após os Processos de Revisão
TextoRevisado  = re.sub(rf'\b{PalavraErrada}\b', NovaPalavra, Texto)

# Exibindo o Texto Após a Substituição ser Realizada
print(TextoRevisado) 