from display import *
from draw import *
from matrix import *

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



#draw_lines( m2, screen, color )
#display(screen)
