from typing import Generator

from Enum.TokenType import TokenType
from Models.Token import Token


def afd_number(file: Generator[str, int, int], current_char, line, column) -> Token:
    state = 0

    token = Token(TokenType.NUMBER.name, "", line, column)
    local_char = current_char

    if local_char == None:
        return None

    while(True):
        if(state == 0):
            if(local_char == None or not local_char.isdigit()):
                return None

            state = 1
            token.lexema += local_char
            
        elif(state == 1):
            if(local_char == " "  or
               local_char == "\n" or
               local_char == "\r" or
               local_char == "\t" or
               local_char == "\0" or
               local_char == None):
                return token
            
            if(not local_char.isdigit()):
                return None

            state = 1
            token.lexema += local_char

        local_char, _, _ = next(file)
