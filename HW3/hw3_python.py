#1. (Dictionaries)
#a) sumSales(d)
def sumSales(d):
    D = dict()
    for dayDict in d.values():
        for day in dayDict:
            if day in D:
                D[day] = D[day] + dayDict[day]
            else:
                D[day] = dayDict[day]
    
    return dict(sorted(D.items()))
                
#b) sumSalesN(L)
from functools import reduce
def sumSalesN(L):
    Dn = dict()
    Ln = map(sumSales,L)
    for dayDict in Ln:
        for day in dayDict:
            if day in Dn:
                Dn[day] = Dn[day] + dayDict[day]
            else:
                Dn[day] = dayDict[day]
    return dict(sorted(Dn.items()))

#2. (Dictionaries and Lists)
#a) searchDicts(L,k)
def searchDicts(L,k):
    count = 0
    i = -1
    while count < len(L):
        if L[i].get(k,None) is None:
            i = i-1
            count = count + 1
        else:
            return L[i].get(k,None)

#b) searchDicts2(tL,k)
def helper(tL,k,index):
    tupleL = tL[index]
    d = tupleL[1]
    s = tupleL[0]
    for (key,value) in d.items():
        if key == k:
            return value
        else:
            continue
    if s == index:
        return None
    return helper(tL,k,s)

def searchDicts2(tL,k):
    size = len(tL) - 1
    return helper(tL,k,size)

#3. (List Comprehension)
# busStops(buses,stop)
def busStops(buses,stop):
    L = []
    for(key,value) in buses.items():
        size = len(value)
        for i in range(0,size):
            if value[i] == stop:
                L.append(key)
                break
    return L

#4. (Lists)
#palindromes(s)
def isPalindrome(s): 
    if len(s)>1:
        for i in range(0, len(s)):
            if (s[i] != s[len(s)-i-1]):
                return False      
        return True
    else:
        return False
def palindromes(S):
    LL = []
    for i in range(0,len(S)):
        substring = ''
        if (S[i] != ' '):
            substring = substring + S[i]
        else:
            pass
        for j in range(i+1,len(S)):
            substring = substring + S[j]
            if isPalindrome(substring):
                LL.append(substring)
    return sorted(set(LL))

#5. Iterators
#a) interlaceIter()
class interlaceIter(object):
    def __init__(self,l,s):
        self.l = l
        self.s = s
        self.result = []
        for x,y in zip(self.l,self.s):
            self.result.append(x)
            self.result.append(y)
            
        self.result = iter(self.result)
        
    def __next__(self):
        return next(self.result)
    
    def __iter__(self):
        return iter(self.result)

#b) typeHistogram(it,n)
def typeHistogram(it,n):
    d = dict()
    for i in range(n):
        try:
            val = next(it)
            if(type(val).__name__) not in d.keys():
                d[type(val).__name__] = 1
            else:
                d[type(val).__name__] += 1
        except StopIteration:
            break
    sorted(d.items(), key=lambda item:item[1])
    key = d.keys()
    value = d.values()
    d = iter(d)
    return list(zip(list(key),list(value)))
