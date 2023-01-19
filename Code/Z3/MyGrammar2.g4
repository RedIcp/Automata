grammar MyGrammar2;

// rules
program : command+ ;

command : declare_fun | assert_cmd | check_sat | get_model | declare_const ;

declare_fun : '(' 'declare-fun' ID '(' INT_W* ')' 'Int' ')' ;

declare_const: '(' 'define-const' ID 'Int' NUMBER ')' ;

assert_cmd : '(' 'assert' formula ')';

distinct_formula : '(' 'distinct' values values values*')' ;

comp_formula: '(' comp formula formula formula* ')';

operation_dormula: '(' operation NUMBER NUMBER NUMBER* ')';

values: (ID | NUMBER);

formula : distinct_formula
        | comp_formula
        | '(' comparator values values ')'
        | operation_dormula
        | '(' equal ID formula ')'
        | values
        ;

comparator : '>=' | '<=' | '<' | '>';

equal: '=';

operation: '+' | '-' | '/' | '*';

comp: 'and' | 'or';

check_sat : '(' 'check-sat' ')';

get_model : '(' 'get-model' ')';

COMMENT : ';' .*? '\n' -> skip ;

// tokens
ID : [a-zA-Z]+[a-zA-Z0-9]* ;
NUMBER : [0-9]+ ;
WS : [ \t\r\n]+ -> skip ;
INT_W: 'Int';