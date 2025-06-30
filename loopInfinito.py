# Segundo Exercício do Curso de Laços

'''
>CÓDIGO COM A FALHA<

contador = 0

while contador < 10:
    print("Processando dados...")
'''

# >MINHA VERSÃO DE CORREÇÃO<

# Variável da Condição
Contador = 0

# Estrutura de Controle do Tipo Loop
while Contador < 10: # Condição do Loop
    print("Processando dados...")
    
# Elemento Responsável Pelo Bom Funcionamento do Programa, Corrigindo Assim o Loop Infinito
    Contador += 1 # O "Contador" Nunca Chegará até 10 Sem Isso, Logo o Programa não irá Parar de Rodar