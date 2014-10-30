from lexer_parser import parser

__author__ = 'tianqilei'
#print(data)
blockTreeList=parser.blockTree_list
classTreeList=parser.classTree_list

def minus(list1, list2):
    return list (set(list1)-set(list2))

def isClassOfBlockExists(class_list, classNameInBlock_list):
    print()

#vérifier
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

allClass=[]
for value in classTreeList:
    allClass.append(value[0])

allClassInBlock=[]
for value in blockTreeList:
    allClassInBlock.append(value[1][0][0])

print(allClass)
print(allClassInBlock)

if minus(allClassInBlock,allClass):
    print("ok")
