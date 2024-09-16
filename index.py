# Vetores

soja = []
milho = []

# funções

def calcular_area (largura, comprimento): #Formato de área escolhido: retangular
    area = (largura * comprimento) / 10000 #Área recebida em metros e transformada para hectar
    return area

def escolha_cultura():
    while True:
        try:
            escolha = int(input("Digite a cultura que deseja [1] Soja e [2] Milho: "))


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
                print("Você escolheu milho!")
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
            print("Digite um dado válido!")

def calculo_insumos (area):
    quantidade_bifrentina = area * 150 #Quantidade de ml por hectar (produto aplicado por via aérea, nao desconta ruas)
    quantidade_agua = area * 100 #Quantidade de litros de água necessária para diluir o insumo por hectar
    return quantidade_bifrentina, quantidade_agua

def atualizar_dados():
    while True:
        try:
            atualizar_cultura = int(input("Digite a cultura que deseja [1] Soja e [2] Milho [3] Retornar ao menu: "))

            if atualizar_cultura == 1: #soja
                #Entrada de dados
                largura = float(input("Digite a largura do terreno em metros: "))
                comprimento = float(input("Digite o comprimento do terreno em metros: "))
                #Cálculos
                area = calcular_area(largura, comprimento)
                quantidade_insumo = calculo_insumos(area)
                #Limpando os dados antigos
                soja.clear()
                #Atualizando
                soja.append([area, quantidade_insumo])
                print("Dados atualizados!")
                menu()
                break
            elif atualizar_cultura == 2: #milho
                #Entrada de dados
                largura = float(input("Digite a largura do terreno em metros: "))
                comprimento = float(input("Digite o comprimento do terreno em metros: "))
                #Calculos
                area = calcular_area(largura, comprimento)
                quantidade_insumo = calculo_insumos(area)
                #Limpando dados antigos
                milho.clear()
                #Atualizando
                milho.append([area, quantidade_insumo])
                print("Dados atualizados!")
                menu()
                break
            elif atualizar_cultura == 3: #Retornar ao menu
                menu()
                break
            else:
                print("Opção inválida!")
        except ValueError:
            print("Digite um dado válido!")

def deletar_dados():

    while True:
        try:
            dado_deletado = int(input("Digite a cultura que deseja deletar [1] Soja [2] Milho [3] Retornar ao menu: "))
            if dado_deletado == 1: #Deletar soja
                #Limpando dados
                soja.clear()
                print("Dados deletados!")
                menu()
                break
            elif dado_deletado == 2: #Deletar milho
                #Limpando
                milho.clear()
                print("Dados deletados!")
                menu()
                break
            elif dado_deletado == 3: #Retornar ao menu
                menu()
                break
            else:
                print("Opção inválida!")
        except ValueError:
            print("Digite um dado válido!")

def exibir_dados():
    if len(soja) > 0 and len(milho) > 0: #Caso tenha dados de ambas as culturas
        print(f"--- Dados da Plantação de SOJA: ---\nÁrea Plantada: {soja[0][0]} Hectar. "
              f"\nQuantidade de Insumo (Bifrentina): {soja[0][1][0]} ML/Hectar.\nQuantidade de Água Para Diluição do Insumo: {soja[0][1][1]} Litros.")

        print(f"--- Dados da Plantação de MILHO: ---\nÁrea Plantada: {milho[0][0]} Hectar. "
              f"\nQuantidade de Insumo (Bifrentina): {milho[0][1][0]} ML/Hectar.\nQuantidade de Água Para Diluição do Insumo: {milho[0][1][1]} Litros.")
        menu()
    elif len(soja) > 0 and len(milho) == 0: #Caso tenha dados apenas de soja
        print(f"--- Dados da Plantação de SOJA: ---\nÁrea Plantada: {soja[0][0]} Hectar. "
              f"\nQuantidade de Insumo (Bifrentina): {soja[0][1][0]} ML/Hectar.\nQuantidade de Água Para Diluição do Insumo: {soja[0][1][1]} Litros.")
        menu()
    elif len(soja) == 0 and len(milho) > 0: #Caso tenha dados apenas de milho
        print(f"--- Dados da Plantação de MILHO: ---\nÁrea Plantada: {milho[0][0]} Hectar. "
              f"\nQuantidade de Insumo (Bifrentina): {milho[0][1][0]} ML/Hectar.\nQuantidade de Água Para Diluição do Insumo: {milho[0][1][1]} Litros.")
        menu()
    else: #Caso nao tenha dados de nenhuma cultura
        print("Nenhum dado disponível.")
        menu()

def menu():

    while True:
        try:
            print("---MENU---")
            print("1 - Atualizar/Inserir Novos Dados")
            print("2 - Deletar Dados")
            print("3 - Exibir Dados")
            print("4 - Sair do Programa")

            escolha = int(input("Escolha uma opção: "))

            if escolha == 1: #Atualizar/inserir dados
                print("Atualizar/Inserir Dados")
                atualizar_dados()
                break

            elif escolha == 2: #Deletar dados
                print("Deletar Dados")
                deletar_dados()
                break

            elif escolha == 3: #Exibir Dados
                print("Exibir Dados")
                exibir_dados()
                break

            elif escolha == 4: #Sair do programa
                print("Voce Saiu do Programa!")
                break
            else:
                print("Escolha Inválida!")
        except ValueError:
            print("Digite um dado válido!")


escolha_cultura()
menu()