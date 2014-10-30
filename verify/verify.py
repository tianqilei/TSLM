from lexer_parser import parser

__author__ = 'tianqilei'
#print(data)
blockTreeList=parser.blockTree_list
classTreeList=parser.classTree_list

def minus(list1, list2):
    return list (set(list1)-set(list2))

def isClassOfBlockExists(class_list, classNameInBlock_list):
    print()

#vérifir
# si toutes les states sont déclarée
# si toutes les states sont util (déclaré, mais pas apparaitre dans transition)
def verifyStateOfClass():
    print()

def verifyClass():
    verifyStateOfClass()

def verifyBlock():
    print()

def verify():
    verifyClass()
    verifyBlock()

verify()



#debug
print("Block : ")
for value in blockTreeList:
    print(value)

print("Class : ")
for value in classTreeList:
    print(value)
