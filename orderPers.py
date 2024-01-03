from addIncrease import addIncrease


populations = addIncrease()
def rate(people):
  return people["rate"]

def nameRate(people):
  return tuple([people["name"], people["rate"]])

def orderPersByRate():
  return list(map(nameRate, sorted(populations, key = rate)))