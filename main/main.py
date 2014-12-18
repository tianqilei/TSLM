__author__ = 'tianqilei'

from verify import verifyClass
from verify import verifyBlock
from verify import calc, verifyReachable
#print(calc.productSynchronized)

reachableStates = verifyReachable.verifyReachability()
#for state in reachableStates :
#    print(state)
#    print()

re = calc.verifyReinitializability(reachableStates, calc.productSynchronized)
if(re) :
    print("State not reinitialisable : ")
    for state in re :
        print(state)

deadlock = calc.verifyDeadlock(reachableStates)
if(deadlock):
    print("Deadlock : ")
    for state in deadlock :
        print(state)

obres = calc.verifySafety(reachableStates)
if(obres):
    print("state safe : ")
    for o in obres :
        print(o)
