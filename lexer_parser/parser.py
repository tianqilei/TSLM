from lexer_parser import lexer
import ply.yacc as yacc

__author__ = 'fae'

tokens = lexer.tokens # Need token list

block_list=[]
class_list=[]
event_list=[]
state_list=[]
eventInTransition_list=[]
className_list=[]
classInstance_list=[]
eventInEventPath_list=[]
classInEventPath_list=[]
originalStateInTransition_list=[]
destStateInTransition_list=[]
eventInSynchronisation_list=[]
eventPathInSynchronization_list=[]
eventInBlock_list=[]
eventInClass_list=[]

blockTree_list=[]
classTree_list=[]
classInstanceTuple_list=[]
eventInSynchronizationTuple_list=[]
transitionTuple_list=[]
classNameInstanceTuple=[]
def p_empty(p):
    'empty :'
    pass

def p_Identifier(p):
    '''Identifier : IDENTIFIER'''
    print("if this string printed, it means there is sth wrong with Identifier : ", p[1])
def p_ClassIdentifier(p):
    '''ClassIdentifier : IDENTIFIER'''
    class_list.append(p[1])

def p_BlockIdentifier(p):
    '''BlockIdentifier : IDENTIFIER'''
    block_list.append(p[1])

#à quoi ça sert? inutile?
#def p_PointIdentifierStar(p):
#    '''PointIdentifierStar : empty
#                           | POINT Identifier PointIdentifierStar'''

#Est-ce qu'on peut faire "block.openning", par example?
# si oui, chager ClassIdentifier à ModelIdentifier en ajoutant :
# p_ModelIdentifier(p):
# '''ModelIdentifier : ClassIdentifier
#                    | BlockIdentifier'''
# après ajouter p_ClassIdentifier et p_BlockIdentifier pour distinguer
# si non, laisse tomber

#replace-back begin
def p_EventPath(p):
    '''EventPath : IDENTIFIER POINT IDENTIFIER'''
    tab = ([p[1],p[3]])
    eventPathInSynchronization_list.append(tab)
#replace-back end

#back begin
#def p_EventPath(p):
#    '''EventPath : ClassIdentifierInEvenPath POINT EventIdentifierInEventPath'''

#def p_ClassIdentifierInEvenPath(p):
#    '''ClassIdentifierInEvenPath : IDENTIFIER'''
#    classInEventPath_list.append(p[1])

#def p_EventIdentifierInEventPath(p):
#    '''EventIdentifierInEventPath : IDENTIFIER'''
#    eventInEventPath_list.append(p[1])
#back end

def p_AndCommercialEvenPathStar(p):
    '''AndCommercialEvenPathStar : empty
                                 | ANDCOMMERCIAL EventPath AndCommercialEvenPathStar'''

def p_MacroEventDefinition(p):
    '''MacroEventDefinition : EventIdentifierInSynchronization DEUXPOINTS EventPath AndCommercialEvenPathStar'''
    eventInSynchronizationTuple=[]
    eventInSynchronizationTuple.append(eventInSynchronisation_list.pop())
    eventInSynchronizationTuple.append(eventPathInSynchronization_list.copy())
    eventInSynchronizationTuple_list.append(eventInSynchronizationTuple.copy())
    eventInSynchronisation_list.clear()
    eventPathInSynchronization_list.clear()

def p_EventIdentifierInSynchronization(p):
    '''EventIdentifierInSynchronization : IDENTIFIER'''
    eventInSynchronisation_list.append(p[1])

def p_Synchronization(p):
    '''Synchronization : MacroEventDefinition'''

def p_SynchronizationStar(p):
    '''SynchronizationStar : empty
                           | Synchronization SynchronizationStar'''

def p_SynchronizationClause(p):
    '''SynchronizationClause : SYNCHRONIZATION SynchronizationStar'''

def p_ClassNameIdentifier(p):
    '''ClassNameIdentifier : IDENTIFIER'''
    className_list.append(p[1])

