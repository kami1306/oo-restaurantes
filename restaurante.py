class Restaurante:

restaurantes = []

def init__(self, nome,categoria):

self.nome nome

self.categoria = categoria self._ativo = False

Restaurante.restaurantes.append(self)

def str eturn ^ self): f:fself } | {self.categoria}

for restaurante in Restaurante. restaurantes

@property

def ativo(self):

def listar_restaurantes():

: | print(f'(restaurante.nome.ljust(25)) | restaurante.categoria.ljust(25) | (restaurante.ativo)')

return if self. ativo else 'o'

restaurante_praca = Restaurante('Praça', 'Gourmet') restaurante_pizza Restaurante('Pizza express', 'Italiana')

Restaurante.listar_restaurantes()