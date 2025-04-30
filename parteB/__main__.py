# Analisador Léxico - Parte A
# Autor: Luiz Eduardo da Silva
import argparse
from lexer import find_column, lexer, symbol_table
from utils.print_tables import print_symbol_table, print_token_list


parser = argparse.ArgumentParser(description='Analisador Léxico')
parser.add_argument('input_file', help='Path to the input file')
args = parser.parse_args()

with open(args.input_file, 'r') as f:
    data = f.read()

# with open("./inputs/input_valido.lsi", 'r') as f:
#     data = f.read()

lexer.input(data)

tokens_encontrados = []
while True:
    token = lexer.token()
    if not token:
        break
    tokens_encontrados.append(token)

print_token_list(tokens_encontrados)

print_symbol_table()
