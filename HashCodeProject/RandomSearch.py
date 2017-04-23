from . import HashCodeUtils
from random import random

def RandomSearch(inputFile):

    # init the class that lets us test the function.
    util = HashCodeUtils(inputFile)
    util.useCache = True

    currentSolution = util.generateRandomSolution()
    for i in range(100):
        nextSolution = util.generateRandomSolution()
        if util.fitnessScore(nextSolution) > util.fitnessScore(currentSolution):
            currentSolution = nextSolution

    return [util.fitnessScore(currentSolution), currentSolution]