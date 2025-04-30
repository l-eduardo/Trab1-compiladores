from lexer import find_column, symbol_table


# Serve simente para printar a tabela que representa a tabela de simbolos
def print_symbol_table():
    if not symbol_table:
        print("Tabela de símbolos vazia.")
        return

    print("\nTabela de Símbolos:")
    print("-" * 40)
    print(f"{'Nome':<20} {'Token':<10}")
    print("-" * 40)
    for nome, dados in symbol_table.items():
        token = dados.get('token', '-')
        print(f"{nome:<20} {token:<10}")
    print("-" * 40)

# Serve pra printar a tabela que representa a lista de tokens
def print_token_list(token_list):
    if not token_list:
        print("Nenhum token encontrado.")
        return

    print("\nLista de Tokens:")
    print("-" * 75)
    print(f"{'Token':<20} {'Lexema':<20} {'Linha':<10} {'Coluna':<10}")
    print("-" * 75)
    for tok in token_list:
        lexema = str(tok.value)
        col = find_column(tok)
        print(f"{tok.type:<20} {lexema:<20} {tok.lineno:<10} {col:<10}")
    print("-" * 75)

