# Quinto Exercício do Curso de Strings e Regex

# Importando o Módulo de Interação com as Regex do Python
import re

# Variável que Recebe a Descrição Pura da Receita
DescReceita = input("Descrição da receita :")

# Variável que Recebe os Valores Encontrados Pelo Método "search", Neste Caso, o Parâmetro de Busca Dele é o Caractere Especial Para Digitos
CodReceita = re.search(r"\d+", DescReceita)

# Exibindo o Número Encontrado na Descrição, Utilizando o Método "group" Para Exibir os Resultados do Método "search"
print(f"O número da receita é : {CodReceita.group()}")