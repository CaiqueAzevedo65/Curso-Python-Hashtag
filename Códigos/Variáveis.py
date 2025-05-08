## Variáveis em Python
# Tipos de Variáveis em Python
"""
Uma variável é um objeto, afinal tudo é um objeto em Python (logo tudo pode ser uma variável).

int: inteiro
string: texto
float: números com casas decimais (ponto flutuante)
bool ou boolean: True ou False

Obs: Variáveis em Python não são declaradas explicitamente, mas isso não significa que você deve ficar mudando o tempo todo

Obs2: Cuidado com os nomes restritos

Obs3: Não usar caracteres especiais para nomear variáveis (exceto _)

Obs4: Não usar números no início do nome da variável.
"""

faturamento = 1000
print(type(faturamento))

faturamento = 1000.00
print(type(faturamento))

faturamento = '1.000'
print(type(faturamento))

ganha_bonus = True
print(type(ganha_bonus))


# Concatenar variáveis (apenas strings podem ser concatenadas)
faturamento = 1000
custo = 800
print('O faturamento da loja foi de R$' + str(faturamento)) 
print('O custo foi de R$ {}'.format(custo)) # Outra forma 
print(f'O lucro foi de R$ {faturamento - custo}') # Outra forma (f-string)

# Mudança de tipo de variável (não é o ideal)
num_serie = 1234567890 # Variável do tipo inteiro (int)
texto = '1234567890' # Variável do tipo string (str)
print(type(num_serie))

float(num_serie) # Transforma a variável em float
str(num_serie) # Transforma a variável em string
int(texto) # Transforma a variável em inteiro