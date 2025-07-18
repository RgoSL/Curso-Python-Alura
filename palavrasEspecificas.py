# Nono Exercício do Curso de Strings e Regex

# Minha maior dificuldade nesse exercício foi fazer o programa considerar a ocorrência da palavra inteira, não só da letra informada.
# Na minha versão eu não utilizei um parâmetro chamado "IGNORECASE", como no resultado do instrutor. Assim, meu programa só funciona com minúsculas.

# Importando o Módulo de Interação com as Regex do Python
import re

# Variável que Recebe o Nome do Livro
Titulo = input("Qual o título do livro?\n")

# Variável que Recebe a Letra Inicial que o Programa ira usar
PrimeiraLetra = input("Digite a letra que estamos buscando :")

# Variável que Define o Padrão de Exibição das Informações Encontradas
PalavraEspec = re.findall(rf'\b{PrimeiraLetra}[a-zà-ÿ]*', Titulo)

print(PalavraEspec)