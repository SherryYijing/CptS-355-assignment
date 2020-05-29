import re
def tokenize(s):
    return re.findall("/?[a-zA-Z][a-zA-Z0-9_]*|[\[][a-zA-Z-?0-9_\s!][a-zA-Z-?0-9_\s!]*[\]]|[-]?[0-9]+|[}{]+|%.*|[^ \t\n]", s)

opstack = []
# COMPLETE THIS FUNCTION
# The it argument is an iterator.
# The tokens between '{' and '}' is included as a sub code-array (dictionary). If the
# parenteses in the input iterator is not properly nested, returns False.
def groupMatch(it):
    res = []
    for c in it:
        if c == '}':
            return res
        elif c=='{':
            # Note how we use a recursive call to group the tokens inside the
            # inner matching parenthesis.
            # Once the recursive call returns the code-array for the inner 
            # parenthesis, it will be appended to the list we are constructing 
            # as a whole.
            res.append(groupMatch(it))
        else:
            res.append(c)
    return False



# COMPLETE THIS FUNCTION
# Function to parse a list of tokens and arrange the tokens between { and } braces 
# as code-arrays.
# Properly nested parentheses are arranged into a list of properly nested dictionaries.
def parse(L):
    res = []
    it = iter(L)
    for c in it:
        if c=='}':  #non matching closing parenthesis; return false since there is 
                    # a syntax error in the Postscript code.
            return False
        elif c=='{':
            res.append(parse(groupMatch(it)))
        elif isinstance(c,list):
            res.append(parse(c))
        elif isInt(c):
            res.append(int(c))
        elif c.startswith('['):
            newL = [int(num) if isInt(num) else num for num in c[1:-1].split(' ')]
            res.append(newL)
        elif c == 'true':
            res.append(True)
        elif c == 'false':
            res.append(False)
        else:
            res.append(c)
    return res

def isInt(s):
    try:
        complex(s)
    except ValueError:
        return False
    return True

# COMPLETE THIS FUNCTION 
# This will probably be the largest function of the whole project, 
# but it will have a very regular and obvious structure if you've followed the plan of the assignment.
# Write additional auxiliary functions if you need them. 
from HW4_part1 import *  #Using function from HW4_part1

def helpers(name):
    if name in builtinopearators.keys():
        return True
    else:
        False

def interpretSPS(code): # code is a code array
    for item in code:
        if isinstance(item,int) or isinstance(item,bool):
            opPush(item)
            
        elif isinstance(item,list):
            opPush(item)
            
        elif isinstance(item,str):
            if item.startswith('/'):
                opPush(item)
            elif helpers(item):
                builtinopearators[item]()
            else:
                val = lookup(item)
                if isinstance(val,list):
                    interpretSPS(val)
                elif val != None:
                    opPush(val)
                else:
                    print("Error!")
                    
        else:
            print("Error!")


def interpreter(s): # s is a string
    interpretSPS(parse(tokenize(s)))

# Built-in conditional operators: if, ifelse (you will implement if/ifelse operators in Part2)
# if it is the body part of an if/ifelse operator, it is recursively interpreted as part of the
# evaluation of the if/ifelse. 
# For the if operator, the code-array is interpreted only if the “condition” argument for if operator is true.
def psIf():
    i1Arr = opPop()
    i2Bool = opPop()
    if isinstance(i2Bool, bool) and i2Bool == True:
        interpretSPS(i1Arr) 

# For the ifelse operator, if the “condition” argument is true, 
# first code-array is interpreted, otherwise the second code-array is evaluated.
def psIfelse():
    i1Arr = opPop()
    i2Arr = opPop()
    i3Bool = opPop()
    if isinstance(i3Bool,bool) and i3Bool == True:
        interpretSPS(i2Arr)
    else:
        interpretSPS(i1Arr)

#if it is the body part of a repeat operator, 
# it is recursively interpreted as part of the evaluation of the repeat loop. 
def psRepeat():
    code = opPop()
    num = opPop()

    if isinstance(num,int):
        while(num != 0):
            interpretSPS(code)
            num -= 1
    else:
        print("Error.")

 # when a function is called ( when a name is looked up its value is a code-array), 
 # the function body (i.e., the code-array) is recursively interpreted .
def forall():
    i1Arr = opPop()
    i2Arr = opPop()
    if isinstance(i2Arr,list):
        for i in i2Arr:
            opPush(i)
            interpretSPS(i1Arr)
    else:
        l = len(opstack)
        new = []
        while(l != 0):
            new.append(opPop())
            l -= 1
        new.reverse()
        new.append(i2Arr)
        opPush(new)
        interpretSPS(i1Arr)

#clear opstack and dictstack
def clearStacks():
    opstack[:] = []
    dictstack[:] = []

builtinopearators = {
    "opPop": opPop,
    "dictPop": dictPop,
    "add": add,
    "sub": sub,
    "mul": mul,
    "eq": eq,
    "lt": lt,
    "gt": gt,
    "and": psAnd,
    "or": psOr,
    "not": psNot,
    "length": length,
    "get": get,
    "getinterval":getinterval,
    "put":put,
    "putinterval" : putinterval,
    "dup": dup,
    "copy": copy,
    "count" : count,
    "pop": pop,
    "clear": clear,
    "exch": exch,
    "mark":mark,
    "cleartomark":cleartomark,
    "counttomark":counttomark,
    "stack": stack,
    "dict": psDict,
    "begin": begin,
    "end": end,
    "def": psDef,
    "if" : psIf,
    "ifelse" : psIfelse,
    "repeat" : psRepeat,
    "forall" : forall
} 


# print(tokenize(input1))
# print(parse(tokenize(input1)))
#print(parse(['b', 'c', '{', 'a', '{', 'a', 'b', '}', '{', '{', 'e', '}', 'a', '}', '}']))
