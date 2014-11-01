__author__ = 'tianqilei'

from lexer_parser import parser
from tools import tools

blockTreeList=parser.blockTree_list
classTreeList=parser.classTree_list

def usability(classTree):
    Allstates=tools.getAllStateOfClass(classTree)
    AllTransition=tools.getAllTransitionOfClass(classTree)
    UsedStates=[]
    for value in AllTransition:
        UsedStates.extend(value[1])
    UsedStates = list(set(UsedStates))
    UnUsedStates=[]
    UnUsedStates=tools.minus(Allstates, UsedStates)
    print("Warning: states declared but not used")
    print(UnUsedStates)
    NotDeclaredStates=[]
    NotDeclaredStates=tools.minus(UsedStates,Allstates)
    print("Error: states used but not declared")
    print(NotDeclaredStates)

def verifyUsability(classTree):
    for classTree in classTreeList:
        print("Usability of class : " + tools.getNameOfClass(classTree))
        usability(classTree)

def verifyEventOfBlock(blockTree):
    b=False
    c=False
    allEventDecl= tools.getAllEventOfBlock(blockTree)
    allSynchronization = tools.getAllSynchronizationOfBlock(blockTree)
    allEventInSynchronization=[]
    for synchronization in allSynchronization:
        allEventInSynchronization.append(synchronization[0])
    eventNotUsed=tools.minus(allEventDecl, allEventInSynchronization)
    if eventNotUsed:
        print("Warning : event not used in the block : " + tools.getNameOfBlock(blockTree))
        print(eventNotUsed)
        b=True

    stateNotDecl=tools.minus(allEventInSynchronization, allEventDecl)
    if stateNotDecl :
        print("Error event not declared in the block : " + tools.getNameOfClass(blockTree))
        print(stateNotDecl)
        c=True

    return b and c

def verifyEvent(blockTreeList):
    for blockTree in blockTreeList:
        verifyEventOfBlock(blockTree)

#verifyEvent(blockTreeList)

def verifySynchronizationOfBlock(blockTree, classTreeList):
    allSynchronization=tools.getAllSynchronizationOfBlock(blockTree)
    for synchronization in allSynchronization:
        for value in synchronization[1]:
            className=tools.getClassNameOfInstanceOfBlock(value[0],blockTree)
            if className != False:
                for classTree in classTreeList:
                    classN=tools.getNameOfClass(classTree)
                    if className==classN:
                        allEvent=tools.getAllEventOfClass(classTree)
                        if not allEvent.__contains__(value[1]) :
                            print("Error : Event : "+value[1]+" in class : "+className+" doesn't exist")
            else :
                print("Error : class not declared")

def verifySynchronization(blockTreeList, classTreeList):
    for blockTree in blockTreeList:
        verifySynchronizationOfBlock(blockTree, classTreeList)

verifySynchronization(blockTreeList,classTreeList)
