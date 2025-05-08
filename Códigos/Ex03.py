# Estruturas de decisão
## Todos os exercícios são feitos partindo-se do pressuposto de que todas as entradas são dadas de forma correta. Casos limite não mencionados no enunciado não são abordados porque não fazem parte do exercício.

### 1. Faça um Programa que peça dois números e imprima o maior deles.

num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))
print(f"O maior número é: {num1 if num1 > num2 else num2}")

### 2. Faça um Programa que peça um valor e mostre na tela se o valor é positivo ou negativo.

valor = float(input("Digite um valor: "))
if valor > 0:
    print("O valor é positivo.")
else:
    print("O valor é negativo.")

### 3. Faça um Programa que verifique o estado civil de uma pessoa. Se a letra digitada é "C" (Casado), "S" (Solteiro), "D" (Divorciado), "V" (Viúvo) ou "O" (outros). Conforme a letra escrita pelo usuário seu programa deve escrever o estado civil, exemplo:
"""
Usuário digita: C

Seu programa deve responder:
C - Casado
"""

estado_civil = input("Digite seu estado civil (C, S, D, V ou O): ").upper()
if estado_civil == "C":
    print("Casado")
elif estado_civil == "S":
    print("Solteiro")
elif estado_civil == "D":
    print("Divorciado")
elif estado_civil == "V":
    print("Viúvo")
elif estado_civil == "O":
    print("Outros")

### 4. Faça um Programa que verifique se o e-mail digitado faz parte dos e-mails de spam.

emails_spam = "fulano@gmail.com,beltrano@gmail.com,ciclano@gmail.com"
email = input("Digite seu e-mail: ")
if email in emails_spam.split(","):
    print("E-mail é spam.")
else:
    print(f"O e-mail {email} não é spam.")

### 5. Faça um programa para a leitura de duas notas parciais de um aluno. O programa deve calcular a média alcançada por aluno e apresentar:
"""	
A mensagem "Aprovado", se a média alcançada for maior ou igual a sete;
A mensagem "Reprovado", se a média for menor do que sete;
A mensagem "Aprovado com Distinção", se a média for igual a dez.
"""

nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
media = (nota1 + nota2) / 2
if media >= 7:
    if media == 10:
        print("Aprovado com Distinção")
    else:
        print("Aprovado")
else:
    print("Reprovado")

### 6. Faça um Programa que leia o orçamento de 3 empresas e mostre o maior deles.

orcamento1 = float(input("Digite o orçamento da empresa 1: "))
orcamento2 = float(input("Digite o orçamento da empresa 2: "))
orcamento3 = float(input("Digite o orçamento da empresa 3: "))
maior_orcamento = max(orcamento1, orcamento2, orcamento3)
print(f"O maior orçamento é: {maior_orcamento}")

### 7. Faça um Programa que leia três orçamentos e mostre o maior e o menor deles.

orcamento1 = float(input("Digite o orçamento da empresa 1: "))
orcamento2 = float(input("Digite o orçamento da empresa 2: "))
orcamento3 = float(input("Digite o orçamento da empresa 3: "))
maior_orcamento = max(orcamento1, orcamento2, orcamento3)
menor_orcamento = min(orcamento1, orcamento2, orcamento3)
print(f"O maior orçamento é: {maior_orcamento}")
print(f"O menor orçamento é: {menor_orcamento}")

### 8. Faça um programa que pergunte o preço de três produtos e informe qual produto você deve comprar, sabendo que a decisão é sempre pelo mais barato.

produto1 = float(input("Digite o preço do produto 1: "))
produto2 = float(input("Digite o preço do produto 2: "))
produto3 = float(input("Digite o preço do produto 3: "))
mais_barato = min(produto1, produto2, produto3)
print(f"O produto mais barato custa: {mais_barato}")

### 9. Faça um Programa que leia três números e mostre-os em ordem decrescente.

num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))
num3 = int(input("Digite o terceiro número: "))	
print("Os números em ordem decrescente são:")
if num1 >= num2 and num1 >= num3: 
    print(num1)
    if num2 >= num3:
        print(num2)
        print(num3)
    else:
        print(num3)
        print(num2)
elif num2 >= num1 and num2 >= num3:
    print(num2)
    if num1 >= num3:
        print(num1)
        print(num3)
    else:
        print(num3)
        print(num1)
