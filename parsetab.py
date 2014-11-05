
# parsetab.py
# This file is automatically generated. Do not edit.
_tabversion = '3.2'

_lr_method = 'LALR'

_lr_signature = b'\xa4J\xe3\x14\xedw]\xc6\xd8\x06\xde\x16"wy\xd3'
    
_lr_action_items = {'TRANSITION':([29,41,42,53,55,76,85,],[43,-32,-1,-31,-38,-1,-39,]),'POINT':([89,],[95,]),'VIRGULE':([26,27,34,35,41,42,47,48,52,74,76,83,],[-15,39,-23,51,-32,54,-36,72,39,51,54,72,]),'CLASS':([0,2,6,24,25,36,37,],[5,5,5,-49,-52,-51,-50,]),'BLOCK':([0,2,6,8,9,10,11,17,18,24,25,26,27,36,37,38,40,52,75,],[4,4,4,-4,4,4,-3,4,4,-49,-52,-15,-1,-51,-50,-16,-18,-1,-17,]),'IDENTIFIER':([4,5,8,9,10,11,14,15,17,18,21,24,25,26,27,28,33,38,39,40,43,46,51,52,54,60,69,70,72,75,77,81,88,91,92,93,94,95,96,97,98,99,100,],[8,11,-4,14,14,-3,-14,26,14,14,34,-49,-52,-15,-1,41,47,-16,26,-18,59,68,34,-1,41,59,-10,68,47,-17,86,89,-1,96,-6,-8,89,99,-26,-24,-1,-5,-7,]),'DEUXPOINTS':([58,59,66,68,],[77,-27,81,-9,]),'END':([13,19,22,23,43,44,45,46,56,57,60,61,62,63,64,65,67,69,70,78,79,80,82,88,92,93,96,97,98,99,100,],[24,-47,-48,37,-1,-1,-1,-1,-30,-28,-1,-43,-1,-46,-45,-11,-13,-10,-1,-29,-42,-44,-12,-1,-6,-8,-26,-24,-1,-5,-7,]),'FLECHE':([86,87,],[-25,91,]),'STATE':([8,9,10,11,],[-4,21,21,-3,]),'OBSERVER':([43,44,45,46,56,57,60,65,67,69,70,78,82,88,92,93,96,97,98,99,100,],[-1,62,62,-1,-30,-28,-1,-11,-13,-10,-1,-29,-12,-1,-6,-8,-26,-24,-1,-5,-7,]),'SYNCHRONIZATION':([32,47,48,71,73,83,90,],[46,-36,-1,-33,-34,-1,-35,]),'EVENT':([16,17,18,20,24,25,26,27,30,31,34,35,38,40,49,50,52,74,75,84,],[28,-20,-19,33,-49,-52,-15,-1,-22,-21,-23,-1,-16,-18,-40,-37,-1,-1,-17,-41,]),'$end':([0,1,2,3,6,7,12,24,25,36,37,],[-1,-55,-1,0,-1,-54,-53,-49,-52,-51,-50,]),'ANDCOMMERCIAL':([88,98,99,],[94,94,-5,]),}

_lr_action = { }
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = { }
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'BlockBody':([9,10,],[13,23,]),'empty':([0,2,6,27,35,42,43,44,45,46,48,52,60,62,70,74,76,83,88,98,],[1,1,1,38,49,55,57,61,61,65,73,38,57,79,65,49,55,73,92,92,]),'StateIdentifier':([21,51,],[35,74,]),'EventIdentifierInSynchronization':([46,70,],[66,66,]),'EventClauseInBlock':([20,],[32,]),'MacroEventDefinition':([46,70,],[69,69,]),'EventVirguleIdentifierStarInClass':([42,76,],[53,85,]),'ClassNameIdentifier':([9,10,17,18,],[15,15,15,15,]),'EventIdentifierInClass':([28,54,],[42,76,]),'StateVirguleIdentifierStar':([35,74,],[50,84,]),'ClassIdentifier':([5,],[10,]),'EventVirguleIdentifierStarInBlock':([48,83,],[71,90,]),'Model':([0,2,6,],[3,7,12,]),'ClassInstance':([9,10,17,18,],[17,17,17,17,]),'TransitionClause':([29,],[44,]),'EndClass':([23,],[36,]),'EndBlock':([13,],[25,]),'Synchronization':([46,70,],[70,70,]),'Transition':([43,60,],[60,60,]),'Block':([0,2,6,9,10,17,18,],[6,6,6,18,18,18,18,]),'ObserverClauseQuestionMark':([44,45,],[63,64,]),'SynchronizationClause':([32,],[45,]),'OriginalStateIdentifierInTransition':([77,],[87,]),'BasicBlockBody':([9,10,],[19,19,]),'ClassInstanceIdentifier':([15,39,],[27,52,]),'BlockIdentifier':([4,],[9,]),'EventClauseInClass':([16,],[29,]),'TransitionStar':([43,60,],[56,78,]),'ComposedBlockClause':([9,10,17,18,],[20,20,30,31,]),'ClassInstanceVirguleIdentifierStar':([27,52,],[40,75,]),'ObserverStar':([62,],[80,]),'Class':([0,2,6,],[2,2,2,]),'SynchronizationStar':([46,70,],[67,82,]),'DestStateIdentifierInTransition':([91,],[97,]),'EventPath':([81,94,],[88,98,]),'EventIdentifierInTransition':([43,60,],[58,58,]),'AndCommercialEvenPathStar':([88,98,],[93,100,]),'EventIdentifierInBlock':([33,72,],[48,83,]),'InternalBlockBody':([9,10,],[22,22,]),'StateClause':([9,10,],[16,16,]),}

