from Framework.Util import *


class Contato:
    def __init__(self, celular=None, email=None, red_social=None):
        self.celular = celular
        self.email = email
        self.red_social = red_social

    def prompt_init():
        """Se crea un diccionario con los índices de..."""
        return dict({
            "celular": input_alpha("Celular"),
            "email": input_alpha("Email:"),
            "red_social": input_alpha("Red Social:")
        })

    prompt_init = staticmethod(prompt_init)
