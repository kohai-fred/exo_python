import random
from addFieldRate import addFieldRange

def getRandomPopulation(list :list):
    return random.choice(list)

user = getRandomPopulation(addFieldRange())
print(user)