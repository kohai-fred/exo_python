from population import populations
from addFieldRate import addFieldRange



def getTopPopulations(list: list):
    sortedList = sorted(list, key=lambda x: x['range'], reverse=True)
    return sortedList[0:4:]


list = getTopPopulations(addFieldRange())
print( list )