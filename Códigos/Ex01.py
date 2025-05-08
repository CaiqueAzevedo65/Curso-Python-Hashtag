# Exercícios Módulo 4 - Operações, Variáveis e Input

"""
## Parte 1 - Operações e Variáveis
Crie um programa que imprima (print) os principais indicadores da loja Hashtag&Drink no último ano.
Obs: faça tudo usando variáveis.

Valores do último ano:

Quantidade de Vendas de Coca = 150<br>
Quantidade de Vendas de Pepsi = 130<br>
Preço Unitário da Coca = 1,50 <br>
Preço Unitário da Pepsi = 1,50<br>
Custo da Loja: 2.500,00

Use o bloco abaixo para criar todas as variáveis que precisar.
"""

quantidade_vendas_coca = 1350.00
quantidade_vendas_pepsi = 1730.00
preco_unit_coca = 1.50
preco_unit_pepsi = 1.50
custo_loja = 2500.00

# 1. Qual foi o faturamento de Pepsi da Loja?

print('Faturamento de Pepsi: R$', quantidade_vendas_pepsi * preco_unit_pepsi,)

# 2. Qual foi o faturamento de Coca da Loja?

print(f'Faturamento de Coca: R${quantidade_vendas_coca * preco_unit_coca}')	

# 3. Qual foi o Lucro da loja?

faturamento_coca = quantidade_vendas_coca * preco_unit_coca
faturamento_pepsi = quantidade_vendas_pepsi * preco_unit_pepsi
lucro_loja = faturamento_coca + faturamento_pepsi - custo_loja
print(f'Lucro da loja: R${faturamento_coca + faturamento_pepsi - custo_loja}')

# 4. Qual foi a Margem da Loja? (Lembre-se, margem = Lucro / Faturamento). Não precisa formatar em percentual

faturamento = faturamento_coca + faturamento_pepsi
margem = lucro_loja / faturamento
print(f'Margem da loja: {margem}')


"""
## Parte 2 - Inputs e Strings

A maioria das empresas trabalham com um Código para cada produto que possuem. A Hashtag&Drink, por exemplo, tem mais de 1.000 produtos e possui um código para cada produto.
Ex: 
Coca -> Código: BEB1300543
Pepsi -> Código: BEB1300545
Vinho Primitivo Lucarelli -> Código: BAC1546001
Vodka Smirnoff -> Código: BAC17675002

Repare que todas as bebidas não alcóolicas tem o início do Código "BEB" e todas as bebidas alcóolicas tem o início do código "BAC".

Crie um programa de consulta de bebida que, dado um código qualquer, identifique se a bebida é alcóolica. O programa deve responder True para bebidas alcóolicas e False para bebidas não alcóolicas. Para inserir um código, use um input.

Dica: Lembre-se do comando in para strings e sempre insira os códigos com letra maiúscula para facilitar.
"""

print('--- CONSULTA DE BEBIDA ---')
codigo = input('Digite o código da bebida (Insira o código em letras maiúsculas): ')
print('O código da bebida é: ' + codigo)
print(f'A bebida é alcóolica? {str('BAC' in codigo)}')