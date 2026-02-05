# Variaveis

age = 2026 - 1978
name = 'Edy Junior'
weight = 70.5
height = 1.61

print(f'Meu nome é {name}, tenho {age} anos, peso {weight} e altura {height}.')

name, age, weight = 'Laila', 2026 - 1987, 65.1

print(f'Meu nome é {name}, tenho {age} anos, peso {weight} e altura {height}.')

# Constantes - não tem em python
# Apenas convenção (combinado)
PI = 3.1415
print(f'PI = {PI} é para ser constante.')
ABS_PATH = '/pasta_fixa/src'
print(f'Caminho Fixo = "{ABS_PATH}" não deve ser alterado.')

# Snake Case - variaveis
meu_nome = 'Zig Doguinho'
# Camel Case - Classe
# class Doguinho

# Conversões de Tipos
valor_str = '2.50'
valor_float = float(valor_str)
desconto_cartao = 0.05
valor_com_desconto = valor_float * (1 - desconto_cartao)
print(f'Valor {valor_float} com {(desconto_cartao * 100):.2f} % de desconto fica {valor_com_desconto:.2f}.')

# concatenar str com numero - necessitar conversão
print(name + str(age))

# print(float('Oi')) - Erro - ValueError: could not convert string to float: 'Oi'
print(int('1000'))
print(int(1.99))
print(float('1.6556'))
print(float(1999))
print(str(1000))
print(str(1.9991))

# Booleano - Vazio = False
print(bool(1))
print(bool(0))
print(bool('True'))
print(bool(''), bool('False'))
print(bool([]), bool([1, 2, 3]))
print(bool({}), bool({'nome': 'Edy'}))
print(bool(None))

# Divisao e Divisão inteira
div = 10 /3
div_int = 10 // 3
print(div, div_int)
print(type(div), type(div_int))