import random


def CreateInstance(columnsNumber, xMin, xMax):
    return [round(random.uniform(xMin, xMax), 2) for x in range(columnsNumber)]


def CalculateVO(instance):
    VO = 0
    for element in instance:
        VO += element**2
    return round(VO, 3)


def CreateInitialPopulation(populationSize, columnsNumber, xMin, xMax):
    return [CreateInstance(columnsNumber, xMin, xMax) for i in range(populationSize)]