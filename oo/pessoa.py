class Pessoa:
    def __init__(self, nome=None, idade=35):
        self.idade = idade
        self.nome = nome
    def cumprimentar(self):
        return f'olá {id(self)}'


if __name__=='__main__':
    p = Pessoa('1sales1')
    print(Pessoa.cumprimentar(p))
    print(id(p))
    print(p.cumprimentar())
    print(p.nome)
    p.nome = 'Ramon'
    print(p.nome)
    print(p.idade)