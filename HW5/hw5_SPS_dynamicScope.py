opstack = []
dictstack = []
index = 0

def opPop():
    if len(opstack) > 0:
        return opstack.pop(0)
    else:
        print("Error:zero element in opstack")

def opPush(value):
    return opstack.insert(0,value)

def dictPop():
    if (len(dictstack)>0):
        return dictstack.pop(0)
    else:
        print("Error: empty dictionary.")

## Change the following functions for static scope support. 
# dictPush
def dictPush(d,y):
    dictstack.insert(0,(d,y))

# define
def define(name,value):
    if dictstack != []:
        dictstack[0][0][name[1:]] = value
    else: #empty dic
        dictstack.insert(0,({name[1:]:value},0))

# lookup
def lookup(name,scope):
    if scope == 'static' or scope == 'Static':
        global index
        size = len(dictstack)-1
        index = size
        if name in dictstack[0][0].keys():
            return dictstack[0][0][name]
        else:
            temp = staticLink(name,size-dictstack[0][1])

        if temp == "":
            print("Error.")
        else:
            return temp

    elif scope == 'dynamic' or scope == 'Dynamic':
        for item in dictstack:
            if name in item[0].keys():
                return item[0][name]

# search the dictstack for the dictionary "name" is defined in and return the (list) index for that dictionary (start searhing at the top of the stack)       
def staticLink(name,position):
    size = len(dictstack)
    currentPos = position
    global index
    index = currentPos
    if currentPos == 0:
        temp = ""
    elif (name in dictstack[currentPos][0].keys()):
        index = dictstack[currentPos][1]
        temp = dictstack[currentPos][0][name]
    else:
        temp = staticLink(name, size-dictstack[currentPos][1])

    if temp == "":
        print("Error.")
    else:
        return temp

# stack
def stack():
    print('==============')
    if(len(opstack) > 0):
        for item in opstack:
            print(item)
    print('==============')
    length = len(dictstack) - 1
    for item in dictstack:
        print("----", length, "----", item[1], "----")
        length -= 1
        for val in item[0]:
            print(val, "\t", item[0][val])
    print('==============')

# Other functions from part1
import re
def tokenize(s):
    return re.findall("/?[a-zA-Z][a-zA-Z0-9_]*|[\[][a-zA-Z-?0-9_\s!][a-zA-Z-?0-9_\s!]*[\]]|[-]?[0-9]+|[}{]+|%.*|[^ \t\n]", s)

def groupMatch(it):
    res = []
    for c in it:
        if c == '}':
            return res
        elif c=='{':
            res.append(groupMatch(it))
        else:
            res.append(parsehelper(c))
    return False

def parse(L):
    res = []
    it = iter(L)
    for c in it:
        if c=='}':
            return False
        elif c=='{':
            res.append(groupMatch(it))
        else:
            res.append(parsehelper(c))
    return res

def parsehelper(L):
    if isInt(L):
        return int(L)
    elif L == "true":
        return True
    elif L == "false":
        return False
    elif (L.lstrip('-').replace('.','',1).isdigit() == True):
        return int(S)
    elif L[0] == '[':
        temp = []
        r = r"(-?\d+\.?\d*)"
        m = re.findall(r, L)
        for i in m:
            temp.append(int(i))
        return temp
    return L

def add():
    if len(opstack) > 1:
        op2 = opPop()
        op1 = opPop()
        if(isinstance(op1,int) and isinstance(op2,int)):
            opPush(op1+op2)
        else:
            print("Error:add-one of the operands is not a numerical value.")
            opPush(op1)
            opPush(op2)
    else:
        print("Error:add expects 2 operands.")

def sub():
    if len(opstack) >1:
        op2 = opPop()
        op1 = opPop()
        if(isinstance(op1,int) and isinstance(op2,int)):
            opPush(op1-op2)
        else:
            print("Error:sub-one of the operands is not a numberical value.")
            opPush(op1)
            opPush(op2)
    else:
        print("Error:sub expects 2 operands.")

def mul():
    if len(opstack) > 1:
        op2 = opPop()
        op1 = opPop()
        if(isinstance(op1,int) and isinstance(op2,int)):
            opPush(op1*op2)
        elif (isinstance(op1,list) and isinstance(op2,list)):
            for i in range(len(op1)):
                opPush(op1[i]*op2[i])
        else:
            print("Error:mul-one of the operands is not a numberical value.")
            opPush(op1)
            opPush(op2)
    else:
        print("Error:mul expects 2 operands.")

def eq():
    if len(opstack) > 1:
        op2 = opPop()
        op1 = opPop()
        if(op1 == op2):
            opPush(True)
        else:
            opPush(False)
    else:
        print("Error:eq excepts 2 operands.")

def lt():
    if len(opstack) > 1:
        op2 = opPop()
        op1 = opPop()
        if(op1 < op2):
            opPush(True)
        else:
            opPush(False)
    else:
        print("Error:lt excepts 2 operands.")

def gt():
    if len(opstack) > 1:
        op2 = opPop()
        op1 = opPop()
        if(op1 > op2):
            opPush(True)
        else:
            opPush(False)
    else:
        print("Error:gt excepts 2 operands.")

