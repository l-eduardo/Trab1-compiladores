
from typing import Generator

from Enum.RelationalOperators import RelationalOperators
from Enum.TokenType import TokenType
from Models.Token import Token


def afd_relational_operator(file: Generator[str, int, int], current_char, line, column) -> Token:
    state = 0

    token = Token(TokenType.RELATIONAL.name, "", line, column)

    local_char = current_char

    while(True):
        if(state == 0):
            if (local_char == "<"):
                state = 1

            elif(local_char == "="):
                state = 5

            elif(local_char == ">"):
                state = 6

            else:
                return None
            
        elif(state == 1):
            if(local_char == "="):
                state = 2

            elif(local_char == ">"):
                state = 3

            elif(local_char == " "):
                token.lexema = RelationalOperators.LESS_THAN.name
                return token

            else:
                return None

        elif(state == 2):
            if(local_char == " "):
                token.lexema = RelationalOperators.LESS_EQUAL.name
                return token

            return None

        elif(state == 3):
            if(local_char == " "):
                token.lexema = RelationalOperators.NOT_EQUAL.name
                return token

            return None

        elif(state == 4):
            if(local_char == " "):
                token.lexema = RelationalOperators.LESS_THAN.name
                return token

            return None
        
        elif(state == 5):
            token.lexema = RelationalOperators.EQUAL.name
            return token
        
        elif(state == 6):
            if(local_char == "="):
                state = 7

            elif(local_char == " "):
                token.lexema = RelationalOperators.GREATER_THAN.name
                return token

            else:
                return None
            
        elif(state == 7):
            if(local_char == " "):
                token.lexema = RelationalOperators.GREATER_EQUAL.name
                return token

            return None
        
        elif(state == 8):
            if(local_char == " "):
                token.lexema = RelationalOperators.GREATER_THAN.name
                return token

            return None
    
        local_char, _, _ = next(file)
