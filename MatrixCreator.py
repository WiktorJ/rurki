import numpy as np
import sympy as sy
from sympy import *

class MatrixCreator:

    def __init__(self, n, factors, rhsv, u0, u0Type, un, unType, equationNumber):
        self.n = n
        self.factors = factors
        self.rhsv = rhsv
        self.u0 = u0
        self.u0Type = u0Type
        self.un = un
        self.unType = unType
        self.equationNumber = equationNumber
        self.matrix = np.zeros(shape=(equationNumber, n))
        self.bmatrix = sy.zeros(equationNumber, 1)
        self.createMatrix()

    def createMatrix(self):
        self.factors = [float(i) for i in self.factors]
        h = sy.Symbol('h')
        h2 = sy.Symbol('h^2')
        self.bmatrix[0] = self.u0 * h
        self.bmatrix[self.equationNumber-1] = self.un * h
        if self.u0Type == 'd\n':
            self.matrix[0] = [0, 1, 0]
        else:
            self.matrix[0] = [0, -1, 1]

        if self.unType == "d\n":
            self.matrix[self.equationNumber-1] = [0, 1, 0]
        else:
            self.matrix[self.equationNumber-1] = [-1, 1, 0]
        for i in range(1, self.equationNumber-1):
            self.matrix[i] = self.factors
            self.bmatrix[i] = self.rhsv * h2