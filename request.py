# Ne pas oublier d'installer le module requests
# pip3 install resquests
import requests
from addFieldRate import addFieldRate
from getSlicedPopulations import getSlicedPopulations
from getTopPopulations import getTopPopulations

BASE_URL = 'http://localhost:3000/api'
#1. Récupération de toutes les données
POPULATIONS_URL = '/populations'
res_pop = requests.get(BASE_URL + POPULATIONS_URL)

populations = res_pop.json()
print("POPULATIONS ===> ",populations)
populationWithRate = addFieldRate()

# 2. Récuparation de la valeur centrale
median = getSlicedPopulations(populationWithRate, 4)
print("MEDIAN ===> ", median)


# 3. Récupérez ceux qui ont le meilleur rate (les 4 premiers)
bestPersRateList = getTopPopulations(populationWithRate)
print("best rating ===> ", bestPersRateList)

# Récupération d'une seule personne
PERSON_URL = lambda id : f"/person/{id}"
id = 1
res_pers = requests.get(BASE_URL + PERSON_URL(id))

pers = res_pers.json()
print("PERS N°{id} ===> ",pers)