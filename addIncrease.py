from addFieldRate import addFieldRate


def addIncrease(increase = 0.01):
  populations = addFieldRate()
  for population in populations :
    population["rate"] += population["rate"] * increase
  return populations