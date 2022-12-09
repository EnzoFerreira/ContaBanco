class Data:
    def __init__(self, dia, mes, ano):
        self.dia = dia
        self.ano = ano
        self.mes = mes

    def formatarData(self):
        print(f'{self.dia}/{self.mes}/{self.ano}')