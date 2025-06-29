# Quarto Exercício do Curso de Condicionais

# Variáveis Utilizadas Para Capturar as Informações
Peso = float(input("Quantos Kgs você pesa?\n"))
Altura = float(input("Quanto de altura você tem?\n"))

# Variável Para Exibir o Cálculo
IMC = Peso/(Altura**2)

print(f"O resultado do seu IMC é : {IMC:.2f}") # ":.2f" Para Limitar o Resultado Decimal em Somente Duas Casas Após a ,

# Estrutura Condicional
if IMC < 18.5:
    print("Você está abaixo do peso ideal.")
    
elif IMC >= 18.5 and IMC < 25:
    print("Você está com o peso ideal.")

elif IMC >= 25:
    print("Você está acima do peso.")