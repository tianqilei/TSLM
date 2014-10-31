__author__ = 'tianqilei'
from lexer_parser import parser
from tools import tools
classTreeList=parser.classTree_list

#print(classTreeList)

def containAll(list1, list2):
    for value in list2:
        if list1.__contains__(value):
            continue
        else:
            return False
    return True

def checkFixpoint(classTree):
    initStat=tools.getAllStateOfClass(classTree)[0]
    allPossibleState=tools.getAllStateReachableWithOnlyOneTransition(initStat,classTree)
    if allPossibleState:
        if allPossibleState.__contains__(initStat):
            print("check fix point result : true")
        else :
            oldRes=[]
            stateVisit=allPossibleState
            b=True
            while (not allPossibleState.__contains__(initStat)) and not containAll(oldRes, allPossibleState):
                oldRes=allPossibleState
                for state in oldRes:
                    allPossibleState=tools.insertState(allPossibleState,tools.getAllStateReachableWithOnlyOneTransition(state, classTree))
                if allPossibleState.__contains__(initStat) :
                    print("check fix point result : true")
                    b=False
                    break

            if b and oldRes == stateVisit:
                print("Warning : check fin point result : false")
    else:
        print("Warning : check fix point result : false")

for classTree in classTreeList:
    print("Class : " + tools.getNameOfClass(classTree))
    checkFixpoint(classTree)
