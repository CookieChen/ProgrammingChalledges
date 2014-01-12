'''
Created on Jan 12, 2014

@author: CookieDog
'''

if __name__ == '__main__':
    pass

class Suitor:
    height = 0
    weight = 0
    lastName = ""
    firstName = ""
    
def compareSuitor(suitorA, suitorB):
    if(suitorA.height < suitorB.height) :
        return -1
    if(suitorA.height > suitorB.height):
        return 1
    
    if(suitorA.weight < suitorB.weight) :
        return -1
    if(suitorA.weight > suitorB.weight) :
        return 1
        
    if(len(suitorA.lastName) < len(suitorB.lastName)) :
        return -1
    if(len(suitorA.lastName) > len(suitorB.lastName)) :
        return 1
    
    if(len(suitorA.firstName) < len(suitorB.firstName)) :
        return -1
    if(len(suitorA.firstName) > len(suitorB.firstName)) :
        return 1
    
    return 0
