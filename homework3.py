# Implement the starts_with() function taking two strings and returning true if the first argument starts with the second one.


# def starts_with(string1,string2):
# 	if string1.startswith(string2):
# 		print("The string1 starts with the string2.")
# 	else:
# 		print("The string1 does not start with the string2. ")
# string1 = "Welcome to Armenia"
# string2 = "Welcome"
# starts_with(string1,string2)




# Implement the ends_with() function taking two strings and returning true if the first argument ends with the second one.



# def ends_with(str1,str2):
# 	if str1.endswith(str2):
# 		print("True")
# 	else:
# 		print("False")
# str1 = "Picsart!"
# str2 = "!"
# ends_with(str1,str2)




# Implement the swap_strings() function taking two strings and swapping their values.



# def swap_strings(str1,str2):
# 	return str2,str1
# str1 = "Nvard"
# str2 = "Nalbandyan"
# str1,str2 = swap_strings(str1,str2)
# print("str1:",str1)
# print("str2:",str2)




# Implement the find_last_not_of() function taking a string and a character sequence as its arguments. The function returns the last character equal to none of the characters in the given character sequence.

def find_last_not_of(string,characters):
	for i in range(len(string)-1,-1,-1):
		if string[i] not in characters:
			return string[i]
	return None
input_string = input("Enter the string: ")
character_sequence = input("Enter a character sequence: ")
result = find_last_not_of(input_string,character_sequence)
if result is not None:
	print("Last character not in sequence:",result)
else:
	print("All characters are in sequence")











# Implement the convert_to_int() function taking a string argument and returning its integer representation. Throw an exception if the conversion is not possible.


# def convert_to_int(s):
# 	try:
# 		return int(s)
# 	except ValueError:
# 		raise Exception("Conversion Failed")
# s = input("Enter string")
# print(convert_to_int(s))




# Implement the rotate_by() function taking an integer array and a number as its arguments. The function returns the array rotated by the specified number of positions (given by the second argument).



# def reverse_array(array,start,end):
# 	while start < end:
# 		array[start],array[end] = array[end],array[start]
# 		start += 1
# 		end -= 1
# def rotate_by(arr,num):
# 	lenght = len(arr)
# 	if num == 0:
# 		return arr
# 	reverse_array(arr,0,lenght-1)
# 	reverse_array(arr,0,num-1)
# 	reverse_array(arr,num,lenght-1)
# 	return arr
# lst = [1,2,3,4,5]
# print(rotate_by(lst,2))	



