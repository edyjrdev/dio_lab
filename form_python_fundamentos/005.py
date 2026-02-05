# Aritmétrica

ope_1 = input('Digite um numero: ')
ope_2 = input('Digite um segundo numero: ')

# conversoes
ope_1_int = int(ope_1)
ope_2_int = int(ope_2)

# operações
soma = ope_1_int + ope_2_int
subtracao = ope_1_int - ope_2_int
multiplicacao = ope_1_int * ope_2_int
divisao = ope_1_int / ope_2_int 
divisao_inteira = ope_1_int // ope_2_int
exponenciacao = ope_1_int ** ope_2_int
modulo = ope_1_int % ope_2_int  
print(f'Para os numeros {ope_1_int} e {ope_2_int} temos:')
print(f'Soma (+): {soma}')
print(f'Subtração (-): {subtracao}')
print(f'Multiplicação (*): {multiplicacao}')
print(f'Divisão (/): {divisao}')
print(f'Divisão Inteira (//): {divisao_inteira}')    
print(f'Exponenciação (**): {exponenciacao}')
print(f'Módulo (% - resto da divisão inteira): {modulo}')