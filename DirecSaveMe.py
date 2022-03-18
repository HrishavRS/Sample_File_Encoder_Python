import os

this_array = [["a",71],["b",82],["c",93],["d",64],["e",55],["f",73],["g",67],["h",80],["i",90],["j",10],["k",11],["l",12],["m",13],["n",14],["o",15],["p",16],["q",17],["r",18],["s",19],["t",20],["u",21],["v",22],["w",23],["x",24],["y",25],["z",26],[".",79],["A",27],["B",28],["C",29],["D",74],["E",30],["F",31],["G",32],["H",33],["I",34],["J",35],["K",36],["L",37],["M",38],["N",39],["O",40],["P",41],["Q",42],["R",43],["S",44],["T",45],["U",46],["V",47],["W",48],["X",49],["Y",50],["Z",51],['0',88],['1',70],['2',60],['3',94],['4',95],['5',96],['6',97],['7',98],['8',99],['9',89],['_',83],[' ',75]]

def revertor(encod):
	encod = str(encod)
	numbers_in_2_groups=[]
	def number_grouper_for_revertor(file):
		for i in range(0,len(list(file))):
			if(i%2 == 0):
				item = list(file)[i]+list(file)[i+1]
				numbers_in_2_groups.append(item)
		return numbers_in_2_groups		
	number_grouper_for_revertor(encod)

	final_reverted_item=[]
	for i in numbers_in_2_groups:
		for item in this_array:
			if(item[1] == int(i)):
				final_reverted_item.append(item[0])

	final_reverted_item = ''.join(map(str,final_reverted_item))			
	return(final_reverted_item)

def convertor(filename):
	final_array = []
	for item in list(filename):
		for index in this_array:
			if(item == index[0]):
				final_array.append(index[1])
				concat_form = ''.join(map(str,final_array))
	return concat_form

# files_in_current_Dir = os.listdir()
# print(files_in_current_Dir)
# encoded_files = []
# for i in files_in_current_Dir:
# 	x = convertor(i)
# 	os.rename(i,x)

# reverted_files=[]
y = revertor(749018559344712255791625)
print(y)
# os.rename(7490185593447122553855791625,y)