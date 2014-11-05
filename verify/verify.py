from lexer_parser import parser
from tools import tools

__author__ = 'tianqilei'
#print(data)
blockTreeList=parser.blockTree_list
classTreeList=parser.classTree_list


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

if tools.minus(allClassInBlock,allClass):
    print("ok")
