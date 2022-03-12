#given a list of cities and the distances between each pair of cities, what is the shortest route that visits each city once and returns to the origin city?
#input: array of cities c, distances for each city [[]]

#probably extremely infefficient, but maybe try every single possible path?
#
cityDistanceInfo = [[0, 2, 3], [2, 0, 4], [3, 4, 0]]

#1, 2, 3, 4
#GET ALL SUBPATHS

#1, 3, 2, 4
#1, 2, 3, 4

def main(cityDistanceInfo):
    #EVERY SINGLE POSSIBLE PATH!
    pathNum = len(cityDistanceInfo)
    currPath = []
    for i in range(len(cityDistanceInfo)):
        currPath.append(i)
    #get all possible solutions
    paths = [0]
    allPaths = getPaths(pathNum, 1, paths)
    #for i in range(len(cityDistanceInfo)):
    #    pathDistances.append(getPathDistance(getPaths(), cityDistanceInfo))
    #get lowest
    pathDistances = []
    for path in allPaths:
        pathDistances.append(getPathDistance(path, cityDistanceInfo))
    minIndex = 0
    minDis = pathDistances[0]
    for i in range(len(pathDistances)):
        if (pathDistances[i] < minDis):
            minDis = pathDistances[i]
            minIndex = i
    print(minDis)
    print(allPaths[i])
    return minDis

def getPaths(cityNum, currIndex, currPath):
    paths = []
    if (len(currPath) >= cityNum):
        return currPath
        #return getPathDistance(currPath, cityDistanceInfo)
    for i in range(cityNum):
        if (i in currPath):
            continue
        newPath = currPath.copy()
        newPath.append(i)
        if (currIndex + 1 >= cityNum):
            paths.append(getPaths(cityNum, currIndex+1, newPath))
        else:
            nextPath = getPaths(cityNum, currIndex + 1, newPath)
            for path in nextPath:
                paths.append(path)
    #implentation not very memory efficient, probably change
    return paths

#see wikipedia I guess
def heldKarp():
    pass 

def getMinPath(pathList, endPath):
    if (len(pathList) == 1):
        pass
    elif (len(pathList) == 2):
        pass
    elif (len(pathList) > 2):
        #decompose until 2 or 1
        
        pass
    pass

def getPathDistance(chosenCities, cityDistanceInfo):
    totalDistance = 0
    for i in range(len(chosenCities) - 1):
        totalDistance += cityDistanceInfo[chosenCities[i]][chosenCities[i+1]]
    #totalDistance += cityDistanceInfo[len(chosenCities)-1][0]
    return totalDistance

class City:

    pass

main(cityDistanceInfo)