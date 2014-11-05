__author__ = 'tianqilei'

from lexer_parser import parser
classTreeList=parser.classTree_list
# list1 - list2 : list1 va supprimer tous les éléments qui se trouve dans list2
def minus(list1, list2):
    return list (set(list1)-set(list2))

def getInitStateOfClass(classTree):
    return classTree[1][0]

def getNameOfClass(classTree):
    return classTree[0]

def getAllStateOfClass(classTree):
    return classTree[1]

def getAllEventOfClass(classTree):
    return classTree[2]

def getAllTransitionOfClass(classTree):
    return classTree[3]

def getNameOfBlock(blockTree):
    return blockTree[0]

def getAllDeclarationOfBlock(blockTree):
    return blockTree[1]

def getAllEventOfBlock(blockTree):
    return blockTree[2]

def getAllSynchronizationOfBlock(blockTree):
    return blockTree[3]

# a given state perform a given transition and return the destination state if the given state correspond the given transition
# for instance :
# transit(A, A->B) -> B
# transit(A, B->C) -> error
def transit(state, transition):
    states = transition[1]
    if state==states[0]:
        return states[1]
    else :
        print("log : error this state doesn't correspond the given transition")

#use only for calc.py
def transitOnlyForCalc(state, transition):
    states = transition[1]
    if state==states[0]:
        return states[1]
    else :
        state


# get all the possible transitions of a given state
# for instance :
# for state A, the possible transitions are : A->B, A->C, etc.
# but not sth like B->C
def getAllPossibleTransitionOfState(state, classTree):
    transitionList=[]
    allTransition=getAllTransitionOfClass(classTree)
    for transition in allTransition:
        if state==transition[1][0]:
            transitionList.append(transition)
    return transitionList

# get all reachable states of the given state with only one transition
# for example,
# state A; event A->B, A->C, B->C
# return [B,C]
def getAllStateReachableWithOnlyOneTransition(state, classTree):
    allReachableStates=[]
    allPossibleTransitions=getAllPossibleTransitionOfState(state,classTree)
    for transition in allPossibleTransitions:
        allReachableStates.append(transition[1][1])
    return allReachableStates

# insert states of list2 into list1, no same states
def insertState(list1, list2):
    for value in list2:
        if not list1.__contains__(value):
            list1.append(value)
    return list1

# return the class name of the given instance
def getClassNameOfInstanceOfBlock(instanceName, blockTree):
    allDecl=getAllDeclarationOfBlock(blockTree)
    for decl in allDecl:
        if decl[1].__contains__(instanceName):
            return decl[0]
    return False

# identifier : opening, className : Door1
def getTransitionWithIdentifier(identifier, className, classTreeList) :
    for classTree in classTreeList:
        if className == getNameOfClass(classTree):
            allTransitions=getAllTransitionOfClass(classTree)
            for transition in allTransitions:
                if transition[0]==identifier:
                    return transition
                else :
                    continue
        else :
            continue

