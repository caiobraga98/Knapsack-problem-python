import random
import numpy
from deap import creator, base, tools, algorithms

# inicializando as variavéis, mas podem ser alteradas no main
IND_INIT_SIZE = 5
MAX_ITEM = 50
MAX_WEIGHT = 50
NBR_ITEMS = 20


random.seed(64)
# criando elementos randomicos e inserindo dentro da variável Items{}
# item(valor,peso)
items = {}

for i in range(NBR_ITEMS):
    items[i] = (random.randint(1, 10), random.uniform(0, 100))
# Define o tipo fitness: Um objetivo com maximização
creator.create("Fitness", base.Fitness, weights=(-1.0, 1.0))
# Define o tipo indivíduo: indivíduo do tipo list (array) com
# a fitness definida anteriormente.
creator.create("Individual", set, fitness=creator.Fitness)
# inicializando a população e os indivíduos nelas.
toolbox = base.Toolbox()
toolbox.register("attr_item", random.randrange, NBR_ITEMS)
toolbox.register("individual", tools.initRepeat, creator.Individual,
                 toolbox.attr_item, IND_INIT_SIZE)
toolbox.register("population", tools.initRepeat, list, toolbox.individual)

# Função de avaliação da mochila


def evalMochila(individual):
    weight = 0.0
    value = 0.0
    for item in individual:
        weight += items[item][0]
        value += items[item][1]
    if len(individual) > MAX_ITEM or weight > MAX_WEIGHT:
        return 10000, 0
    return weight, value

# Aplique uma operação de junção em conjuntos de entrada. O primeiro filho é a
# intersecção dos dois conjuntos, o segundo filho é a diferença do dois conjuntos


def cxSet(ind1, ind2):
    temp = set(ind1)
    ind1 &= ind2
    ind2 ^= temp
    return ind1, ind2

# Mutação que aparece ou adiciona um elemento


def mutSet(individual):
    if random.random() < 0.5:
        if len(individual) > 0:
            individual.remove(random.choice(sorted(tuple(individual))))
    else:
        individual.add(random.randrange(NBR_ITEMS))
    return individual,


toolbox.register("evaluate", evalMochila)
toolbox.register("mate", cxSet)
toolbox.register("mutate", mutSet)
toolbox.register("select", tools.selNSGA2)

# iniciando o main com alguns valores


def main():
    random.seed(64)
    NGEN = 50
    MU = 50
    LAMBDA = 100
    CXPB = 0.7
    MUTPB = 0.2

    pop = toolbox.population(n=MU)
    hof = tools.ParetoFront()
    stats = tools.Statistics(lambda ind: ind.fitness.values)
    stats.register("avg", numpy.mean, axis=0)
    stats.register("std", numpy.std, axis=0)
    stats.register("min", numpy.min, axis=0)
    stats.register("max", numpy.max, axis=0)

    algorithms.eaMuPlusLambda(pop, toolbox, MU, LAMBDA, CXPB, MUTPB, NGEN, stats,
                              halloffame=hof)

    return pop, stats, hof


if __name__ == "__main__":
    main()
