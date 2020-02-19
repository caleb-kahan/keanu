from display import *
from draw import *
from matrix import *

screen = new_screen()
color = [ 0, 255, 0 ]
m2 = []
print("Testing add_edge and print_matrix")
print("adding one edge")
add_edge(m2,0,4.96,1.234,-4.214,-2.498,0.693)
print_matrix(m2)
print("adding another edge")
add_edge(m2,0,4.96,66,4.214,-2.498,88)
print_matrix(m2)

print("testing indent")
ident(m2)
print_matrix(m2)



#draw_lines( m2, screen, color )
#display(screen)
