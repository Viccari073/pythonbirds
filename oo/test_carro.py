"""
Unittest
"""

from unittest import TestCase
from oo.carro import Motor


class CarroTestCase(TestCase):
    def teste_velocidade_inicial(self):  # Deve SEMPRE começar com o prefixo test.
        motor = Motor()
        self.assertEqual(0, motor.velocidade)     # Método herdado da classe TestCase.

    def teste_acelerar(self):
        motor = Motor()
        motor.acelerar()
        self.assertEqual(1, motor.velocidade)