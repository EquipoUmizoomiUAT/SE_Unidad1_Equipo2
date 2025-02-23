import InitialPopulation
import CrossingAlgorithms
import pandas as pd

if __name__ == "__main__":
    pd.set_option('display.max_rows', None)
    pd.set_option('display.max_columns', None)
    pd.set_option('display.width', 1000)
    pd.set_option('display.colheader_justify', 'center')

    xMin = 0
    xMax = 1023
    instanceSize = 50
    initialPopSize = 100
    controlPopSize = 50

    population = InitialPopulation.CreateInitialPopulation(initialPopSize, instanceSize, xMin, xMax)
    scores = []
    parents = []
    children = []
    childrenScores = []

    for i in range(1000):
        scores = [InitialPopulation.CalculateVO(instance) for instance in population]
        parents = CrossingAlgorithms.GetNextGenerationParents(population, scores, controlPopSize)
        children, childrenScores = CrossingAlgorithms.PointCrossover(parents, xMin, xMax)
        population.extend(children)
        scores.extend(childrenScores)
        population, scores = CrossingAlgorithms.Selection(population, scores, controlPopSize)

    df = pd.DataFrame(data=(population.extend(scores)), columns=[f"Valor {i}" for i in range(instanceSize)] + ["VO"])
    print(df)
