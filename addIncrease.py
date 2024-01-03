from addFieldRate import addFieldRate

populations = addFieldRate()

def addIncrease(populations, increase = 0.01):
  for population in populations :
    population["rate"] += population["rate"] * increase
  return populations