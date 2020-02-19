from display import *
from draw import *
from matrix import *

screen = new_screen()
color = [ 0, 255, 0 ]
matrix = []
#Testing add_edge
add_edge(matrix,0,4.96,1.234,-4.214,-2.498,0.693)
#Testing print_matrix
print_matrix(matrix)

draw_lines( matrix, screen, color )
display(screen)
