colaboradores = int(input('Informe o número de colaboradores:'))

colabNum = 0

contadores = {
    'segunda-feira': 0,
    'terça-feira': 0,
    'quarta-feira': 0,
    'quinta-feira': 0,
    'sexta-feira': 0
}


while (colabNum < colaboradores):
    diaEscolhido = input('Informe o dia de sua preferência(segunda-feira,terça-feira,quarta-feira,quinta-feira,sexta-feira):')
    
    
    if diaEscolhido in contadores:
        contadores[diaEscolhido] += 1
        colabNum+= 1
    else: 
        print('Dia invalido!')
diaMaisEscolhido = max(contadores,key=contadores.get)
print(f'O dia escolhido pelos colaboradores é :{diaMaisEscolhido}')

