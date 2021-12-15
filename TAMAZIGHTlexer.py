import ply.lex as lex

#Personnaliser l'ecriture des messages d'erreurs et de succés###########
BLUE   = '\33[34m'
RED = '\033[91m'
END = '\033[0m'
BOLD = '\033[1m'
UNDERLINE = '\033[4m'

tokens = [
    'ADD',
    'MINUS',
    'MULTIP',
    'DIV',
    'INT',
    'FLOAT',
    'EQ',
    'NOT_EQ',
    'LESS_T',
    'BIG_T',
    'LESS_E',
    'BIG_E',
    'LPAR',
    'RPAR',
    'LACC',
    'RACC',
    'VAR',
    'STRING',
    'DIV_EUC',
    'MOD',
    'AFFECT',
    'LBRA',
    'RBRA',
    'FINLIGNE',
    'CONDITION',
    'BOUCLE_FOR',
    'BOUCLE_WHILE',
    'BOOL'
]

#For Simple Tokens
t_ADD = r'\+'
t_MINUS = r'\-'
t_MULTIP = r'\*'
t_DIV = r'\/'
t_EQ = r'=='
t_NOT_EQ = r'!='
t_LESS_T = r'<'
t_BIG_T = r'>'
t_LESS_E = r'<='
t_BIG_E = r'>='
t_DIV_EUC = r'//'
t_MOD = r'%'
t_AFFECT = r'='
t_LPAR=r'\('
t_RPAR=r'\)'
t_LACC=r'\{'
t_RACC=r'\}'
t_LBRA=r'\['
t_RBRA=r'\]'
t_FINLIGNE = r';'

#For Complex Tokens INT FLOAT VAR STRING 
def t_BOOL(t):
    r'false|true'
    return t

def t_BOUCLE_FOR(t) :
    r'for'
    return t

def t_BOUCLE_WHILE(t) :
    r'while'
    return t

def t_CONDITION(t):
    r'if'
    return t

def t_STRING(t):
    r'("[^"]*")|(\'[^\']*\')'
    t.value = str(t.value)
    return t

def t_VAR(t):
    r'[$_]*\w+'
    t.type = 'VAR'
    return t

def t_FLOAT(t) :
    r'\d+\.\d*'
    t.value = float(t.value)
    return t

def t_INT(t) :
    r'\d+'
    t.value = int(t.value)
    return t

#Default Configuration

t_ignore = ' '

def t_error(t):
    print(f"{RED}  {BOLD}  ERROR MESSAGE TAMAZIGHT {END}:  {BLUE} '{t.value[0]}' {END}")
    t.lexer.skip(1)

def t_newline(t) :
    r'\n+'
    t.lexer.lineno = len(t.value)

#To display Lexer Results
lexer = lex.lex()

data = '''
    while;
    for;
    true;
    false;
    if;
'''
lexer.input(data)

while(True) :
    token = lexer.token()
    if not token :
        break
    print(token)