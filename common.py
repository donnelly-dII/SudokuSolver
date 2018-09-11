class constants:
	NONE = 0
	X = 1
	O = 2

class variables:
	explored=0
	
def print_sudoku(sudoku):
	print()
	for y in range(9):
		v=""
		for x in range(9):
			v+=str(sudoku[y][x]);
		printf(v)

def can_yx_be_z(sudoku, y, x, z):
	for i in range(9):
		if (sudoku[y][i]==z):
			return False
		if (sudoku[i][x]==z):
			return False
		if(sudoku[(y/3)*3+i/3][(x/3)*3+i%3]==z): 
			return False
	return True
		
def init_sudoku():
	return [[0 for x in range(9)] for x in range(9)]

def set_sudoku(sudoku, data):
	for y in range(9):
		for x in range(9):
			sudoku[y][x]=int(data[y*9+x])
