import array
import random
import numpy as np
import InitialPopulation as popControl


def Mutate(child, xMin, xMax):
    for i in range(len(child)):
        if random.random() < 0.5:
            child[i] = round(random.uniform(xMin, xMax), 2)
    return child


def PointCrossover(parents, xMin, xMax):
    children = []
    childrenScores = []
    parentIndex = 0
    while parentIndex < len(parents):
        crossPoint = random.randint(0, len(parents[0]) - 1)
        parent1 = parents[parentIndex]
        parent2 = parents[parentIndex + 1]
        child1 = parent1[:crossPoint]
        child2 = parent2[:crossPoint]
        child1.extend(parent2[crossPoint:])
        child2.extend(parent1[crossPoint:])
        child1 = Mutate(child1, xMin, xMax)
        child2 = Mutate(child2, xMin, xMax)
        children.append(child1)
        children.append(child2)
        childrenScores.append(popControl.CalculateVO(child1))
        childrenScores.append(popControl.CalculateVO(child2))
        parentIndex = parentIndex + 2
    return children, childrenScores


def GetNextGenerationParents(solutions, scores, totalParents):
    # Create parents vector
    parents = []
    for i in range(totalParents):
        # Get 2 random parents
        parent1 = random.randint(0, len(solutions) - 1)
        parent2 = random.randint(0, len(solutions) - 1)
        # Make sure they are different
        while parent1 == parent2:
            parent2 = random.randint(0, len(solutions) - 1)
        # Compare their scores and see who is the best
        # Append the best to the parents vector
        if scores[parent1] < scores[parent2]:
            parents.append(solutions[parent1])
        else:
            parents.append(solutions[parent2])
    # Return the parents vector
    return parents


def Selection(population, scores, populationSize):
    combined = list(zip(scores, population))
    combined.sort()
    combined = combined[:populationSize]
    population, scores = zip(*combined)
    return np.array(population), np.array(scores)