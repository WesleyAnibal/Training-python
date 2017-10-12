
class Jogo():

    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco
        self.maiorScore = 0
        self.jogou = 0
        self.zerou = 0

    def registraJogada(self, score, zerou):
        self.jogou+=1
        if score > self.maiorScore:
            self.maiorScore = score
        if zerou:
            self.zerou+=1
'''
    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, nome):
        self._nome = nome

    @property
    def preco(self):
        return self._preco

    @preco.setter
    def preco(self, preco):
        self._preco = preco

    @property
    def maiorScore(self):
        self._maiorScore

    @maiorScore.setter
    def maiorScore(self, score):
        self._maiorScore = score

    @property
    def jogou(self):
        self._jogou

    @jogou.setter
    def jogou(self, jogou):
        self._jogou = jogou

    @property
    def zerou(self):
        self._zerou

    @zerou.setter
    def zerou(self, zerou):
        self._zerou = zerou
    '''


