# Terceiro Exercício do Curso de Strings e Regex

# Variável que Receba a Palavra que Passará por Slicing
Palavra_Chave = input("Qual é a palavra chave?\n")

# Variáveis que Guardam os Valores do Slicing
Primeira = Palavra_Chave[:3]
Ultima = Palavra_Chave[-3:]

# F-String Para Anexar Variáveis no Texto
print(F"Primeiras : {Primeira}\nÚltimas : {Ultima}")