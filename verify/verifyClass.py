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
    return b and c

def verifyTransitionOfClass(classTree):
    className = tools.getNameOfClass(classTree)
    allTransitions = tools.getAllTransitionOfClass(classTree)
    allStates = tools.getAllStateOfClass(classTree)
    allEvents = tools.getAllEventOfClass(classTree)
    for transition in allTransitions:
        transitionName = transition[0]
        transitionContent = transition[1]
        if(not allEvents.__contains__(transitionName)):
            print("Error : transition identifier : " + transitionName + " used, but not declared in class : " + className)
        for content in transitionContent:
            if (not allStates.__contains__(content)) :
                print("Error : state : " + content +" used, but not declared in class : " + className)


def usability(classTree):
    Allstates=tools.getAllStateOfClass(classTree)
    AllTransition=tools.getAllTransitionOfClass(classTree)
    UsedStates=[]
    for value in AllTransition:
        UsedStates.extend(value[1])
    UsedStates = list(set(UsedStates))
    UnUsedStates=[]
    UnUsedStates=tools.minus(Allstates, UsedStates)
    if (UnUsedStates) :
        print("Warning: states declared but not used")
        print(UnUsedStates)
    NotDeclaredStates=[]
    NotDeclaredStates=tools.minus(UsedStates,Allstates)
    if (NotDeclaredStates):
        print("Error: states used but not declared")
        print(NotDeclaredStates)

def verifyUsability():
    for classTree in classTreeList:
        usability(classTree)

def verifyEvent(classTreeList):
    for classTree in classTreeList:
        verifyEventOfClass(classTree)

def verifyState(classTreeList):
    for classTree in classTreeList:
        verifyStateOfClass(classTree)

def verifyTransition(classTreeList):
    for classTree in classTreeList:
        verifyTransitionOfClass(classTree)

def verifyClass() :
    verifyEvent(classTreeList)
    verifyState(classTreeList)
    verifyTransition(classTreeList)
    verifyUsability()

verifyClass()
