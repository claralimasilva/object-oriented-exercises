class TV:

    def __init__(self):
        self.cor = 'preta'
        self.ligada = False
        self.tamanho = 55
        self.canal = 'Netflix'
        self.volume = 10


tv_sala = TV()
tv_quarto = TV()


tv_sala.cor = 'branca'

print(tv_sala.cor)
print(tv_quarto.cor)

tv_quarto.tamanho = 30

print(tv_sala.tamanho)
print(tv_quarto.tamanho)