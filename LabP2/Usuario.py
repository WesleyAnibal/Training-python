from Jogo import Jogo
from Noob import Noob
from Veterano import Veterano

class Usuario:

    def __init__(self, nome, login):
        self.nome = nome
        self.login = login
        self.jogos = []
        self.dinheiro = 0.0
        self.user = Noob()

    def comprarJogo(self, jogo):
        money = self.user.desconto(jogo)
        if self.dinheiro >= money:
            if not jogo in self.jogos:
                self.dinheiro-= money
                self.jogos.append(jogo)

    def addDinheiro(self, valor):
        if valor > 0:
            self.dinheiro+= valor

    def update(self):
        self.user = Veterano()


