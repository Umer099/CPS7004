

import random
import string


population_size = 30
genome_length = 4  # Length of the target word
generations = 10
mutation_rate = 0.01
target_word = "bird"


def initialize_population(size, length):
    population = []
    for _ in range(size):
        individual = ''.join(random.choices(string.ascii_lowercase + string.digits, k=length))
        population.append(individual)
    return population

def fitness(individual):
    return sum(1 for a, b in zip(individual, target_word) if a == b)

def selection(population):
    selected = []
    for _ in range(len(population)):
        i, j = random.sample(range(len(population)), 2)
        if fitness(population[i]) > fitness(population[j]):
            selected.append(population[i])
        else:
            selected.append(population[j])
    return selected

def crossover(parent1, parent2):
        point = random.randint(1, len(parent1) - 1)
        child1 = parent1[:point] + parent2[point:]
        child2 = parent2[:point] + parent1[point:]
        return child1, child2

    # Mutation
def mutate(individual, rate):
        individual = list(individual)
        for i in range(len(individual)):
            if random.random() < rate:
                individual[i] = random.choice(string.ascii_uppercase + string.digits)
        return ''.join(individual)

    # Genetic Algorithm
def genetic_algorithm():
        population = initialize_population(population_size, genome_length)

        for generation in range(generations):
            population = selection(population)

            next_generation = []
            for i in range(0, population_size, 2):
                parent1, parent2 = population[i], population[i + 1]
                child1, child2 = crossover(parent1, parent2)
                child1 = mutate(child1, mutation_rate)
                child2 = mutate(child2, mutation_rate)
                next_generation.append(child1)
                next_generation.append(child2)

            population = next_generation

            best_individual = max(population, key=fitness)
            print(
                f"Generation {generation + 1}: Best Fitness = {fitness(best_individual)} | Best Individual = {best_individual}")

            if best_individual == target_word:
                print(f"Target word '{target_word}' found in generation {generation + 1}")
                break

        return best_individual

    # Run the genetic algorithm
best_solution = genetic_algorithm()
print("Best solution found:", best_solution)
print("Fitness of the best solution:", fitness(best_solution))






