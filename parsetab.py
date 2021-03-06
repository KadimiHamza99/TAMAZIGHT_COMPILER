
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = "leftPLUSMINUSleftMULTIPLYDIVIDEDIVIDE EE EQUALS FLOAT GE GT INT LE LT MINUS MULTIPLY NAME NE PLUS STRING agejdan aru azayez efk ilem ma sehviver taggayt tamenguct tasekkirt urkid uslig\n    code : encaps taggayt NAME '{' inner_code '}' code \n        | empty\n    \n    encaps : azayez\n            | uslig\n            | sehviver\n            | empty\n    \n    inner_code :  attribut_statement functions_statement\n            | attribut_statement\n            | functions_statement\n    \n    attribut_statement : encaps NAME ';'\n    \n    functions_statement : method functions_statement\n                        | main functions_statement\n                        | empty\n    \n        method : encaps NAME '(' ')' '{' fStates '}'\n    \n        fStates : fState fState\n                | empty\n    \n    fState : var_assign\n            | print_statement\n            | scanf_statement\n            | if_statement\n            | loop_control\n            | empty\n    \n    main :  encaps urkid ilem agejdan '(' ')' '{' statements '}'\n    \n    statements : statement statements\n                | empty\n    \n    statement   : var_assign\n                | print_statement\n                | call_function\n                | scanf_statement\n                | if_statement\n                | loop_control\n                | empty\n    \n    var_assign : NAME EQUALS expression ';'\n    \n    call_function : tasekkirt NAME ';'\n    \n    print_statement : aru '(' expression ')' ';'\n    \n    scanf_statement : efk '(' NAME ')' ';'\n    \n        loop_control : tamenguct '(' INT ')' '{' statementsLoop '}'\n    \n        statementsLoop : statementLoop statementLoop\n                        | empty\n    \n    statementLoop : var_assign\n                    | print_statement\n                    | scanf_statement\n                    | if_statement\n                    | empty\n    \n    if_statement : ma '(' condition ')' '{' con_statements '}'\n    \n    con_statements : con_statement con_statement con_statement\n                    | empty\n    \n        con_statement : var_assign\n                        | print_statement\n                        | scanf_statement\n                        | if_statement\n                        | empty\n    \n        condition : expression comparaison expression\n    \n        comparaison : GT\n                    | LT\n                    | GE\n                    | LE\n                    | EE\n                    | NE\n    \n    expression :  expression MULTIPLY expression\n                | expression DIVIDE expression\n                | expression MINUS expression\n                | expression PLUS expression\n    \n    expression : INT\n                | FLOAT\n    \n    expression : STRING\n    \n    expression : NAME\n    \n    empty :\n    "
    
