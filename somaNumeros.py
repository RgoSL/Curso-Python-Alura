# Quarto Exercício do Curso de Laços

# Neste exercício eu escolhi o Loop For porque o limite da coleção já estava definido.

# Coleção do Tipo Lista
Valores = [10, 20, 30, 40, 50]

# Estrutura de Controle do Tipo Loop
for Valor in Valores:
    
    # Variável que Guarda e Calcula a Soma dos Valores
    Total = sum(Valores) # Na Minha Versão eu Utilizei a Função Padrão do Python Para Somas. Mas Poderia Ser Resolvido com "Total += Valor"

print(f"A soma total das receitas é : {Total}") # F-String Para Exibir Variáveis em um Texto