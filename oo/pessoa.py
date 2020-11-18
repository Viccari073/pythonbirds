# Método: função que pertence a uma classe e portanto, sempre está conectada a um objeto.


# OBS: self -> parametro que será um objeto a ser recebido. Não é uma palavra reservada (pode ser qlq coisa).

# ATENÇÃO: se o atributo for o mesmo para todos os objetos, o atributo será o de classe, se não, será um atributo de instância.

class Pessoa:  # Classe

    olhos = orelhas = 2  # Atributos de classe ou atributo default.
    boca = nariz = 1

    def __init__(self, *filhos, nome=None, idade=70):  # Atributo de dado ou atributo de instância.
        self.idade = idade
        self.nome = nome  # Está passando para o atributo nome (self.nome) o parâmentro nome (nome=None)
        self.filhos = list(filhos)  # objeto complexo

    def cumprimentar(self):  # Método de instância (atributo da classe)
        return f'Olá, meu nome é: {self.nome}'

    @staticmethod  # Decorator
    def metodo_estatico():  # Método de classe
        return 42

    @classmethod
    def nome_e_atributos_de_classe(cls):  # como utilizo o cls, eu posso acessar os atributos de classe da classe Pessoa
        return f'{cls} - Olhos: {cls.olhos}, Orelhas: {cls.orelhas}, Nariz: {cls.nariz}, Boca: {cls.boca}'


class Homem(Pessoa):  # A classe homem (filha) herdará todos os atributos da class pai (Pessoa). Polimorfismo através da herança
    def cumprimentar(self):  # sobrescrita de método
        cumprimentar_da_classe = super().cumprimentar()  # o método super acessa os elementos da classe pai de Homem, seja ela quer for!
        return f'{cumprimentar_da_classe}. Aperto de mão!'

class Mutante(Pessoa):
    olhos = 3  # SOBRESCRITA de atributo. Pq estamos sobrepondo o atritudo na classe Mutante em relação à calsse Pai Pessoa


if __name__ == '__main__':
    lucas = Mutante(nome='Lucas', idade=36)  # Objeto 'p'
    carol = Pessoa(nome='Carol', idade=40)
    ricardo = Homem(lucas, carol, nome='Ricardo')
    print(Pessoa.cumprimentar(ricardo))  # Forma não usual. Declara a classe, chama o método e define o parâmetro.
    print(id(ricardo))
    print(ricardo.cumprimentar())  # chamando o método a partir do objeto
    print(ricardo.nome)
    print(ricardo.idade)
    for filhos in ricardo.filhos:
        print(filhos.nome, filhos.idade)
    print(ricardo.filhos)
    del ricardo.filhos  # Removendo um atriburo dinamicamente
    ricardo.olhos = 1  # altera o atributo do objeto, mas não da classe
    del ricardo.olhos  # deleta o atributo do objeto, mas não ca classe
    lucas.sobrenome = 'Viccari'  # atributo dinâmico
    print(lucas.__dict__)  # atributo especial. o 'dunder dict' contem os atribuots de instância.
    print(ricardo.__dict__)
#    Pessoa.olhos = 3  # altera o valor do atributo para todos os objetos da classe
    print(Pessoa.olhos)
    print(ricardo.olhos)
    print(lucas.olhos)
    print(id(Pessoa.olhos), id(ricardo.olhos), id(lucas.olhos))
    print(Pessoa.metodo_estatico(), lucas.metodo_estatico())
    print(Pessoa.nome_e_atributos_de_classe(), lucas.nome_e_atributos_de_classe())
    pessoa = Pessoa('Anômino')  # pessoa <- objeto (variável). Pessoa <- classe
    print(isinstance(pessoa, Pessoa))  # serve pra perguntar se um objeto é de determinada classe (objeto, classe). Resposta em bolleano.
    print(isinstance(pessoa, Homem))
    print(isinstance(lucas, Pessoa))
    print(isinstance(lucas, Homem))
    print(lucas.olhos)  # está buscando a informação na classe Mutante.
    print(lucas.cumprimentar())
    print(ricardo.cumprimentar())
