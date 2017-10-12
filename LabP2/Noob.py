from Usuario import Usuario

class Noob(Usuario):

    def desconto(self, jogo):
        return jogo.preco - (jogo.preco*0.10)