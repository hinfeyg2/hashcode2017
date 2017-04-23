from . import HashCodeUtils
import random
import copy

def HillClimbing(inputFile):

	# init the class that lets us test the function.
	util = HashCodeUtils.HashCodeUtils(inputFile)

	# create a place to store the current best answer.
	finalSolution = [0, []]

	# set the number of times to restart the algorithm to restart the algorithm.
	numberJumps = 2

	# loop through each jump.
	for i in range(numberJumps):

		# generate a random solution.
		initSolution = util.generateRandomSolution()

		# turn that solution into a matrix of numbers.
		initSolutionMatrix = util.convertToMatrix(initSolution)
		# create a copy of that solution.
		initSolutionMatrixTest = [0, []]
		initSolutionMatrixTest[1] = initSolutionMatrix.copy()
	
		# count the number of videos and multiply them by the number of caches.
		count = len(initSolutionMatrixTest[1][0]) * len(initSolutionMatrixTest[1])
		# create a variable to hold the overall score.
		overall_score = 0

		# create a counter for the while loop.
		z = 0
		while z < count:

			# create a variable for the score of this iteration.
			score = [0, []]

			# look though each video position in the current solution.
			for i in range(len(initSolutionMatrix)):
				for j in range(len(initSolutionMatrix[i])):

					# flip the bit of the current video position
					initSolutionMatrixTest[1][i][j] ^= 1

					# get the score with the modified bit.
					currentScore = util.fitnessScore(util.convertToSolution(initSolutionMatrixTest[1]))
					
					# if the score is better than the best score of this iteration
					# replace it and keep a note of the solution.
					if score[0] < currentScore:
						score[0] = currentScore
						score[1] = [i, j]

					# flip the bit back.
					initSolutionMatrixTest[1][i][j] ^= 1

			# update the matrix with only best score in the iteration.
			initSolutionMatrixTest[1][score[1][0]][score[1][1]] ^= 1
			initSolutionMatrixTest[0] = score[0]
			# increment the while loop counter.
			z = z + 1

		# if this hill climb is the best so far then keep it.
		if finalSolution[0] < initSolutionMatrixTest[0]:
			finalSolution[0] = initSolutionMatrixTest[0]
			finalSolution[1] = util.convertToSolution(initSolutionMatrixTest[1])

	# return the best answer after all jumps.
	return finalSolution

if __name__ == "__main__":
	print("dogs")
