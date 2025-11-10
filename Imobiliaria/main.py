# Importação das classes principais do sistema
from models.imovel import Imovel
from models.cliente import Cliente
from models.contrato import Contrato

# Função auxiliar para perguntar algo ao usuário e garantir resposta válida
def perguntar(texto):
    resposta = input(texto + " (s/n):  ").strip().lower()
    return resposta == "s"

# Função principal do sistema
def main():
    print("Sistema de Orcamento de Aluguel - Imobiliária R.M ")
    print("Tipos de imóvel:")
    print("1 - Apartamento")
    print("2 - Casa")
    print("3 - Estúdio")

    # Entrada do tipo de imóvel
    opcao_tipo = input("Escolha o tipo de imóvel (1/2/3):  ").strip()
    
    # Define o tipo de imóvel conforme a opção escolhida
    if opcao_tipo == "1":
        tipo = "apartamento"
    elif opcao_tipo == "2":
        tipo = "casa"
    elif opcao_tipo == "3":
        tipo = "estudio"
    else:
        # Caso o usuário digite algo diferente de 1, 2 ou 3
        print("Opção inválida. Tente novamente!")
        return
                
    # Se o tipo for apartamento ou casa, pergunta sobre quartos e garagem
    if tipo in ["apartamento", "casa"]:
        # Pergunta quantos quartos o imóvel possui
        quartos = int(input("Quantidade de quartos (1 ou 2):  ").strip())
        # Caso o usuário digite algo fora do esperado
        if quartos not in [1,2]:
            print("Quantidade de quartos inválida. Usando 1 quarto.")
            quartos = 1
        # Pergunta se o imóvel possui garagem
        garagem = perguntar("Deseja incluir vaga de garagem?")
        vagas_estacionamento = 0 # Apartamentos e casas não usam esse campo
    else:
        # Caso o tipo seja estúdio
        quartos = 1 # Estúdios sempre têm 1 quarto
        garagem = False # Estúdios não possuem garagem
        # Pergunta quantas vagas de estacionamento o estúdio tem
        vagas_estacionamento = int( input("Quantidade de vagas de estacionamento:  ").strip())

     # Cadastro das informações do cliente
    nome_cliente = input("Nome do cliente: ").strip()
    tem_criancas = perguntar("O cliente possui crianças?")

    # Cria o objeto Cliente com as informações preenchidas
    cliente = Cliente(nome_cliente, possui_criancas=tem_criancas)
    
    # Cria o objeto Imovel com base nos dados coletados
    imovel = Imovel(tipo=tipo, quartos=quartos, garagem=garagem, vagas_estacionamento=vagas_estacionamento)

    # Pergunta em quantas parcelas o contrato será feito
    parcelas_contrato = int(input("Em quantas vezes deseja parcelar o contrato (1 a 5): ").strip())

    # Cria o objeto Contrato ligando cliente e imóvel
    contrato = Contrato(imovel, cliente, parcelas_contrato=parcelas_contrato)
    # Exibe o nome do cliente para conferência
    print(f"Cliente: {cliente.nome}")

    # Calcula o valor do aluguel mensal
    aluguel_mensal = contrato.calcular_aluguel_mensal()
    # Calcula o valor de cada parcela do contrato
    parcela_contrato = contrato.calcular_parcela_contrato()

    # Exibe os resultados finais formatados
    print("ORÇAMENTO GERADO")
    print(f"Cliente: {cliente.nome}")
    print(f"Tipo de imóvel: {imovel.tipo.capitalize()}")
    print(f"Valor do aluguel mensal: R${aluguel_mensal:.2f}")
    print(f"Valor do contrato: R${contrato.valor_contrato:.2f}")
    print(f"Parcelado em {contrato.parcelas_contrato}x de R${parcela_contrato:.2f}")

    # Gera o arquivo CSV com os dados do orçamento
    contrato.gerar_csv_orcamento()
    # Mensagem final de confirmação
    print("Arquivo 'orcamento.csv' gerado na pasta 'output'.")

# Verifica se o arquivo está sendo executado diretamente
if __name__ == "__main__":
    main()     

          