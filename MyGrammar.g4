grammar MyGrammar;

prog
    : single_statement*
    ;

single_statement
    : function_declaration
    | function_call ';'
    | print_statement ';'
    | assignment ';'
    | if_statement
    | while_statement
    ;

function_declaration
    : type ID '(' (parameter_declaration (',' parameter_declaration)*)? ')' block
    ;

parameter_declaration
    : type ID
    ;

block
    : '{' (statement)* '}'
    ;

statement
    : function_call ';'
    | print_statement ';'
    | return_statement ';'
    | assignment ';'
    | if_statement
    | while_statement
    ;

function_call
    : ID '(' (expression (',' expression)*)? ')'
    ;
    
print_statement
    : 'print' '(' expression ')'
    ;

return_statement
    : 'return' expression
    ;

assignment
    : type ID '=' expression
    ;

if_statement
    : 'if' '(' expression ')' statement ('else' statement)?
    ;

while_statement
    : 'while' '(' expression ')' statement
    ;

expression
    : ID
    | INT
    | FLOAT
    | BOOL
    | STRING
    | function_call
    | '(' expression ')'
    | expression (PLUS | MINUS | MULTIPLY | DIVIDE | MODULO | EQUALS | NOT_EQUALS | GREATER_THAN | LESS_THAN | GREATER_THAN_EQUALS | LESS_THAN_EQUALS | AND | OR) expression
    ;

type 
    : 'int' 
    | 'float' 
    | 'bool' 
    | 'string' 
    | 'void'
    ;

ID  : [a-zA-Z]+;
INT : [0-9]+;
FLOAT : [0-9]+ '.' [0-9]+;
BOOL : 'true' | 'false';
STRING : '"' .*? '"';
PLUS : '+';
MINUS : '-';
MULTIPLY : '*';
DIVIDE : '/';
MODULO : '%';
EQUALS : '==';
NOT_EQUALS : '!=';
GREATER_THAN : '>';
LESS_THAN : '<';
GREATER_THAN_EQUALS : '>=';
LESS_THAN_EQUALS : '<=';
AND : '&&';
OR : '||';
WS: [ \t\r\n]+ -> skip ;