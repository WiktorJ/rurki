from MatrixCreator import MatrixCreator
import sympy as sy


__author__ = 'Wiktor'

# input file looks like this:
# 1 - number of factors
# 2 .. number of factors +1 = n - factors
# right hand side value of equation
# n+1 - u0 condition
# n+2 - u0 type : d - >Dirichlet, n -> Neumann
# n+3 - un conditiony
# n+4 - un type : d - >Dirichlet, n -> Neumann
# n+5 - number of equation
# n+6 - a
# n+7 - b

def transform_matrix_to_row_echelon_form():
    for i in range(0, equationNumbers-1):
        tmp = matrix[i][1]
        for j in range(1, n):
            matrix[i][j] = matrix[i][j] / tmp
        bmatrix[i] = bmatrix[i]/tmp
        tmp = matrix[i+1][0]
        for j in range(0, n-1):
            matrix[i+1][j] = matrix[i+1][j] - tmp*matrix[i][j+1]
        bmatrix[i+1] = bmatrix[i+1] - bmatrix[i]*tmp
    bmatrix[equationNumbers-1] = bmatrix[equationNumbers - 1]/matrix[equationNumbers-1][1]
    matrix[equationNumbers-1][1] = matrix[equationNumbers - 1][1]/matrix[equationNumbers-1][1]


def solve_linear_equations():
    prev = prev2 = 0
    h1 = sy.Symbol('h')
    r = (b-a)/equationNumbers
    # print " as: ", bmatrix[1].subs(h1, 1)
    for i in reversed(range(int(equationNumbers))):
        print 'u' + `i`, ' = ', bmatrix[i] - prev * matrix[i][2], " = ", bmatrix[i].subs(h1, r) - prev2 * matrix[i][2]
        prev = bmatrix[i] - prev * matrix[i][2]
        prev2 = bmatrix[i].subs(h1, r) - prev2 * matrix[i][2]

f = open('input.txt', 'r')
n = int(f.readline())
factors = []
for x in range(0, int(n)):
    factors.append(f.readline())
rhsv = float(f.readline())
u0 = float(f.readline())
u0Type = f.readline()
un = float(f.readline())
unType = f.readline()
equationNumbers = int(f.readline())
a = float(f.readline())
b = float(f.readline())

creator = MatrixCreator(n, factors, rhsv, u0, u0Type, un, unType, equationNumbers)
matrix = creator.matrix
bmatrix = creator.bmatrix
transform_matrix_to_row_echelon_form()
# print matrix
# for i in range(0, equationNumbers):
#     print bmatrix[i]
solve_linear_equations()



