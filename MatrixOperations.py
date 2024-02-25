#The purpose of this python library will be to compute linear equations into a matrix
#It will take in n equations with n variables and will convert them to a matrix as long as they have the same elements
#It can also turn linear equations into their standard form through algebraic operations
#It will take in equations as strings, and output arrays/matrices
#
#Authored by Christopher Kerslake
#kerslake.r.chris@gmail.com

#This function will allow a user to input a matrix, separated by commas in rows
#It will assume that variables are in order, with the constant at the end
#For example, it will assume you are inputting the coefficients for x, y, z, c in that order
#and then it will convert to a double array size dependant on the number of variables per line

#import Array module


#!/usr/bin/python3
def create_matrix ():
	matrix = [[1, 2, 3, 4],[2, 4, 6, 8]]
	matrix_add(matrix, 1, 0)
	print(matrix)
	matrix_sub(matrix, 0, 1)
	print(matrix)
	print(type(matrix))


#This function is used to add row n to row m within the given matrix
def matrix_add(matrix, n, m):
	a = 0
	for x in matrix[n]:
		matrix[m][a] = matrix[m][a] + matrix[n][a]
		a = a + 1

def matrix_sub(matrix, n, m):
	a = 0
	for x in matrix[n]:
		matrix[m][a] = matrix[m][a] - matrix[n][a]
		a = a + 1

create_matrix()
