# Método: função que pertence a uma classe e portanto, sempre está conectada a um objeto.


# OBS: self -> parametro que será um objeto a ser recebido. Não é uma palavra reservada (pode ser qlq coisa).

class Pessoa:  # Classe
    def __init__(self, nome=None, idade=35):  # Atributo de dado ou atributo de instância.
        self.idade = idade
        self.nome = nome  # Está passando para o atributo nome (self.nome) o parâmentro nome (nome=None)


    def cumprimentar(self):  # Método (atributo da classe)
        return f'Olá {id(self)}'


if __name__ == '__main__':
    p = Pessoa('Ricardo')  # Objeto 'p'
    print(Pessoa.cumprimentar(p))  # Forma não usual. Declara a classe, chama o método e define o parâmetro.
    print(id(p))
    print(p.cumprimentar())  # chamando o método a partir do objeto
    print(p.nome)
    p.nome = 'Lucas'
    print(p.nome)
    print(p.idade)
