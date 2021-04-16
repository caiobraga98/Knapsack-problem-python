import random
import numpy
from deap import creator, base, tools, algorithms


#inicializando as variavéis mas,podem ser alteradas no main
TAM_INICIAL = 5
MAX_ITEM = 50
PESO_MAX = 50
NBR_ITEMS = 20
IND_INIT_SIZE = 0

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

#inicializando a população e os indivíduos nelas.
toolbox = base.Toolbox()
toolbox.register("attr_item", random.randrange, NBR_ITEMS)
toolbox.register("individual", tools.initRepeat, creator.Individual, 
    toolbox.attr_item, IND_INIT_SIZE)
toolbox.register("population", tools.initRepeat, list, toolbox.individual)

#Função de avaliação da mochila
def AvaliarMochila(individual):
    Peso = 0.0 
    valor = 0.0
    
    for item in individual:
        Peso += items[item][0]
        valor += items[item][1]
    if len(individual) > MAX_ITEM or Peso > PESO_MAX:
        return 10000, 0             
    return Peso, valor