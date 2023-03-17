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
dimension: INTLIT COMMA dimension | INTLIT;

//Variables ---------------------------------------------------------------
vardecl: vardeclNoEq | vardeclEq;
vardeclNoEq: idlist COLON (eletype | arraytype) SEMI;
vardeclEq
	: IDENTIFIER COMMA assignment COMMA expr SEMI
	| IDENTIFIER COLON (eletype | arraytype) EQUAL expr SEMI
;
assignment
	: IDENTIFIER COMMA assignment COMMA expr
	| IDENTIFIER COLON (eletype | arraytype) EQUAL expr
;

arraylit: LCB (exprlist |) RCB;
idlist: IDENTIFIER COMMA idlist | IDENTIFIER;
exprlist: expr COMMA exprlist | expr;

parameter
	: (INHERIT |) (OUT |) IDENTIFIER COLON (eletype | arraytype)
;

expr: expr1 CONCAT expr1 | expr1;

expr1: expr2 compare expr2 | expr2;
compare: EQUAL_TO | NOT_EQUAL | LESS | GREATER | LTE | GTE;
expr2: expr2 (AND | OR) expr3 | expr3;
expr3: expr3 (PLUS | MINUS) expr4 | expr4;
expr4: expr4 (MUL | DIV | MOD) expr5 | expr5;
expr5: NOT expr5 | expr6;
expr6: MINUS expr6 | expr7;
expr7: IDENTIFIER LSB exprlist RSB | expr8;
expr8: (LB expr RB) | factor;
factor
	: INTLIT
	| FLOATLIT
	| STRINGLIT
	| IDENTIFIER
	| funccall
	| arraylit
	| BOOLEANLIT
;

arrayCell: IDENTIFIER LSB exprlist RSB;
funccall: (IDENTIFIER LB (exprlist |) RB) |  specialFunction;

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

assignStmt: lhs EQUAL expr SEMI;
lhs: IDENTIFIER LSB exprlist RSB | IDENTIFIER;

ifStmt: (IF expr stmtlocal ELSE stmtlocal) | IF expr stmtlocal;

forStmt
	: FOR LB initExpr COMMA conditionExpr COMMA updateExpr RB stmtlocal
;

initExpr: IDENTIFIER EQUAL expr;

conditionExpr: expr operator expr;
operator: LESS | GREATER | LTE | GTE | NOT_EQUAL | EQUAL_TO;

updateExpr: expr;

whileStmt: WHILE LB expr RB stmtlocal;

doWhileStmt: DO blockStmt WHILE expr SEMI;

callStmt: ( specialFunction | (IDENTIFIER LB (exprlist |) RB)) SEMI;

blockStmt: LCB stmtTerm RCB;
stmtTerm: stmtList |;
stmtList: stmt stmtList | stmt;

breakStmt: BREAK SEMI;

continueStmt: CONTINUE SEMI;

returnStmt: RETURN (expr |) SEMI;


funcdecl
	: IDENTIFIER COLON FUNCTION returnType LB paramterList RB inheritance blockStmt
;

inheritance: INHERIT IDENTIFIER |;
paramterList: paramterListTerm |;
paramterListTerm: parameter COMMA paramterListTerm | parameter;
returnType: INTEGER
			| FLOAT
			| BOOLEAN
			| STRING
			| VOID
			| AUTO
			| arraytype
;

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
superCall: SUPER LB exprlist RB;
SUPER: 'super';
preDefault: PREVENTDEFAULT LB RB;
PREVENTDEFAULT: 'preventDefault';


/* --------------------------------------TOKEN---------------------------------*/
COMMENT: (SingleLineComment | MultiLineComment) -> skip;
fragment SingleLineComment: '//' ~('\r' | '\n')*;
fragment MultiLineComment: '/*' .*? '*/';
fragment CommentAll: '/*' .*? EOF;

INTLIT
	: '0'
	| [1-9][0-9]* (UNDERSCORE [0-9]+)* {self.text = self.text.replace("_","")}
;

fragment UNDERSCORE: '_';

FLOATLIT
	: (
		INTLIT DECPART EXPPART
		| INTLIT DECPART
		| INTLIT EXPPART
		| DECPART EXPPART
	) {self.text = self.text.replace("_","")}
;
fragment DECPART: PERIOD [0-9]*;
fragment EXPPART: [eE] [-+]? [0-9]+;

BOOLEANLIT: FALSE | TRUE;
fragment FALSE: 'false';
fragment TRUE: 'true';

STRINGLIT
	: DUO_QUOTE (ESC | ~[\n\r"])* DUO_QUOTE {self.text=str(self.text[1:-1])}
;
fragment NOTESC
	: '\\' ~('b' | 'f' | 'n' | 'r' | 't' | '"' | '\'' | '\\')
;
fragment ESC
	: '\\' ('b' | 'f' | 'n' | 'r' | 't' | '\'' | '\\' | '"')
;
fragment AllEscSeq: '\\' ~["];
fragment DUO_QUOTE: ["];
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
PLUS: '+';
MINUS: '-';
MUL: '*';
DIV: '/';
MOD: '%';
LESS: '<';
GREATER: '>';
LTE: '<=';
GTE: '>=';
NOT: '!';
AND: '&&';
OR: '||';
EQUAL_TO: '==';
NOT_EQUAL: '!=';
CONCAT: '::';
PERIOD: '.';
COMMA: ',';
SEMI: ';';
EQUAL: '=';
COLON: ':';
LB: '(';
RB: ')';
LSB: '[';
RSB: ']';
LCB: '{';
RCB: '}';
IDENTIFIER: [a-zA-Z_]+ [a-zA-Z0-9_]*;
WS: [ \t\r\n]+ -> skip; 
UNCLOSE_STRING
	: DUO_QUOTE (~["] | ESC)*? ([\r\n] | EOF) {
s = self.text
if s[len(s) - 1] == '\n' or s[len(s) - 1] == '\r':
    raise UncloseString(self.text[1:-1])
raise UncloseString(self.text[1:])
}
;
ILLEGAL_ESCAPE
	: DUO_QUOTE (~[\\"] | ESC)* NOTESC {raise IllegalEscape(self.text[1:])
		}
;
ERROR_CHAR: .{raise ErrorToken(self.text)};