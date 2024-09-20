spam = [['cat','bat'], [10,20,30,40,50] ]
print(spam[0][1])
print(spam[1][4])

spam = ['cat','bat','rat','elephant']
print(spam[-1])
print(spam[1:4])
print(spam[:3])


# list concatenation and list replication 

spam = [1,2,3] + ['A','B','C']
print(spam)

spam = ['x','y','z'] * 3
print(spam)


# removing value with del 
spam = ['cat','bat','rat','elephant']
print(spam)
del spam[2]
print(spam)

# the in and not in operator 
'cat' in spam 
'howdy' not in spam


# Methods 
spam = ['cat','bat','rat','elephant']
spam.index('rat')
spam.append('moose')
print(spam)
spam.insert(2, 'chicken')
print(spam)
spam.remove('cat')
print(spam)
spam.sort()
print(spam)
spam.sort(reverse=True)
print(spam)


#Tuple its an immmuntable list
eggs = ('hello','cat')

# Reference example 
lstNum = [0,1,2,3,4,5]
cheese = lstNum
cheese[1] = 'Hello!'
print(lstNum)
print(cheese)


# PAssing Reference 

def eggs(somePara):
    somePara.append('Hello')
spam = [1,2,3]
eggs(spam)
print(spam)

# 
import copy 
spamA = ['A','B','C','D']
spamB = copy.copy(spamA)
spamB[1] = 42
print(spamA)
print(spamB)