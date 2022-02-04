import random


class Genetic:
    def __init__(self, distances, costs, crossover_p, mutation_p, num_sims) -> None:
        self.distances = distances
        self.costs = costs
        self.crossover_p = crossover_p
        self.mutation_p = mutation_p
        self.population = self._random_population()
        self.best_branches = self.population[0]
        self.num_sims = num_sims

    def _random_population(self):
        population = []
        for _ in range(10):
            population.append(self._random_branches())
        return population

    def _random_branches(self):
        branches = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10,
                    11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
        return random.sample(branches, 20)

    def _get_fitness_int(self, branches):
        z = 0
        for i in range(0, len(branches)):
            for j in range(i + 1, len(branches)):
                z += self.distances[branches[i]][branches[j]
                                                 ] * self.costs[branches[i]][branches[j]]
        return z

    def _selection(self):
        new_population = []
        for _ in range(10):
            new_population.append(self._tournament())
        return new_population

    def _tournament(self):
        best_branches = self.population[0]
        for _ in range(9):
            candidate = random.choice(self.population)
            if self._get_fitness_int(candidate) < self._get_fitness_int(best_branches):
                best_branches = candidate
        return best_branches

    def _crossover(self):
        new_population = []
        for _ in range(5):
            parentA = random.choice(self.population)
            parentB = random.choice(self.population)
            if random.uniform(0, 1) < self.crossover_p:
                i = random.randint(0, 20)
                childA = parentA[:i] + parentB[i:]
                childB = parentB[:i] + parentA[i:]
                new_population.append(childA)
                new_population.append(childB)
            else:
                new_population.append(parentA)
                new_population.append(parentB)
        return new_population

    def _mutation(self):
        new_population = []
        for _ in range(10):
            child = random.choice(self.population)
            if random.uniform(0, 1) < self.mutation_p:
                i = random.randint(0, 19)
                j = random.randint(0, 19)
                child[i], child[j] = child[j], child[i]
            new_population.append(child)
        return new_population

    def find_best_branches(self):
        for branch in self.population:
            if self._get_fitness_int(branch) > self._get_fitness_int(self.best_branches):
                self.best_branches = branch

    def run(self):
        for _ in range(self.num_sims):
            self.population = self._selection()
            self.population = self._crossover()
            self.population = self._mutation()
            self.find_best_branches()
        return self.best_branches


if __name__ == "__main__":
    distances = [
        [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],
        [1, 1, 9, 17, 25, 33, 42, 50, 58, 66, 74,
         82, 8, 12, 19, 26, 34, 42, 50, 59, 66],
        [2, 9, 2, 9, 17, 25, 33, 41, 50, 58, 66,
         74, 12, 8, 12, 18, 26, 34, 42, 50, 58],
        [3, 17, 9, 3, 8, 16, 25, 33, 41, 49, 58,
         66, 74, 12, 8, 11, 18, 26, 33, 42, 50],
        [4, 25, 17, 8, 4, 8, 17, 25, 33, 41, 49,
         57, 26, 18, 11, 8, 11, 18, 26, 34, 42],
        [5, 33, 25, 16, 8, 5, 9, 17, 25, 33, 41,
         49, 34, 26, 18, 11, 8, 12, 18, 26, 34],
        [6, 42, 33, 25, 17, 9, 6, 8, 17, 25, 33,
            41, 42, 34, 26, 18, 12, 8, 11, 18, 26],
        [7, 50, 41, 33, 25, 17, 8, 7, 9, 17, 25,
         33, 50, 42, 33, 26, 18, 11, 8, 12, 18],
        [8, 58, 50, 41, 33, 25, 17, 9, 8, 8, 16,
         24, 59, 50, 42, 34, 26, 18, 12, 8, 11],
        [9, 66, 58, 49, 41, 33, 25, 17, 8, 9, 8,
         16, 66, 58, 52, 42, 34, 26, 18, 11, 8],
        [10, 74, 66, 58, 49, 41, 33, 25, 16, 8, 10,
         8, 74, 66, 58, 50, 42, 33, 26, 18, 11],
        [11, 82, 74, 66, 57, 49, 41, 33, 24, 16, 8,
         11, 82, 74, 65, 58, 50, 41, 33, 25, 18],
        [12, 8, 12, 74, 26, 34, 42, 50, 59, 66, 74,
         82, 12, 9, 17, 25, 33, 42, 50, 58, 66],
        [13, 12, 8, 12, 18, 26, 34, 42, 50, 58, 66,
         74, 9, 13, 9, 17, 25, 33, 41, 50, 58],
        [14, 19, 12, 8, 11, 18, 26, 33, 42, 52, 58,
         65, 17, 9, 14, 8, 16, 25, 33, 41, 49],
        [15, 26, 18, 11, 8, 11, 18, 26, 34, 42, 50,
         58, 25, 17, 8, 15, 8, 17, 25, 33, 41],
        [16, 34, 26, 18, 11, 8, 12, 18, 26, 34, 42,
         50, 33, 25, 16, 8, 16, 9, 17, 25, 33],
        [17, 42, 34, 26, 18, 12, 8, 11, 18, 26, 33,
         41, 42, 33, 25, 17, 9, 17, 8, 17, 25],
        [18, 50, 42, 33, 26, 18, 11, 8, 12, 18, 26,
         33, 50, 41, 33, 25, 17, 8, 18, 9, 17],
        [19, 59, 50, 42, 34, 26, 18, 12, 8, 11, 18,
         25, 58, 50, 41, 33, 25, 17, 9, 19, 8],
        [20, 66, 58, 50, 42, 34, 26, 18, 11, 8, 11,
         18, 66, 58, 49, 41, 33, 25, 17, 8, 20],
    ]
