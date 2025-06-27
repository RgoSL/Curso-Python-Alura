# Primeiro Exercício do Curso de Condicionais

# Variáveis Para Saber a Quantidade de Frutas
QntMaca = int(input("Quantas maçãs foram vendidas? \n"))
QntBana = int(input("Quantas bananas foram vendidas? \n"))

# Exibindo as Quantidades das Frutas
print(f"Foram vendidas {QntMaca} maçãs, e {QntBana} bananas.") # F-String Para Conseguir Exibir o Texto com Variáveis.

# Estrutura Condicional
if QntMaca > QntBana:
    print("A venda de maçãs foi melhor.")
    
elif QntMaca < QntBana:
    print("A venda de bananas foi melhor.")
    
else:
    print("As frutas venderam igualmente.")