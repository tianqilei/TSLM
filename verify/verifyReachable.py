__author__ = 'tianqilei'
from lexer_parser import parser
from tools import tools
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

for classTree in classTreeList:
    print("State(s) unreachable of class : " + tools.getNameOfClass(classTree))
    reachable(classTree)
