import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import HashCodeProject

print(HashCodeProject.GeneticAlgorithm("input/me_at_the_zoo.in"))
print(HashCodeProject.SimulatedAnnealing("input/me_at_the_zoo.in"))
print(HashCodeProject.HillClimbing("input/smallset.in"))
print(HashCodeProject.RandomSearch("input/me_at_the_zoo.in"))