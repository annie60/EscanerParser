
# parsetab.py
# This file is automatically generated. Do not edit.
_tabversion = '3.8'

_lr_method = 'LALR'

_lr_signature = 'EF738E088248BF9596319351E3ED881D'
    
_lr_action_items = {'PROGRAM':([0,],[2,]),'PLUS':([24,25,26,27,34,36,37,38,40,42,44,45,56,57,58,59,60,61,63,64,65,66,67,68,76,77,78,],[41,41,41,41,-53,-52,41,-45,63,-55,-54,-49,41,-44,41,41,41,41,41,41,41,-51,-50,41,-48,-47,-46,]),'ENDLINE':([3,17,19,28,34,35,36,38,39,40,42,44,45,51,52,57,62,66,67,69,76,77,78,79,80,81,82,83,84,88,89,94,96,97,98,],[4,-20,-18,-19,-53,54,-52,-45,-37,-40,-55,-54,-49,72,74,-44,-39,-51,-50,87,-48,-47,-46,-34,-35,-36,-42,-41,-43,-38,-38,-27,99,100,-28,]),'MORETHAN':([34,36,38,39,40,42,44,45,57,62,66,67,76,77,78,82,83,84,],[-53,-52,-45,60,-40,-55,-54,-49,-44,-39,-51,-50,-48,-47,-46,-42,-41,-43,]),'OPENEXP':([4,7,23,29,30,33,53,70,71,72,73,74,75,90,91,92,93,95,],[5,5,-5,-8,-6,-7,-9,5,5,-10,-14,-11,-15,-12,-16,-13,-17,5,]),'ELSE':([17,19,28,88,89,],[-20,-18,-19,95,95,]),'DIFFERENT':([34,36,38,39,40,42,44,45,57,62,66,67,76,77,78,82,83,84,],[-53,-52,-45,61,-40,-55,-54,-49,-44,-39,-51,-50,-48,-47,-46,-42,-41,-43,]),'TYPEFLOAT':([31,],[52,]),'MINUS':([24,25,26,27,34,36,37,38,40,42,44,45,56,57,58,59,60,61,63,64,65,66,67,68,76,77,78,],[43,43,43,43,-53,-52,43,-45,64,-55,-54,-49,43,-44,43,43,43,43,43,43,43,-51,-50,43,-48,-47,-46,]),'DIVIDE':([34,36,38,42,44,45,66,67,76,],[-53,-52,56,-55,-54,-49,-51,-50,-48,]),'$end':([1,6,9,10,17,19,20,28,],[0,-1,-4,-3,-20,-18,-2,-19,]),'VARIABLE':([4,],[8,]),'TYPEINT':([31,],[51,]),'IDENTIFIER':([2,5,8,12,15,16,18,24,25,26,27,32,37,41,43,54,56,58,59,60,61,63,64,65,68,72,73,74,75,86,87,99,100,],[3,11,21,-23,11,-21,-22,34,34,34,34,21,34,34,34,-24,34,34,34,34,34,34,34,34,34,21,21,21,21,-33,-29,-25,-26,]),'LESSTHAN':([34,36,38,39,40,42,44,45,57,62,66,67,76,77,78,82,83,84,],[-53,-52,-45,59,-40,-55,-54,-49,-44,-39,-51,-50,-48,-47,-46,-42,-41,-43,]),'PRINT':([5,12,15,16,18,54,86,87,99,100,],[13,-23,13,-21,-22,-24,-33,-29,-25,-26,]),'OPENCOND':([13,14,24,25,26,27,37,56,58,59,60,61,63,64,65,68,],[25,26,37,37,37,37,37,37,37,37,37,37,37,37,37,37,]),'TIMES':([34,36,38,42,44,45,66,67,76,],[-53,-52,58,-55,-54,-49,-51,-50,-48,]),'error':([8,14,32,34,36,38,40,42,44,45,51,52,57,66,67,69,72,73,74,75,76,77,78,],[22,27,22,-53,-52,-45,65,-55,-54,-49,73,75,-44,-51,-50,86,22,22,22,22,-48,-47,-46,]),'IF':([5,12,15,16,18,54,86,87,99,100,],[14,-23,14,-21,-22,-24,-33,-29,-25,-26,]),'INTEGER':([24,25,26,27,37,41,43,56,58,59,60,61,63,64,65,68,],[44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,]),'STRING':([25,68,],[46,46,]),'SEPARATE':([21,22,34,36,38,39,40,42,44,45,47,57,62,66,67,76,77,78,79,80,81,82,83,84,],[32,32,-53,-52,-45,-37,-40,-55,-54,-49,68,-44,-39,-51,-50,-48,-47,-46,-34,-35,-36,-42,-41,-43,]),'FLOATNUM':([24,25,26,27,37,41,43,56,58,59,60,61,63,64,65,68,],[42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,]),'CLOSEEXP':([5,12,15,16,18,54,86,87,99,100,],[17,-23,17,-21,-22,-24,-33,-29,-25,-26,]),'ASSIGN':([21,22,],[31,31,]),'EQUALS':([11,],[24,]),'CLOSECOND':([34,36,38,39,40,42,44,45,46,47,48,49,50,55,57,62,66,67,76,77,78,79,80,81,82,83,84,85,],[-53,-52,-45,-37,-40,-55,-54,-49,-32,-30,69,70,71,76,-44,-39,-51,-50,-48,-47,-46,-34,-35,-36,-42,-41,-43,-31,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'program':([0,],[1,]),'writing':([5,15,],[12,12,]),'constant':([24,25,26,27,37,41,43,56,58,59,60,61,63,64,65,68,],[36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,]),'vars2':([21,22,],[30,33,]),'exp':([24,25,26,27,37,59,60,61,63,64,65,68,],[39,39,39,39,39,79,80,81,82,83,84,39,]),'term1':([38,],[57,]),'asignation':([5,15,],[16,16,]),'vars1':([8,32,72,73,74,75,],[23,53,90,91,92,93,]),'condition1':([88,89,],[96,97,]),'condition':([5,15,],[18,18,]),'block':([4,7,70,71,95,],[9,9,88,89,98,]),'expression':([24,25,26,27,37,68,],[35,47,49,50,55,47,]),'vars3':([21,22,],[29,29,]),'block1':([5,15,],[19,28,]),'vars':([4,],[7,]),'writing1':([25,68,],[48,85,]),'factor':([24,25,26,27,37,56,58,59,60,61,63,64,65,68,],[38,38,38,38,38,38,38,38,38,38,38,38,38,38,]),'estat':([5,15,],[15,15,]),'term':([24,25,26,27,37,56,58,59,60,61,63,64,65,68,],[40,40,40,40,40,77,78,40,40,40,40,40,40,40,]),'program2':([4,7,],[10,20,]),'exp1':([40,],[62,]),'program1':([4,],[6,]),'factor1':([24,25,26,27,37,41,43,56,58,59,60,61,63,64,65,68,],[45,45,45,45,45,66,67,45,45,45,45,45,45,45,45,45,]),'empty':([88,89,],[94,94,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> program","S'",1,None,None,None),
  ('program -> PROGRAM IDENTIFIER ENDLINE program1','program',4,'p_program','escannerP.py',70),
  ('program1 -> vars program2','program1',2,'p_program1','escannerP.py',73),
  ('program1 -> program2','program1',1,'p_program1','escannerP.py',74),
  ('program2 -> block','program2',1,'p_program2','escannerP.py',77),
  ('vars -> VARIABLE vars1','vars',2,'p_vars','escannerP.py',80),
  ('vars1 -> IDENTIFIER vars2','vars1',2,'p_vars1','escannerP.py',83),
  ('vars1 -> error vars2','vars1',2,'p_vars1_error','escannerP.py',86),
  ('vars2 -> vars3','vars2',1,'p_vars2','escannerP.py',89),
  ('vars2 -> SEPARATE vars1','vars2',2,'p_vars2','escannerP.py',90),
  ('vars3 -> ASSIGN TYPEINT ENDLINE','vars3',3,'p_vars3','escannerP.py',93),
  ('vars3 -> ASSIGN TYPEFLOAT ENDLINE','vars3',3,'p_vars3','escannerP.py',94),
  ('vars3 -> ASSIGN TYPEINT ENDLINE vars1','vars3',4,'p_vars3','escannerP.py',95),
  ('vars3 -> ASSIGN TYPEFLOAT ENDLINE vars1','vars3',4,'p_vars3','escannerP.py',96),
  ('vars3 -> ASSIGN TYPEINT error','vars3',3,'p_vars3_error','escannerP.py',99),
  ('vars3 -> ASSIGN TYPEFLOAT error','vars3',3,'p_vars3_error','escannerP.py',100),
  ('vars3 -> ASSIGN TYPEINT error vars1','vars3',4,'p_vars3_error','escannerP.py',101),
  ('vars3 -> ASSIGN TYPEFLOAT error vars1','vars3',4,'p_vars3_error','escannerP.py',102),
  ('block -> OPENEXP block1','block',2,'p_block','escannerP.py',105),
  ('block1 -> estat block1','block1',2,'p_block1','escannerP.py',108),
  ('block1 -> CLOSEEXP','block1',1,'p_block1','escannerP.py',109),
  ('estat -> asignation','estat',1,'p_estat','escannerP.py',112),
  ('estat -> condition','estat',1,'p_estat','escannerP.py',113),
  ('estat -> writing','estat',1,'p_estat','escannerP.py',114),
  ('asignation -> IDENTIFIER EQUALS expression ENDLINE','asignation',4,'p_asignation','escannerP.py',117),
  ('condition -> IF OPENCOND expression CLOSECOND block condition1 ENDLINE','condition',7,'p_condition','escannerP.py',120),
  ('condition -> IF error expression CLOSECOND block condition1 ENDLINE','condition',7,'p_condition_error','escannerP.py',123),
  ('condition1 -> empty','condition1',1,'p_condition1','escannerP.py',127),
  ('condition1 -> ELSE block','condition1',2,'p_condition1','escannerP.py',128),
  ('writing -> PRINT OPENCOND writing1 CLOSECOND ENDLINE','writing',5,'p_writing','escannerP.py',131),
  ('writing1 -> expression','writing1',1,'p_writing1','escannerP.py',134),
  ('writing1 -> expression SEPARATE writing1','writing1',3,'p_writing1','escannerP.py',135),
  ('writing1 -> STRING','writing1',1,'p_writing1','escannerP.py',136),
  ('writing -> PRINT OPENCOND writing1 CLOSECOND error','writing',5,'p_writing_error','escannerP.py',139),
  ('expression -> exp LESSTHAN exp','expression',3,'p_expression','escannerP.py',142),
  ('expression -> exp MORETHAN exp','expression',3,'p_expression','escannerP.py',143),
  ('expression -> exp DIFFERENT exp','expression',3,'p_expression','escannerP.py',144),
  ('expression -> exp','expression',1,'p_expression','escannerP.py',145),
  ('empty -> <empty>','empty',0,'p_empty','escannerP.py',148),
  ('exp -> term exp1','exp',2,'p_exp','escannerP.py',151),
  ('exp -> term','exp',1,'p_exp','escannerP.py',152),
  ('exp1 -> MINUS exp','exp1',2,'p_exp1','escannerP.py',155),
  ('exp1 -> PLUS exp','exp1',2,'p_exp1','escannerP.py',156),
  ('exp1 -> error exp','exp1',2,'p_exp1_error','escannerP.py',159),
  ('term -> factor term1','term',2,'p_term','escannerP.py',162),
  ('term -> factor','term',1,'p_term','escannerP.py',163),
  ('term1 -> TIMES term','term1',2,'p_term1','escannerP.py',166),
  ('term1 -> DIVIDE term','term1',2,'p_term1','escannerP.py',167),
  ('factor -> OPENCOND expression CLOSECOND','factor',3,'p_factor','escannerP.py',169),
  ('factor -> factor1','factor',1,'p_factor','escannerP.py',170),
  ('factor -> MINUS factor1','factor',2,'p_factor','escannerP.py',171),
  ('factor -> PLUS factor1','factor',2,'p_factor','escannerP.py',172),
  ('factor1 -> constant','factor1',1,'p_factor1','escannerP.py',174),
  ('constant -> IDENTIFIER','constant',1,'p_constant','escannerP.py',176),
  ('constant -> INTEGER','constant',1,'p_constant','escannerP.py',177),
  ('constant -> FLOATNUM','constant',1,'p_constant','escannerP.py',178),
]
