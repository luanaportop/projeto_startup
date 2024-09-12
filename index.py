# Vetores


dados_cultura = []

soja = []
exibir_soja = []
milho = []
exibir_milho = []

# funções

def calcularArea (largura, comprimento): #retangulo
    area = (largura * comprimento) / 10000 # área recebida em metros e transformada para hectar
    return area

def escolhaCultura():
    while True:
        try:
            escolha_cultura = int(input("Digite a cultura que deseja [1] soja e [2] milho [3] Sair: "))


            if escolha_cultura == 1:

                print("Você escolheu soja!")

                largura = float(input("Digite a largura do terreno em metros: "))
                comprimento = float(input("Digite o comprimento do terreno em metros: "))

                area = calcularArea(largura, comprimento)

                quantidade_insumo = calculoInsumos(area)

                soja.append([area, quantidade_insumo])

                print(soja)

                print("Dados armazenados!")
                break

            elif escolha_cultura == 2:
                print("vc escolheu milho")

                largura = float(input("Digite a largura do terreno em metros: "))
                comprimento = float(input("Digite o comprimento do terreno em metros: "))

                area = calcularArea(largura, comprimento)

                quantidade_insumo = calculoInsumos(area)

                milho.append([area, quantidade_insumo])


                print("Dados armazenados!")
                break

            else:
                print("Escolha inválida")

        except ValueError:
            print("Digite um número válido")


def calculoInsumos (area):
    quantidade_insumos = area * 150 #Produto: Talstar (via aérea)
    return quantidade_insumos

#def atualizarDados():
    #indice = int(input("Digite o índice a ser atualizado [1] atualizar largura [2] atualizar comprimento: "))

    #if  0<=indice < len()

#def deletarDados():


def menu():
    while True:

        print("---MENU---")
        print("1 - Atualizar dados")
        print("2 - Deletar dados")
        print("3 - Exibir dados")
        print("4 - Sair do Programa")

        escolha = int(input("Escolha uma opção: "))

        if escolha == 1:
            print("Atualizar dados")
            #atualizarDados()
            break

        elif escolha == 2:
            print("Deletar dados")
            #deletarDados()
            break

        elif escolha == 3:
            print("Exibir dados")
            #exibirDados()
            break

        elif escolha == 4:
            print("Voce saiu!")
            break
        else:
            print("Escolha inválida!")



escolhaCultura()
menu()