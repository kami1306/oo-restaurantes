class Restaurante:
    def __init__(self,nome,categoria):
        self.nome = nome
        self.categoria=categoria
        self.ativo= False

        Restaurante_praca = Restaurante('Praça','Gourmet')
        Restaurante_pizza = Restaurante('pizza','italiana')

        Restaurantes =[Restaurante_pizza,Restaurante_praca]

        print(vars(Restaurante_praca))
        print(vars(Restaurante_pizza))