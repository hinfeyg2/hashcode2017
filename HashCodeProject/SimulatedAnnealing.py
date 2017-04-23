from . import HashCodeUtils
from random import random

def SimulatedAnnealing(inputFile):
	"""This is taken from link provided by Anthony Ventresque:
	http://katrinaeg.com/simulated-annealing.html"""

	# init the class that lets us test the function.
	util = HashCodeUtils(inputFile)

	# generate a random solution and get its cost.
	solution = util.generateRandomSolution()
	old_cost = (-1 * util.fitnessScore(solution))
	T = 1.0
	T_min = 0.00001
	alpha = 0.9

	while T > T_min:
		i = 1
		while i <= 100:
			new_solution = util.addMutation(solution)
			new_cost = (-1 * util.fitnessScore(new_solution))
			ap = util.acceptanceProbability(old_cost, new_cost, T)
			# print(ap)
			if ap > random():
				solution = new_solution
				old_cost = new_cost
			i += 1
		T = T*alpha
	return abs(old_cost), new_solution