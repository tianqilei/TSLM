__author__ = 'tianqilei'
from lexer_parser import parser
from tools import tools
classTreeList = parser.classTree_list

# verify the events of class :
# events declared but not used -> Warning
# events used but not declared -> Error
def verifyEventOfClass(classTree):
    b=False
    c=False
    allEventDecl= tools.getAllEventOfClass(classTree)
    allTransition = tools.getAllTransitionOfClass(classTree)
    allStateInTransition=[]
    for transition in allTransition:
        allStateInTransition.append(transition[0])
    stateNotUsed=tools.minus(allEventDecl, allStateInTransition)
    if stateNotUsed:
        print("Warning : event not used in the class : " + tools.getNameOfClass(classTree))
        print(stateNotUsed)
        b=True

    stateNotDecl=tools.minus(allStateInTransition, allEventDecl)
    if stateNotDecl :
        print("Error event not declared in the class : " + tools.getNameOfClass(classTree))
        print(stateNotDecl)
        c=True

    return b and c

def verifyStateOfClass(classTree):
    b=False
    c=False
    allState = tools.getAllStateOfClass(classTree)
    allTransition=tools.getAllTransitionOfClass(classTree)
    stateInTransition=[]
    for transition in allTransition:
        stateInTransition=tools.insertState(stateInTransition,transition[1])
    stateNotUsed=tools.minus(allState, stateInTransition)
    stateNotDecl=tools.minus(stateInTransition, allState)
    if stateNotUsed:
        print("Warning : state not used in the class : " + tools.getNameOfClass(classTree))
        print(stateNotUsed)
        b=True
    if stateNotDecl:
        print("Error : state not declared in the class : " + tools.getNameOfClass(classTree))
        print(stateNotDecl)
        c=True
    return  b and c

def verifyEvent(classTreeList):
    for classTree in classTreeList:
        verifyEventOfClass(classTree)

def verifyState(classTreeList):
    for classTree in classTreeList:
        verifyStateOfClass(classTree)

verifyEvent(classTreeList)
verifyState(classTreeList)

