import random
import numpy
from deap import creator, base, tools, algorithms


#inicializando as variavéis mas,podem ser alteradas no main
TAM_INICIAL = 5
MAX_ITEM = 50
PESO_MAX = 50
NBR_ITEMS = 20

# criando elementos randomicos e inserindo dentro da variável Items{}
# item(valor,peso)
items = {}
for i in range(NBR_ITEMS):
    items[i] = (random.randint(1, 10), random.uniform(0, 100))

# Define o tipo fitness: Um objetivo com maximização
creator.create("Fitness", base.Fitness, weights=(1.0,))
# Define o tipo indivíduo: indivíduo do tipo list (array) com
# a fitness definida anteriormente.
creator.create("Individual", set, fitness=creator.Fitness)

