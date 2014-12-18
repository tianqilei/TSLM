__author__ = 'tianqilei'
from lexer_parser import parser
from tools import tools
from verify import calc
classTreeList=parser.classTree_list

def reachable(classTree):
    initState=tools.getInitStateOfClass(classTree)
    stateReachable=tools.getAllStateReachableWithOnlyOneTransition(initState, classTree)
    oldStates=[]
    stateReachableTemp=stateReachable
    while stateReachableTemp and stateReachableTemp!=oldStates:
        oldStates=stateReachable
        stateReachable=[]
        for state in oldStates:
            temp=tools.getAllStateReachableWithOnlyOneTransition(state, classTree)
            stateReachable=tools.insertState(stateReachable,temp)
        stateReachableTemp=tools.insertState(stateReachableTemp, stateReachable)
    allState=tools.getAllStateOfClass(classTree)
    allStateBesideInit=tools.minus(allState,[tools.getInitStateOfClass(classTree)])
    stateInreachable=tools.minus(allStateBesideInit, stateReachableTemp)
    print(stateInreachable)
def verifyReachable():
    for classTree in classTreeList:
        print("State(s) unreachable of class : " + tools.getNameOfClass(classTree))
        reachable(classTree)

def addToListWithNoDuplicate(list1,list2) :
    for element in list1 :
        if not list2.__contains__(element) :
            list2.append(element)


def verifyReachability() :
    stateVisit=[]
    initState=tools.getInitStateOfProductSynchronized(calc.productSynchronized)
    stateVisit.append(initState)

    newStates=tools.getAllReachableStateWithOnlyOneTransition(initState,calc.productSynchronized)
    while checkNewState(newStates, stateVisit) :
        addToListWithNoDuplicate(newStates,stateVisit)
        tempNewStates=[]
        for newState in newStates :
            tempNewStates.extend(tools.getAllReachableStateWithOnlyOneTransition(newState,calc.productSynchronized))
        newStates = tempNewStates
    return stateVisit

def checkNewState(newStates, stateVisit) :
    for state in newStates :
        if not stateVisit.__contains__(state) :
            return True
    return False