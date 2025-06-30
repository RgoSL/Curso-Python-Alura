# Sétimo Exercício do Curso de Laços

# Neste exercício eu tive mais dificuldade, fiquei preso a uma falsa necessidade de usar Coleções de Dados.

# Variável Fixa Para os Itens em Estoque
Estoque = 5

# Estrutura de Controle do Tipo Loop
while Estoque > 0:
    print(f"Venda realizada! Itens em estoque : {Estoque}") # F-String Para Poder Exibir Variáveis Diretamente em um Texto
    Estoque -= 1 
    
print("O estoque está vazio.")