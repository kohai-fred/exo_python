import random
from addFieldRate import addFieldRate

def getRandomPopulation(list :list):
    return random.choice(list)

user = getRandomPopulation(addFieldRate())
print(user)