####IMPORTATIONS####
import ply.lex as lex
import ply.yacc as yacc
import sys

# Personnaliser l'ecriture des messages d'erreurs et de succés#

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
    'efk': 'efk',
    'sehviver': 'sehviver',
    'uslig': 'uslig',
    'ma': 'ma',
    'tamenguct': 'tamenguct'
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
             'STRING',
             'GT',
             'LT',
             'GE',
             'LE',
             'EE',
             'NE'
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
t_uslig = r'uslig'
t_sehviver = r'sehviver'
t_tamenguct = r'tamenguct'
t_aru = r'aru'
t_efk = r'efk'
t_ma = r'ma'
t_GT = r'\>'
t_LT = r'\<'
t_GE = r'\>\='
t_LE = r'\<\='
t_EE = r'\=\='
t_NE = r'\!\='

t_ignore = r' '


def t_STRING(t):
    r'("[^"]")|(\'[^\']\')'
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
    code : encaps taggayt NAME '{' inner_code '}'
    '''


def p_Encaps(p):
    '''
    encaps : azayez
            | uslig
            | sehviver
            | empty
    '''


def p_inCode(p):
    '''
    inner_code :  attribut_statement functions_statement
            | attribut_statement
            | functions_statement
    '''


def p_attr_statement(p):
    '''
    attribut_statement : encaps NAME
    '''


def p_function(p):
    '''
    functions_statement : main functions_statement
                        | method
                        | empty
    '''


def p_method(p):
    '''
        method : encaps NAME '(' ')' '{' statements '}'
    '''


def p_main(p):
    '''
    main :   encaps urkid ilem agejdan '(' ')' '{' statements '}'
    '''


def p_statements(p):
    '''
    statements : statement statements
                | empty
    '''


def p_statement(p):
    '''
    statement   : var_assign
                | print_statement
                | scanf_statement
                | if_statement
                | loop_control
                | empty
    '''
    run(p[1])


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


def p_loopControl(p):
    '''
        loop_control : tamenguct '(' INT ')' '{' statementsLoop '}'
    '''
    p[0] = ('loopStat', p[3],p[6])

def p_statementsLoop(p):
    '''
        statementsLoop : statementLoop statementLoop
                        | empty
    '''

    p[0] =(p[1], p[2])

def p_statementloop(p):
    '''
     statementLoop : var_assign
                        | print_statement
                        | scanf_statement
                        | if_statement
                        | empty
    '''
    p[0] = p[1]

def p_ifStatement(p):
    '''
    if_statement : ma '(' condition ')' '{' con_statements '}'
    '''
    p[0] = ('if_statement', p[3], p[6])

    # (0,1(0,1,2),2)


def p_conStatements(p):
    '''
    con_statements : con_statement con_statement con_statement
                    | empty
    '''
    p[0] = (p[1], p[2], p[3])


def p_conStatement(p):
    '''
        con_statement : var_assign
                        | print_statement
                        | scanf_statement
                        | if_statement
                        | empty
    '''
    p[0] = p[1]


def p_condition(p):
    '''
        condition : expression comparaison expression
    '''
    p[0] = (p[2], p[1], p[3])


def p_comparaison(p):
    '''
        comparaison : GT
                    | LT
                    | GE
                    | LE
                    | EE
                    | NE
    '''
    p[0] = p[1]


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
            if type(p[2]) == tuple and p[2][0] == 'string':
                env[p[1]] = p[2][1]
            else:
                env[p[1]] = run(p[2])
            print(env)
        elif p[0] == 'var':
            if p[1] not in env:
                return 'Undeclared variable found!'
            else:
                return env[p[1]]
        elif p[0] == 'aru_statement':
            if p[1] in env:
                print(env[p[1]])
            elif p[1][1] in env:
                print(env[p[1][1]])
            else:
                return run(p[1])
        elif p[0] == 'efk_statement':
            s = input()
            if s.isnumeric():
                print("it s int")
                env[p[1]] = int(s)
            elif s.isalnum():
                env[p[1]] = s
                print("its string")
            elif isfloat(s):
                env[p[1]] = float(s)
                print("it s float")
        elif p[0] == 'loopStat':
            print("hahuwa")
            print(p)
            a = p[1]
            print(p[2])
            for i in range(a):
                run(p[2][0])
                run(p[2][1])

        elif p[0] == 'if_statement':
            print(p[2])
            if p[1][0] == "==":
                if isinstance(p[1][2], int) and p[1][1][0] == 'var':
                    if compare(env[p[1][1][1]], p[1][2]):
                        for i in [0, 1, 2]:
                            run(p[2][i])
                elif isinstance(p[1][2], float) and p[1][1][0] == 'var':
                    if compare(env[p[1][1][1]], p[1][2]):
                        for i in [0, 1, 2]:
                            run(p[2][i])
                elif p[1][1][0] == 'var' and p[1][2][0] == 'var':
                    if compare(env[p[1][1][1]], env[p[1][2][0]]):
                        for i in [0, 1, 2]:
                            run(p[2][i])
                else:
                    print("condition error")
            elif p[1][0] == ">=":
                if isinstance(p[1][2], int) and p[1][1][0] == 'var':
                    if env[p[1][1][1]] >= p[1][2]:
                        for i in [0, 1, 2]:
                            run(p[2][i])
                elif isinstance(p[1][2], float) and p[1][1][0] == 'var':
                    if env[p[1][1][1]] >= p[1][2]:
                        for i in [0, 1, 2]:
                            run(p[2][i])
                elif p[1][1][0] == 'var' and p[1][2][0] == 'var':
                    if env[p[1][1][1]] >= env[p[1][2][0]]:
                        for i in [0, 1, 2]:
                            run(p[2][i])
                else:
                    print("condition error")
            elif p[1][0] == "<=":
                if isinstance(p[1][2], int) and p[1][1][0] == 'var':
                    if env[p[1][1][1]] <= p[1][2]:
                        for i in [0, 1, 2]:
                            run(p[2][i])
                elif isinstance(p[1][2], float) and p[1][1][0] == 'var':
                    if env[p[1][1][1]] <= p[1][2]:
                        for i in [0, 1, 2]:
                            run(p[2][i])
                elif p[1][1][0] == 'var' and p[1][2][0] == 'var':
                    if env[p[1][1][1]] <= env[p[1][2][0]]:
                        for i in [0, 1, 2]:
                            run(p[2][i])
                else:
                    print("condition error")
            elif p[1][0] == ">":
                if isinstance(p[1][2], int) and p[1][1][0] == 'var':
                    if env[p[1][1][1]] > p[1][2]:
                        for i in [0, 1, 2]:
                            run(p[2][i])
                elif isinstance(p[1][2], float) and p[1][1][0] == 'var':
                    if env[p[1][1][1]] > p[1][2]:
                        for i in [0, 1, 2]:
                            run(p[2][i])
                elif p[1][1][0] == 'var' and p[1][2][0] == 'var':
                    if env[p[1][1][1]] > env[p[1][2][0]]:
                        for i in [0, 1, 2]:
                            run(p[2][i])
                else:
                    print("condition error")
            elif p[1][0] == "<":
                if isinstance(p[1][2], int) and p[1][1][0] == 'var':
                    if env[p[1][1][1]] < p[1][2]:
                        for i in [0, 1, 2]:
                            run(p[2][i])
                elif isinstance(p[1][2], float) and p[1][1][0] == 'var':
                    if env[p[1][1][1]] < p[1][2]:
                        for i in [0, 1, 2]:
                            run(p[2][i])
                elif p[1][1][0] == 'var' and p[1][2][0] == 'var':
                    if env[p[1][1][1]] < env[p[1][2][0]]:
                        for i in [0, 1, 2]:
                            run(p[2][i])
                else:
                    print("condition error")
            elif p[1][0] == "!=":
                if isinstance(p[1][2], int) and p[1][1][0] == 'var':
                    if not compare(env[p[1][1][1]], p[1][2]):
                        for i in [0, 1, 2]:
                            run(p[2][i])
                elif isinstance(p[1][2], float) and p[1][1][0] == 'var':
                    if not compare(env[p[1][1][1]], p[1][2]):
                        for i in [0, 1, 2]:
                            run(p[2][i])
                elif p[1][1][0] == 'var' and p[1][2][0] == 'var':
                    if not compare(env[p[1][1][1]], env[p[1][2][0]]):
                        for i in [0, 1, 2]:
                            run(p[2][i])
                else:
                    print("condition error")
            else:
                print("error")
    else:
        return p


def compare(a, b):
    if a == b:
        return True
    return False


parser = yacc.yacc()

data = '''
    azayez taggayt $className {
        uslig urkid ilem agejdan(){
            $a=4;
            tamenguct(5){
                aru($a);
                $b = 6;
            }
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


# elif p[0] == 'conditionSOS':
# if p[0][1] == "==":
#     if run(p[1][1]) == run(p[1][2]):
#         run(p[2])
# if p[0][1] == ">=":
#     if run(p[1][1]) >= run(p[1][2]):
#         run(p[2])
# if p[0][1] == "<=":
#     if run(p[1][1]) <= run(p[1][2]):
#         run(p[2])
# if p[0][1] == ">":
#     if run(p[1][1]) > run(p[1][2]):
#         run(p[2])
# if p[0][1] == "<":
#     if run(p[1][1]) < run(p[1][2]):
#         run(p[2])
# if p[0][1] == "!=":
#     if run(p[1][1]) != run(p[1][2]):
#         run(p[2])


# elif p[1][0] == ">=":
# if run(p[1][1]) >= run(p[1][2]):
#     run(p[2])
# elif p[1][0] == "<=":
#     if run(p[1][1]) <= run(p[1][2]):
#         run(p[2])
#     elif p[1][0] == "<":
#     if run(p[1][1]) < run(p[1][2]):
#         run(p[2])
#     elif p[1][0] == ">":
#     if run(p[1][1]) > run(p[1][2]):
#         run(p[2])
#     elif p[1][0] == "!=":
#     if run(p[1][1]) != run(p[1][2]):
#         run(p[2])