def p_ClassInstanceIdentifier(p) :
    '''ClassInstanceIdentifier : IDENTIFIER'''
    classInstance_list.append(p[1])

def p_ClassInstanceVirguleIdentifierStar(p):
    '''ClassInstanceVirguleIdentifierStar : empty
                             | VIRGULE ClassInstanceIdentifier ClassInstanceVirguleIdentifierStar'''

#dans quel cas on est la?!
def p_ClassInstance(p):
    '''ClassInstance : ClassNameIdentifier ClassInstanceIdentifier ClassInstanceVirguleIdentifierStar'''
    classNameInstanceTuple.append(className_list.pop())
    classNameInstanceTuple.append(classInstance_list.copy())
    className_list.clear()
    classInstance_list.clear()
    classInstanceTuple_list.append(classNameInstanceTuple.copy())
    classNameInstanceTuple.clear()
    className_list.clear()
    classInstance_list.clear()

def p_ComposedBlockClause(p):
    '''ComposedBlockClause : Block
                           | ClassInstance
                           | Block ComposedBlockClause
                           | ClassInstance ComposedBlockClause'''


def p_StateIdentifier(p):
    '''StateIdentifier : IDENTIFIER'''
    state_list.append(p[1])

#def p_EventIdentifier(p):
#    '''EventIdentifier : IDENTIFIER'''
#    event_list.append(p[1])

def p_Transition(p):
    '''Transition : EventIdentifierInTransition DEUXPOINTS OriginalStateIdentifierInTransition FLECHE DestStateIdentifierInTransition'''

def p_OriginalStateIdentifierInTransition(p):
    '''OriginalStateIdentifierInTransition : IDENTIFIER'''
    originalStateInTransition_list.append(p[1])

def p_DestStateIdentifierInTransition(p):
    '''DestStateIdentifierInTransition : IDENTIFIER'''
    destStateInTransition_list.append(p[1])

def p_EventIdentifierInTransition(p):
    '''EventIdentifierInTransition : IDENTIFIER'''
    eventInTransition_list.append(p[1])

def p_TransitionStar(p):
    '''TransitionStar : empty
                      | Transition TransitionStar'''

def p_TransitionClause(p):
    '''TransitionClause : TRANSITION TransitionStar'''

def p_EventClauseInClass(p):
    '''EventClauseInClass : EVENT EventIdentifierInClass EventVirguleIdentifierStarInClass'''

def p_EventIdentifierInClass(p):
    '''EventIdentifierInClass : IDENTIFIER'''
    eventInClass_list.append(p[1])

def p_EventClauseInBlock(p):
    '''EventClauseInBlock : EVENT EventIdentifierInBlock EventVirguleIdentifierStarInBlock'''

def p_EventVirguleIdentifierStarInBlock(p):
    '''EventVirguleIdentifierStarInBlock : empty
                                            | VIRGULE EventIdentifierInBlock EventVirguleIdentifierStarInBlock'''

def p_EventIdentifierInBlock(p):
    '''EventIdentifierInBlock : IDENTIFIER'''
    eventInBlock_list.append(p[1])

def p_StateClause(p):
    '''StateClause : STATE StateIdentifier StateVirguleIdentifierStar'''

def p_EventVirguleIdentifierStarInClass(p):
    '''EventVirguleIdentifierStarInClass : empty
                                    | VIRGULE EventIdentifierInClass EventVirguleIdentifierStarInClass'''

def p_StateVirguleIdentifierStar(p):
    '''StateVirguleIdentifierStar : empty
                                    | VIRGULE StateIdentifier StateVirguleIdentifierStar'''

def p_ObserverStar(p):
    '''ObserverStar : empty
    '''

def p_ObserverClauseQuestionMark(p) :
    '''ObserverClauseQuestionMark : empty
                                    | OBSERVER ObserverStar'''

