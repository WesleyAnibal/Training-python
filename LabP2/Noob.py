from UsuarioTemplate import UsuarioTemplate

class Noob(UsuarioTemplate):

    def desconto(self, jogo):
        return jogo.preco - (jogo.preco*0.10)