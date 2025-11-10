# Importação das classes necessárias
from models.imovel import Imovel
from models.cliente import Cliente
import csv
import os

# Classe responsável por representar o contrato entre cliente e imóvel
class Contrato:
    def __init__(self, imovel: Imovel, cliente: Cliente, parcelas_contrato: int = 5):
        # Associação das classes Cliente e Imovel ao contrato
        self.imovel = imovel
        self.cliente = cliente
        self.valor_contrato = 2000.0 # Valor fixo do contrato base

        # Garante que o número de parcelas esteja entre 1 e 5
        self.parcelas_contrato = max(1, min(5, parcelas_contrato))

    # Cálculo do valor do aluguel mensal (com possíveis descontos)
    def calcular_aluguel_mensal(self):
        aluguel = self.imovel.calcular_aluguel()
        print("Valor bruto do aluguel:", aluguel)
        print("Tipo de imóvel:", self.imovel.tipo)
        print("Cliente possui crianças?:", self.cliente.possui_criancas)

        # Desconto de 5% para apartamentos sem crianças
        if self.imovel.tipo == "apartamento" and not self.cliente.possui_criancas:
            aluguel *= 0.95 # Aplica desconto
            print("Desconto aplicado! Novo valor:", aluguel)
        else:
            print("Sem desconto aplicado.")
        return round(aluguel, 2)
    
    # Cálculo do valor de cada parcela do contrato
    def calcular_parcela_contrato(self):
        return self.valor_contrato / self.parcelas_contrato

    # Geração do arquivo CSV com o orçamento detalhado
    def gerar_csv_orcamento(self, caminho_arquivo="output/orcamento.csv"):
        aluguel = self.calcular_aluguel_mensal()
        parcela_contrato = self.calcular_parcela_contrato()

        #Garante que a pasta exista
        diretorio = os.path.dirname(caminho_arquivo)
        if diretorio and not os.path.exists(diretorio):
            os.makedirs(diretorio)

        with open(caminho_arquivo, mode="w", newline="", encoding="utf-8") as arquivo:
            escritor = csv.writer(arquivo, delimiter=";")
            # Cabeçalho das colunas
            escritor.writerow(["Mês", "Aluguel (R$)", "Parcela contrato (R$)", "Total do mês (R$)"])
            
            # Gera os valores mês a mês (12 meses)
            for mes in range(1, 13):
                valor_parcela = parcela_contrato if mes <= self.parcelas_contrato else 0.0
                total_mes = aluguel + valor_parcela
                # Escreve cada linha no CSV
                escritor.writerow([mes, f"{aluguel:.2f}", f"{valor_parcela:.2f}", f"{total_mes:.2f}"])