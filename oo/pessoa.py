# Método: função que pertence a uma classe e portanto, sempre está conectada a um objeto.


# OBS: self -> parametro que será um objeto a ser recebido. Não é uma palavra reservada (pode ser qlq coisa).

class Pessoa:  # Classe
    def __init__(self, *filhos, nome=None, idade=35) -> object:  # Atributo de dado ou atributo de instância.
        self.idade = idade
        self.nome = nome  # Está passando para o atributo nome (self.nome) o parâmentro nome (nome=None)
        self.filhos = list(filhos)  # objeto complexo

    def cumprimentar(self):  # Método (atributo da classe)
        return f'Olá {id(self)}'


if __name__ == '__main__':
    lucas = Pessoa(nome='Lucas')  # Objeto 'p'
    ricardo = Pessoa(lucas, nome='Ricardo')
    print(Pessoa.cumprimentar(ricardo))  # Forma não usual. Declara a classe, chama o método e define o parâmetro.
    print(id(ricardo))
    print(ricardo.cumprimentar())  # chamando o método a partir do objeto
    print(ricardo.nome)
    print(ricardo.idade)
    for filhos in ricardo.filhos:
        print(filhos.nome)
    print(ricardo.filhos)