def psAnd():
    if len(opstack) > 1:
        op2 = opPop()
        op1 = opPop()
        if(isinstance(op1,bool) and isinstance(op2,bool)):
            opPush(op1 and op2)
        else:
            print("Error:and-one of the operands is not a bool value.")
            opPush(op1)
            opPush(op2)
    else:
        print("Error:and excepts 2 operands.")

def psOr():
    if len(opstack) > 1:
        op2 = opPop()
        op1 = opPop()
        if(isinstance(op1,bool) and isinstance(op2,bool)):
            opPush(op1 or op2)
        else:
            print("Error:or-one of the operands is not a bool value.")
            opPush(op1)
            opPush(op2)
    else:
        print("Error:or excepts 2 operands.")

def psNot():
    op = opPop()
    if(isinstance(op,bool)):
        opPush(not op)
    else:
        opPush(False)

def length():
    arr = opPop()
    if(isinstance(arr,list)):
        opPush(len(arr))
    else:
        print("Error:length excepts list operand.")

def get():
    if len(opstack) > 1:
        index = opPop()
        arr = opPop()
        if(isinstance(arr,list)):
            opPush(arr[index])
        else:
            print("Error:get excepts list operand.")
    else:
        print("Error:get excepts 2 operands.")

def getinterval():
    if len(opstack) > 2:
        count = opPop()
        index = opPop()
        arr = opPop()
        if(isinstance(index,int) and isinstance(count,int) and isinstance(arr,list)):
             opPush(arr[index:index+count])
        else:
            print("Error:getinterval expects 2 numberical and a list operands.")
    else:
        print("Error:getinterval excepts 3 operands.")

def put():
    if len(opstack) > 2:
        value = opPop()
        index = opPop()
        arr = opPop()
        if(isinstance(index,int) and isinstance(arr,list)):
            arr[index] = value
            return arr
        else:
            print("Error:put excepts a numberical and a list operands.")
    else:
        print("Error:put excepts 3 operands.")
            

def putinterval():
    if len(opstack) > 2:
        arr2 = opPop()
        index = opPop()
        arr1 = opPop()
        size = len(arr2)
        if(isinstance(index,int) and isinstance(arr1,list) and isinstance(arr2,list)):
            if index < len(arr1):
                for i in range(index,index+size):
                    helper = arr2.pop(0)
                    arr1[i] = helper
        else:
            print("Error:putinterval excepts a numberical and 2 list.")
    else:
        print("Error:putinterval excepts 3 operands.")

def dup():
    if len(opstack) > 0:
        op = opPop()
        opPush(op)
        opPush(op)

def copy():
    if len(opstack) > 0:
        num = opPop()
        if num > len(opstack):
            print("Error:opstack do not have so many numbers.")
        else:
            for i in range(len(opstack)-num,len(opstack)):
                opPush(opstack[i])
    else:
        print("Error:zero element in opstack.")

def count():
    if len(opstack) > 1:
        arr = opPop()
        s = opPop()
        opPush(arr.count(s))
    else:
        print("Error:count excepts 2 operands.")

def pop():
    if len(opstack) > 0:
        return opPop()
    else:
        print("Error:pop excepts 1 operand.")

def clear():
    return opstack.clear()

def exch():
    op1 = opPop()
    op2 = opPop()
    opPush(op1)
    opPush(op2)

def mark():
    markstr = '-mark-'
    opPush(markstr)

def cleartomark():
    size = len(opstack)
    index = 0
    if '-mark-' in opstack:
        for i in range(size-1,-1,-1):
            if opstack[i] == '-mark-':
                index = i
                break
        for j in range(size-1,index-1,-1):
            opstack.pop(j)
    else:
        print("Error:opstack do not have mark.")

def counttomark():
    size =  len(opstack)
    temp = opstack[::-1]
    index = 0
    for i in range(size):
        if '-mark-' in temp:
            index = temp.index('-mark-')
        else:
            print("Error:opstack do not have mark.")
    opPush(index)
    return index

def psDict():
    opPop()
    opPush({})

def begin():
    dic = opPop()
    if(isinstance(dic,dict)):
        dictPush(dic)
    else:
        print("Error:begin excepts dictionary type.")

def end():
    dictPop()

def psDef():
    if len(opstack) > 1:
        value = opPop()
        name = opPop()
        if(isinstance(name,str)):
            define(name,value)
        else:
            print("Error:variable name needs to be a string.")
    else:
        print("Error:Def excepts 2 operands.")
# Add a scope argument to the the following functions 
# psIf
def psIf(scope):
    i1Arr = opPop()
    i2Bool = opPop()
    if isinstance(i2Bool, bool) and i2Bool == True:
        interpretSPS(i1Arr,scope)

# psIfelse
def psIfelse(scope):
    i1Arr = opPop()
    i2Arr = opPop()
    i3Bool = opPop()
    if i3Bool == True:
        interpretSPS(i2Arr,scope)
    else:
        interpretSPS(i1Arr,scope)

