valorDivida = float(input('Digite o valor da divida:'))
valorSemJuros = print(f'Total:R${valorDivida} Juros:R${valorDivida*(0/100)} Número de parcelas:1 Valor da Parcela:R${valorDivida}')

        

for parcelas in range(3,13,3):
    if parcelas == 3:
        taxa = 0.10  
    elif parcelas == 6:
        taxa = 0.15  
    elif parcelas == 9:
        taxa = 0.20  
    elif parcelas == 12:
        taxa = 0.25
        
        
    precoFinal = valorDivida * (1 + taxa)
    valorParcela  = precoFinal / parcelas
    print(f'Total:R$ {precoFinal:.2f} Juros:R$ {precoFinal - valorDivida:.2f} Número de parcelas:{parcelas} Valor da parcela:R$ {valorParcela:.2f}')