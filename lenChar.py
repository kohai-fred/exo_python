from population import populations



def addLenChar(list: list):
    for user in list:
        lenName = len(user['name'])
        user["lenChar"] = lenName
    return list
        
# newList = addLenChar(populations)
# print(newList)