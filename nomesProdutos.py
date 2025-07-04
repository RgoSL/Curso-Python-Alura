# Primeiro Exercício do Curso de Strings e Regex

# Variável que Recebe o Texto Puro
NomeProduto = input("Digite o nome do produto:")

# Variável Usada Para Receber os Valores já Passados Pelos Métodos de Correção de String
NomeFormatado = NomeProduto.lower().strip()
# Strip Remove Espaços em Branco, e Lower Converte Todos os Caracteres Para Minúsculos

# Exibindo a Variável com os Padrões já Aplicados
print(NomeFormatado)