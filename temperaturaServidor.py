# Terceiro Exercício do Curso de Condicionais

# Variável Para Saber a Temperatura 
TempSala = float(input("A temperatura da sala está a quantos graus? \n"))

# Variável com Temperatura Adequada, Permitindo Flexibilidade do Programa
TempAdequada = 25

# Estrutura Condicional
if TempSala > TempAdequada:
    print("A temperatura está acima do limite ideal!")

elif TempSala < 18: # Curiosidade: A Temperatura Ideal de uma Sala Como Essa é Entre 18° e 27° 
    print("A temperatura está muito abaixo do normal!")
    
else:
    print("Está tudo sob controle.")