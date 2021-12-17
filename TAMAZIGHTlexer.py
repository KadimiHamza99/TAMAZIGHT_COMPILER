import ply.lex as lex

#Personnaliser l'ecriture des messages d'erreurs et de succés###########
BLUE   = '\33[34m'
RED = '\033[91m'
END = '\033[0m'
BOLD = '\033[1m'
UNDERLINE = '\033[4m'
reserved = {
    'AZAYEZ' : 'AZAYEZ',
    'USLIG' : 'USLIG',
    'SEHVIVER' : 'SEHVIVER',
    'TAGGAYT' : 'TAGGAYT',
    'TIMMAD' : 'TIMMAD',
    'ILAW' : 'ILAW',
    'ASEKKIT' : 'ASEKKIT',
    'ARU' : 'ARU',
    'GHER' : 'GHER',
    'MA' : 'MA',
    'MA_ULAC' : 'MA_ULAC',
    'T_TIDETT' : 'T_TIDETT',
    'ADERYIS' : 'ADERYIS',
    'TUKKEST' : 'TUKKEST'
}

literals = [',', ';', '=', '(', ')', '{', '}']

tokens = [
    'ADD','MINUS','MULTIP','DIV','DIV_EUC','MOD',
    'VAR','INT','FLOAT','STRING','BOOL',
] + list(reserved.values())

#For Simple Tokens
    ##You should avoid writing individual rules for reserved words
t_ADD = r'\+'
t_MINUS = r'\-'
t_MULTIP = r'\*'
t_DIV = r'\/'
t_MOD = r'%'
t_DIV_EUC = r'//'

#For Complex Tokens INT FLOAT VAR STRING
def t_BOOL(t):
    r'false|true'
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
def t_COMMENT(t):
    r'\@.*'
    pass

t_ignore = ' '

def t_error(t):
    print(f"{RED}  {BOLD}  ERROR MESSAGE TAMAZIGHT {END}:  {BLUE} '{t.value[0]}' {END}")
    t.lexer.skip(1)

def t_newline(t) :
    r'\n+'
    t.lexer.lineno = len(t.value)

#To display Lexer Results
lexer = lex.lex(debug=0)

data = '''
    USLIG TAGGAYT test{
        private string = "hamza kadimi";
        protected a = 6;
        @hamza
    }
'''
lexer.input(data)

while(True) :
    token = lexer.token()
    if not token :
        break
    print(token)