# Inventário de TI
import os

inventario = []
resposta = "S"

while resposta == "S":
    equipamento = [input('Equipamento: '),
                   float(input('Valor: ')),
                   input('Número Serial: '),
                   input('Departamento: ')]
    inventario.append(equipamento)
    resposta = input('Digite "S" para continuar cadastrando: ').capitalize()

for elemento in inventario:
    print('n')
    print('Nome: ', elemento[0])
    print('Valor: ', elemento[1])
    print('Serial: ', elemento[2])
    print('Departamento: ', elemento[3])
    print('\n')

print('Valores dos ativos \n')

valores = []
for elemento in inventario:
    valores.append(elemento[1])
if len(valores) > 0:
    print('O equipamento mais caro custa: ', max(valores))
    print('O equipamento mais barato custa: ', min(valores))
    print('O valor total em equipamentos é de: ', sum(valores))
    print('\n')

busca = input(
    'Informe o nome do equipamento que deseja localizar: ').capitalize()
for elemento in inventario:
    if busca == elemento[0]:
        print('Valor..: ', elemento[1])
        print('Serial.:', elemento[2])
        print('Departamento.: ', elemento[3])
