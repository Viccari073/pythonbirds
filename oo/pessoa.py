# Método: função que pertence a uma classe e portanto, sempre está conectada a um objeto.


# OBS: self -> parametro que será um objeto a ser recebido. Não é uma palavra reservada (pode ser qlq coisa).

class Pessoa:  # Classe
    def cumprimentar(self):  # Método.
        return f'Olá {id(self)}'


if __name__ == '__main__':
    p = Pessoa()  # Objeto 'p'
    print(Pessoa.cumprimentar(p))  # Forma não usual. Declara a classe, chama o método e define o parâmetro.
    print(id(p))
    print(p.cumprimentar())  # chamando o método a partir do objeto
