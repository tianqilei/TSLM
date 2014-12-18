# -----------------------------------------------------------------------------
# lexer.py
#
# A simple calculator with variables -- all in one file.
# -----------------------------------------------------------------------------

reserved = {
    'class':'CLASS',
    'block':'BLOCK',
    'event':'EVENT',
    'transition':'TRANSITION',
    'state':'STATE',
    'end':'END',
    'synchronization':'SYNCHRONIZATION',
    'observer':'OBSERVER',
    'and':'AND',
    'or':'OR',
    'not': 'NOT'
}


tokens = [ 'POINT', 'DEUXPOINTS', 'FLECHE', 'ANDCOMMERCIAL', 'VIRGULE',
	 'IDENTIFIER', 'LEFTBRACKET', 'RIGHTBRACKET' ] + list(reserved.values())

# Tokens

t_VIRGULE = r'\,'
t_DEUXPOINTS  = r'\:'
t_ANDCOMMERCIAL = r'\&'
t_POINT = r'\.'
t_FLECHE = r'\->'
t_LEFTBRACKET = r'\('
t_RIGHTBRACKET = r'\)'



# Ignored characters
t_ignore = " \t"


def t_newline(t):
    r'\n+'
    t.lexer.lineno += t.value.count("\n")

def t_IDENTIFIER(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    t.type = reserved.get(t.value,'IDENTIFIER')    # Check for reserved words
    t.value = t.value
    return t


def t_error(t):
    print("lexer : Illegal character '%s'" % t.value[0] + "at the line : " + str(t.lexer.lineno))
    print("Syntax error! Exit the program!")
    t.lexer.skip(1)
    exit(1)


# Build the lexer
import ply.lex as lex
lex.lex()

from data import getFilePath
file = open(getFilePath.getFilePath())
data=''
while 1:
    line = file.readline()
    if not line:
        break
    data += line

#print(data)
lex.input(data)
