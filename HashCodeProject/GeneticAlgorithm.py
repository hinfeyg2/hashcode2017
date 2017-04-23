from . import HashCodeUtils
import random
import copy

def GeneticAlgorithm(inputFile):

	# init the class that lets us test the function.
	util = HashCodeUtils.HashCodeUtils(inputFile)

	# set util fitness score to use a cache.
	util.useCache = True
	
	# some global variables which tune the genetic algorithm

	# set the polulation size. amount of generations to breed will be a percentage of this.
	# should be no less than 50 or an error will occur
	populationSize = 100
	# currently 30% of population size.
	survivorsSize = int((populationSize/100) * 30)
	# the number of low qaulity results to add to the survivors.
	# currently 10%
	percentLowQualitySurvivor = int((populationSize/100) * 10)
	# how often to add mutations.
	percetageMutation = int((populationSize/100) * 10)
	# total number of generations.
	numberGenerations = 200

	# generate 50 random individuals to create a population in a list
	population = []

	# create a list of unique fitness results.
	# uniqueFitnessScores = []

	for i in range(populationSize):
		# generate a random solution
		individual = util.generateRandomSolution()
		# add that indivudual plus its score to the population.
		population.append([util.fitnessScore(individual), individual])
		# add just the score to the unique fitness list.
		# uniqueFitnessScores.append(population[i][0])
	# the the number of unique items in the fitness list
	# numUniqueFitnessScores = len(Counter(uniqueFitnessScores).keys())

	# to check the number of generations gone through.
	currentGeneration = 0

	# numUniqueFitnessScores > 1

	# run as man generations as there are population size.
	while currentGeneration < numberGenerations:
		
		# if its not the first iteration set population to the next generation.
		if currentGeneration != 0:
			population = next_generation

		# sort the polulation by its fitness.
		population = sorted(population, key=lambda x: (x[0]))

		# get a list of discarded solutions.
		leftovers = population[survivorsSize:]
		# get a list of choosen solutions.
		survivors = population[-survivorsSize:]

		# add some random entries too.
		# 10% of the population size here.
		for z in range(percentLowQualitySurvivor):
			survivors.append(leftovers[random.randint(1, len(leftovers) -1)])

		# print the sorted population
		next_generation = []

		# reinitialize the unique fitness core list. This will be checked after every generation.
		# uniqueFitnessScores = []

		while len(next_generation) < populationSize+1:
			# now randomly breed the survivors together until the population is restored

			# get a random index of a survivor.
			twoRandomIndexes = random.sample(range(0, len(survivors)-1), 2)
			A = survivors[twoRandomIndexes[0]]
			B = survivors[twoRandomIndexes[1]]

			# return the head and tail of two different random parents and put them together
			head = A[1][:len(A[1])//2]
			tail = B[1][len(B[1])//2:]
			result = head + tail

			###### ADD MUTATION
			if random.randint(0, populationSize) < percetageMutation:
				result = util.addMutation(result)

			# temp = random.choice(result)
			# print(random.choice(temp))
			# if not illegal add to next_generation.
			if util.underMaxSize(result):
				score = util.fitnessScore(result)
				next_generation.append([score, result])

				# append to a list of scores only
				# uniqueFitnessScores.append(score)

		# get number of unique results.
		# numUniqueFitnessScores = len(Counter(uniqueFitnessScores).keys())

		# sort the next generation.
		next_generation = sorted(next_generation, key=lambda x: (x[0]))

		# increment generation
		currentGeneration = currentGeneration + 1

	# return the best score in the list.
	return next_generation[-1]