elif num3 >= num1 and num3 >= num2:
    print(num3)
    if num1 >= num2:
        print(num1)
        print(num2)
    else:
        print(num2)
        print(num1)

### 10. Faça um Programa que pergunte em que turno você estuda. Peça para digitar M-matutino ou V-Vespertino ou N- Noturno. Imprima a mensagem "Bom Dia!", "Boa Tarde!" ou "Boa Noite!" ou "Valor Inválido!", conforme o caso.

turno = input("Digite o turno em que estuda (M - Matutino, V - Vespertino, N - Noturno): ").upper()
if turno == "M":
    print("Bom Dia!")
elif turno == "V":
    print("Boa Tarde!")
elif turno == "N":
    print("Boa Noite!")
else:
    print("Valor Inválido!")

### 11. As Organizações Tabajara resolveram dar um aumento de salário aos seus colaboradores e lhe contraram para desenvolver o programa que calculará os reajustes. Faça um programa que recebe o salário de um colaborador e o reajuste segundo o seguinte critério, baseado no salário atual:

salario = float(input("Digite o salário atual: "))

#### salários até R\\$ 280,00 (incluindo) : aumento de 20% 

aumento = 0.2 if salario <= 280 else 0

#### salários entre R\\$ 280,00 e R\\$ 700,00 : aumento de 15% 

aumento = 0.15 if 280 < salario <= 700 else aumento

#### salários entre R\\$ 700,00 e R\\$ 1500,00 : aumento de 10% 

aumento = 0.1 if 700 < salario <= 1500 else aumento

#### salários de R\\$ 1500,00 em diante : aumento de 5% Após o aumento ser realizado, informe na tela: 

aumento = 0.05 if salario > 1500 else aumento

#### o salário antes do reajuste;

print(f"Salário antes do reajuste: R${salario:.2f}")

#### o percentual de aumento aplicado;

print(f"Percentual de aumento aplicado: {aumento * 100:.2f}%")

#### o valor do aumento;

print(f"Valor do aumento: R${salario * aumento:.2f}")

#### o novo salário, após o aumento.

print(f"Novo salário, após o aumento: R${salario + (salario * aumento):.2f}")

### 12 . Faça um programa para o cálculo de uma folha de pagamento, sabendo que os descontos são do Imposto de Renda, que depende do salário bruto (conforme tabela abaixo) e que o FGTS corresponde a 11% do Salário Bruto, mas não é descontado (é a empresa que deposita). O Salário Líquido corresponde ao Salário Bruto menos os descontos. O programa deverá pedir ao usuário o valor da sua hora e a quantidade de horas trabalhadas no mês.
"""
Desconto do IR:
Salário Bruto até 900 (inclusive) - isento
Salário Bruto até 1500 (inclusive) - desconto de 5%
Salário Bruto até 2500 (inclusive) - desconto de 10%
Salário Bruto acima de 2500 - desconto de 20%
Imprima na tela as informações, dispostas conforme o exemplo abaixo. No exemplo o valor da hora é 5 e a quantidade de hora é 220.

Salário Bruto: (5 * 220)        : R\\$ 1100,00
(-) IR (5%)                     : R\\$   55,00
(-) INSS ( 10%)                 : R\\$  110,00
FGTS (11%)                      : R\\$  121,00
Total de descontos              : R\\$  165,00
Salário Liquido                 : R\\$  935,00
"""

salario_hora = float(input("Digite o valor da sua hora: "))
horas_trabalhadas = float(input("Digite a quantidade de horas trabalhadas no mês: "))
salario_bruto = salario_hora * horas_trabalhadas
if salario_bruto <= 900:
    ir = 0
elif salario_bruto <= 1500:
    ir = 0.05 * salario_bruto
elif salario_bruto <= 2500:
    ir = 0.1 * salario_bruto
else:
    ir = 0.2 * salario_bruto
inss = 0.1 * salario_bruto
fgts = 0.11 * salario_bruto
total_descontos = ir + inss
salario_liquido = salario_bruto - total_descontos + fgts
print(f"Salário Bruto: R${salario_bruto:.2f}")
print(f"(-) IR (5%) : R${ir:.2f}")
print(f"(-) INSS (10%) : R${inss:.2f}")
print(f"FGTS (11%) : R${fgts:.2f}")
print(f"Total de descontos : R${total_descontos:.2f}")
print(f"Salário Líquido : R${salario_liquido:.2f}")

