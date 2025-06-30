# Quinto Exercício do Curso de Laços

# O que acontece nesse código é o seguinte: ao encontrar o item faltando na lista, o programa irá "saltar" para uma próxima instrução.
# Eu usei a expressão "continue" na resolução, mas poderia ter sido feito com uma condição if else também.

# Coleção do Tipo Lista
Projetos = ["Website", "Jogo", "Análise de Dados", None, "App Mobile"]

# Estrutura de Controle do Tipo Loop
for Projeto in Projetos: # Vai Ler Cada Elemento na Coleção
    
    if Projeto == None: # Condição Usada Para Encontrar o Item Faltando
        
        print("Projeto Ausente") # Mensagem Quando o Encontrou
        
        continue # Comando Para dar Sequência Mesmo com o Item Faltando
    
    print(Projeto) # Ação que Acontece Após o "Salto"