_lr_action_items = {'azayez':([0,9,12,14,15,19,24,48,92,],[4,4,4,4,4,4,-10,-14,-23,]),'uslig':([0,9,12,14,15,19,24,48,92,],[5,5,5,5,5,5,-10,-14,-23,]),'sehviver':([0,9,12,14,15,19,24,48,92,],[6,6,6,6,6,6,-10,-14,-23,]),'$end':([0,1,3,19,27,],[-68,0,-2,-68,-1,]),'taggayt':([0,2,3,4,5,6,19,],[-68,7,-6,-3,-4,-5,-68,]),'NAME':([4,5,6,7,9,10,12,14,15,16,21,24,31,35,36,37,38,39,40,41,47,48,51,52,53,55,67,68,69,70,71,72,73,74,75,76,77,78,79,80,84,85,86,87,88,89,90,92,99,100,101,103,104,106,107,108,109,110,111,113,114,115,116,117,118,119,120,121,122,],[-3,-4,-5,8,-68,17,-68,-68,-68,-6,28,-10,33,33,-22,-17,-18,-19,-20,-21,56,-14,56,62,56,33,33,-32,-26,-27,-28,-29,-30,-31,94,-33,56,56,56,56,56,-54,-55,-56,-57,-58,-59,-23,-35,-36,33,33,-34,33,-52,-48,-49,-50,-51,33,-44,-40,-41,-42,-43,-45,33,-52,-37,]),'urkid':([4,5,6,9,10,12,14,15,16,21,24,48,92,],[-3,-4,-5,-68,18,-68,-68,-68,-6,18,-10,-14,-23,]),'{':([8,29,46,83,91,],[9,31,55,101,103,]),'}':([9,11,12,13,14,15,16,20,22,23,24,31,34,35,36,37,38,39,40,41,48,49,50,55,66,67,68,69,70,71,72,73,74,76,92,93,99,100,101,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,123,124,125,],[-68,19,-8,-9,-68,-68,-13,-7,-11,-12,-10,-68,48,-68,-16,-17,-18,-19,-20,-21,-14,-15,-22,-68,92,-68,-25,-26,-27,-28,-29,-30,-31,-33,-23,-24,-35,-36,-68,-68,-34,119,-68,-47,-48,-49,-50,-51,122,-68,-39,-40,-41,-42,-43,-45,-68,-52,-37,-38,-44,-46,]),';':([17,56,57,58,59,60,81,82,94,95,96,97,98,],[24,-67,76,-64,-65,-66,99,100,104,-60,-61,-62,-63,]),'(':([17,28,30,42,43,44,45,],[25,25,32,51,52,53,54,]),'ilem':([18,],[26,]),')':([25,32,56,58,59,60,61,62,63,65,95,96,97,98,102,],[29,46,-67,-64,-65,-66,81,82,83,91,-60,-61,-62,-63,-53,]),'agejdan':([26,],[30,]),'aru':([31,35,36,37,38,39,40,41,55,67,68,69,70,71,72,73,74,76,99,100,101,103,104,106,107,108,109,110,111,113,114,115,116,117,118,119,120,121,122,],[42,42,-22,-17,-18,-19,-20,-21,42,42,-32,-26,-27,-28,-29,-30,-31,-33,-35,-36,42,42,-34,42,-52,-48,-49,-50,-51,42,-44,-40,-41,-42,-43,-45,42,-52,-37,]),'efk':([31,35,36,37,38,39,40,41,55,67,68,69,70,71,72,73,74,76,99,100,101,103,104,106,107,108,109,110,111,113,114,115,116,117,118,119,120,121,122,],[43,43,-22,-17,-18,-19,-20,-21,43,43,-32,-26,-27,-28,-29,-30,-31,-33,-35,-36,43,43,-34,43,-52,-48,-49,-50,-51,43,-44,-40,-41,-42,-43,-45,43,-52,-37,]),'ma':([31,35,36,37,38,39,40,41,55,67,68,69,70,71,72,73,74,76,99,100,101,103,104,106,107,108,109,110,111,113,114,115,116,117,118,119,120,121,122,],[44,44,-22,-17,-18,-19,-20,-21,44,44,-32,-26,-27,-28,-29,-30,-31,-33,-35,-36,44,44,-34,44,-52,-48,-49,-50,-51,44,-44,-40,-41,-42,-43,-45,44,-52,-37,]),'tamenguct':([31,35,36,37,38,39,40,41,55,67,68,69,70,71,72,73,74,76,99,100,104,119,122,],[45,45,-22,-17,-18,-19,-20,-21,45,45,-32,-26,-27,-28,-29,-30,-31,-33,-35,-36,-34,-45,-37,]),'EQUALS':([33,],[47,]),'INT':([47,51,53,54,77,78,79,80,84,85,86,87,88,89,90,],[58,58,58,65,58,58,58,58,58,-54,-55,-56,-57,-58,-59,]),'FLOAT':([47,51,53,77,78,79,80,84,85,86,87,88,89,90,],[59,59,59,59,59,59,59,59,-54,-55,-56,-57,-58,-59,]),'STRING':([47,51,53,77,78,79,80,84,85,86,87,88,89,90,],[60,60,60,60,60,60,60,60,-54,-55,-56,-57,-58,-59,]),'tasekkirt':([55,67,68,69,70,71,72,73,74,76,99,100,104,119,122,],[75,75,-32,-26,-27,-28,-29,-30,-31,-33,-35,-36,-34,-45,-37,]),'MULTIPLY':([56,57,58,59,60,61,64,95,96,97,98,102,],[-67,77,-64,-65,-66,77,77,-60,-61,77,77,77,]),'DIVIDE':([56,57,58,59,60,61,64,95,96,97,98,102,],[-67,78,-64,-65,-66,78,78,-60,-61,78,78,78,]),'MINUS':([56,57,58,59,60,61,64,95,96,97,98,102,],[-67,79,-64,-65,-66,79,79,-60,-61,-62,-63,79,]),'PLUS':([56,57,58,59,60,61,64,95,96,97,98,102,],[-67,80,-64,-65,-66,80,80,-60,-61,-62,-63,80,]),'GT':([56,58,59,60,64,95,96,97,98,],[-67,-64,-65,-66,85,-60,-61,-62,-63,]),'LT':([56,58,59,60,64,95,96,97,98,],[-67,-64,-65,-66,86,-60,-61,-62,-63,]),'GE':([56,58,59,60,64,95,96,97,98,],[-67,-64,-65,-66,87,-60,-61,-62,-63,]),'LE':([56,58,59,60,64,95,96,97,98,],[-67,-64,-65,-66,88,-60,-61,-62,-63,]),'EE':([56,58,59,60,64,95,96,97,98,],[-67,-64,-65,-66,89,-60,-61,-62,-63,]),'NE':([56,58,59,60,64,95,96,97,98,],[-67,-64,-65,-66,90,-60,-61,-62,-63,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'code':([0,19,],[1,27,]),'encaps':([0,9,12,14,15,19,],[2,10,21,21,21,2,]),'empty':([0,9,12,14,15,19,31,35,55,67,101,103,106,113,120,],[3,16,16,16,16,3,36,50,68,68,107,114,121,124,121,]),'inner_code':([9,],[11,]),'attribut_statement':([9,],[12,]),'functions_statement':([9,12,14,15,],[13,20,22,23,]),'method':([9,12,14,15,],[14,14,14,14,]),'main':([9,12,14,15,],[15,15,15,15,]),'fStates':([31,],[34,]),'fState':([31,35,],[35,49,]),'var_assign':([31,35,55,67,101,103,106,113,120,],[37,37,69,69,108,115,108,115,108,]),'print_statement':([31,35,55,67,101,103,106,113,120,],[38,38,70,70,109,116,109,116,109,]),'scanf_statement':([31,35,55,67,101,103,106,113,120,],[39,39,72,72,110,117,110,117,110,]),'if_statement':([31,35,55,67,101,103,106,113,120,],[40,40,73,73,111,118,111,118,111,]),'loop_control':([31,35,55,67,],[41,41,74,74,]),'expression':([47,51,53,77,78,79,80,84,],[57,61,64,95,96,97,98,102,]),'condition':([53,],[63,]),'statements':([55,67,],[66,93,]),'statement':([55,67,],[67,67,]),'call_function':([55,67,],[71,71,]),'comparaison':([64,],[84,]),'con_statements':([101,],[105,]),'con_statement':([101,106,120,],[106,120,125,]),'statementsLoop':([103,],[112,]),'statementLoop':([103,113,],[113,123,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> code","S'",1,None,None,None),
  ('code -> encaps taggayt NAME { inner_code } code','code',7,'p_code','TamazightLexerParser.py',129),
  ('code -> empty','code',1,'p_code','TamazightLexerParser.py',130),
  ('encaps -> azayez','encaps',1,'p_Encaps','TamazightLexerParser.py',136),
  ('encaps -> uslig','encaps',1,'p_Encaps','TamazightLexerParser.py',137),
  ('encaps -> sehviver','encaps',1,'p_Encaps','TamazightLexerParser.py',138),
  ('encaps -> empty','encaps',1,'p_Encaps','TamazightLexerParser.py',139),
  ('inner_code -> attribut_statement functions_statement','inner_code',2,'p_inCode','TamazightLexerParser.py',145),
  ('inner_code -> attribut_statement','inner_code',1,'p_inCode','TamazightLexerParser.py',146),
  ('inner_code -> functions_statement','inner_code',1,'p_inCode','TamazightLexerParser.py',147),
  ('attribut_statement -> encaps NAME ;','attribut_statement',3,'p_attr_statement','TamazightLexerParser.py',153),
  ('functions_statement -> method functions_statement','functions_statement',2,'p_function','TamazightLexerParser.py',159),
  ('functions_statement -> main functions_statement','functions_statement',2,'p_function','TamazightLexerParser.py',160),
  ('functions_statement -> empty','functions_statement',1,'p_function','TamazightLexerParser.py',161),
  ('method -> encaps NAME ( ) { fStates }','method',7,'p_method','TamazightLexerParser.py',168),
  ('fStates -> fState fState','fStates',2,'p_fStates','TamazightLexerParser.py',176),
  ('fStates -> empty','fStates',1,'p_fStates','TamazightLexerParser.py',177),
  ('fState -> var_assign','fState',1,'p_fState','TamazightLexerParser.py',184),
  ('fState -> print_statement','fState',1,'p_fState','TamazightLexerParser.py',185),
  ('fState -> scanf_statement','fState',1,'p_fState','TamazightLexerParser.py',186),
  ('fState -> if_statement','fState',1,'p_fState','TamazightLexerParser.py',187),
  ('fState -> loop_control','fState',1,'p_fState','TamazightLexerParser.py',188),
  ('fState -> empty','fState',1,'p_fState','TamazightLexerParser.py',189),
  ('main -> encaps urkid ilem agejdan ( ) { statements }','main',9,'p_main','TamazightLexerParser.py',196),
  ('statements -> statement statements','statements',2,'p_statements','TamazightLexerParser.py',202),
  ('statements -> empty','statements',1,'p_statements','TamazightLexerParser.py',203),
  ('statement -> var_assign','statement',1,'p_statement','TamazightLexerParser.py',209),
  ('statement -> print_statement','statement',1,'p_statement','TamazightLexerParser.py',210),
  ('statement -> call_function','statement',1,'p_statement','TamazightLexerParser.py',211),
  ('statement -> scanf_statement','statement',1,'p_statement','TamazightLexerParser.py',212),
  ('statement -> if_statement','statement',1,'p_statement','TamazightLexerParser.py',213),
  ('statement -> loop_control','statement',1,'p_statement','TamazightLexerParser.py',214),
  ('statement -> empty','statement',1,'p_statement','TamazightLexerParser.py',215),
  ('var_assign -> NAME EQUALS expression ;','var_assign',4,'p_varAssign','TamazightLexerParser.py',222),
  ('call_function -> tasekkirt NAME ;','call_function',3,'p_callFunction','TamazightLexerParser.py',229),
  ('print_statement -> aru ( expression ) ;','print_statement',5,'p_printStat','TamazightLexerParser.py',236),
  ('scanf_statement -> efk ( NAME ) ;','scanf_statement',5,'p_scanfStat','TamazightLexerParser.py',243),
  ('loop_control -> tamenguct ( INT ) { statementsLoop }','loop_control',7,'p_loopControl','TamazightLexerParser.py',250),
  ('statementsLoop -> statementLoop statementLoop','statementsLoop',2,'p_statementsLoop','TamazightLexerParser.py',257),
  ('statementsLoop -> empty','statementsLoop',1,'p_statementsLoop','TamazightLexerParser.py',258),
  ('statementLoop -> var_assign','statementLoop',1,'p_statementloop','TamazightLexerParser.py',266),
  ('statementLoop -> print_statement','statementLoop',1,'p_statementloop','TamazightLexerParser.py',267),
  ('statementLoop -> scanf_statement','statementLoop',1,'p_statementloop','TamazightLexerParser.py',268),
  ('statementLoop -> if_statement','statementLoop',1,'p_statementloop','TamazightLexerParser.py',269),
  ('statementLoop -> empty','statementLoop',1,'p_statementloop','TamazightLexerParser.py',270),
  ('if_statement -> ma ( condition ) { con_statements }','if_statement',7,'p_ifStatement','TamazightLexerParser.py',277),
  ('con_statements -> con_statement con_statement con_statement','con_statements',3,'p_conStatements','TamazightLexerParser.py',286),
  ('con_statements -> empty','con_statements',1,'p_conStatements','TamazightLexerParser.py',287),
  ('con_statement -> var_assign','con_statement',1,'p_conStatement','TamazightLexerParser.py',294),
  ('con_statement -> print_statement','con_statement',1,'p_conStatement','TamazightLexerParser.py',295),
  ('con_statement -> scanf_statement','con_statement',1,'p_conStatement','TamazightLexerParser.py',296),
  ('con_statement -> if_statement','con_statement',1,'p_conStatement','TamazightLexerParser.py',297),
  ('con_statement -> empty','con_statement',1,'p_conStatement','TamazightLexerParser.py',298),
  ('condition -> expression comparaison expression','condition',3,'p_condition','TamazightLexerParser.py',305),
  ('comparaison -> GT','comparaison',1,'p_comparaison','TamazightLexerParser.py',312),
  ('comparaison -> LT','comparaison',1,'p_comparaison','TamazightLexerParser.py',313),
  ('comparaison -> GE','comparaison',1,'p_comparaison','TamazightLexerParser.py',314),
  ('comparaison -> LE','comparaison',1,'p_comparaison','TamazightLexerParser.py',315),
  ('comparaison -> EE','comparaison',1,'p_comparaison','TamazightLexerParser.py',316),
  ('comparaison -> NE','comparaison',1,'p_comparaison','TamazightLexerParser.py',317),
  ('expression -> expression MULTIPLY expression','expression',3,'p_expression','TamazightLexerParser.py',324),
  ('expression -> expression DIVIDE expression','expression',3,'p_expression','TamazightLexerParser.py',325),
  ('expression -> expression MINUS expression','expression',3,'p_expression','TamazightLexerParser.py',326),
  ('expression -> expression PLUS expression','expression',3,'p_expression','TamazightLexerParser.py',327),
  ('expression -> INT','expression',1,'p_expression_int_float','TamazightLexerParser.py',334),
  ('expression -> FLOAT','expression',1,'p_expression_int_float','TamazightLexerParser.py',335),
  ('expression -> STRING','expression',1,'p_expression_string','TamazightLexerParser.py',342),
  ('expression -> NAME','expression',1,'p_expression_var','TamazightLexerParser.py',349),
  ('empty -> <empty>','empty',0,'p_empty','TamazightLexerParser.py',356),
]
