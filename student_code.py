import common
class variables:
	counter=0

class Board:
	def __init__(self, s, cR, cC):
		self.sudoku = s
		self.currRow = cR
		self.currCol = cC

def Copy_Board(sudoku): return [row[:] for row in sudoku]

class Stack:
        def __init__(self):
                self.array = []
                self.size = 0
        def put(self, node):
                self.array.insert(0,node)
                self.size = self.size + 1
        def get(self):
                if(self.size == 0):
                        return None
                else:
                        self.size = self.size - 1
                        return self.array.pop(0)
        def empty(self):
                if(self.size == 0):
                        return True
                else:
                        return False

def get_initial_point(sudoku):
	initRow = 0
	initCol = 0
	while sudoku[initRow][initCol] != 0:
		if initCol < 8:
			initCol +=1 
		else: 
			if initRow < 8:
				initRow += 1
				initCol = 0
			else:
				return None
	return initRow, initCol

def get_next_square(currRow, currCol):
	#Set the next
	if currCol < 8:
		nexCol = currCol + 1
		nexRow = currRow
	else:
		nexRow = currRow + 1
		nexCol = 0
	return nexRow, nexCol

def StopCheck(sudoku):
	for row in range(9):
		for col in range(9):
			if sudoku[row][col] == 0:
				return False
	return True

def sudoku_backtracking(sudoku):
	variables.counter=0
	#Initialize the Stack
	stack = Stack();
	#Find where to start
	initRow, initCol = get_initial_point(sudoku)
	#Create the initial Board and add it to stack
	initBoard = Board(Copy_Board(sudoku),initRow,initCol)
	stack.put(initBoard)
	#Iterate for as long as the stack is full
	while not stack.empty():
		variables.counter+= 1
		#Get current information
		currBoard = stack.get()
		currRow = currBoard.currRow
		currCol = currBoard.currCol
		if currRow > 8 or currCol > 8:
			continue
		#Get the next point
		nexRow, nexCol = get_next_square(currRow, currCol)
		#If square is already filled, move forward
		if currBoard.sudoku[currRow][currCol] != 0:
			stack.put(Board(currBoard.sudoku, nexRow, nexCol))
		#If square is empty, look for which values to fill it
		for newLabel in range(1,10):
			if common.can_yx_be_z(currBoard.sudoku, currRow, currCol, newLabel):
				newB = Copy_Board(currBoard.sudoku)
				newB[currRow][currCol] = newLabel
				if StopCheck(newB): break
				stack.put(Board(newB, nexRow, nexCol))
		if StopCheck(newB): break
	for row in range(9):
		for col in range(9):
			sudoku[row][col] = newB[row][col]
	return variables.counter
####################################################################################################################
####################################################################################################################
'''
												FORWARD CHECKING ALG
'''
####################################################################################################################
####################################################################################################################
def Find_Possible_Entries(row, column, sudoku):
	returnArr = []
	if sudoku[row][column] != 0:
		return returnArr
	for num in range(1,10):
		if common.can_yx_be_z(sudoku, row, column, num):
			returnArr.append(num)
	if len(returnArr) == 0:
		return None
	return returnArr

def Generate_Forward_Tracker(sudoku):
	tracker = [[0 for x in range(9)] for x in range(9)]
	for row in range(9):
		for col in range(9):
			hold = Find_Possible_Entries(row,col,sudoku)
			if hold == None:
				return None
			tracker[row][col] = hold
	return tracker

def sudoku_forwardchecking(sudoku):
	variables.counter=0
	#Initialize the Stack
	stack = Stack();
	#Find where to start
	initRow, initCol = get_initial_point(sudoku)
	#Create the initial Board and add it to stack
	initBoard = Board(Copy_Board(sudoku),initRow,initCol)
	stack.put(initBoard)
	#Iterate for as long as the stack is full
	while not stack.empty():
		variables.counter += 1
		#Get current information
		currBoard = stack.get()
		currRow = currBoard.currRow
		currCol = currBoard.currCol
		if currRow > 8 or currCol > 8:
			continue
		#Get the next point
		nexRow, nexCol = get_next_square(currRow, currCol)
		#If square is already filled, move forward
		if currBoard.sudoku[currRow][currCol] != 0:
			stack.put(Board(currBoard.sudoku, nexRow, nexCol))
			continue
		#If square is empty, look for which values to fill it
		for newLabel in range(1,10):
			if common.can_yx_be_z(currBoard.sudoku, currRow, currCol  , newLabel):
				#Generate new Sudoku board
				newB = Copy_Board(currBoard.sudoku)
				newB[currRow][currCol] = newLabel
				#Check if the board is full
				if StopCheck(newB):
					finalBoard = newB
					break
				#Now use forward checking to see if this newLabel should be added to the stack
				newTracker = Generate_Forward_Tracker(newB)
				if newTracker == None:
					continue
				stack.put(Board(newB, nexRow, nexCol))
		if StopCheck(newB):
			break

	for row in range(9):
		for col in range(9):
			sudoku[row][col] = newB[row][col]
	return variables.counter
####################################################################################################################
####################################################################################################################
'''
												MRV ALG
'''
####################################################################################################################
####################################################################################################################
class MRV_Board:
	def __init__(self, s, cR, cC, t):
		self.sudoku = s
		self.currRow = cR
		self.currCol = cC
		self.List = t 

def get_domain(sudoku, currRow, currCol):
	returnArr = []
	for num in range(1,10):
		if common.can_yx_be_z(sudoku,currRow, currCol, num):
			returnArr.append(num)
	return returnArr

def find_mrv(sudoku):
	minVal = 10
	minRow = 0 
	minCol = 0
	finalList = []
	for row in range(9):
		for col in range(9):
			if sudoku[row][col] == 0:
				ds = get_domain(sudoku, row, col)
				if len(ds) < minVal:
					minVal = len(ds)
					minRow = row
					minCol = col
					finalList = ds
	return minRow, minCol, finalList

def sudoku_mrv(sudoku):
	variables.counter = 0
	#initialize the stack
	stack = Stack()
	#Find where to start
	initRow, initCol, initList = find_mrv(sudoku)
	initBoard = MRV_Board(sudoku, initRow, initCol, initList)
	stack.put(initBoard)
	while not stack.empty():
		variables.counter += 1
		#Get the next attempt
		currBoard = stack.get()
		currRow = currBoard.currRow
		currCol = currBoard.currCol
		for newLabel in currBoard.List:
			newB = Copy_Board(currBoard.sudoku)
			newB[currRow][currCol] = newLabel
			if StopCheck(newB):
				finalBoard = newB
				break
			#Now find new mrv to branch on
			nexRow, nexCol, nexList = find_mrv(newB)
			stack.put(MRV_Board(newB, nexRow, nexCol, nexList))
	for row in range(9):
		for col in range(9):
			sudoku[row][col] = finalBoard[row][col]
	return variables.counter












