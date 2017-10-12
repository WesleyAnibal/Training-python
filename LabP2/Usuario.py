from abc import ABCMeta, abstractmethod

class Usuario(metaclass=ABCMeta):

    def __init__(self, nome, login):
        self.nome = nome
        self.login = login
        self.jogos = []
        self.dinheiro = 0.0


    def comprarJogo(self, jogo):
        if self.dinheiro >= self.desconto(jogo):
            if not jogo in self.jogos:
                self.jogos.append(jogo)


    def addDinheiro(self, valor):
        if valor > 0:
            self.dinheiro += valor

    @abstractmethod
    def desconto(self, jogo):
        pass