_lr_goto = { }
for _k, _v in _lr_goto_items.items():
   for _x,_y in zip(_v[0],_v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = { }
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> Model","S'",1,None,None,None),
  ('empty -> <empty>','empty',0,'p_empty','/Users/tianqilei/PycharmProjects/TSLM/lexer_parser/parser.py',31),
  ('Identifier -> IDENTIFIER','Identifier',1,'p_Identifier','/Users/tianqilei/PycharmProjects/TSLM/lexer_parser/parser.py',35),
  ('ClassIdentifier -> IDENTIFIER','ClassIdentifier',1,'p_ClassIdentifier','/Users/tianqilei/PycharmProjects/TSLM/lexer_parser/parser.py',38),
  ('BlockIdentifier -> IDENTIFIER','BlockIdentifier',1,'p_BlockIdentifier','/Users/tianqilei/PycharmProjects/TSLM/lexer_parser/parser.py',42),
  ('EventPath -> IDENTIFIER POINT IDENTIFIER','EventPath',3,'p_EventPath','/Users/tianqilei/PycharmProjects/TSLM/lexer_parser/parser.py',60),
  ('AndCommercialEvenPathStar -> empty','AndCommercialEvenPathStar',1,'p_AndCommercialEvenPathStar','/Users/tianqilei/PycharmProjects/TSLM/lexer_parser/parser.py',79),
  ('AndCommercialEvenPathStar -> ANDCOMMERCIAL EventPath AndCommercialEvenPathStar','AndCommercialEvenPathStar',3,'p_AndCommercialEvenPathStar','/Users/tianqilei/PycharmProjects/TSLM/lexer_parser/parser.py',80),
  ('MacroEventDefinition -> EventIdentifierInSynchronization DEUXPOINTS EventPath AndCommercialEvenPathStar','MacroEventDefinition',4,'p_MacroEventDefinition','/Users/tianqilei/PycharmProjects/TSLM/lexer_parser/parser.py',83),
  ('EventIdentifierInSynchronization -> IDENTIFIER','EventIdentifierInSynchronization',1,'p_EventIdentifierInSynchronization','/Users/tianqilei/PycharmProjects/TSLM/lexer_parser/parser.py',92),
  ('Synchronization -> MacroEventDefinition','Synchronization',1,'p_Synchronization','/Users/tianqilei/PycharmProjects/TSLM/lexer_parser/parser.py',96),
  ('SynchronizationStar -> empty','SynchronizationStar',1,'p_SynchronizationStar','/Users/tianqilei/PycharmProjects/TSLM/lexer_parser/parser.py',99),
  ('SynchronizationStar -> Synchronization SynchronizationStar','SynchronizationStar',2,'p_SynchronizationStar','/Users/tianqilei/PycharmProjects/TSLM/lexer_parser/parser.py',100),
  ('SynchronizationClause -> SYNCHRONIZATION SynchronizationStar','SynchronizationClause',2,'p_SynchronizationClause','/Users/tianqilei/PycharmProjects/TSLM/lexer_parser/parser.py',103),
  ('ClassNameIdentifier -> IDENTIFIER','ClassNameIdentifier',1,'p_ClassNameIdentifier','/Users/tianqilei/PycharmProjects/TSLM/lexer_parser/parser.py',106),
  ('ClassInstanceIdentifier -> IDENTIFIER','ClassInstanceIdentifier',1,'p_ClassInstanceIdentifier','/Users/tianqilei/PycharmProjects/TSLM/lexer_parser/parser.py',110),
  ('ClassInstanceVirguleIdentifierStar -> empty','ClassInstanceVirguleIdentifierStar',1,'p_ClassInstanceVirguleIdentifierStar','/Users/tianqilei/PycharmProjects/TSLM/lexer_parser/parser.py',114),
  ('ClassInstanceVirguleIdentifierStar -> VIRGULE ClassInstanceIdentifier ClassInstanceVirguleIdentifierStar','ClassInstanceVirguleIdentifierStar',3,'p_ClassInstanceVirguleIdentifierStar','/Users/tianqilei/PycharmProjects/TSLM/lexer_parser/parser.py',115),
  ('ClassInstance -> ClassNameIdentifier ClassInstanceIdentifier ClassInstanceVirguleIdentifierStar','ClassInstance',3,'p_ClassInstance','/Users/tianqilei/PycharmProjects/TSLM/lexer_parser/parser.py',119),
  ('ComposedBlockClause -> Block','ComposedBlockClause',1,'p_ComposedBlockClause','/Users/tianqilei/PycharmProjects/TSLM/lexer_parser/parser.py',130),
  ('ComposedBlockClause -> ClassInstance','ComposedBlockClause',1,'p_ComposedBlockClause','/Users/tianqilei/PycharmProjects/TSLM/lexer_parser/parser.py',131),
  ('ComposedBlockClause -> Block ComposedBlockClause','ComposedBlockClause',2,'p_ComposedBlockClause','/Users/tianqilei/PycharmProjects/TSLM/lexer_parser/parser.py',132),
  ('ComposedBlockClause -> ClassInstance ComposedBlockClause','ComposedBlockClause',2,'p_ComposedBlockClause','/Users/tianqilei/PycharmProjects/TSLM/lexer_parser/parser.py',133),
  ('StateIdentifier -> IDENTIFIER','StateIdentifier',1,'p_StateIdentifier','/Users/tianqilei/PycharmProjects/TSLM/lexer_parser/parser.py',137),
  ('Transition -> EventIdentifierInTransition DEUXPOINTS OriginalStateIdentifierInTransition FLECHE DestStateIdentifierInTransition','Transition',5,'p_Transition','/Users/tianqilei/PycharmProjects/TSLM/lexer_parser/parser.py',145),
  ('OriginalStateIdentifierInTransition -> IDENTIFIER','OriginalStateIdentifierInTransition',1,'p_OriginalStateIdentifierInTransition','/Users/tianqilei/PycharmProjects/TSLM/lexer_parser/parser.py',148),
  ('DestStateIdentifierInTransition -> IDENTIFIER','DestStateIdentifierInTransition',1,'p_DestStateIdentifierInTransition','/Users/tianqilei/PycharmProjects/TSLM/lexer_parser/parser.py',152),
  ('EventIdentifierInTransition -> IDENTIFIER','EventIdentifierInTransition',1,'p_EventIdentifierInTransition','/Users/tianqilei/PycharmProjects/TSLM/lexer_parser/parser.py',156),
  ('TransitionStar -> empty','TransitionStar',1,'p_TransitionStar','/Users/tianqilei/PycharmProjects/TSLM/lexer_parser/parser.py',160),
  ('TransitionStar -> Transition TransitionStar','TransitionStar',2,'p_TransitionStar','/Users/tianqilei/PycharmProjects/TSLM/lexer_parser/parser.py',161),
  ('TransitionClause -> TRANSITION TransitionStar','TransitionClause',2,'p_TransitionClause','/Users/tianqilei/PycharmProjects/TSLM/lexer_parser/parser.py',164),
  ('EventClauseInClass -> EVENT EventIdentifierInClass EventVirguleIdentifierStarInClass','EventClauseInClass',3,'p_EventClauseInClass','/Users/tianqilei/PycharmProjects/TSLM/lexer_parser/parser.py',167),
  ('EventIdentifierInClass -> IDENTIFIER','EventIdentifierInClass',1,'p_EventIdentifierInClass','/Users/tianqilei/PycharmProjects/TSLM/lexer_parser/parser.py',170),
  ('EventClauseInBlock -> EVENT EventIdentifierInBlock EventVirguleIdentifierStarInBlock','EventClauseInBlock',3,'p_EventClauseInBlock','/Users/tianqilei/PycharmProjects/TSLM/lexer_parser/parser.py',174),
  ('EventVirguleIdentifierStarInBlock -> empty','EventVirguleIdentifierStarInBlock',1,'p_EventVirguleIdentifierStarInBlock','/Users/tianqilei/PycharmProjects/TSLM/lexer_parser/parser.py',177),
  ('EventVirguleIdentifierStarInBlock -> VIRGULE EventIdentifierInBlock EventVirguleIdentifierStarInBlock','EventVirguleIdentifierStarInBlock',3,'p_EventVirguleIdentifierStarInBlock','/Users/tianqilei/PycharmProjects/TSLM/lexer_parser/parser.py',178),
  ('EventIdentifierInBlock -> IDENTIFIER','EventIdentifierInBlock',1,'p_EventIdentifierInBlock','/Users/tianqilei/PycharmProjects/TSLM/lexer_parser/parser.py',181),
  ('StateClause -> STATE StateIdentifier StateVirguleIdentifierStar','StateClause',3,'p_StateClause','/Users/tianqilei/PycharmProjects/TSLM/lexer_parser/parser.py',185),
  ('EventVirguleIdentifierStarInClass -> empty','EventVirguleIdentifierStarInClass',1,'p_EventVirguleIdentifierStarInClass','/Users/tianqilei/PycharmProjects/TSLM/lexer_parser/parser.py',188),
  ('EventVirguleIdentifierStarInClass -> VIRGULE EventIdentifierInClass EventVirguleIdentifierStarInClass','EventVirguleIdentifierStarInClass',3,'p_EventVirguleIdentifierStarInClass','/Users/tianqilei/PycharmProjects/TSLM/lexer_parser/parser.py',189),
  ('StateVirguleIdentifierStar -> empty','StateVirguleIdentifierStar',1,'p_StateVirguleIdentifierStar','/Users/tianqilei/PycharmProjects/TSLM/lexer_parser/parser.py',192),
  ('StateVirguleIdentifierStar -> VIRGULE StateIdentifier StateVirguleIdentifierStar','StateVirguleIdentifierStar',3,'p_StateVirguleIdentifierStar','/Users/tianqilei/PycharmProjects/TSLM/lexer_parser/parser.py',193),
  ('ObserverStar -> empty','ObserverStar',1,'p_ObserverStar','/Users/tianqilei/PycharmProjects/TSLM/lexer_parser/parser.py',196),
  ('ObserverClauseQuestionMark -> empty','ObserverClauseQuestionMark',1,'p_ObserverClauseQuestionMark','/Users/tianqilei/PycharmProjects/TSLM/lexer_parser/parser.py',200),
  ('ObserverClauseQuestionMark -> OBSERVER ObserverStar','ObserverClauseQuestionMark',2,'p_ObserverClauseQuestionMark','/Users/tianqilei/PycharmProjects/TSLM/lexer_parser/parser.py',201),
  ('InternalBlockBody -> ComposedBlockClause EventClauseInBlock SynchronizationClause ObserverClauseQuestionMark','InternalBlockBody',4,'p_InternalBlockBody','/Users/tianqilei/PycharmProjects/TSLM/lexer_parser/parser.py',204),
  ('BasicBlockBody -> StateClause EventClauseInClass TransitionClause ObserverClauseQuestionMark','BasicBlockBody',4,'p_BasicBlockBody','/Users/tianqilei/PycharmProjects/TSLM/lexer_parser/parser.py',208),
  ('BlockBody -> BasicBlockBody','BlockBody',1,'p_BlockBody','/Users/tianqilei/PycharmProjects/TSLM/lexer_parser/parser.py',212),
  ('BlockBody -> InternalBlockBody','BlockBody',1,'p_BlockBody','/Users/tianqilei/PycharmProjects/TSLM/lexer_parser/parser.py',213),
  ('EndBlock -> END','EndBlock',1,'p_EndBlock','/Users/tianqilei/PycharmProjects/TSLM/lexer_parser/parser.py',217),
  ('EndClass -> END','EndClass',1,'p_EndClass','/Users/tianqilei/PycharmProjects/TSLM/lexer_parser/parser.py',231),
  ('Class -> CLASS ClassIdentifier BlockBody EndClass','Class',4,'p_Class','/Users/tianqilei/PycharmProjects/TSLM/lexer_parser/parser.py',259),
  ('Block -> BLOCK BlockIdentifier BlockBody EndBlock','Block',4,'p_Block','/Users/tianqilei/PycharmProjects/TSLM/lexer_parser/parser.py',263),
  ('Model -> Block Model','Model',2,'p_Model','/Users/tianqilei/PycharmProjects/TSLM/lexer_parser/parser.py',266),
  ('Model -> Class Model','Model',2,'p_Model','/Users/tianqilei/PycharmProjects/TSLM/lexer_parser/parser.py',267),
  ('Model -> empty','Model',1,'p_Model','/Users/tianqilei/PycharmProjects/TSLM/lexer_parser/parser.py',268),
]
