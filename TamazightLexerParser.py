####IMPORTATIONS####
import ply.lex as lex
import ply.yacc as yacc
import sys

#Personnaliser l'ecriture des messages d'erreurs et de succés#

BLUE = '\33[34m'
RED = '\033[91m'
END = '\033[0m'
BOLD = '\033[1m'
UNDERLINE = '\033[4m'

####< L E X E R > ###

reserved = {
    'azayez': 'azayez',
    'taggayt': 'taggayt',
    'urkid': 'urkid',
    'ilem': 'ilem',
    'agejdan': 'agejdan',
    'aru': 'aru',
    'efk': 'efk'
}

tokens = [
    'INT',
    'FLOAT',
    'NAME',
    'PLUS',
    'MINUS',
    'DIVIDE',
    'MULTIPLY',
    'EQUALS',
    'STRING'
] + list(reserved.values())

literals = [',', ';', '(', ')', '{', '}']

t_PLUS = r'\+'
t_MINUS = r'\-'
t_MULTIPLY = r'\*'
t_DIVIDE = r'\/'
t_EQUALS = r'\='
t_azayez = r'azayez'
t_taggayt = r'taggayt'
t_urkid = r'urkid'
t_ilem = r'ilem'
t_agejdan = r'agejdan'
t_aru = r'aru'
t_efk = r'efk'

t_ignore = r' '


def t_STRING(t):
    r'("[^"]*")|(\'[^\']*\')'
    t.value = str(t.value)
    return t


def t_FLOAT(t):
    r'\d+\.\d*'
    t.value = float(t.value)
    return t


def t_INT(t):
    r'\d+'
    t.value = int(t.value)
    return t


def t_NAME(t):
    r'\$[a-zA-Z_][a-zA-Z0-9_]*'
    t.type = "NAME"
    return t


def t_error(t):
    print(
        f"{RED}  {BOLD}  ERROR MESSAGE TAMAZIGHT {END}:  {BLUE} '{t.value[0]}' {END}")
    t.lexer.skip(1)


def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)


def t_COMMENT(t):
    r'\@.*'
    pass


lexer = lex.lex()

### < / L E X E R > ###

### < P A R S E R >###

precedence = (
    ('left', 'PLUS', 'MINUS'),
    ('left', 'MULTIPLY', 'DIVIDE')
)


def p_code(p):
    '''
    code : azayez taggayt NAME '{' main '}'
    '''


def p_main(p):
    '''
    main : azayez urkid ilem agejdan '(' ')' '{' statements '}'
    '''


def p_statements(p):
    '''
    statements : statements statement
                | empty
    '''


def p_statement(p):
    '''
    statement   : var_assign
                | print_statement
                | scanf_statement
                | empty
    '''
    print(run(p[1]))


def p_varAssign(p):
    '''
    var_assign : NAME EQUALS expression ';'
    '''
    p[0] = ('=', p[1], p[3])


def p_printStat(p):
    '''
    print_statement : aru '(' expression ')' ';'
    '''
    p[0] = ('aru_statement', p[3])


def p_scanfStat(p):
    '''
    scanf_statement : efk '(' NAME ')' ';'
    '''
    p[0] = ('efk_statement', p[3])


def p_expression(p):
    '''
    expression :  expression MULTIPLY expression
                | expression DIVIDE expression
                | expression MINUS expression
                | expression PLUS expression
    '''
    p[0] = (p[2], p[1], p[3])


def p_expression_int_float(p):
    '''
    expression : INT 
                | FLOAT
    '''
    p[0] = p[1]


def p_expression_string(p):
    '''
    expression : STRING
    '''
    p[0] = ('string', p[1])


def p_expression_var(p):
    '''
    expression : NAME
    '''
    p[0] = ('var', p[1])


def p_empty(p):
    '''
    empty :
    '''
    p[0] = None


def p_error(p):
    print("Syntax error found !")


env = {}


def run(p):
    if type(p) == tuple:
        if p[0] == '+':
            return run(p[1]) + run(p[2])
        elif p[0] == '-':
            return run(p[1]) - run(p[2])
        elif p[0] == '*':
            return run(p[1]) * run(p[2])
        elif p[0] == '/':
            return run(p[1]) / run(p[2])
        elif p[0] == '=':
            if (type(p[2]) == tuple and p[2][0] == 'string'):
                env[p[1]] = p[2][1]
            else:
                env[p[1]] = run(p[2])
            print(env)
        elif p[0] == 'var':
            if(p[1] not in env):
                return 'Undeclared variable found!'
            else:
                return env[p[1]]
        if(p[0] == 'aru_statement'):
            if(p[1] in env):
                print(env[p[1]])
            else:
                return run(p[1])
        elif(p[0] == 'efk_statement'):
            s = input()
            if(s.isnumeric()):
                print("it s int")
                env[p[1]] = int(s)
            elif(s.isalnum()):
                env[p[1]] = s
                print("its string")
            elif(isfloat(s)):
                env[p[1]] = float(s)
                print("it s float")
    else:
        return p


parser = yacc.yacc()

data = '''
    azayez taggayt $className {
        azayez urkid ilem agejdan(){
            efk($a);
            efk($b);
            $c = $a+$b;
            aru($c);
        }
    }
'''


def isfloat(num):
    try:
        float(num)
        return True
    except ValueError:
        return False


parser.parse(data)

# while True:
#     try:
#         s=input('>> ')
#     except EOFError:
#         break
#     parser.parse(s)

### < / P A R S E R > ###
