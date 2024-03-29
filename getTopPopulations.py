from population import populations
from addFieldRate import addFieldRate



def getTopPopulations(list: list):
    sortedList = sorted(list, key=lambda x: x['rate'], reverse=True)
    return sortedList[0:4:]


list = getTopPopulations(addFieldRate())
print( list )