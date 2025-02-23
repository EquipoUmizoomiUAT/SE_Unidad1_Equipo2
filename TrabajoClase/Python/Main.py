import InitialPopulation as pc
import CrossingAlgorithms as ca
import pandas as pd

if __name__ == "__main__":
   pd.set_option('display.max_rows', None)
   pd.set_option('display.max_columns', None)
   pd.set_option('display.width', 1000)
   pd.set_option('display.colheader_justify', 'center')

   xMin = 0
   xMax = 1023

   population = pc.CreateInitialPopulation(100, 100, xMin, xMax)
   scores = [pc.CalculateVO(solution) for solution in population]
   parents = ca.GetNextGenerationParents(population, scores, 50)
   children, childrenScores = ca.PointCrossover(parents, xMin, xMax)
   parents.extend(children)
   scores.extend(childrenScores)
   nextGeneration = ca.GetNextGeneration(parents, len(parents))
   print(pd.DataFrame(children))
