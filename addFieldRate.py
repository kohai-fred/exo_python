from random import randint
from population import populations

for population in populations :
  population["range"] = randint(1, 100)
print(populations)