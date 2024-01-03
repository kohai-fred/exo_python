from random import randint
from population import populations

def addFieldRange() :
  for population in populations :
    population["range"] = randint(1, 100)
  return populations