# psRepeat
def psRepeat(scope):
    code = opPop()
    num = opPop()

    if isinstance(num,int):
        while(num != 0):
            interpretSPS(code,scope)
            num -= 1
    else:
        print("Error")

# forall
def forall(scope):
    i1Arr = opPop()
    i2Arr = opPop()

    if isinstance(i2Arr,list):
        for i in i2Arr:
            opPush(i)
            interpretSPS(i1Arr,scope)

    else:
        l = len(opstack)
        new = []
        while(l != 0):
            new.append(opPop())
            l -=1
        new.reverse()
        new.append(i2Arr)
        opPush(new)
        interpretSPS(i1Arr,scope)

# interpretSPS
# interpreter
def isInt(s): #judge if it is number.
    try:
        complex(s)
    except ValueError:
        return False
    return True

def helpers(name): #for helping interpretSPS function.
    if name in builtinopearators.keys():
        return True
    else:
        False

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

# ------ SSPS functions -----------
#the main recursive interpreter function
def interpretSPS(code, scope): 
    global index
    dictPush({}, index)
    index = 0
    for item in code:
        interprethelper(item, scope)
    end()
def interprethelper(token, scope):
    if isinstance(token, int) or isinstance(token, bool) or isinstance(token,list):
        opPush(token)

    elif token[0] == '/':
        opPush(token)

    elif helpers(token):
        if token == 'if' or token == 'ifelse' or token == 'repeat' or token == 'forall':
            temp = builtinopearators[token]
            temp(scope)
        else:
            builtinopearators[token]()
    else:
        temp = lookup(token,scope)
        if isinstance(temp, list):
            if (all(isinstance(x, int) for x in temp)):
                opPush(temp)
            else:
                interpretSPS(temp, scope)
        else:
            opPush(temp)
    

#parses the input string and calls the recursive interpreter to solve the
#program
def interpreter(s, scope):
    tokenL = parse(tokenize(s))
    interpretSPS(tokenL,scope)

#clears both stacks
def clearBoth():
    opstack[:] = []
    dictstack[:] = []

        
########################################################################
####  ASSIGNMENT 5 - SSPS TESTS
########################################################################

def sspsTests():
    testinput1 = """
    /x 4 def
    /g { x stack } def
    /f { /x 7 def g } def
    f
    """
    testinput2 = """
    /x 4 def
    [1 1 1] dup 1 [2 3] putinterval /arr exch def
    /g { x stack } def
    /f { 0 arr {7 mul add} forall /x exch def g } def
    f
    """
    testinput3 = """
    /m 50 def
    /n 100 def
    /egg1 {/m 25 def n} def
    /chic
    	{ /n 1 def
	      /egg2 { n stack} def
	      m  n
	      egg1
	      egg2
	    } def
    n
    chic
        """
    testinput4 = """
    /x 10 def
    /A { x } def
    /C { /x 40 def A stack } def
    /B { /x 30 def /A { x } def C } def
    B
    """
    testinput5 = """
    /x 10 def
    /n 5  def
    /A { 0  n {x add} repeat} def
    /C { /n 3 def /x 40 def A stack } def
    /B { /x 30 def /A { x } def C } def
    B
    """
    testinput6 = """
    /out true def 
    /xand { true eq {pop false} {true eq { false } { true } ifelse} ifelse dup /x exch def stack} def 
    /myput { out dup /x exch def xand } def 
    /f { /out false def myput } def 
    false f
    """
    testinput7 = """
    /x [1 2 3 4] def
    /A { x length } def
    /C { /x [10 20 30 40 50 60] def A stack } def
    /B { /x [6 7 8 9] def /A { x 0 get} def C } def
    B
    """
    testinput8 = """
    [0 1 2 3 4 5 6 7 8 9 10] 3 4 getinterval /x exch def
    /a 10 def  
    /A { x length } def
    /C { /x [a 2 mul a 3 mul dup a 4 mul] def A  a x stack } def
    /B { /x [6 7 8 9] def /A { x 0 get} def /a 5 def C } def
    B
    """

    additionTest1 = """
    /x 6 def
    /A { x stack} def
    /B { /x 5 def A } def
    /C { /x 4 def B } def
    /D { /x 3 def C } def
    /E { /x 2 def D } def
    /F { /x 1 def E } def
    F
    """

    additionTest2 = """
    /x [4 3 2 1] def
    /A { x length } def
    /C { /x [1 2 3 4 5 6] def A stack } def
    /B { /x [8 9 10 11] def /A { x 0 get} def C } def
    B
    """

    additionTest3 = """
    /x 2019 def
    /A { x } def
    /C { /x 2020 def A stack } def
    /B { /x 2021 def /A { x } def C } def
    B
    """
    ssps_testinputs = [testinput1, testinput2, testinput3, testinput4, testinput5, testinput6, testinput7, testinput8, additionTest1, additionTest2,additionTest3]
    i = 1
    for input in ssps_testinputs:
        print('TEST CASE -',i)
        i += 1
        print("Static")
        interpreter(input, 'static')
        clear()
        print("Dynamic")
        interpreter(input, 'dynamic')
        print('\n-----------------------------')
        clear()

if __name__=='__main__':
    sspsTests()
