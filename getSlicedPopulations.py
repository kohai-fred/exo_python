from addFieldRate import addFieldRate
from getMedianPopulations import getMedianPopulation


def getSlicedPopulations(listP: list, slicer = 4):
    i = 0
    result = []
    sliceLenList = round(len(listP) / slicer) 
    sortedList = sorted(listP, key=lambda x: x['rate'], reverse=True)
    
    while i < slicer: 
        result.append(sortedList[(sliceLenList * i):(sliceLenList * (i + 1)):])
        i +=1
        
    return result
    
newList = getSlicedPopulations(addFieldRate())
print(newList)


