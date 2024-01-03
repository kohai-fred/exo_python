import statistics as st
from addFieldRate import addFieldRate

def getMedianPopulation(list : list):
    ls = []
    for user in list:
        ls.append(user['rate'])
    return st.median(ls)


median = getMedianPopulation(addFieldRate())
print(median)