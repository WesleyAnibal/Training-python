from UsuarioTemplate import UsuarioTemplate

class Veterano(UsuarioTemplate):

    def desconto(self, jogo):
        return jogo.preco -(jogo.preco*0.2)