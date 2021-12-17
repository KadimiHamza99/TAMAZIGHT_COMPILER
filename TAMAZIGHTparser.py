from TAMAZIGHTlexer import tokens,lexer
from ply import yacc

def p_string_exp(p):
    '''
    exp : STRING
    '''
    p[0] = ('string', p[1])

def p_int_exp(p):
    '''
    exp : INT
    '''
    p[0] = ('string', p[1])

def p_float_exp(p):
    '''
    exp : FLOAT
    '''
    p[0] = ('string', p[1])

def p_code(p) :
    '''
    code : USLIG TAGGAYT VAR '{' statements '}'
        | AZAYEZ TAGGAYT VAR '{' statements '}'
        | SEHVIVER TAGGAYT VAR '{' statements '}'
    '''

def p_statements(p) :
    '''
    statements : statementList
    '''

def p_statementList(p) :
    '''
    statementList : statement statementList
                | empty
    '''