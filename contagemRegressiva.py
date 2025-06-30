# Oitavo Exercício do Curso de Laços

# Aprendi ao ver a resposta que era possível colocar a ordem ao contrário com uma simples adição do valor -1 dentro dos parâmetros do Range.

# Estrutura de Controle do Tipo Loop
for Num in range(10, 0, -1):
    if Num % 2 == 0: # Operador Aritmético Para Conferir a Paridade
        print(f"Faltam apenas {Num} segundo(s) - Não perca essa oportunidade!") # F-String Para Poder Exibir Variáveis Diretamente em um Texto
        
    else:
        print(f"A contagem continua : {Num} segundo(s) restante(s).")

print("Aproveite a promoção agora")