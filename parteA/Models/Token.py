class Token:
    def __init__(self, tipo, lexema, linha, coluna):
        self.tipo = tipo
        self.lexema = lexema
        self.linha = linha
        self.coluna = coluna

    def __str__(self):
        return f"Token({self.tipo}, {self.lexema}) - Linha: {self.linha}, Coluna: {self.coluna})"