### 13. Faça um Programa que leia um número e exiba o dia correspondente da semana. (1-Domingo, 2- Segunda, etc.), se digitar outro valor deve aparecer valor inválido.

numero = int(input("Digite um número de 1 a 7: "))
if numero == 1:
    print("Domingo")
elif numero == 2:
    print("Segunda")
elif numero == 3:
    print("Terça")
elif numero == 4:
    print("Quarta")
elif numero == 5:
    print("Quinta")
elif numero == 6:
    print("Sexta")
elif numero == 7:
    print("Sábado")

### 14. Faça um programa que lê as duas notas parciais obtidas por um aluno numa disciplina ao longo de um semestre, e calcule a sua média. Em seguida, mostre qual conceito o aluno teve. A atribuição de conceitos obedece à tabela abaixo:
"""
Média de Aproveitamento  Conceito
Entre 9.0 e 10.0        A
Entre 7.5 e 9.0         B
Entre 6.0 e 7.5         C
Entre 4.0 e 6.0         D
Entre 4.0 e zero        E
"""

nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
media = (nota1 + nota2) / 2
if media >= 9.0:
    conceito = "A"
elif media >= 7.5:
    conceito = "B"
elif media >= 6.0:
    conceito = "C"
elif media >= 4.0:
    conceito = "D"
else:
    conceito = "E"
print(f"A média é: {media:.2f}")
print(f"O conceito é: {conceito}")

### 15. Você está construindo um calendário para controlar dias de trabalho a pedido do RH. Nessa construção, você vai precisar definir quais anos são bissextos e quais não são, para montar o calendário de forma correta. Faça um Programa que peça um número correspondente a um determinado ano e em seguida informe se este ano é ou não bissexto.
"""
Dica para determinar se um ano é bissexto: 
- São bissextos todos os anos múltiplos de 400, p.ex.: 1600, 2000, 2400, 2800...
- São bissextos todos os múltiplos de 4, exceto se for múltiplo de 100 mas não de 400, 
p.ex.: 1996, 2000, 2004, 2008, 2012, 2016, 2020, 2024, 2028...
- Não são bissextos todos os demais anos.
ex1: 2004 é múltiplo de 4, mas não é múltiplo de 100, então é bissexto.
ex2: 2000 é múltiplo de 4, mas é múltiplo de 100, só que também é multiplo de 400, então é bissexto (porque todo ano múltiplo de 400 é bissexto, independente do resto).
ex3: 1900 é múltiplo de 4, é múltiplo de 100, mas não é múltiplo de 400, então não é bissexto

Dica: lembre que: numero % 4 é o resto da divisão do número por 4, ex: 10 % 3 = 1 (já que 10/3 = 3 e resta 1)
"""

ano = int(input("Digite um ano: "))
if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
    print(f"O ano {ano} é bissexto.")
else:
    print(f"O ano {ano} não é bissexto.")

### 16. Faça um Programa para leitura de três notas parciais de um aluno. O programa deve calcular a média alcançada por aluno e presentar:
"""
A mensagem "Aprovado", se a média for maior ou igual a 7, com a respectiva média alcançada;
A mensagem "Reprovado", se a média for menor do que 7, com a respectiva média alcançada;
A mensagem "Aprovado com Distinção", se a média for igual a 10.
"""

nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
nota3 = float(input("Digite a terceira nota: "))
media = (nota1 + nota2 + nota3) / 3
if media >= 7:
    if media == 10:
        print("Aprovado com Distinção")
    else:
        print(f"Aprovado com média {media:.2f}")
else:
    print(f"Reprovado com média {media:.2f}")

### 17. João Papo-de-Pescador, homem de bem, comprou um microcomputador para controlar o rendimento diário de seu trabalho. Toda vez que ele traz um peso de peixes maior que o estabelecido pelo regulamento de pesca do estado de São Paulo (50 quilos) deve pagar uma multa de R$ 4,00 por quilo excedente. João precisa que você faça um programa que leia a variável peso (peso de peixes) e calcule o excesso. Gravar na variável excesso a quantidade de quilos além do limite e na variável multa o valor da multa que João deverá pagar. Imprima os dados do programa com as mensagens adequadas.

