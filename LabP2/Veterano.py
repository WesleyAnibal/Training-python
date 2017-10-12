from Usuario import Usuario

classcd  Veterano(Usuario):

    def desconto(self, jogo):
        return jogo.preco -(jogo.preco*0.2)