def p_InternalBlockBody(p):
    '''InternalBlockBody : ComposedBlockClause EventClauseInBlock SynchronizationClause ObserverClauseQuestionMark'''


def p_BasicBlockBody(p):
    '''BasicBlockBody : StateClause EventClauseInClass TransitionClause ObserverClauseQuestionMark'''


def p_BlockBody(p):
        '''BlockBody : BasicBlockBody
                 | InternalBlockBody'''

#observer?
def p_EndBlock(p):
    '''EndBlock : END'''
    blockTreeTuple=[]
    blockName=block_list.pop()
    blockTreeTuple.append(blockName)
    blockTreeTuple.append(classInstanceTuple_list.copy())
    blockTreeTuple.append(eventInBlock_list.copy())
    blockTreeTuple.append(eventInSynchronizationTuple_list.copy())
    blockTree_list.append(blockTreeTuple)
    block_list.clear()
    classInstanceTuple_list.clear()
    eventInBlock_list.clear()
    eventInSynchronizationTuple_list.clear()

def p_EndClass(p):
    '''EndClass : END'''
    classTreeTuple=[]
    transitionTuple_list=[]
    className=class_list.pop()
    classTreeTuple.append(className)
    classTreeTuple.append(state_list.copy())
    classTreeTuple.append(eventInClass_list.copy())
    oLen = originalStateInTransition_list.__len__()
    dLen = destStateInTransition_list.__len__()
    eLen = eventInTransition_list.__len__()
    if oLen == dLen == eLen:
        for index in range(oLen):
            transitionTuple=[]
            transitionTuple.append(eventInTransition_list[index])
            transitionTuple.append([originalStateInTransition_list[index], destStateInTransition_list[index]])
            transitionTuple_list.append(transitionTuple)
    else:
        print("oLen, dLen, eLen : problem with transition in the class " + className)
    classTreeTuple.append(transitionTuple_list.copy())
    classTree_list.append(classTreeTuple)
    state_list.clear()
    eventInClass_list.clear()
    class_list.clear()
    originalStateInTransition_list.clear()
    destStateInTransition_list.clear()
    eventInTransition_list.clear()

def p_Class(p):
    '''Class : CLASS ClassIdentifier BlockBody EndClass'''

#If ne faut pas ajouter BlockIdentifier dans une liste, pg il est just un symbole qui n'est pas encore reduce
def p_Block(p):
    '''Block : BLOCK BlockIdentifier BlockBody EndBlock'''

def p_Model(p):
    '''Model : Block Model
             | Class Model
             | empty'''

def p_error(t):
    print("parse : Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)


file = open("../data/automate.txt")
data=''
while 1:
    line = file.readline()
    if not line:
        break
    data += line

#print(data)

yacc.yacc(start = 'Model')
yacc.parse(data)


#debug

'''print("When there is WARNING about 'Identifier' not used, it means this program is OK, if no WARNING, it means we left somewhere 'Identifier'")
for value in block_list:
    print ("block identifier: " + value)

for value in class_list:
    print ("class identifier : " + value)

for value in eventInBlock_list :
    print("event identifier in block : " + value)

for value in eventInClass_list :
    print("event identifier in class : " + value)

for value in state_list:
    print ("state identifier : " + value)

for value in eventInTransition_list:
    print("event identifier in transition : " + value)

for value in className_list:
    print("class name identifier : " + value)

for value in classInstance_list:
    print("class instance identifier : " + value)

for value in eventInEventPath_list:
    print("event identifier in EventPath : " + value)

for value in classInEventPath_list:
    print("class instance identifier in EventPath : " + value)

for value in originalStateInTransition_list:
    print("original state in transition : " + value)

for value in destStateInTransition_list:
    print("dest state in transition : " + value)

for value in eventInSynchronisation_list :
    print("event identifier in synchronization : " + value)

for value in eventPathInSynchronization_list:
    print("EventPath identifier in synchronization : " + value[0],value[1])'''

#fais attention au Identifier !!!