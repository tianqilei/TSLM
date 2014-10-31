__author__ = 'cyrine horchani'
from lexer_parser import parser
from tools import tools
classTreeList=parser.classTree_list

def usability(classTree):
    Allstates=tools.getAllStateOfClass(classTree)
    print("Declared states")
    print(Allstates)
    AllTransition=tools.getAllTransitionOfClass(classTree)
    print("Used states")
    UsedStates=[]
    for value in AllTransition:
        UsedStates.extend(value[1])
    UsedStates = list(set(UsedStates))
    print(UsedStates)
    UnUsedStates=[]
    UnUsedStates=tools.minus(Allstates, UsedStates)
    print("Warning: state declared but not used")
    print(UnUsedStates)
    NotDeclaredStates=[]
    NotDeclaredStates=tools.minus(UsedStates,Allstates)
    print("Error: state used but not declared")
    print(NotDeclaredStates)

for classTree in classTreeList:
    print("Usability of class : " + tools.getNameOfClass(classTree))
    usability(classTree)
