# Sexto Exercício do Curso de Laços

# Neste exercício eu optei por permitir que o usuário definisse o livro que quer achar, no enunciado ele é fixo.

# Coleção do Tipo Lista
Livros = ["Dom Casmurro", "O Alquimista", "O Pequeno Príncipe", "A Morte de Ivan Ilitich", "O Lado Bom do Lado Ruim"]

LivroEscolhido = input("Qual livro você está buscando?\n")

# Estrutura de Controle do Tipo Loop
for Livro in Livros:
    if Livro == LivroEscolhido: # A Condição do Meu Break é Comparar se o Elemento na Lista é Igual ao Livro Pedido Pelo Usuário
        
        print(f"Encontramos o seu livro!\n {LivroEscolhido}") # F-String Para Exibir Variáveis em um Texto
        
        break # O Break Encerra o Programa se a Condição For Atendida
    
    print(f"Não encontramos este livro no sistema!\n Acervo : {Livro}") # Caso o Break não Ocorra, o Programa Segue Para Essa Ação