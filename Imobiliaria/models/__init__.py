# Esse arquivo aqui serve pra transformar a pasta "models" em um pacote Python.
# Basicamente, ele faz o Python entender que dentro dessa pasta tem código que pode ser importado.
# Assim, eu posso chamar as classes direto do pacote, em vez de precisar colocar o caminho completo.

# Por exemplo, lá no main.py eu posso importar assim:
# from models import Imovel, Cliente, Contrato
# em vez de ficar escrevendo from models.imovel import Imovel, etc.

# Aqui embaixo eu já importo as principais classes do sistema.
# Isso facilita o uso e deixa o código mais limpo.

from .imovel import Imovel   # Classe que representa os tipos de imóveis (apartamento, casa, estúdio)
from .cliente import Cliente # Classe que representa o cliente (nome e se tem crianças)
from .contrato import Contrato # Classe que calcula o contrato, parcelas e gera o orçamento
