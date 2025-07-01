# Nono Exercício do Curso de Laços

# Demorei um pouco para resolver este exercício porque fiquei me perguntando se isso era uma lista ou um dicionário.

# Coleção do Tipo Dicionário
Livros = [
    {"Nome" : "Dom Casmurro", "Estoque" : 5},
    {"Nome" : "O Alquimista", "Estoque" : 0},
    {"Nome" : "O Pequeno Príncipe", "Estoque" : 3},
    {"Nome" : "A Morte de Ivan Ilitch", "Estoque" : 0},
    {"Nome" : "O Lado Bom do Lado Ruim", "Estoque" : 2}
    ]

# Estrutura de Controle do Tipo Loop
for Livro in Livros: # Vai Ler Cada Elemento na Coleção
    
    if Livro["Estoque"] == 0: # Condição Usada Para Encontrar o Item Sem Estoque
        
        continue # Comando Para dar Sequência ao Código Após a Condição
    
    print(f"Livro disponível : {Livro['Nome']}") # F- String Para Exibir o Dicionário, [] Para Exibir uma Chave no Dicionário