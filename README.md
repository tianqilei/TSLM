TSLM
====

projet bizzar :

travail à faire : 
1. ajouter OBSERVER
2. vérifier instance name non duplicate

eventInBlock_list=[] => ([blockName, classInstanceTuple list, eventInBlock list, eventInSynchronizationTuple list], [], …)
eventInClass_list=[(className, state list, event list, transitionTuple list), … ]

Door A, B
Door : ClassNameIdentifier
A,B : ClassInstanceIdentifier

block_list : une list contenant tous les noms des blocks
class_list : une list contenant tous les noms des classes
event_list : (dans class automate) une liste contenant tous les noms des events
event_InTransition : (dans class automate)…
className_list : (dans block automate) les noms des class déclaré dans un block
classInstance_list : les noms des instances dans un block
eventInEventPath_list et classInEventPath_list, par example, A.openning => classInEventPath.eventInEventPath

synchronization
  aopen : A.opening
  bopen : B.opening
  -> eventPathInSynchronization_list : [(A.opening),(B.opening)]


fais attention : dsvqdsvsd
class Door
state open, close
event opening, closing1
transition
opening: close -> open
closing2: open -> close
end

unsafe : dans une boucle, il y a pas d'arrêt sortant sauf ce qui pointe sur les point dans cette boucle



