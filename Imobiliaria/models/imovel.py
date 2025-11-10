class Imovel:
    # Classe responsável por representar um imóvel e calcular o valor do aluguel com base nas suas características
    def __init__(self, tipo, quartos=1, garagem=False, vagas_estacionamento=0):
        # Define o tipo de imóvel (apartamento, casa ou estúdio
        self.tipo = tipo.lower()
        
        # Quantidade de quartos (1 ou 2)
        self.quartos = quartos
        
        # Define se o imóvel possui garagem (True ou False
        self.garagem = garagem

        # Número de vagas de estacionamento (usado apenas para estúdio)
        self.vagas_estacionamento = vagas_estacionamento

    # Retorna o valor base do aluguel conforme o tipo de imóvel
    def calcular_valor_base(self):
        if self.tipo == "apartamento":
            return 700.0
        elif self.tipo == "casa":
            return 900.0
        elif self.tipo == "estudio":
            return 1200.0
        else:
            return 0.0

    # Calcula o valor total do aluguel aplicando adicionais
    def calcular_aluguel(self):
        valor = self.calcular_valor_base()

        # Apartamento com 2 quartos: +200
        if self.tipo == "apartamento" and self.quartos == 2:
            valor += 200.0

        # Casa com 2 quartos: +250
        if self.tipo == "casa" and self.quartos == 2:
            valor += 250.0

        # Garagem para casa ou apartamento: +300
        if self.garagem and self.tipo in ["apartamento", "casa"]:
            valor += 300.0

        # Estúdio com vagas de estacionamento
        if self.tipo == "estudio":
            
            # Duas vagas: +R$250,00
            if self.vagas_estacionamento >= 2:
                valor += 250.0

            # Mais de duas vagas: +R$60,00 por vaga extra
            if self.vagas_estacionamento > 2:
                vagas_extras = self.vagas_estacionamento - 2
                valor += vagas_extras * 60.0

        # Retorna o valor total do aluguel calculado
        return valor
