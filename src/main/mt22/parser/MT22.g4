grammar MT22
; 

@lexer::header {
from lexererr import *
}

options {
	language = Python3;
}

program: decl+ EOF;

decl: vardecl | funcdecl; 

arraytype: ARRAY LSB dimension RSB OF eletype;
number: INTLIT | FLOATLIT;
eletype: INTEGER | FLOAT | BOOLEAN | STRING | AUTO;
dimension: INTLIT CM dimension | INTLIT;

//Variables ---------------------------------------------------------------
vardecl: vardeclNoEq | vardeclEq;
vardeclNoEq: idlist CL (eletype | arraytype) SM;
vardeclEq
	: ID CM assignment CM expr SM
	| ID CL (eletype | arraytype) ASSIGN expr SM
;
assignment
	: ID CM assignment CM expr
	| ID CL (eletype | arraytype) ASSIGN expr
;

arraylit: LCB (expList |) RCB;
idlist: ID CM idlist | ID;
expList: expr CM expList | expr;

param
	: (INHERIT |) (OUT |) ID CL (eletype | arraytype)
;

expr: expr1 CONCAT expr1 | expr1;

expr1: expr2 compare expr2 | expr2;
compare: EQ | NOT_EQ | LESS | GT | LTE | GTE;
expr2: expr2 (AND | OR) expr3 | expr3;
expr3: expr3 (ADD | SUB) expr4 | expr4;
expr4: expr4 (MUL | DIV | MOD) expr5 | expr5;
expr5: NOT expr5 | expr6;
expr6: SUB expr6 | expr7;
expr7: ID LSB expList RSB | expr8;
expr8: (LB expr RB) | factor;
factor
	: INTLIT
	| FLOATLIT
	| STRINGLIT
	| ID
	| funccall
	| arraylit
	| BOOLEANLIT
;


funccall: (ID LB (expList |) RB) |  specialFunction;

stmt
	: assignStmt
	| ifStmt
	| forStmt
	| whileStmt
	| doWhileStmt
	| returnStmt
	| continueStmt
	| breakStmt
	| callStmt
	| vardecl
;

stmtlocal: stmt | blockStmt;

assignStmt: lhs ASSIGN expr SM;
lhs: ID LSB expList RSB | ID;

ifStmt: (IF expr stmtlocal ELSE stmtlocal) | IF expr stmtlocal;

forStmt
	: FOR LB initExpr CM conditionExpr CM updateExpr RB stmtlocal
;

initExpr: ID ASSIGN expr;

conditionExpr: expr operator expr;
operator: LESS | GT | LTE | GTE | NOT_EQ | EQ;

updateExpr: expr;
whileStmt: WHILE LB expr RB stmtlocal;
doWhileStmt: DO blockStmt WHILE expr SM;
callStmt: ( specialFunction | (ID LB (expList |) RB)) SM;
blockStmt: LCB stmtList RCB;
stmtList: stmts |;
stmts: stmt stmts | stmt;
breakStmt: BREAK SM;
continueStmt: CONTINUE SM;
returnStmt: RETURN (expr |) SM;

funcdecl : ID CL FUNCTION returnType LB paramList RB inherit blockStmt;

inherit: INHERIT ID |;
paramList: paramTail |;
paramTail: param CM paramTail | param;
returnType: INTEGER
			| FLOAT
			| BOOLEAN
			| STRING
			| VOID
			| AUTO
			| arraytype;

 specialFunction: readInteger
				| readFloat
				| printInteger
				| writeFloat
				| printBoolean
				| readString
				| printString
				| superCall
				| preDefault
;

readInteger: READINTEGER LB RB;
READINTEGER: 'readInteger';
printInteger: PRINTINTEGER LB expr RB;
PRINTINTEGER: 'printInteger';
readFloat: READFLOAT LB RB;
READFLOAT: 'readFloat';
writeFloat: WRITEFLOAT LB expr RB;
WRITEFLOAT: 'writeFloat';
printBoolean: PRINTBOOLEAN LB expr RB;
PRINTBOOLEAN: 'printBoolean';
readString: READSTRING LB RB;
READSTRING: 'readString';
printString: PRINTSTRING LB expr RB;
PRINTSTRING: 'printString';
superCall: SUPER LB expList RB;
SUPER: 'super';
preDefault: PREVENTDEFAULT LB RB;
PREVENTDEFAULT: 'preventDefault';


/* --------------------------------------TOKEN---------------------------------*/
COMMENT: (LINE_CMT | BLOCK_CMT) -> skip;
fragment LINE_CMT: '//' ~('\r' | '\n')*;
fragment BLOCK_CMT: '/*' .*? '*/';


INTLIT: '0' | [1-9][0-9]* ('_' [0-9]+)* {self.text = self.text.replace("_","")};

FLOATLIT: (INTLIT DECPART EXPPART | INTLIT DECPART | INTLIT EXPPART | DECPART EXPPART) {self.text = self.text.replace("_","")}
;
fragment DECPART: DOT [0-9]*;
fragment EXPPART: [eE] [-+]? [0-9]+;

BOOLEANLIT: FALSE | TRUE;
fragment FALSE: 'false';
fragment TRUE: 'true';

STRINGLIT: DOUBLE_QUOTE (ESC | ~[\n\r"])* DOUBLE_QUOTE {self.text=str(self.text[1:-1])};
fragment NOT_ESC: '\\' ~('b' | 'f' | 'n' | 'r' | 't' | '"' | '\'' | '\\');
fragment ESC: '\\' ('b' | 'f' | 'n' | 'r' | 't' | '\'' | '\\' | '"');

fragment DOUBLE_QUOTE: ["];
fragment SINGLE_QUOTE: ['];
AUTO: 'auto';
BREAK: 'break';
INTEGER: 'integer';
VOID: 'void';
ARRAY: 'array';
FLOAT: 'float';
RETURN: 'return';
OUT: 'out';
BOOLEAN: 'boolean';
FOR: 'for';
STRING: 'string';
CONTINUE: 'continue';
DO: 'do';
FUNCTION: 'function';
OF: 'of';
ELSE: 'else';
IF: 'if';
WHILE: 'while';
INHERIT: 'inherit';
ADD: '+';
SUB: '-';
MUL: '*';
DIV: '/';
MOD: '%';
LESS: '<';
GT: '>';
LTE: '<=';
GTE: '>=';
NOT: '!';
AND: '&&';
OR: '||';
EQ: '==';
NOT_EQ: '!=';
CONCAT: '::';
DOT: '.';
CM: ',';
SM: ';';
ASSIGN: '=';
CL: ':';
LB: '(';
RB: ')';
LSB: '[';
RSB: ']';
LCB: '{';
RCB: '}';
ID: [a-zA-Z_]+ [a-zA-Z0-9_]*;
WS: [ \t\r\n]+ -> skip; 
UNCLOSE_STRING
	: DOUBLE_QUOTE (~["] | ESC)*? ([\r\n] | EOF) {
s = self.text
if s[len(s) - 1] == '\n' or s[len(s) - 1] == '\r':
    raise UncloseString(self.text[1:-1])
raise UncloseString(self.text[1:])
}
;
ILLEGAL_ESCAPE
	: DOUBLE_QUOTE (~[\\"] | ESC)* NOT_ESC {raise IllegalEscape(self.text[1:])
		}
;
ERROR_CHAR: .{raise ErrorToken(self.text)};