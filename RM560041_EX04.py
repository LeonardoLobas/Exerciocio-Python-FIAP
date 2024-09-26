print('Escolha o tipo de investimento:\n1. CDB \n2. LCI \n3. LCA')
escolhaInvestimento = int(input('Digite o tipo de investimento(1,2 ou 3): '))
if escolhaInvestimento == 1:
    print("Você escolheu CDB.")
    valorResgate = float(input('Digite o valor do resgate: '))
    qtdDias = int(input('Digite o número de dias que o valor permaneceu investido: '))
    if qtdDias <= 180 :
        valorImposto = valorResgate * (1 + 0.225)  - valorResgate
        print(f'O valor do imposto de renda a ser pago é: {valorImposto}')
    elif 181 <= qtdDias <= 360:
        valorImposto = valorResgate * (1 +  0.2) - valorResgate
        print(f'O valor do imposto de renda a ser pago é: {valorImposto}')
    elif 361 <= qtdDias <= 720:
        valorImposto = valorResgate * (1 +  0.175) - valorResgate
        print(f'O valor do imposto de renda a ser pago é: {valorImposto}')
    
    else:
        valorImposto = valorResgate * (1 + 0.15 ) - valorResgate
        print(f'O valor do imposto de renda a ser pago é: {valorImposto}')
elif escolhaInvestimento == 2:
    print("Você escolheu LCI.")
    valorResgate = float(input('Digite o valor do resgate: '))
    print(f'Valor resgatado no valor de: R${valorResgate}, OBS: esse tipo de investimento é livre de imposto de renda')
elif escolhaInvestimento == 3:
    print("Você escolheu LCA.")
    valorResgate = float(input('Digite o valor do resgate: '))
    print(f'Valor resgatado no valor de: R${valorResgate}, OBS: esse tipo de investimento é livre de imposto de renda')
else:
    print("Opção inválida. Por favor, escolha 1, 2 ou 3.")

