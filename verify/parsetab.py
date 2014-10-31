
# parsetab.py
# This file is automatically generated. Do not edit.
_tabversion = '3.2'

_lr_method = 'LALR'

_lr_signature = b'\xd0)]\x16\x06\xc8t\x82\xcbB\x88\x92\x0e\x8ent'
    
_lr_action_items = {'ANDCOMMERCIAL':([87,96,97,],[92,-5,92,]),'VIRGULE':([24,25,26,27,44,45,48,49,52,53,77,82,],[39,-23,43,-15,56,-36,-32,68,39,43,56,68,]),'SYNCHRONIZATION':([30,44,45,54,55,77,85,],[46,-1,-36,-34,-33,-1,-35,]),'POINT':([86,],[91,]),'BLOCK':([0,4,5,7,8,11,12,17,22,26,27,31,32,36,37,41,42,53,76,],[6,6,6,6,-3,6,-4,6,6,-1,-15,-51,-50,-49,-52,-18,-16,-1,-17,]),'CLASS':([0,4,5,31,32,36,37,],[2,2,2,-51,-50,-49,-52,]),'EVENT':([17,19,21,22,24,25,26,27,28,35,36,37,38,40,41,42,52,53,75,76,],[-19,29,33,-20,-1,-23,-1,-15,-21,-22,-49,-52,-40,-37,-18,-16,-1,-1,-41,-17,]),'TRANSITION':([34,48,49,66,67,82,88,],[51,-32,-1,-31,-38,-1,-39,]),'$end':([0,1,3,4,5,9,10,31,32,36,37,],[-1,-55,0,-1,-1,-54,-53,-51,-50,-49,-52,]),'OBSERVER':([46,47,50,51,57,60,61,62,70,72,74,79,83,87,93,94,96,97,98,99,100,],[-1,64,64,-1,-11,-13,-10,-1,-28,-1,-30,-12,-29,-1,-6,-8,-5,-1,-26,-24,-7,]),'STATE':([7,8,11,12,],[13,-3,13,-4,]),'DEUXPOINTS':([58,59,71,73,],[-9,78,-27,84,]),'FLECHE':([89,90,],[-25,95,]),'IDENTIFIER':([2,6,7,8,11,12,13,14,16,17,22,26,27,29,33,36,37,39,41,42,43,46,51,53,56,61,62,68,72,76,78,84,87,91,92,93,94,95,96,97,98,99,100,],[8,12,16,-3,16,-4,25,27,-14,16,16,-1,-15,45,48,-49,-52,25,-18,-16,27,58,71,-1,45,-10,58,48,71,-17,86,89,-1,96,86,-6,-8,98,-5,-1,-26,-24,-7,]),'END':([15,18,20,23,46,47,50,51,57,60,61,62,63,64,65,69,70,72,74,79,80,81,83,87,93,94,96,97,98,99,100,],[-47,-48,32,36,-1,-1,-1,-1,-11,-13,-10,-1,-43,-1,-45,-46,-28,-1,-30,-12,-42,-44,-29,-1,-6,-8,-5,-1,-26,-24,-7,]),}

