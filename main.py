class Bola:
    def __init__(self, cor):
        self.quantidade = 5
        self.COR = cor
    def quantidade_de_bola(self):
        return self.quantidade

bola = Bola("verde")
print(bola.COR)
print(bola.quantidade_de_bola())
