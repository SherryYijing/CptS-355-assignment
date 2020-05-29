opstack = []

def opPop():
    if len(opstack) > 0:
        return opstack.pop(-1)
    else:
        print("Error:zero element in opstack")

def opPush(value):
    return opstack.append(value)

dictstack = []

def dictPop():
    if (len(dictstack)>0):
        return dictstack.pop()

def dictPush(d):
    return dictstack.append(d)

def define(name, value):
    if dictstack != []:
        if isinstance(dictstack[-1],dict):
            dictstack[-1].update({name:value})
    else:
        newD = dict()
        newD.update({name:value})
        dictPush(newD)

def lookup(name):
    for d in reversed(dictstack):
        if d.get('/'+name):
            return d.get('/'+name)
    return None

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

def stack():
    if len(opstack) > 0:
        for op in opstack[::-1]:
            print(op)
    else:
        print("Error:zero element in opstack.")

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
