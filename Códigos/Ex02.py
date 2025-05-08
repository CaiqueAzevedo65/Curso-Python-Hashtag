# Exercícios Módulo 5 - Operações, Variáveis e Input

## 1. Faça um Programa que mostre a mensagem (print) "Alo mundo" na tela.

print('Alo mundo')

## 2. Faça um Programa que peça um número (input) e então mostre a mensagem: "O número informado foi [número]."

numero = int(input('Digite um número: '))
print(f'O número informado foi {numero}')

## 3. Faça um Programa que peça dois números e imprima a soma.

num1 = int(input('Digite o primeiro número: '))
num2 = int(input('Digite o segundo número: '))
soma = num1 + num2
print(f'A soma dos números é {soma}')

## 4. Faça um Programa que peça as 4 notas bimestrais de um aluno e mostre a média de todas as notas.

nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))
nota3 = float(input('Digite a terceira nota: '))
nota4 = float(input('Digite a quarta nota: '))
media = (nota1 + nota2 + nota3 + nota4) / 4
print(f'A média das notas é {media}')

## 5. Faça um Programa que converta metros para centímetros. Você pode pedir o comprimento em metros para o usuário (input).

comprimento_metros = float(input('Digite o comprimento em metros: '))
centimetros = comprimento_metros * 100
print(f'O comprimento em centímetros é {centimetros} cm')

## 6. Faça um Programa que calcule a área de uma sala de um apartamento. Para isso, o seu programa precisa pedir a largura da sala, o comprimento da sala e imprimir a área em m² da sala.

largura = float(input('Digite a largura da sala em metros: '))
comprimento = float(input('Digite o comprimento da sala em metros: '))
area = largura * comprimento
print(f'A área da sala é {area} m²')

## 7. Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês.

salario_hora = int(input('Digite quanto você ganha por hora: '))
horas_trabalhadas = int(input('Digite quantas horas você trabalhou no mês: '))
salario = salario_hora * horas_trabalhadas
print(f'O seu salário no mês é R${salario}')

## 8. Vamos criar um conversor de temperatura. Faça um Programa que peça a temperatura em graus Fahrenheit, transforme e mostre a temperatura em graus Celsius.
### Fórmula: C = (F - 32) * 5/9

temperatura_fahrenheit = float(input('Digite a temperatura em graus Fahrenheit: '))
temperatura_celsius = (temperatura_fahrenheit - 32) * 5/9
print(f'A temperatura em graus Celsius é {temperatura_celsius}°C')

## 9. Faça um Programa que peça a temperatura em graus Celsius, transforme e mostre em graus Fahrenheit.
### Fórmula: F = C * 9/5 + 32

temperatura_celsius = float(input('Digite a temperatura em graus Celsius: '))
temperatura_fahrenheit = temperatura_celsius * 9/5 + 32
print(f'A temperatura em graus Fahrenheit é {temperatura_fahrenheit}°F')

## 10. Tendo como dados de entrada a altura (h) de uma pessoa, construa um algoritmo que calcule seu peso ideal, usando a seguinte fórmula:
### Fórmula: P = 72,7h - 58

altura = float(input('Digite a altura da pessoa em metros: '))
peso_ideal = 72.7 * altura - 58
print(f'O peso ideal da pessoa é {peso_ideal} kg')

## 11. Tendo como dado de entrada a altura (h) de uma pessoa, construa um algoritmo que calcule seu peso ideal, utilizando as seguintes fórmulas:
### a. Para homens: $P = 72,7h - 58$

altura = float(input('Digite a altura da pessoa em metros: '))
peso_ideal_homem = 72.7 * altura - 58
print(f'O peso ideal do homem é {peso_ideal_homem} kg')

### b. Para mulheres: $P = 62,1h - 44,7$

altura = float(input('Digite a altura da mulher em metros: '))
peso_ideal_mulher = 62.1 * altura - 44.7    
print(f'O peso ideal da mulher é {peso_ideal_mulher} kg')

## 12. Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês.

salario_hora = float(input('Digite quanto você ganha por hora: '))
horas_trabalhadas = float(input('Digite quantas horas você trabalhou no mês: '))

###  Calcule o salário bruto (horas * salario por hora)

salario_bruto = salario_hora * horas_trabalhadas
print(f'O salário bruto é R${salario_bruto}')

### Calcule o desconto do IR (11% do salário bruto)

desconto_ir = salario_bruto * 0.11
print(f'O desconto do IR é R${desconto_ir}')

### Calcule o desconto do INSS (8% do salário bruto)

desconto_inss = salario_bruto * 0.08
print(f'O desconto do INSS é R${desconto_inss}')

### Calcule o desconto do sindicato (5% do salário bruto)

desconto_sindicato = salario_bruto * 0.05   
print(f'O desconto do sindicato é R${desconto_sindicato}')

### Calcule o salário líquido (salário bruto - descontos)

salario_liquido = salario_bruto - (desconto_ir + desconto_inss + desconto_sindicato)
print(f'O salário líquido é R${salario_liquido}')

## 13. Faça um programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada. Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00. Informe ao usuário a quantidades de latas de tinta a serem compradas e o preço total. (para simplificação nesse momento, não se preocupe em arredondar a quantidade de latas a serem compradas - vamos trabalhar isso em breve)

area = float(input('Digite o tamanho da área a ser pintada em metros quadrados: '))
# 1 litro = 3 metros
# 1 lata = 18 litros
# 1 lata = R$ 80,00
litros = area / 3 # litros necessários
latas = litros / 18 # área em latas
preco_total = latas * 80.00 # preço total
print(f'A quantidade de latas de tinta a serem compradas é {latas} e o preço total é R${preco_total}')

## 14. Faça um programa que peça o tamanho de um arquivo para download (em MB) e a velocidade de um link de Internet (em Mbps), calcule e informe o tempo aproximado de download do arquivo usando este link (em minutos).
### Detalhe: MB significa megabyte, Mb (com b minúsculo) significa megabit. Um megabit é 1/8 de um megabyte. 

tamanho_arquivo = float(input('Digite o tamanho do arquivo para download em MB: '))
velocidade_link = float(input('Digite a velocidade do link de Internet em Mbps: '))
# 1 MB = 8 Mb
# 1 Mbps = 1/8 MBps
tempo_download = (tamanho_arquivo * 8) / velocidade_link # tempo em segundos
tempo_download_minutos = tempo_download / 60 # tempo em minutos
print(f'O tempo aproximado de download do arquivo é {tempo_download_minutos} minutos')