import common
import student_code
import time

class bcolors:
	RED    = "\x1b[31m"
	GREEN  = "\x1b[32m"
	NORMAL = "\x1b[0m"

def check_result(sudoku, show):
	result=True
	for y in range(9):
		v=""
		for x in range(9):
			value = sudoku[y][x];
			sudoku[y][x]=0
			if (value!=0 and common.can_yx_be_z(sudoku,y,x,value)):
				v+=bcolors.GREEN
			else:
				result = False
				v+=bcolors.RED
			v+=str(value)
			sudoku[y][x]=value
		if (show):
			print(v)
	return result

	
def run_experiment(data, btlimit, fclimit, mrvlimit):
	result=True
    
	sudoku = common.init_sudoku();
	common.set_sudoku(sudoku, data);
	bt1 = student_code.sudoku_backtracking(sudoku);
	if ( not check_result(sudoku,False)):
		print("Backtracking results: "+bcolors.RED+"FAIL"+bcolors.NORMAL)
		check_result(sudoku,True);
		result=False;
	else:
		print("Backtracking results: "+bcolors.GREEN+"SUCCESS"+bcolors.NORMAL)

	if (bt1>btlimit):
		print("Backtracking count: "+str(bt1) +"("+bcolors.RED+"FAIL"+bcolors.NORMAL+")")
		result=False
	else:
		print("Backtracking count: "+str(bt1) +"("+bcolors.GREEN+"SUCCESS"+bcolors.NORMAL+")")

	common.set_sudoku(sudoku, data)
	fc1 = student_code.sudoku_forwardchecking(sudoku)
	if (not check_result(sudoku,False)):
		print("Forwardchecking results: "+bcolors.RED+"FAIL"+bcolors.NORMAL)
		check_result(sudoku,True)
		result=False
	else:
		print("Forwardchecking results: "+bcolors.GREEN+"SUCCESS"+bcolors.NORMAL)

	if (fc1>fclimit):
		print("Forwardchecking count: "+str(fc1) +"("+bcolors.RED+"FAIL"+bcolors.NORMAL+")")
		result=False;
	else:
		print("Forwardchecking count: "+str(fc1) +"("+bcolors.GREEN+"SUCCESS"+bcolors.NORMAL+")")

	common.set_sudoku(sudoku, data);
	mrv1 = student_code.sudoku_mrv(sudoku);
	if (not check_result(sudoku,True)):
		print("MRV results: "+bcolors.RED+"FAIL"+bcolors.NORMAL)
		check_result(sudoku,True)
		result=False
	else:
		print("MRV results: "+bcolors.GREEN+"SUCCESS"+bcolors.NORMAL)
		
	if (mrv1>mrvlimit):
		print("MRV count: "+str(mrv1) +"("+bcolors.RED+"FAIL"+bcolors.NORMAL+")")
		result=False;
	else:
		print("MRV count: "+str(mrv1) +"("+bcolors.GREEN+"SUCCESS"+bcolors.NORMAL+")")

	return result



data1 = ("900670000"
"006800470"
"800010003"
"003000001"
"005406900"
"600000300"
"300060008"
"068005200"
"000082006")

data2 = ("006100050"
"200605008"
"000090002"
"000019300"
"002000800"
"003570000"
"900040000"
"800301009"
"040006100")

data3 = ("530070000"
"600195000"
"098000060"
"800060003"
"400803001"
"700020006"
"060000280"
"000419005"
"000080079")

data4 = ("009000400"
"600400020"
"840031090"
"008007041"
"500060003"
"160800700"
"070290065"
"020005004"
"005000900")

data5 = ("700008120"
"000090300"
"004005009"
"600030400"
"000010000"
"009080006"
"100900500"
"007060000"
"048700003")



start_time = time.time()
print ("Board 1")
exp1 = run_experiment(data1, 35000, 4000, 2500)
print ("Board 2")
exp2 = run_experiment(data2, 200000, 30000, 3500)
print ("Board 3")
exp3 = run_experiment(data3, 40000, 4500, 300)
print ("Board 4")
exp4 = run_experiment(data4, 6000, 800, 650)
print ("Board TEST")
exp4 = run_experiment(data5, 20000, 20000, 6500)
print("--- %s seconds ---" % (time.time() - start_time))

all_passed = exp1 and exp2 and exp3 and exp4 


