# Sétimo Exercício do Curso de Condicionais

# Variáveis que Recebem a Nota dos Alunos
Nota01 = float(input("Qual foi a 1ª menção?\n")) 
Nota02 = float(input("Qual foi a 2ª menção?\n"))
Nota03 = float(input("Qual foi a 3ª menção?\n"))

# Variável que Guarda o Valor da Média
Media = (Nota01 + Nota02 + Nota03)/3

print(f"A média deste aluno foi de {Media:.2f}") # ":.2f" Para Limitar o Resultado Decimal em Somente Duas Casas Após a ,

# Estrutura Condicional
if Media >= 7:
    print("Este aluno está aprovado!")

elif Media >= 5 and Media < 7:
    print("Este aluno está de recuperação.")

else:
    print("Este aluno foi reprovado!")