class Carro:
    modelo = ''
    cor = ''
    ano = None
    placa = ''
    kilometragem = 0

    def __init__(self, modelo, cor, ano, placa, kilometragem):
        self.modelo = modelo
        self.cor = cor
        self.ano = ano
        self.placa = placa
        self.kilometragem = kilometragem

    def andar(self, kilometros):
        self.kilometragem = self.kilometragem + kilometros
        return "O carro " + self.modelo + " " + self.cor \
            + str(self.ano) + " com placa " \
            + self.placa + " andou " + str(kilometros) \
            + " km(s) e agora está com " + str(self.kilometragem) + "kms"

    