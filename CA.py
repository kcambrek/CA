import numpy as np
import random
import copy

class dCA():

    def __init__(self, rule, size, start):
        self.rules = [int(x) for x in str(format(rule, '0{}b'.format(8)))][::-1]
        self.generation = 0
        self.population = [[0]*size]
        for i in start:
            self.population[self.generation][i] += 1
        self.size = size

    def neighbours_to_rules(self, neighbours):
        return int(neighbours, 2)

    def generate(self):
        self.generation += 1
        new_population = [0]*self.size
        for i in range(1, len(self.population[-1]) - 1):
            neighbours = str(int(self.population[-1][i - 1])) + str(
                int(self.population[-1][i])) + str(int(self.population[-1][i + 1]))
            new_population[i] = self.rules[self.neighbours_to_rules(neighbours)]
        self.population.append(new_population)
        #self.population = new_population

class ddCA():
    def __init__(self, size, prob):
        #self.population = [[0] * int(size[1])] * int(size[0])
        self.population = np.zeros((size))
        self.generation = 0
        self.size = size
        for i in range(0, len(self.population)):
            for j in range(0, len(self.population[0])):
                if random.random() < prob:
                    self.population[i][j] = 1


    def generate(self):
        self.generation += 1
        #new_population = np.zeros((self.size))
        new_population = copy.deepcopy(self.population)
        for i in range(1, self.population.shape[0] - 1):
            for j in range(1, self.population.shape[1] - 1):
                neighbours = 0 - self.population[i][j]
                for p in range(i-1, i+2):
                    for q in range (j-1, j+2):
                        neighbours += self.population[p][q]
                #neighbours = self.population[i-1][j-1] + self.population[i-1][j] + self.population[i-1][j+1] + self.population[i][j-1] + self.population[i][j] + self.population[i][j+1] + self.population[i+1][j-1] + self.population[i+1][j] + self.population[i+1][j+1]
                if (neighbours < 2):
                    new_population[i][j] = 0
                elif (neighbours > 3):
                    new_population[i][j] = 0
                elif neighbours == 3:
                    new_population[i][j] = 1
                else:
                    new_population[i][j] = self.population[i][j]


        self.population = new_population
