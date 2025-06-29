# Oitavo Exercício do Curso de Condicionais

# Variável que Recebe o Valor Chave do Programa
Distancia = float(input("Qual foi a distância percorrida em Km?\n"))
# ^ Esse \n Depois do Texto Serve Para Criar um Espaçamento Entre as Linhas. Uso Para Formatar o Input

# Estrutura Condicional
if Distancia <= 100:
    print("Valor do pedágio : R$10,00")

elif Distancia > 100 and Distancia <= 200:
    print("Valor do pedágio : R$20,00")

else:
    print("Valor do pedágio : R$30,00")