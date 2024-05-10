class Restaurante:
    restaurantes = []

    def __init__(self,nome,categoria):
        self.nome = nome
        self.categoria=categoria
        self.ativo= False
        Restaurante.restaurantes.append(self)
    
    def _str_(self):
       return f'{self.nome} | {self.categoria}'

    def listar_restaurantes():
        for restaurante in Restaurante.restaurantes:
            print(f' {Restaurante.nome} | {restaurante.categoria} | {restaurante.ativo}')


Restaurante_praca = Restaurante('Praça','Gourmet')
Restaurante_pizza = Restaurante('pizza', 'categoria')

Restaurante.listar_restaurantes()