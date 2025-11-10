# Classe que representa o cliente do sistema de aluguel
class Cliente:
    # Método construtor: inicializa o cliente com nome e se possui crianças
    def __init__(self,nome, possui_criancas):
        self.nome = nome # Nome do cliente
        self.possui_criancas = possui_criancas # Indica se o cliente tem crianças (True/False)
        