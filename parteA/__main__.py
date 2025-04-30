# Analisador Léxico - Parte A
# Autor: Luiz Eduardo da Silva
import argparse

from Automatos.AfdRelationalOperator import afd_relational_operator
from Automatos.AfdIdentifier import afd_identifier
from Automatos.AfdNumber import afd_number


def read_chars(path):
    with open(path, 'r') as f:
        for lineno, line in enumerate(f, start=1):
            print(f"\n---- Linha: {lineno} ----")
            for colno, ch in enumerate(line, start=1):
                yield ch, lineno, colno
    yield None, None, None 

def is_new_line(char):
    return char == "\n" or char == "\r"

def is_relational_operator(char):
    return char == ">" or char == "<" or char == "=" or char == "≥" or char == "≤" or char == "≠"

parser = argparse.ArgumentParser(description='Analisador Léxico')
parser.add_argument('input_file', help='Path to the input file')
args = parser.parse_args()

file_gen = read_chars(args.input_file)

# file_gen = read_chars("./inputs/input_valido.txt")

if __name__ == "__main__":
    for char, line, col in file_gen:
        if char is None:
            break

        if is_relational_operator(char):
            token = afd_relational_operator(file_gen, char, line, col)
            if token != None:
                print(token)
            else:
                raise Exception(f"Erro na linha {line}, coluna {col}: operador relacional inválido")

        if char.isdigit():
            token = afd_number(file_gen, char, line, col)
            if token != None:
                print(token)
            else:
                raise Exception(f"Erro na linha {line},  coluna {col}: número inválido")

        if char.isalpha():
            token = afd_identifier(file_gen, char, line, col)
            if token != None:
                print(token)
            else:
                raise Exception(f"Erro na linha {line}, coluna {col}: identificador inválido")
     