# Quinto Exercício do Curso de Condicionais

# Variável que Estabelece o Limite de Gasto Mensal
GastoLim = 3000.00

# Variáveis Para Receber os Valores do Programa (Opcional, Coloquei Isso Como Funcionalidade Extra)
Despesa01 = float(input("Valor de uma das despesas :"))
Despesa02 = float(input("Valor de outra despesa :"))
Despesa03 = float(input("Valor de mais uma despesa :"))
Despesa04 = float(input("Valor da última despesa :"))

# Variável que Guarda o Valor Total Gasto em Despesas no Mês
GastoMensal = Despesa01 + Despesa02 + Despesa03 + Despesa04

# Variável que Guarda o Excedente do Limite de Gasto Mensal
Deficit = GastoMensal - GastoLim # Coloquei Como um Detalhe Para a Exibição

# Estrutura Condicional
if GastoMensal > GastoLim:
    print(f"Você gastou R${GastoMensal} este mês. Você ultrapassou em R${Deficit} o seu limite de gastos mensal! ")
    
elif GastoMensal == GastoLim:
    print("Você atingiu o limite mensal!")

else:
    # F-String Para Conseguir Exibir o Texto com Variáveis.
    print(f"Você gastou R${GastoMensal} este mês. Você ainda não atingiu o limite de gastos mensal.") 
