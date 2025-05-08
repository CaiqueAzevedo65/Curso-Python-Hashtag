# Em python, todo código é lido de cima para baixo, dessa forma o código é lido linha por linha e a ordem das coisas importa 
# print(texto) -> Exibe um valor, sendo texto (string) ou número (int, float, etc)

print('O faturamento da loja foi de R$1.000')

# Textos (strings) são sempre entre aspas
"""
'texto' -> é uma string
texto -> vai ser reconhecido como uma variável
"""


# Operações Matemáticas no Python (a ordem de precedência é a mesma da matemática):
## Adição
print(3 + 5)

## Subtração
print(5 - 3)

## Divisão
print(5 / 3)

## Multiplicação
print(5 * 3)

## Potenciação
print(5 ** 3)

## Mod (resto da divisão de 5 por 3)
print(5 % 3)


# Operações Básicas com String
## Concatenar
print('O faturamento da loja foi ' + '1000')

## Verificar se um texto está dentro do outro (possui case sensitive | diferencia maiúsculas de minúsculas)
print('C' in 'Caique') 
print('c' in 'Caique')
nome = 'Caique'
print('C' in nome)


# Variável
## variavel = valor (uma variável recebe um valor, que pode ser um texto, número, etc.)
faturamento = 1500
custo = 800
lucro = faturamento - custo 
print(faturamento)
print(lucro)

# Pegar informações do Usuário
variavel = input('Texto para o Usuário')

## Para cadastrar um cliente
cpf = input('Digite seu cpf (apenas números, sem pontos e traços)')
print('O cpf do cliente é ' + cpf)