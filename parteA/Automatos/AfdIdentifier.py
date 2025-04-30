
from typing import Generator

from Enum.TokenType import TokenType
from Models.Token import Token


def afd_identifier(file: Generator[str, int, int], current_char, line, column) -> Token:
    state = 0

    token = Token(TokenType.IDENTIFIER.name, "", line, column)

    local_char = current_char

    while(True):
        if(state == 0):
            state = 1
            token.lexema += local_char
            
        elif(state == 1):
            if(local_char.isalnum()):
                state = 1
                token.lexema += local_char
            else:
                return token
        
        local_char, _, _ = next(file)
