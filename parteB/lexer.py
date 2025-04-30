import ply.lex as lex


reserved = {
    'def': 'DEF',
    'int': 'INT',
    'if': 'IF',
    'else': 'ELSE',
    'return': 'RETURN',
    'print': 'PRINT',
}

tokens = [
    # Identificadores e números
    'ID', 'NUM',

    # Operadores relacionais
    'LESS_THAN', 'GREATER_THAN',
    'LESS_EQUAL', 'GREATER_EQUAL',
    'EQUAL_COMPARISON', 'NOT_EQUAL',

    # Operadores aritméticos e de atribuição
    'PLUS', 'MINUS', 'TIMES', 'DIVIDE',
    'ASSIGN',

    # Delimitadores
    'LPAREN', 'RPAREN',
    'LBRACE', 'RBRACE',
    'COMMA', 'SEMICOLON'
] + list(reserved.values())

# -------------------------------
# Regex - Tokens
# -------------------------------

# Operadores relacionais
t_LESS_EQUAL        = r'<='
t_GREATER_EQUAL     = r'>='
t_EQUAL_COMPARISON  = r'=='
t_NOT_EQUAL         = r'!='
t_LESS_THAN         = r'<'
t_GREATER_THAN      = r'>'

# Operadores aritméticos
t_PLUS              = r'\+'
t_MINUS             = r'-'
t_TIMES             = r'\*'
t_DIVIDE            = r'/'

# Atribuicao
t_ASSIGN            = r'='

# Símbolos e pontuação
t_LPAREN            = r'\('
t_RPAREN            = r'\)'
t_LBRACE            = r'\{'
t_RBRACE            = r'\}'
t_COMMA             = r','
t_SEMICOLON         = r';'

# abulações
t_ignore = ' \t'

symbol_table = {}

def t_ID(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    t.type = reserved.get(t.value, 'ID') 
    if t.type == 'ID':
        if t.value not in symbol_table:
            symbol_table[t.value] = {'token': 'ID'}
    return t

def t_NUM(t):
    r'\d+'
    t.value = int(t.value)
    return t

def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

def t_error(t):
    col = find_column(t)
    print(f"Erro léxico: caractere inválido '{t.value[0]}' na linha {t.lexer.lineno}, coluna {col}")
    t.lexer.skip(1)

def find_column(token):
    last_cr = lexer.lexdata.rfind('\n', 0, token.lexpos)
    if last_cr < 0:
        last_cr = -1
    return token.lexpos - last_cr

lexer = lex.lex()
