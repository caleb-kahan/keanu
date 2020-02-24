from display import *
from draw import *
from matrix import *
import copy
import random

screen = new_screen()
color = [ 0, 255, 0 ]
m2 = []
print("m2: Testing add_edge and print_matrix")
print("m2: adding one edge (4,8,12) and (5,10,15)")
add_edge(m2,4,8,12,5,10,15)
print_matrix(m2)
print("m2: adding a point (3,6,9)")
add_point(m2,3,6,9)
print_matrix(m2)
print("m2: adding a point (2,2,2)")
add_point(m2,2,2,2)
print_matrix(m2)

m1 = new_matrix()
print("m1:testing indent")
ident(m1)
print_matrix(m1)

print("Testing m1 X m2")
matrix_mult(m1,m2)
print_matrix(m2)

m1 = new_matrix()
m1[0] = [1,2,3,1]
m1[1] = [3,2,1,1]
m1.pop()
m1.pop()
print("m1 reset")
print_matrix(m1)
print("testing m2 X m1")
matrix_mult(m2,m1)
print_matrix(m1)

eight_matrix = [[-1,2,0,1],[1,2,0,1],[1,2,0,1],[1,0,0,1],[1,0,0,1],[1,-2,0,1],[1,-2,0,1],
[-1,-2,0,1],[-1,-2,0,1],[-1,0,0,1],[-1,0,0,1],[-1,2,0,1],[-1,0,0,1],[1,0,0,1]]
nine_matrix = copy.deepcopy(eight_matrix)
nine_matrix.remove([1,-2,0,1])
nine_matrix.remove([-1,-2,0,1])
nine_matrix.remove([-1,-2,0,1])
nine_matrix.remove([-1,0,0,1])
four_matrix = copy.deepcopy(nine_matrix)
four_matrix.remove([-1,2,0,1])
four_matrix.remove([1,2,0,1])
six_matrix = copy.deepcopy(eight_matrix)
six_matrix.pop(2)
six_matrix.pop(2)
five_matrix = copy.deepcopy(six_matrix)
five_matrix.pop(-5)
five_matrix.pop(-5)
three_matrix = copy.deepcopy(eight_matrix)
three_matrix.pop(-3)
three_matrix.pop(-3)
three_matrix.pop(-3)
three_matrix.pop(-3)
seven_matrix = copy.deepcopy(three_matrix)
seven_matrix.pop(-1)
seven_matrix.pop(-1)
seven_matrix.pop(-1)
seven_matrix.pop(-1)
one_matrix = copy.deepcopy(seven_matrix)
one_matrix.pop(0)
one_matrix.pop(0)
zero_matrix = copy.deepcopy(eight_matrix)
zero_matrix.pop()
zero_matrix.pop()
two_matrix = copy.deepcopy(eight_matrix)
two_matrix.pop(-3)
two_matrix.pop(-3)
two_matrix.pop(4)
two_matrix.pop(4)

def index_to_matrix(index):
    switcher = {
        0: zero_matrix,
        1: one_matrix,
        2: two_matrix,
        3: three_matrix,
        4: four_matrix,
        5: five_matrix,
        6: six_matrix,
        7: seven_matrix,
        8: eight_matrix,
        9: nine_matrix
    }
    matrix = switcher.get(index)
    return copy.deepcopy(matrix)

displayMatrix = [[0,0,0,1],[0,0,0,1]]

for x in range(0,len(screen[0]),6):
    if(x%20>random.randint(1,3)):
        listNumbers = [1,1,1,1,1,1,1,1,1,1]
        y=len(screen)
        while(sum(listNumbers)):
            for i in range(10):
                if listNumbers[i]:
                    examp = index_to_matrix(i)
                    translate_matrix(examp,x,y)
                    matrix_add(displayMatrix,examp)
                    if random.randint(1,10)<3:
                        listNumbers[i]=0
                    y-=random.randint(3,7)
            y-=4

draw_lines( displayMatrix, screen, color )
display(screen)