peso_peixes = float(input("Digite o peso dos peixes: "))
if peso_peixes > 50:
    excesso = peso_peixes - 50
    multa = excesso * 4
    print(f"Excesso: {excesso:.2f} kg")
    print(f"Multa: R${multa:.2f}")
else:
    print("Não há excesso.")

### 18. Faça um Programa para um caixa eletrônico. O programa deverá perguntar ao usuário a valor do saque e depois informar quantas notas de cada valor serão fornecidas. As notas disponíveis serão as de 1, 5, 10, 50 e 100 reais. O valor mínimo é de 10 reais e o máximo de 600 reais. O programa não deve se preocupar com a quantidade de notas existentes na máquina.
"""
Exemplo 1: Para sacar a quantia de 256 reais, o programa fornece duas notas de 100, uma nota de 50, uma nota de 5 e uma nota de 1;
Exemplo 2: Para sacar a quantia de 399 reais, o programa fornece três notas de 100, uma nota de 50, quatro notas de 10, uma nota de 5 e quatro notas de 1.


Dica1: numero // 10 vai te dar como resposta a parte inteira da divisão do número por 10.
Dica2: numero % 10 vai te dar o resto da divisão do número por 10.
"""

saque = int(input("Digite o valor do saque (mínimo R$ 10 e máximo R$ 600): "))
if 10 <= saque <= 600:
    notas_100 = saque // 100
    saque %= 100
    notas_50 = saque // 50
    saque %= 50
    notas_10 = saque // 10
    saque %= 10
    notas_5 = saque // 5
    saque %= 5
    notas_1 = saque // 1

    print(f"Notas de R$ 100: {notas_100}")
    print(f"Notas de R$ 50: {notas_50}")
    print(f"Notas de R$ 10: {notas_10}")
    print(f"Notas de R$ 5: {notas_5}")
    print(f"Notas de R$ 1: {notas_1}")

### 19. Faça um programa que faça 5 perguntas para uma pessoa sobre um crime. As perguntas são:
"""
"Telefonou para a vítima?"
"Esteve no local do crime?"
"Mora perto da vítima?"
"Devia para a vítima?"
"Já trabalhou com a vítima?" 
O programa deve no final emitir uma classificação sobre a participação da pessoa no crime. Se a pessoa responder positivamente a 2 questões ela deve ser classificada como "Suspeita", entre 3 e 4 como "Cúmplice" e 5 como "Assassino". Caso contrário, ele será classificado como "Inocente".
"""

pergunta1 = input("Telefonou para a vítima? (s/n): ").lower()
pergunta2 = input("Esteve no local do crime? (s/n): ").lower()
pergunta3 = input("Mora perto da vítima? (s/n): ").lower()
pergunta4 = input("Devia para a vítima? (s/n): ").lower()
pergunta5 = input("Já trabalhou com a vítima? (s/n): ").lower()
respostas_positivas = sum([pergunta1 == 's', pergunta2 == 's', pergunta3 == 's', pergunta4 == 's', pergunta5 == 's'])

if respostas_positivas == 2:
    classificacao = "Suspeita"
elif 3 <= respostas_positivas <= 4:
    classificacao = "Cúmplice"
elif respostas_positivas == 5:
    classificacao = "Assassino"
else:
    classificacao = "Inocente"
print(f"Classificação: {classificacao}")

### 20. Um posto está vendendo combustíveis com a seguinte tabela de descontos:
"""
Álcool:
até 20 litros, desconto de 3% por litro
acima de 20 litros, desconto de 5% por litro
Gasolina:
até 20 litros, desconto de 4% por litro
acima de 20 litros, desconto de 6% por litro

Escreva um algoritmo que leia o número de litros vendidos, o tipo de combustível (codificado da seguinte forma: A-álcool, G-gasolina), calcule e imprima o valor a ser pago pelo cliente sabendo-se que o preço do litro da gasolina é R$ 2,50 o preço do litro do álcool é R$ 1,90.
"""

litros_vendidos = float(input("Digite o número de litros vendidos: "))
combustivel = input("Digite o tipo de combustível (A - Álcool, G - Gasolina): ").upper()
preco_alcool = 1.90
preco_gasolina = 2.50
if combustivel == "A":
    if litros_vendidos <= 20:
        desconto = 0.03
    else:
        desconto = 0.05
    preco_total = litros_vendidos * preco_alcool * (1 - desconto)
