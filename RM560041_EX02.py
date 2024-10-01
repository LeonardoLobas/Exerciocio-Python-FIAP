valorBruto = float(input('Digite o preço do carro:'))
print(f'O preço á vista com desconto de 20% é: {valorBruto-(valorBruto*0.2)}')

    
for possibParcelas in range(6,61,6):
        precoFinal = valorBruto * (1 + ((possibParcelas/2) / 100)) 
        print(f'O preço final parcelado em {possibParcelas}X é de R$ {precoFinal:.2f} com parcelas de R$ {(precoFinal / possibParcelas):.2f}')