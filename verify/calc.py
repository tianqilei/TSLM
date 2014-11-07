__author__ = 'tianqilei'

from lexer_parser import parser
from tools import tools

blockTreeList=parser.blockTree_list
classTreeList=parser.classTree_list
productSynchronized=[]
statesExistingOfPS=[]
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
    c=0
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
#        print(statesExistingOfPS)
#        print()
        if not newStatesOfPS :
            break
#    print(productSynchronized)

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

'''def getNewState(newState, synchronizaion):
    for state in newState:
        for syn in synchronizaion[1]:
            if state[0]==syn[0] and state[2]==syn[1] :
                transition=tools.getTransitionWithIdentifier(syn[2],syn[0],classTreeList)
                state.insert(1,tools.transit(state[1],transition))
                state.remove(state[2])'''

def check(newState, synchronization):
    for syn in synchronization[1] :
        c=0
        for state in newState :
            transition= tools.getTransitionWithIdentifier(syn[2],state[0],classTreeList)
            if state[1] == transition[1][0] and syn[2]==transition[0] and syn[0]==state[0]:
                c=1
                break
        if c!= 1:
            return False
    return True


clacProduitSyn()

print(statesExistingOfPS)
print(productSynchronized)