_lr_action = { }
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = { }
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'ClassInstanceIdentifier':([14,43,],[26,53,]),'EventIdentifierInClass':([33,68,],[49,82,]),'Transition':([51,72,],[72,72,]),'AndCommercialEvenPathStar':([87,97,],[94,100,]),'EventVirguleIdentifierStarInBlock':([44,77,],[55,85,]),'SynchronizationStar':([46,62,],[60,79,]),'Class':([0,4,5,],[4,4,4,]),'StateIdentifier':([13,39,],[24,52,]),'EventIdentifierInTransition':([51,72,],[73,73,]),'BasicBlockBody':([7,11,],[15,15,]),'ObserverStar':([64,],[81,]),'ClassInstanceVirguleIdentifierStar':([26,53,],[41,76,]),'Synchronization':([46,62,],[62,62,]),'EventIdentifierInSynchronization':([46,62,],[59,59,]),'EventClauseInClass':([21,],[34,]),'ClassInstance':([7,11,17,22,],[22,22,22,22,]),'ClassIdentifier':([2,],[7,]),'BlockIdentifier':([6,],[11,]),'ObserverClauseQuestionMark':([47,50,],[65,69,]),'Block':([0,4,5,7,11,17,22,],[5,5,5,17,17,17,17,]),'TransitionClause':([34,],[50,]),'EventVirguleIdentifierStarInClass':([49,82,],[66,88,]),'DestStateIdentifierInTransition':([95,],[99,]),'ComposedBlockClause':([7,11,17,22,],[19,19,28,35,]),'EndBlock':([23,],[37,]),'EndClass':([20,],[31,]),'InternalBlockBody':([7,11,],[18,18,]),'empty':([0,4,5,24,26,44,46,47,49,50,51,52,53,62,64,72,77,82,87,97,],[1,1,1,38,42,54,57,63,67,63,70,38,42,57,80,70,54,67,93,93,]),'OriginalStateIdentifierInTransition':([84,],[90,]),'TransitionStar':([51,72,],[74,83,]),'BlockBody':([7,11,],[20,23,]),'EventIdentifierInBlock':([29,56,],[44,77,]),'StateClause':([7,11,],[21,21,]),'EventPath':([78,92,],[87,97,]),'ClassNameIdentifier':([7,11,17,22,],[14,14,14,14,]),'StateVirguleIdentifierStar':([24,52,],[40,75,]),'EventClauseInBlock':([19,],[30,]),'Model':([0,4,5,],[3,9,10,]),'MacroEventDefinition':([46,62,],[61,61,]),'SynchronizationClause':([30,],[47,]),}

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
  ('ComposedBlockClause -> Block','ComposedBlockClause',1,'p_ComposedBlockClause','/Users/tianqilei/PycharmProjects/TSLM/lexer_parser/parser.py',126),
  ('ComposedBlockClause -> ClassInstance','ComposedBlockClause',1,'p_ComposedBlockClause','/Users/tianqilei/PycharmProjects/TSLM/lexer_parser/parser.py',127),
  ('ComposedBlockClause -> Block ComposedBlockClause','ComposedBlockClause',2,'p_ComposedBlockClause','/Users/tianqilei/PycharmProjects/TSLM/lexer_parser/parser.py',128),
  ('ComposedBlockClause -> ClassInstance ComposedBlockClause','ComposedBlockClause',2,'p_ComposedBlockClause','/Users/tianqilei/PycharmProjects/TSLM/lexer_parser/parser.py',129),
  ('StateIdentifier -> IDENTIFIER','StateIdentifier',1,'p_StateIdentifier','/Users/tianqilei/PycharmProjects/TSLM/lexer_parser/parser.py',136),
  ('Transition -> EventIdentifierInTransition DEUXPOINTS OriginalStateIdentifierInTransition FLECHE DestStateIdentifierInTransition','Transition',5,'p_Transition','/Users/tianqilei/PycharmProjects/TSLM/lexer_parser/parser.py',144),
  ('OriginalStateIdentifierInTransition -> IDENTIFIER','OriginalStateIdentifierInTransition',1,'p_OriginalStateIdentifierInTransition','/Users/tianqilei/PycharmProjects/TSLM/lexer_parser/parser.py',147),
  ('DestStateIdentifierInTransition -> IDENTIFIER','DestStateIdentifierInTransition',1,'p_DestStateIdentifierInTransition','/Users/tianqilei/PycharmProjects/TSLM/lexer_parser/parser.py',151),
  ('EventIdentifierInTransition -> IDENTIFIER','EventIdentifierInTransition',1,'p_EventIdentifierInTransition','/Users/tianqilei/PycharmProjects/TSLM/lexer_parser/parser.py',155),
  ('TransitionStar -> empty','TransitionStar',1,'p_TransitionStar','/Users/tianqilei/PycharmProjects/TSLM/lexer_parser/parser.py',159),
  ('TransitionStar -> Transition TransitionStar','TransitionStar',2,'p_TransitionStar','/Users/tianqilei/PycharmProjects/TSLM/lexer_parser/parser.py',160),
  ('TransitionClause -> TRANSITION TransitionStar','TransitionClause',2,'p_TransitionClause','/Users/tianqilei/PycharmProjects/TSLM/lexer_parser/parser.py',163),
  ('EventClauseInClass -> EVENT EventIdentifierInClass EventVirguleIdentifierStarInClass','EventClauseInClass',3,'p_EventClauseInClass','/Users/tianqilei/PycharmProjects/TSLM/lexer_parser/parser.py',166),
  ('EventIdentifierInClass -> IDENTIFIER','EventIdentifierInClass',1,'p_EventIdentifierInClass','/Users/tianqilei/PycharmProjects/TSLM/lexer_parser/parser.py',169),
  ('EventClauseInBlock -> EVENT EventIdentifierInBlock EventVirguleIdentifierStarInBlock','EventClauseInBlock',3,'p_EventClauseInBlock','/Users/tianqilei/PycharmProjects/TSLM/lexer_parser/parser.py',173),
  ('EventVirguleIdentifierStarInBlock -> empty','EventVirguleIdentifierStarInBlock',1,'p_EventVirguleIdentifierStarInBlock','/Users/tianqilei/PycharmProjects/TSLM/lexer_parser/parser.py',176),
  ('EventVirguleIdentifierStarInBlock -> VIRGULE EventIdentifierInBlock EventVirguleIdentifierStarInBlock','EventVirguleIdentifierStarInBlock',3,'p_EventVirguleIdentifierStarInBlock','/Users/tianqilei/PycharmProjects/TSLM/lexer_parser/parser.py',177),
  ('EventIdentifierInBlock -> IDENTIFIER','EventIdentifierInBlock',1,'p_EventIdentifierInBlock','/Users/tianqilei/PycharmProjects/TSLM/lexer_parser/parser.py',180),
  ('StateClause -> STATE StateIdentifier StateVirguleIdentifierStar','StateClause',3,'p_StateClause','/Users/tianqilei/PycharmProjects/TSLM/lexer_parser/parser.py',184),
  ('EventVirguleIdentifierStarInClass -> empty','EventVirguleIdentifierStarInClass',1,'p_EventVirguleIdentifierStarInClass','/Users/tianqilei/PycharmProjects/TSLM/lexer_parser/parser.py',187),
  ('EventVirguleIdentifierStarInClass -> VIRGULE EventIdentifierInClass EventVirguleIdentifierStarInClass','EventVirguleIdentifierStarInClass',3,'p_EventVirguleIdentifierStarInClass','/Users/tianqilei/PycharmProjects/TSLM/lexer_parser/parser.py',188),
  ('StateVirguleIdentifierStar -> empty','StateVirguleIdentifierStar',1,'p_StateVirguleIdentifierStar','/Users/tianqilei/PycharmProjects/TSLM/lexer_parser/parser.py',191),
  ('StateVirguleIdentifierStar -> VIRGULE StateIdentifier StateVirguleIdentifierStar','StateVirguleIdentifierStar',3,'p_StateVirguleIdentifierStar','/Users/tianqilei/PycharmProjects/TSLM/lexer_parser/parser.py',192),
  ('ObserverStar -> empty','ObserverStar',1,'p_ObserverStar','/Users/tianqilei/PycharmProjects/TSLM/lexer_parser/parser.py',195),
  ('ObserverClauseQuestionMark -> empty','ObserverClauseQuestionMark',1,'p_ObserverClauseQuestionMark','/Users/tianqilei/PycharmProjects/TSLM/lexer_parser/parser.py',199),
  ('ObserverClauseQuestionMark -> OBSERVER ObserverStar','ObserverClauseQuestionMark',2,'p_ObserverClauseQuestionMark','/Users/tianqilei/PycharmProjects/TSLM/lexer_parser/parser.py',200),
  ('InternalBlockBody -> ComposedBlockClause EventClauseInBlock SynchronizationClause ObserverClauseQuestionMark','InternalBlockBody',4,'p_InternalBlockBody','/Users/tianqilei/PycharmProjects/TSLM/lexer_parser/parser.py',203),
  ('BasicBlockBody -> StateClause EventClauseInClass TransitionClause ObserverClauseQuestionMark','BasicBlockBody',4,'p_BasicBlockBody','/Users/tianqilei/PycharmProjects/TSLM/lexer_parser/parser.py',207),
  ('BlockBody -> BasicBlockBody','BlockBody',1,'p_BlockBody','/Users/tianqilei/PycharmProjects/TSLM/lexer_parser/parser.py',211),
  ('BlockBody -> InternalBlockBody','BlockBody',1,'p_BlockBody','/Users/tianqilei/PycharmProjects/TSLM/lexer_parser/parser.py',212),
  ('EndBlock -> END','EndBlock',1,'p_EndBlock','/Users/tianqilei/PycharmProjects/TSLM/lexer_parser/parser.py',216),
  ('EndClass -> END','EndClass',1,'p_EndClass','/Users/tianqilei/PycharmProjects/TSLM/lexer_parser/parser.py',230),
  ('Class -> CLASS ClassIdentifier BlockBody EndClass','Class',4,'p_Class','/Users/tianqilei/PycharmProjects/TSLM/lexer_parser/parser.py',258),
  ('Block -> BLOCK BlockIdentifier BlockBody EndBlock','Block',4,'p_Block','/Users/tianqilei/PycharmProjects/TSLM/lexer_parser/parser.py',262),
  ('Model -> Block Model','Model',2,'p_Model','/Users/tianqilei/PycharmProjects/TSLM/lexer_parser/parser.py',265),
  ('Model -> Class Model','Model',2,'p_Model','/Users/tianqilei/PycharmProjects/TSLM/lexer_parser/parser.py',266),
  ('Model -> empty','Model',1,'p_Model','/Users/tianqilei/PycharmProjects/TSLM/lexer_parser/parser.py',267),
]
