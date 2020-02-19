"""
A matrix will be an N sized list of 4 element lists.
Each individual list will represent an [x, y, z, 1] point.
For multiplication purposes, consider the lists like so:
x0  x1      xn
y0  y1      yn
z0  z1  ... zn
1  1        1
"""
import math

#print the matrix such that it looks like
#the template in the top comment
def print_matrix( matrix ):
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            print(str(matrix[i][j])+" ")
        print("\n")

#turn the paramter matrix into an identity matrix
#you may assume matrix is square
def ident( matrix ):
    for i in range(len(matrix)):
        matrix[i][i] = 1

#multiply m1 by m2, modifying m2 to be the product
#m1 * m2 -> m2
def matrix_mult( m1, m2 ):
    #Condiitons to multiply
    if len(m1) != len(m2[0]):
        return;
    m2Clone = copy.deepcopy(m2)
    for rowM1 in range(len(m1[0])):
        list = []
        for colM1 in range(len(m1)):
            list.append(m1[colM1][rowM1])
        for colM2 in range(len(m2Clone)):
            m2[colM2][rowM1]  = list_mult(m2Clone[colM2],list)

def list_mult(l1,l2):
    sum = 0
    for i in range(len(l1)):
        sum+=(l1*l2)
    return sum


def new_matrix(rows = 4, cols = 4):
    m = []
    for c in range( cols ):
        m.append( [] )
        for r in range( rows ):
            m[c].append( 0 )
    return m
