colaboradores = int(input('Informe o número de colaboradores:'))

colabNum = 0

contadores = {
    'segunda-feira': 0,
    'terça-feira': 0,
    'quarta-feira': 0,
    'quinta-feira': 0,
    'sexta-feira': 0
}

while colabNum < colaboradores:
    diaEscolhido = input('Informe o dia de sua preferência (segunda-feira, terça-feira, quarta-feira, quinta-feira, sexta-feira): ').strip().lower()
    
    if diaEscolhido in contadores:
        contadores[diaEscolhido] += 1
        colabNum += 1
    else: 
        print('Dia inválido!')


max_votos = max(contadores.values())


dias_mais_escolhidos = [dia for dia, votos in contadores.items() if votos == max_votos]


if len(dias_mais_escolhidos) > 1:
    print(f"Há um empate entre os seguintes dias: {', '.join(dias_mais_escolhidos)}")
else:
    print(f"O dia mais escolhido pelos colaboradores é: {dias_mais_escolhidos[0]}")
