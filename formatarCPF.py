# Oitavo Exercício do Curso de Strings e Regex

# Minha solução foi bem diferente daquela que o instrutor deu nesse exercício. Eu utilizei somente 1 variável e passei o padrão do CPF diretamente na condicional.

# Importando o Módulo das Ferramentas Regex
import re

# Variável que Recebe o CPF do Usuário
CPF = input("Por favor, informe seu CPF :")

# Estrutura de Condição Para Validar o Formato do CPF
if re.fullmatch(r"\d{3}.\d{3}.\d{3}-\d{2}", CPF): 
    print("O CPF está no formato correto.")

else:
    print("Por favor, digite o CPF corretamente xxx.xxx.xxx-xx")