# Décimo Exercício do Curso de Condicionais

# Variável que Recebe o Valor Ganho Mensalmente Pelo Usuário
RendaMensal = float(input("Qual é a sua renda mensal?\n"))

# Variável que Recebe o Valor do Empréstimo Desejado Pelo Usuário
Emprestimo = float(input("Qual o valor do empréstimo desejado?\n"))

# Variáveis que Guardam os Valores Necessários Para a Execução do Programa
RendaMin = 2000.00 # Variável de Requisito Mínimo Para Flexibilidade do Programa
LimiteEmp = (RendaMensal / 10) * 3 # Foi Minha Alternativa Para Realizar o Cálculo da Porcentagem

# Estrutura Condicional
if RendaMensal >= RendaMin and Emprestimo <= LimiteEmp:
    print("O pedido de empréstimo foi liberado!")

elif RendaMensal < RendaMin:
    print("Você não atinge a renda mínima necessária para fazer o empréstimo.")
    
else:
    print(f"Empréstimo negado : Pedido maior que 30% da renda.\n O seu limite é de : R${LimiteEmp}")