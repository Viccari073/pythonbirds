"""
Criar uma classe carro, que vai possuir dois atributos compostos por outras duas classes:

1) Motor
2) Direção

O Motor deverá ter a responsabilidade de controlar a velocidade. Ele oferece os seguintes atributos:
1)Atributo de dado velocidade;
2) Método acelerar, que deverá incrementar a velocidade em uma unidade;
3) Método frear, que deverá decrementar a velocidade em duas unidades.

A direção terá a responsabilidade de controlar a direção. Ela oferece os seguintes atributos:
1) Valor de direção com valores possíveis: Norte, Sul, Leste, Oeste
2) Método girar_a_direita
3) Método girar_a_esquerda

  N
O  L
 S

Exemplo:
    # Testando Motor
    >>> motor = Motor()
    >>> motor.velocidade
    0
    >>> motor.acelerar()
    >>> motor.velocidade
    1
    >>> motor.acelerar()
    >>> motor.velocidade
    2
    >>> motor.acelerar()
    >>> motor.velocidade
    3
    >>> motor.frear()
    >>> motor.velocidade
    1
    >>> motor.frear()
    >>> motor.velocidade
    0

    # Testando direção
    >>> direcao = Direcao()
    >>> direcao.valor
    'Norte'
    >>> direcao.girar_a_direita
    >>> direcao.valor
    'Leste'
    >>> direcao.girar_a_direita
    >>> direcao.valor
    'Sul'
    >>> direcao.girar_a_direita
    >>> direcao.valor
    'Oeste'
    >>> direcao.girar_a_direita
    >>> direcao.valor
    'Norte'
    >>> direcao.girar_a_esquerda
    >>> direcao.valor
    'Oeste'
    >>> direcao.girar_a_esquerda
    >>> direcao.valor
    'Sul'
    >>> direcao.girar_a_esquerda
    >>> direcao.valor
    'Leste'
    >>> direcao.girar_a_esquerda
    >>> direcao.valor
    'Norte'
    >>> carro = Carro(direcao, motor)
    >>> carro.calcular_velocidade()
    0
    >>> carro.acelerar()
    >>> carro.calcular_velocidade()
    1
    >>> carro.acelerar()
    >>> carro.calcular_velocidade()
    2
    >>> carro.frear()
    >>> carro.calcular_velocidade()
    0
    >>> carro.calcular_direcao()
    'Norte'
    >>> carro.girar_a_direita()
    >>> carro.calcular_direcao()
    'Leste'
    >>> carro.girar_a_esquerda()
    >>> carro.calcular_direcao()
    'Norte'
    >>> carro.girar_a_direita()
    >>> carro.calcular_direcao()
    'Oeste'
"""


class Motor:
    def __init__(self, velocidade=0):  # Criando atributo velocidade
        self.velocidade = velocidade

    def acelerar(self):
        self.velocidade += 1

    def frear(self):
        if self.velocidade >= 2:
            self.velocidade -= 2
        elif self.velocidade == 1:
            self.velocidade -= 1
        else:
            self.velocidade == 0


class Direcao:
    def __init__(self, direcao='Norte'):
        self.valor = direcao

    def girar_a_direita(self):
        if self.direcao == 'Norte':
            self.valor = 'Leste'
        elif self.direcao == 'Leste':
            self.direcao = 'Sul'
        elif self.direcao == 'Sul':
            self.direcao = 'Oeste'
        elif self.direcao == 'Oeste':
            self.direcao = 'Norte'

    def girar_a_esquerda(self):
        if self.direcao == 'Norte':
            self.direcao = 'Oeste'
        elif self.direcao == 'Oeste':
            self.direcao = 'Sul'
        elif self.direcao == 'Sul':
            self.direcao = 'Leste'
        elif self.direcao == 'Leste':
            self.direcao = 'Norte'