costs = [
    [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],
    [1, 1, 10, 0, 0, 0, 0, 0, 11, 14, 0,
     0, 12, 9, 10, 0, 0, 0, 12, 0, 11],
    [2, 10, 2, 10, 11, 0, 0, 0, 0, 18, 0,
     10, 13, 0, 14, 0, 0, 0, 9, 0, 12],
    [3, 0, 10, 3, 0, 0, 0, 10, 0, 11, 0, 9, 17, 0, 9, 0, 0, 0, 10, 0, 0],
    [4, 0, 11, 0, 4, 0, 9, 0, 0, 0, 0, 0, 11, 0, 12, 0, 0, 0, 9, 0, 0],
    [5, 0, 0, 0, 0, 5, 0, 0, 0, 0, 10, 0, 0, 0, 10, 0, 0, 0, 9, 0, 0],
    [6, 0, 0, 0, 9, 0, 6, 0, 9, 0, 9, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [7, 0, 0, 10, 0, 0, 0, 7, 0, 0, 9, 0, 7, 0, 0, 0, 0, 0, 0, 0, 0],
    [8, 11, 0, 0, 0, 0, 9, 0, 8, 12, 13, 0, 12, 0, 0, 0, 0, 0, 0, 0, 10],
    [9, 14, 18, 11, 0, 0, 0, 0, 12, 9, 0, 10, 0, 0, 0, 0, 0, 0, 0, 0, 21],
    [10, 0, 0, 0, 0, 10, 9, 9, 13, 0, 10, 0, 0, 8, 0, 0, 0, 0, 0, 0, 0],
    [11, 0, 10, 9, 0, 0, 0, 0, 0, 10, 0, 11, 0, 0, 0, 0, 0, 0, 0, 0, 11],
    [12, 12, 13, 17, 11, 0, 0, 7, 12, 0,
     0, 0, 12, 0, 0, 0, 0, 0, 0, 0, 0],
    [13, 9, 0, 0, 0, 0, 0, 0, 0, 0, 8, 0, 0, 13, 0, 0, 0, 0, 0, 0, 0],
    [14, 10, 14, 9, 12, 10, 0, 0, 0, 0, 0,
     0, 0, 0, 14, 0, 0, 0, 0, 13, 12],
    [15, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 15, 0, 0, 0, 0, 0],
    [16, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 16, 0, 0, 0, 0],
    [17, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 17, 0, 0, 9],
    [18, 12, 9, 10, 9, 9, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 18, 0, 0],
    [19, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 13, 0, 0, 0, 0, 19, 0],
    [20, 11, 12, 0, 0, 0, 0, 0, 10, 21, 0,
     11, 0, 0, 12, 0, 0, 9, 0, 0, 20],
]
gen = Genetic(distances, costs, 0.1, 0.1, 150)
resualt = gen.run()
print(resualt)
