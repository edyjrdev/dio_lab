# Tipos de Dados
# Tamanho em memória
# Operações

# Tipos Comuns

# Numérico: int, float, complex
# int()
a = 1
b = 2
c = 3
print(a, b, c)
# float()
d = 1.0
e = 2.0
f = 3.0
print(d, e, f)
# complex()
g = 1j
h = 2j
i = 3j
print(g, h, i)

# Booleano: bool
# bool()
j = True
k = False
print(j, k)
# Texto: str
# str()
frase = 'Ouviram do Ipiranga'
poema = "O 'ser' ou não 'ser' é um questionamento"
nome = "Edy Junior"
sobrenome = 'Junior'
paragrafo  = """
Um dia lindo
vou programar
ate ficar feliz
e o sono me derrubar."""

print(frase, poema, nome, sobrenome)
print(paragrafo)
# Sequencia: list, tuple, range
# list()
# tuple()
# range()
# Mapa: dict
# dict()
# Coleção: set, frozenset (sem repetição)
# set()
# frozenset()
# Binário: bytes, bytearray, memoryview
# bytes()
# bytearray()
# memoryview()
# None: NoneType

# dir()  # Retorna o escopo local das bibliotecas, variaveis em uso
print(dir())  

print('-' * 35)
print(dir(paragrafo))  # descreve metodos e propriedades do objeto

# help() - descreve a ajuda offline 
# help > Consulta Objeto
# help > math
# help > str
# help> q + Enter - sai do help
# help (var_obj) - descreve objeto