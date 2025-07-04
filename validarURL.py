# Quarto Exercício do Curso de Strings e Regex

# Variável que Recebe a URL do Site
URL = input("Cole a URL do site aqui :")

# Estrutura Condicional Para Validar a URL
if URL.startswith("https://") and URL.endswith(".com"): 
# O Método "starts" Verifica se a URL Começa com o Valor que Queremos, e o "ends" Verifica se a URL Termina com o Valor que Queremos.

    print("Esta URL é válida!")

else:
    print("URL com formato inválido!")