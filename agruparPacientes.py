# Décimo Exercício do Curso de Strings e Regex

# Esse exercício foi um pouco diferente na execução final, exigiu um uso diferente da condicional. Pode ser considerado como mais organizado

# Importando o Módulo de Interação com as Regex do Python
import re

# Variável que Recebe as Três Informações do Paciente
Dados = input("Por favor, informe o nome completo e o ano de nascimento do paciente : ")  

# Variável que Receba a Formatação que o Programa irá Buscar
Padrao = r'(\w+) (\w+) (\d{4})'  

# Variável que Busca Pelo Padrão Determinado
Grupo = re.search(Padrao, Dados)

# Estrutura de Condição com Variáveis Internas Para Cada Formato
if Grupo:
    Nome = Grupo.group(1)
    Sobrenome = Grupo.group(2)
    Nascimento = Grupo.group(3)

# Usando o "\n" as Mensagens Ficam Espaçadas Dentro de Apenas um uso da Função "Print"
    print(f"Primeiro Nome: {Nome}\n" f"Sobrenome: {Sobrenome}\n" f"Ano de Nascimento: {Nascimento}" )