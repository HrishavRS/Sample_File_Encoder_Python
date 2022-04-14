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

def convertor(filename):
	final_array = []
	for item in list(filename):
		for index in this_array:
			if(item == index[0]):
				final_array.append(index[1])
				concat_form = ''.join(map(str,final_array))
	return concat_form

def convertor_test(filename):
	counter=0
	for item in list(filename):
		for index in this_array:
			if(item == index[0]):
				counter+=1
	unknown_characters = len(list(filename))-counter			
	return unknown_characters