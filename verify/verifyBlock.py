__author__ = 'tianqilei'

from lexer_parser import parser
from tools import tools

blockTreeList=parser.blockTree_list
classTreeList=parser.classTree_list

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
    blockName = tools.getNameOfBlock(blockTree)
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
                print("Error : class " + value[0] +" in the synchronisation : "+ value[1] +" is not declared in block : " + blockName)


def verifySynchronization(blockTreeList, classTreeList):
    for blockTree in blockTreeList:
        verifySynchronizationOfBlock(blockTree, classTreeList)

#verifySynchronization(blockTreeList,classTreeList)

def verifyBlockNb(blockTreeList) :
    if(blockTreeList.__len__() != 1) :
        print("Error : you have more than one block !")

#verifyBlockNb(blockTreeList)

def verifyNomAmbigue():
    nameList = []
    for blockTree in blockTreeList :
        blockName = tools.getNameOfBlock(blockTree)
        declarations = tools.getAllDeclarationOfBlock(blockTree)
        for declaration in declarations :
            if(nameList.__contains__(declaration[1])) :
                #print("Error : The instance name : " + declaration[1] + " exist already in block " + blockName)
                print("No")
            else :
                nameList.append(declaration[1])

def verifyBlock():
    verifyBlockNb(blockTreeList)
    verifyEvent(blockTreeList)
    verifySynchronization(blockTreeList,classTreeList)
    verifyNomAmbigue()

verifyBlock()