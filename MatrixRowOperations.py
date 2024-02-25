#The purpose of the following functions is to perform simple matrix operations on any given matrix
#Inputs are are:
#	A Matrix (Formatted as a list of lists with numbers inside)
#	A row which exists within the matrix to perform the operation on(starting from 0)
#	A row to perform the operation using (add/subtract USING which row)
#	A constant to multiply/divide the row by (scale by a factor of what)
#
#Authored by Christopher Kerslake
#kerslake.r.chris@gmail.com

#!/usr/bin/python3


#This function is used to add row n to row m within the given matrix
#Takes in a Matrix (list of lists), a row number to perform the operation ON (m), a row number to use for the operation (n)
def matrix_row_add(matrix, m, n):
	a = 0
	for x in matrix[n]:
		matrix[m][a] = matrix[m][a] + matrix[n][a]
		a = a + 1
	return matrix

#This function is used to subtract row n from row m within the given matrix
#Takes in a Matrix (list of lists), a row number to perform the operation ON (m), a row number to use for the operation (n)
def matrix_row_sub(matrix, m, n):
	a = 0
	for x in matrix[m]:
		matrix[m][a] = matrix[m][a] - matrix[n][a]
		a = a + 1
	return matrix

#This function is used to multiply row m within the given matrix by c
#Takes in a Matrix (list of lists), a row number to perform the operation ON (m), a constant to multiply the row by (c)
def matrix_row_multiply(matrix, m, c):
	a = 0
	for x in matrix[m]:
		matrix[m][a] = matrix[m][a] * c
		a = a + 1
	return matrix

#This function is used to divide row m within the given matrix by c
#Takes in a Matrix (list of lists), a row number to perform the operation ON (m), a constant to divide the row by (c)
def matrix_row_divide(matrix, m, c):
	a = 0
	for x in matrix[m]:
		matrix[m][a] = matrix[m][a] / c
		a = a + 1
	return matrix

#*****This Concludes Simple Row Operations within Matrices*****#
#*****Use these basic operations to solve simple Matrices *****#
