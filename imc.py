# calcule seu Índice de Massa Corporal (IMC) e mostre seu status, de acordo com a tabela abaixo:
# – IMC abaixo de 18,5: Abaixo do Peso
# – Entre 18,5 e 25: Peso Ideal
# – 25 até 30: Sobrepeso
# – 30 até 40: Obesidade
# – Acima de 40: Obesidade Mórbida
print('-'*31)
print('\033[30;46m Índice de Massa Corporal (IMC)\033[m')
print('-'*31)
peso = float(input('Digite o seu peso em kg:'))
altura = float(input('Digite sua altura em metros:'))
imc = peso / (altura ** 2)
print('Seu IMC é de {:.2f} :'.format(imc))
if imc < 18.5:
    print('Você está ABAIXO DO PESO IDEAL:')
elif imc <= 25:
    print('Você está com PESO IDEAL:')
elif imc <= 30:
    print('Você está com SOBREPESO:')
elif imc <= 40:
    print('Você está com OBESIDADE:')
else:
    print('Você está com OBESIDADE MÓRBIDA')
    