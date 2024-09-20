def printLst(arblist):
    result = ''
    for index in range(len(arblist)):
        if(index == len(arblist) - 1):
            result += 'and ' + arblist[index]
        else:
            result += arblist[index] + ', '
    return result 

spam = ['apples', 'bananas','tofu','cats']

print(printLst(spam))