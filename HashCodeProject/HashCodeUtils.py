from . import ReadGoogle
import random
import copy
import math


class HashCodeUtils:

	def __init__(self, inputFile):
		self.data = ReadGoogle.ReadGoogle(inputFile)
		self.fitnessCache = []
		self.useCache = False

	def fitnessScore(self, solution):

		# check to see if the input solution is in the fitness cache
		if self.useCache:
			for f in range(len(self.fitnessCache)):
				# if it is return the previously calculated result.
				if solution == self.fitnessCache[f][0]:
					return self.fitnessCache[f][1]

		#Checks if cache is under max size.
		if not self.underMaxSize(solution):
			return 0

		# video_ed_request returns (vid number, endpoint): number of requests
		video_ed_request = self.data["video_ed_request"]
		totalCalcTop = 0
		totalCalcBottom = 0

		# print(data["video_ed_request"])
		# print(data["video_ed_request"])
		# iterate over all the vidnumber to endpoint connections.
		for x in self.data["video_ed_request"]:
			# dictionary that does something.
			foundAt = {}
			# a list to hold something.
			availableCachedSolution = []
			# another temp list.
			temp = []
			# boolean thing
			inCache = False

			# ed_cache_list is a list of lists. each list represents an endpoint. list content represents a cache connection.
			# iterate over the endpoints. add used 
			# create a temp list of connections to the endpoints.
			for a in self.data["ed_cache_list"][int(x[1])]:
				temp.append(int(a))
			
			# sort the temp list of connections
			temp.sort()

			# get available caches in solution for current vidnumber to endpoint connections.
			for b in temp:
				availableCachedSolution.append(solution[int(b)])

			# for solutions in available caches
			for i in availableCachedSolution:
				for j in i:
					# int(x[0] is a vidnumber in this cache to endpoint conection.
					if j == int(x[0]):
						# get the latency for that vid for the current cache to endpoint connection.
						foundAt[int(self.data["ep_to_cache_latency"][int(x[1])][availableCachedSolution.index(i)])] = availableCachedSolution.index(i)
						# set inCache boolean to true.
						inCache = True

			# if the video is in a cache in the solution and if the latency does not read 501 (which means its not in a cache.)
			if inCache and int(self.data["ep_to_cache_latency"][int(x[1])][availableCachedSolution.index(i)]) != int("501"):
				# get the latency to cache for the current video. Make sure its the minimum latency if there are options.
				latency_to_cache = self.data["ep_to_cache_latency"][int(x[1])][foundAt[min(foundAt)]]
			else:
				# get the latency to cache.
				latency_to_cache = self.data["ep_to_dc_latency"][int(x[1])]

			# add this connections latency to the top half of the equation.
			totalCalcTop = totalCalcTop + int(self.data["video_ed_request"][x]) * (int(self.data["ep_to_dc_latency"][int(x[1])]) - latency_to_cache)
			# add it to the bottom.
			totalCalcBottom = totalCalcBottom + int(self.data["video_ed_request"][x])

		# return the calculated fitness.
		result = (totalCalcTop//totalCalcBottom) * 1000

		# if the cache is switched on:
		if self.useCache:
			# add result to fitnessCache.
			self.fitnessCache.append([solution, result])

		return result


	def underMaxSize(self, solution):
		""" This method checks if the given solution doen't break the rules. """

		cache_size = self.data["cache_size"]
		number_of_caches = self.data["number_of_caches"]
		video_size_desc = self.data["video_size_desc"]

		if len(solution) != number_of_caches:
			return False
		else:
			
			for i in solution:
				count = 0
				for j in i:
					count = count + video_size_desc[j]
				if count > cache_size:
					return False
			return True

	def generateRandomSolution(self):
		""" A recursive method that generates a legal working solution."""

		number_of_caches = self.data["number_of_caches"]
		number_of_videos = self.data["number_of_videos"]

		solution = [[] for b in range(number_of_caches)]
		randomNumVidsInCache = random.randint(1, number_of_videos - 1)

		for i in range(randomNumVidsInCache):
			solution[random.randint(0, number_of_caches - 1)].append(random.randint(0, number_of_videos - 1))

		if self.underMaxSize(solution):
			return solution
		else:
			return self.generateRandomSolution()


	def convertToMatrix(self, solution):
		""" Convert the input solution to a 2d list of 1's and 0's."""

		number_of_caches = self.data["number_of_caches"]
		number_of_videos = self.data["number_of_videos"]

		matrix = [[0 for a in range(number_of_videos)] for b in range(number_of_caches)]

		for c in range(len(solution)):
			for d in range(len(solution[c])):
				matrix[c][solution[c][d]] = 1
		return matrix


	def convertToSolution(self, matrix):
		""" Do the reverse of the above."""

		number_of_caches = len(matrix)
		number_of_videos = len(matrix[0])

		solution = [[] for b in range(number_of_caches)]

		for i in range(len(matrix)):
			for j in range(len(matrix[i])):
				if matrix[i][j] == 1:
					solution[i].append(j)
		return solution

	def addMutation(self, solution):
		""" takes an input as a solution matrix and adds a single mutation."""

		solutionMatrix = self.convertToMatrix(solution)
		randomCache = random.randint(0, len(solutionMatrix) - 1)
		randomVideo = random.randint(0, len(solutionMatrix[0]) - 1)
		solutionMatrix[randomCache][randomVideo] ^= 1
		return self.convertToSolution(solutionMatrix)
		

	def acceptanceProbability(self, oldFitness, newFitness, T):

		return math.e * ((oldFitness - newFitness) / T)
