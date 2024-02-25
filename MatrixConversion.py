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
	matrix_operation_test(matrix)
	print(matrix)
	print(type(matrix))

def matrix_operation_test(matrix):
	x = 0
	for a in matrix:
		y = 0
		for b in matrix[x]:
			print(matrix[x][y])
			y = y + 1
		x = x + 1
create_matrix()
