__author__ = 'tianqilei'

from lexer_parser import parser
from tools import tools

blockTreeList=parser.blockTree_list
classTreeList=parser.classTree_list
productSynchronized=[]
statesExistingOfPS=[]

def returnAllStatesOfPS():
    return statesExistingOfPS

def returnProductSynchronized():
    return productSynchronized

def clacProduitSyn():
    allSynchronizations=tools.getAllSynchronizationOfBlock(blockTreeList[0])
    initStates=[]
    allDecls=tools.getAllDeclarationOfBlock(blockTreeList[0])
    for decl in allDecls:
        for classTree in classTreeList:
            if decl[0] == tools.getNameOfClass(classTree):
                for instance in decl[1]:
                    temp=[]
                    temp.append(tools.getNameOfClass(classTree))
                    temp.append(tools.getInitStateOfClass(classTree))
                    temp.append(instance)
                    initStates.append(temp)
    #add the instance name to the list
    for synchronization in allSynchronizations:
        for syn in synchronization[1]:
            temp=tools.getClassNameOfInstanceOfBlock(syn[0], blockTreeList[0])
            syn.insert(0,temp)

    # states which are already contained in product synchronized
    statesExistingOfPS.append(initStates)

    #new states of product synchronized : a new state is also a list
    newStatesOfPS=[]
    newStatesOfPS.append(initStates)
    # a list of transition like [(A,B) -> (A',B'), (A,B) -> (A',B)]

    # it might exist more than one new state
    while 1 :
        oldStateExistingOfPS=[]
        oldStateExistingOfPS=statesExistingOfPS.copy()
        for newState in newStatesOfPS:
            for synchronization in allSynchronizations:
                newStateTemp=newState
                if check(newStateTemp,synchronization) :
                    res=[]
                    res = getNewState(newStateTemp,synchronization)
                    addToProductSyn(newStateTemp, synchronization, res, productSynchronized)
                    if not statesExistingOfPS.__contains__(res) :
                        statesExistingOfPS.append(res)
        newStatesOfPSNextTime=[]
        for stateExisting in statesExistingOfPS:
            if not oldStateExistingOfPS.__contains__(stateExisting) :
                newStatesOfPSNextTime.append(stateExisting)
        newStatesOfPS = newStatesOfPSNextTime
        if not newStatesOfPS :
            break

def addToProductSyn(state1, syn, state2, productSyn) :
    temp=[]
    temp.append(state1)
    temp.append(syn)
    temp.append(state2)
    productSyn.append(temp)

def getNewState(newState, synchronizaion):
    res=[]
    for state in newState:
        temp=state.copy()
        for syn in synchronizaion[1]:
            if temp[0]==syn[0] and temp[2]==syn[1] :
                transition=tools.getTransitionWithIdentifier(syn[2],syn[0],classTreeList)
                temp.insert(1,tools.transitOnlyForCalc(temp[1],transition))
                temp.remove(temp[2])
        res.append(temp)
    return res

def check(newState, synchronization):
    for syn in synchronization[1] :
        c=0
        for state in newState :
            # transition can be not correspond
            transition= tools.getTransitionWithIdentifier(syn[2],state[0],classTreeList)
            if transition != None :
                if state[1] == transition[1][0] and syn[2]==transition[0] and syn[0]==state[0]:
                    c=1
                    break
        if c!= 1:
            return False
    return True

def verifyReachabilityOfPoints():
    stateList=[]
    for blockTree in blockTreeList :
        for instanceList in tools.getAllDeclarationOfBlock(blockTree) :
            for instanceName in instanceList[1] :
                className=tools.getClassNameOfInstanceOfBlock(instanceName,blockTree)
                for classTree in classTreeList :
                    if tools.getNameOfClass(classTree) == className :
                        for stateOfClass in tools.getAllStateOfClass(classTree) :
                            temp=[]
                            temp.append(tools.getNameOfClass(classTree))
                            temp.append(stateOfClass)
                            temp.append(instanceName)
                            stateList.append(temp)
    for state in statesExistingOfPS :
        for stateToVerify in stateList :
            if state.__contains__(stateToVerify) :
                if stateList.__contains__(stateToVerify) :
                    stateList.remove(stateToVerify)
    return stateList

def getPath(stateOrigin, stateDest) :
    path=[]
    return path

#All reachable states can return to initial state
def remote(state, productSynchronized) :
    res = []
    for step in productSynchronized :
        if(step[0] == state) :
            res.append(step[2])
    return res

def addNoDuplicate(e, l) :
    if (not l.__contains__(e)) :
        l.append(e)

