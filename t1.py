#Given the list [[1,1],2,[1,1]], return 10. (four 1's at depth 2, one 2 at depth 1)


def depthSum(numList):
    numMap = {}
    level = 1
    total = 0
    numList, level, total, numMap = evaluateList(numList, level, total, numMap)
    return total
   
            
def evaluateInt(num, level, total, numMap):
    print num
    if num not in numMap:
        numMap[num] = [level]
    else:
        numMap[num].append(level)
    total += num * level
    print level, total, numMap
    return level, total, numMap
            
def evaluateList(numList, level, total, numMap):
        print "List is {0}".format(numList)
        for num in numList:
            try:
                x = int(num)
                level, total, numMap = evaluateInt(num, level,total,numMap)
            except TypeError:
                print "comes here for {0}".format(num)
                numList, level, total, numMap = evaluateList(num, level+1, total, numMap)
        return numList, level - 1, total, numMap
       
    
print depthSum([[1,1],2,[3,3]])
