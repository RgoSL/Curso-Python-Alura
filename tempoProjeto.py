# Segundo Exercício do Curso de Condicionais

# Variáveis que Recebem a Duração de Cada Atividade
TempoDiagrama = int(input("De quantos dias precisamos para fazer a UML? \n"))
TempoWireframes = int(input("De quantos dias precisamos para fazer os Wireframes? \n"))
TempoMonografia = int(input("E para terminar a Monografia? \n"))

# Variável Para Calcular a Duração Total do Projeto
Tempo_de_Projeto = TempoDiagrama + TempoWireframes + TempoMonografia

# Estrutura Condiconal
if TempoDiagrama < 0 or TempoWireframes <0 or TempoMonografia < 0:
    print("Não é possível a duração ser negativa.")

else:
    print(f"Vamos terminar tudo em {Tempo_de_Projeto} dias.") # F-String Para Conseguir Exibir o Texto com Variáveis.