def addNoDuplicateList(l1, l2) :
    for e in l1 :
        addNoDuplicate(e, l2)

def remoteAll(state, productSynchronized) :
    res = remote(state, productSynchronized)
    newRes = []
    while res != newRes :
        newRes = res
        for i in res :
            resTemp = remote(i, productSynchronized)
            addNoDuplicateList(resTemp, newRes)
    return newRes

def verifyReinitializability(reachableState, productSynchronized):
    res = []
    initState = productSynchronized[0][0]
    for state in reachableState :
        if(state == initState) :
            continue
        l = remoteAll(state, productSynchronized)
        if(not l.__contains__(initState)) :
            res.append(state)
    return res
clacProduitSyn()

#print("remote")
#l=remoteAll([['Door', 'close', 'D'], ['Cabin', 'move', 'Ca'], ['Floor', 'f1', 'F'], ['Choice', 'c1', 'Ch']], productSynchronized)
#print(l)

# state : [['Door', 'open', 'D'], ['Cabin', 'stop', 'Ca'], ['Floor', 'f0', 'F'], ['Choice', 'c0', 'Ch']] s : ['Cabin', 'Ca', 'moving'] => stop
def getStateName(state, s) :
    for sn in state :
        if(sn[0] == s[0] and sn[2] == s[1]) :
            return sn[1]

def verifyDeadlock(reachableState) :
    res = []
    b=0
    c=0
    allSyn = tools.getAllSynchronizationOfBlock(blockTreeList[0])
    for state in reachableState:
        for syn in allSyn :
            for s in syn[1] :
                #print(s)
                transition = tools.getTransitionWithIdentifier(s[2],s[0],classTreeList)
                temp = getStateName(state,s)
                if (transition[1][0] != temp) :
                    b=1
                    break
            if(b==1):
                b=0
            else :
                c = c+1
        if(c >= 1) :
            c=0
            if (not res.__contains__(state)):
                res.append(state)
        b=0
    temp = []
    for s in reachableState :
        if(not res.__contains__(s)) :
            temp.append(s)
    return temp

def verifySafety(reachableState):
    stateUnsafy = []
    andList = []
    obList = []
    observers = tools.getObserversOfBlock(blockTreeList[0])
    for observer in observers :
        oneAnd = []
        for o in observer[1][0] :
            andTuple = []
            if (o[o.__len__()-1] == "or"):
                if(oneAnd != []):
                    andList.append(oneAnd)
                    oneAnd = []
                andTuple = []
                if(o[0] == "not") :
                    andTuple.append("not")
                    andTuple.append(o[1])
                    andTuple.append(o[2])
                    oneAnd.append(andTuple)
                    andTuple = []
                else :
                    andTuple.append(o[0])
                    andTuple.append(o[1])
                    oneAnd.append(andTuple)
                    andTuple= []
            elif (o[o.__len__()-1] == "and"):
                if(o[0] == "not"):
                    andTuple.append("not")
                    andTuple.append(o[1])
                    andTuple.append(o[2])
                    oneAnd.append(andTuple)
                    andTuple = []
                else :
                    andTuple.append(o[0])
                    andTuple.append(o[1])
                    oneAnd.append(andTuple)
                    andTuple = []
            else :
                if(o[0] != "not"):
                    andTuple.append(o[0])
                    andTuple.append(o[1])
                    oneAnd.append(andTuple.copy())
                    andTuple = []
                else :
                    andTuple.append("not")
                    andTuple.append(o[1])
                    andTuple.append(o[2])
                    oneAnd.append(andTuple.copy())
                    andTuple = []
        if(oneAnd != []) :
            andList.append(oneAnd)
        obList.append([observer[0],andList])
        andList = []
  #  for ob in obList :
   #     print(ob[1])
    stateSafy=[]
    for state in reachableState :
        for ob in obList :
            for os in ob[1] :
                oneAnd = os
                cpt = 0
                yes = 0
                for o in oneAnd :
                    for s in state :
                        if (o[0] != "not"):
                            if (o[0] == s[2]):
                                if(o[1] != s[1]) :
                                    break
                                else :
                                    cpt += 1
                        else :
                            if (o[1] == s[2]):
                                if(o[2] == s[1]) :
                                    break
                                else :
                                    cpt += 1
                    if (cpt == oneAnd.__len__()):
                        yes = yes + 1
                cpt=0
                if(yes >= 1):
                    if(not stateSafy.__contains__(state)):
                        stateSafy.append(state)
                yes = 0
    for state in reachableState :
        if (not stateSafy.__contains__(state)) :
            stateUnsafy.append(state)
    return stateUnsafy
