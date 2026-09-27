grammar gramatica;

// PARSER

program
    : stat+ EOF                # Programa
    ;

stat
    : ID '=' expr ';'          # Asignacion
    | expr ';'                 # SentenciaExpr
    ;

expr
    : term expr_prima          # ReglaExpr
    ;

expr_prima
    : op=('+'|'-') term expr_prima # OpSumaResta
    |                              # VacioExpr
    ;

term
    : factor term_prima        # ReglaTerm
    ;

term_prima
    : op=('*'|'/'|'%') factor term_prima # OpMulDivMod
    |                                    # VacioTerm
    ;

factor
    : FUNC '(' expr ')'        # FuncionTrig
    | ID                       # Variable
    | NUM                      # Numero
    | '(' expr ')'             # Parentesis
    | op=('+'|'-') factor      # Unario
    ;

// LEXER 

FUNC: 'sen' | 'sin' | 'cos' | 'tan' | 'abs'
    | 'Sen' | 'Sin' | 'Cos' | 'Tan' | 'Abs'
    ;

ID  : [a-zA-Z_][a-zA-Z0-9_]* ;
NUM : [0-9]+ ('.' [0-9]+)? ;

WS  : [ \t\r\n]+ -> skip ;
LINE_COMMENT : '//' ~[\r\n]* -> skip ;
BLOCK_COMMENT: '/*' .*? '*/' -> skip ;