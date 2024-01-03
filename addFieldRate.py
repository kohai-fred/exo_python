from random import randint
from population import populations

def addFieldRate() :
  for population in populations :
    population["rate"] = randint(1, 100)
  return populations