# utils.py
# Math library
# Author: Sébastien Combéfis
# Version: February 8, 2018

from math import sqrt
import scipy.integrate


def fact(n):
	"""Computes the factorial of a natural number.
	
	Pre: -
	Post: Returns the factorial of 'n'.
	Throws: ValueError if n < 0
	"""
	if n == 0:
		return 1
	
	return fact(n-1) * n

def roots(a, b, c):
	"""Computes the roots of the ax^2 + bx + x = 0 polynomial.
	
	Pre: -
	Post: Returns a tuple with zero, one or two elements corresponding
		to the roots of the ax^2 + bx + c polynomial.
	"""

	# Calcul the delta
	d_delta = b**2 - 4*a*c

	#Return in function of the delta
	if d_delta < 0:
		return ()
	elif d_delta == 0:
		return ((-b) / (2 * a))
	else:
		x_1 = ((-b + sqrt(d_delta)) /(2 * a))
		x_2 = ((-b - sqrt(d_delta)) / (2 * a))
		return (x_1, x_2)

def integrate(function, lower, upper):
	"""Approximates the integral of a fonction between two bounds
	
	Pre: 'function' is a valid Python expression with x as a variable,
		'lower' <= 'upper',
		'function' continuous and integrable between 'lower‘ and 'upper'.
	Post: Returns an approximation of the integral from 'lower' to 'upper'
		of the specified 'function'.

	Hint: You can use the 'integrate' function of the module 'scipy' and
		you'll probably need the 'eval' function to evaluate the function
		to integrate given as a string.
	"""
	func = lambda x:eval(function)

	return scipy.integrate.quad(func, lower, upper)[0]

if __name__ == '__main__':
	print(fact(5))
	print(roots(1, 0, 1))
	print(integrate('x ** 2 - 1', -1, 1))
