# Vetores


dados_cultura = []

soja = []
exibir_soja = []
milho = []
exibir_milho = []

# funções

def calcular_area (largura, comprimento): #retangulo
    area = (largura * comprimento) / 10000 # área recebida em metros e transformada para hectar
    return area

def escolha_cultura():
    while True:
        try:
            escolha = int(input("Digite a cultura que deseja [1] soja e [2] milho: "))


            if escolha == 1:

                print("Você escolheu soja!")
                # Entrada de dados
                largura = float(input("Digite a largura do terreno em metros: "))
                comprimento = float(input("Digite o comprimento do terreno em metros: "))
                # Calculos
                area = calcular_area(largura, comprimento)
                quantidade_insumo = calculo_insumos(area)
                # Armazenando dados
                soja.append([area, quantidade_insumo])
                print("Dados armazenados!")
                break

            elif escolha == 2:
                print("vc escolheu milho")
                # Entrada de dados
                largura = float(input("Digite a largura do terreno em metros: "))
                comprimento = float(input("Digite o comprimento do terreno em metros: "))
                # Calculos
                area = calcular_area(largura, comprimento)
                quantidade_insumo = calculo_insumos(area)
                # Armazenando dados
                milho.append([area, quantidade_insumo])
                print("Dados armazenados!")
                break

            else:
                print("Escolha inválida")

        except ValueError:
            print("Digite um número válido")


def calculo_insumos (area):
    quantidade_insumos = area * 150 #Produto: Talstar (via aérea, nao desconta ruas)
    return quantidade_insumos

def atualizar_dados():
    while True:
        atualizar_cultura = int(input("Digite a cultura que deseja [1] soja e [2] milho [3] Retornar ao menu: "))

        if atualizar_cultura == 1:
            largura = float(input("Digite a largura do terreno em metros: "))
            comprimento = float(input("Digite o comprimento do terreno em metros: "))
            area = calcular_area(largura, comprimento)
            quantidade_insumo = calculo_insumos(area)
            #limpando os dados antigos
            soja.clear()
            #Atualizando
            soja.append([area, quantidade_insumo])
            print("Dados atualizados!")
            print(soja)
            menu()
            break
        elif atualizar_cultura == 2:
            #entrada de dados
            largura = float(input("Digite a largura do terreno em metros: "))
            comprimento = float(input("Digite o comprimento do terreno em metros: "))
            #calculos
            area = calcular_area(largura, comprimento)
            quantidade_insumo = calculo_insumos(area)
            #limpando dados antigos
            milho.clear()
            #Atualizanof
            milho.append([area, quantidade_insumo])
            print("Dados atualizados!")
            menu()
            break
        elif atualizar_cultura == 3:
            menu()
            break

def deletar_dados():
    while True:
        dado_deletado = int(input("Qual dado deseja deletar? [1] soja [2] milho: "))
        if dado_deletado == 1:
            soja.clear()
            print("Dados deletados!")
            menu()
            break
        elif dado_deletado == 2:
            milho.clear()
            print("Dados deletado!")
            menu()
            break
        else:
            print("Opção inválida!")


def exibir_dados():
    if len(soja) > 0 and len(milho) > 0:
        print(f"Dados da plantação de soja: \nÁrea plantada: {soja[0][0]} hectar. \nQuantidade de insumo: {soja[0][1]} ml/hectar.")
        print(f"Dados da plantação de milho: \nÁrea plantada: {milho[0][0]} hectar. \nQuantidade de insumo: {milho[0][1]} ml/hectar.")
        menu()
    elif len(soja) > 0 and len(milho) == 0:
        print(f"Dados da plantação de soja: \nÁrea plantada: {soja[0][0]} hectar. \nQuantidade de insumo: {soja[0][1]} ml/hectar.")
        menu()
    elif len(soja) == 0 and len(milho) > 0:
        print(f"Dados da plantação de milho: \nÁrea plantada: {milho[0][0]} hectar. \nQuantidade de insumo: {milho[0][1]} ml/hectar.")
        menu()
    else:
        print("Nenhum dado disponível.")
        menu()


def menu():
    while True:

        print("---MENU---")
        print("1 - Atualizar/Inserir novos dados")
        print("2 - Deletar dados")
        print("3 - Exibir dados")
        print("4 - Sair do Programa")

        escolha = int(input("Escolha uma opção: "))

        if escolha == 1:
            print("Atualizar dados")
            atualizar_dados()
            break

        elif escolha == 2:
            print("Deletar dados")
            deletar_dados()
            break

        elif escolha == 3:
            print("Exibir dados")
            exibir_dados()
            break

        elif escolha == 4:
            print("Voce saiu do programa!")
            break
        else:
            print("Escolha inválida!")



escolha_cultura()
menu()