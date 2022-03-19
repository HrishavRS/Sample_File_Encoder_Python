import os
import pickle

#This Encoding is done based on values from array saved in the pickle file.

pickle_in = open("datasets.pickle","rb")
this_array = pickle.load(pickle_in)

#The below function reverses the encoding procedure
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

#the below function is the black mamba, THE ENCODER
#writing in comments feels like being a ghost-guide, Even the words a grey.
def convertor(filename):
	final_array = []
	for item in list(filename):
		for index in this_array:
			if(item == index[0]):
				final_array.append(index[1])
				concat_form = ''.join(map(str,final_array))
	return concat_form


#You can use this to encode your files just like i tried below
# files_in_current_Dir = os.listdir()
# print(files_in_current_Dir)
# encoded_files = []
# for i in files_in_current_Dir:
# 	x = convertor(i)
# 	os.rename(i,x)

# reverted_files=[]

test = 27121890678020751415237525152175111415237580152375902072197564151455751915756715156475122193117555149315649014677975271219157534756415147220751114152375238025752515217571185575211990146775208090197525152175192021169064759064901520

y = revertor(x)
print(y)