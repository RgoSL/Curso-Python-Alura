# Sexto Exercício do Curso de Condicionais

# Variável que Recebe as Horas Atuais
Horario = float(input("Que horas são?\n")) # Esse \n Depois do Texto Serve Para Criar um Espaçamento Entre as Linhas. Uso Para Formatar o Input

# Estrutura Condicional
if Horario >= 8 and Horario <= 18:
    print("Acesso liberado.")

else:
    print("Acesso negado.")