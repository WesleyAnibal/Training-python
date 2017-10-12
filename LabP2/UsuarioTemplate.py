from abc import ABCMeta, abstractmethod

class UsuarioTemplate(metaclass=ABCMeta):

    @abstractmethod
    def desconto(self, jogo):
        pass

