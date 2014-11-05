__author__ = 'tianqilei'

from lexer_parser import parser
from tools import tools

blockTreeList=parser.blockTree_list
classTreeList=parser.classTree_list

def clacProduitSyn():
    allSynchronizations=tools.getAllSynchronizationOfBlock(blockTreeList[0])
    initStates=[]
    # non C !!!!!!!!!!!!!!!!!
    allDecls=tools.getAllDeclarationOfBlock(blockTreeList[0])
    #print(allDecls)
    for decl in allDecls:
        #print(decl)
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
#    print(allSynchronizations)

    # states which are already contained in product synchronized
    statesExistingOfPS=[]
    statesExistingOfPS.append(initStates)
    #new states of product synchronized : a new state is also a list
    newStatesOfPS=[]
    newStatesOfPS.append(initStates)
#    newStatesOfPS.append(1)
    #print(newStatesOfPS)
    # a list of transition like [(A,B) -> (A',B'), (A,B) -> (A',B)]
    produitSynchronized=[]
    # it might exist more than one new state
    for newState in newStatesOfPS:
        for synchronization in allSynchronizations:
            newStateTemp=[]
            if check(newState,synchronization) :
                print(newState)
                print(synchronization)
                print()


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