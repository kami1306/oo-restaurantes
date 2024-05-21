class Restaurante:
    restaurante =[]
      
    def __init__(self, nome, categoria):
       self.nome = nome.title()
       self.categoria = categoria.upper()
       self._ativo = False
       Restaurante.restaurantes.append(self)
       
    def __str__(self):
        return f'{self.nome} | {self.categoria}'
    
    @classmethod
    def listar_restaurantes(cls):
        print(f'{"Nome do restaurante".ljust(25)} | {"categoria".ljust(25)} | {"status".ljust(25)}')
        for restaurante in Restaurante.restaurantes:
            print(f'{restaurante.nome.ljust(25)} | {restaurante.categoria.ljust(25)} | {"status".ljust(25)}')

    @property
    def ativo(self):
     return '⌧' if self._ativo else '☐'
    
    def alternar_estado(self):
       self._ativo = not self._ativo


restaurante_praca = Restaurante('praça', 'Gourmet')
restaurante_praca.alternar_estado()
restaurante_pizza = Restaurante('pizza Express', 'Italiana')

Restaurante.listar_restaurantes()