elif combustivel == "G":
    if litros_vendidos <= 20:
        desconto = 0.04
    else:
        desconto = 0.06
    preco_total = litros_vendidos * preco_gasolina * (1 - desconto)

print(f"Valor a ser pago: R${preco_total:.2f}")

### 21. Uma fruteira está vendendo frutas com a seguinte tabela de preços:
"""
                    Até 5 Kg           Acima de 5 Kg
Morango         R$ 2,50 por Kg          R$ 2,20 por Kg
Maçã            R$ 1,80 por Kg          R$ 1,50 por Kg
Se o cliente comprar mais de 8 Kg em frutas ou o valor total da compra ultrapassar R$ 25,00, receberá ainda um desconto de 10% sobre este total. Escreva um algoritmo para ler a quantidade (em Kg) de morangos e a quantidade (em Kg) de maças adquiridas e escreva o valor a ser pago pelo cliente.
"""



### 22. O Hipermercado Tabajara está com uma promoção de carnes que é imperdível. Confira:
"""
                    Até 5 Kg           Acima de 5 Kg
File Duplo      R$ 4,90 por Kg          R$ 5,80 por Kg
Alcatra         R$ 5,90 por Kg          R$ 6,80 por Kg
Picanha         R$ 6,90 por Kg          R$ 7,80 por Kg
Para atender a todos os clientes, cada cliente poderá levar apenas um dos tipos de carne da promoção, porém não há limites para a quantidade de carne por cliente. Se compra for feita no cartão Tabajara o cliente receberá ainda um desconto de 5% sobre o total da compra. Escreva um programa que peça o tipo e a quantidade de carne comprada pelo usuário e gere um cupom fiscal, contendo as informações da compra: tipo e quantidade de carne, preço total, tipo de pagamento, valor do desconto e valor a pagar.
"""

### 23. Faça um Programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada. Considere que a cobertura da tinta é de 1 litro para cada 6 metros quadrados e que a tinta é vendida em latas de 18 litros, que custam R\\$ 80,00 ou em galões de 3,6 litros, que custam R\\$ 25,00.
area = float(input('Informe o tamanho da área a ser pintada em m²: '))
litros_tinta = area / 6
"""
Informe ao usuário as quantidades de tinta a serem compradas e os respectivos preços em 3 situações.

Dica: lembre dos operadores // e % mostrados em exercícios anteriores<br>
Dica1: numero // 10 vai te dar como resposta a parte inteira da divisão do número por 10.<br>
Dica2: numero % 10 vai te dar o resto da divisão do número por 10.

1. Comprar apenas latas de 18 litros: (apenas latas inteiras)

2. Comprar apenas galões de 3,6 litros: (apenas galoes inteiros)

3. Misturar latas e galões, de forma que o desperdício de tinta seja menor. Acrescente 10% de folga e sempre arredonde os valores para cima, isto é, considere latas cheias.
O custo da lata é 80/18 = 4,44 R\\$/L

O custo do galão é 25/3,6 = 6,94 R\\$/L

A lata é mais econômica, então todas as latas inteiras que pudermos usar devemos comprar em latas. Se ficar faltando alguma coisa para completar devemos avaliar se é melhor comprar latas ou galões. Exemplo:

Se queremos comprar 90 litros. 5 latas dão exatamente 90 litros. Então devemos comprar tudo em latas.

Se queremos comprar 95 litros. 5 latas dão exatamente 90 litros. Então devemos comprar pelo menos 5 latas e avaliar o que falta, se estes últimos 5 litros valem mais apenas em latas ou galões.

Para os 5 litros faltantes precisamos de 2 galões que custam 50 reais no total. Ou de uma lata que custa 80 reais no total. Portanto, neste caso vale mais a pena usar 2 galões.

Se queremos comprar 107 litros. 5 latas dão exatamente 90 litros. Então devemos comprar pelo menos 5 latas e avaliar o que falta, se estes últimos 5 litros valem mais apenas em latas ou galões.

Para os 17 litros faltantes precisamos de 5 galões que custam 125 reais no total. Ou de uma lata que custa 80 reais no total. Portanto, neste caso vale mais a pena usar uma lata.

3 galões custam 75 reais, 4 galões custam 100 reais. Então, se for possível completar com até 3 galões escolhe-se galões. Qualquer quantidade maior que 3 galões, usa-se latas.

Podemos ir ao exercício:
"""