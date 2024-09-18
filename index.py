import rpy2.robjects as ro
from rpy2.robjects.vectors import FloatVector

# Vetores para armazenar dados
soja = []
milho = []
desvio_soja = []
desvio_milho = []

# Funções para cálculo de média e desvio
def calcular_media_desvios(dados):
    if len(dados) >= 2:
        dados_vector = FloatVector(dados)
        media = ro.r('mean')(dados_vector)[0]
        desvio = ro.r('sd')(dados_vector)[0]
        return media, desvio
    else:
        return None, None

# Função para adicionar dados
def adicionar_dados(cultura, area, quantidade_insumo, qtd_producao):
    cultura.append([area, quantidade_insumo, qtd_producao])

# Função para calcular a área
def calcular_area(largura, comprimento):
    return (largura * comprimento) / 10000  # Área em hectares

# Função para calcular os insumos
def calculo_insumos(area):
    quantidade_bifrentina = area * 150  # ml por hectare
    quantidade_agua = area * 100  # litros por hectare
    return quantidade_bifrentina, quantidade_agua

# Funções para calcular a quantidade de produção
def quantidade_soja(area):
    return area * 3.24  # Toneladas por hectare

def quantidade_milho(area):
    return area * 5.28  # Toneladas por hectare

# Função para mostrar estatísticas
def mostrar_estatisticas(cultura):
    bifrentina = [item[1][0] for item in cultura]
    agua = [item[1][1] for item in cultura]

    media_bifrentina, desvio_bifrentina = calcular_media_desvios(bifrentina)
    media_agua, desvio_agua = calcular_media_desvios(agua)

    if media_bifrentina is not None:
        print(f"Média Bifrentina: {media_bifrentina}, Desvio Bifrentina: {desvio_bifrentina}")
        print(f"Média Água: {media_agua}, Desvio Água: {desvio_agua}")
    else:
        print("Mais dados são necessários para calcular estatísticas.")

# Função para exibir os dados
def exibir_dados():
    if len(soja) > 0:
        print("--- Dados da Plantação de SOJA: ---")
        for i, item in enumerate(soja):
            print(f"[{i}] Área Plantada: {item[0]} ha, Produção: {item[2]} toneladas, Insumo: {item[1][0]} ml, Água: {item[1][1]} L")

    if len(milho) > 0:
        print("--- Dados da Plantação de MILHO: ---")
        for i, item in enumerate(milho):
            print(f"[{i}] Área Plantada: {item[0]} ha, Produção: {item[2]} toneladas, Insumo: {item[1][0]} ml, Água: {item[1][1]} L")

# Função para garantir a escolha de cultura válida
def escolher_cultura():
    while True:
        try:
            cultura_escolhida = int(input("Digite a cultura que deseja [1] Soja e [2] Milho: "))
            if cultura_escolhida in [1, 2]:
                return cultura_escolhida
            else:
                print("Escolha inválida. Por favor, digite 1 para Soja ou 2 para Milho.")
        except ValueError:
            print("Entrada inválida. Por favor, digite 1 para Soja ou 2 para Milho.")

# Função para deletar dados
def deletar_dados(cultura):
    exibir_dados()
    try:
        indice = int(input("Digite o índice do dado que deseja deletar: "))
        if 0 <= indice < len(cultura):
            del cultura[indice]
            print("Dado deletado com sucesso!")
        else:
            print("Índice inválido.")
    except ValueError:
        print("Entrada inválida. Digite um número.")

# Função para atualizar dados
def atualizar_dados(cultura):
    exibir_dados()
    try:
        indice = int(input("Digite o índice do dado que deseja atualizar: "))
        if 0 <= indice < len(cultura):
            largura = float(input("Digite a nova largura do terreno em metros: "))
            comprimento = float(input("Digite o novo comprimento do terreno em metros: "))
            area = calcular_area(largura, comprimento)
            quantidade_insumo = calculo_insumos(area)
            if cultura == soja:
                qtd_producao = quantidade_soja(area)
            else:
                qtd_producao = quantidade_milho(area)

            cultura[indice] = [area, quantidade_insumo, qtd_producao]
            print("Dados atualizados com sucesso!")
        else:
            print("Índice inválido.")
    except ValueError:
        print("Entrada inválida. Digite um número.")

# Menu principal
def menu():
    while True:
        try:
            escolha = int(input("Escolha uma opção: [1] Adicionar dados, [2] Mostrar Estatísticas, [3] Exibir Dados, [4] Deletar Dados, [5] Atualizar Dados, [6] Sair: "))
            if escolha == 1:
                cultura_escolhida = escolher_cultura()
                largura = float(input("Digite a largura do terreno em metros: "))
                comprimento = float(input("Digite o comprimento do terreno em metros: "))
                area = calcular_area(largura, comprimento)
                quantidade_insumo = calculo_insumos(area)
                qtd_producao = quantidade_soja(area) if cultura_escolhida == 1 else quantidade_milho(area)

                if cultura_escolhida == 1:
                    adicionar_dados(soja, area, quantidade_insumo, qtd_producao)
                else:
                    adicionar_dados(milho, area, quantidade_insumo, qtd_producao)

            elif escolha == 2:
                cultura_escolhida = escolher_cultura()
                if cultura_escolhida == 1:
                    mostrar_estatisticas(soja)
                else:
                    mostrar_estatisticas(milho)

            elif escolha == 3:
                exibir_dados()

            elif escolha == 4:
                cultura_escolhida = escolher_cultura()
                if cultura_escolhida == 1:
                    deletar_dados(soja)
                else:
                    deletar_dados(milho)

            elif escolha == 5:
                cultura_escolhida = escolher_cultura()
                if cultura_escolhida == 1:
                    atualizar_dados(soja)
                else:
                    atualizar_dados(milho)

            elif escolha == 6:
                print("Você saiu do programa!")
                break

            else:
                print("Opção inválida!")
        except ValueError:
            print("Digite um dado válido!")
# Início do programa
menu()