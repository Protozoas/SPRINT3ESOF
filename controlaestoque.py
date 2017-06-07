enterpriseName = 'Protozoas Softwares Developments'

Stock = {'tenis': {'vans': 0, 'allstar': 0, 'qix': 0},
           'camisetas': {'nike': 0, 'adidas': 0, 'nicoboco': 0},
           'calcas': {'levis': 0, 'gucci': 0, 'calvinklein': 0}}

def showStock(goods, leftWidth, rightWidth):
    print('ESTOQUE'.center(leftWidth + rightWidth, '-'))
    for i, j in goods.items():
        print(str(j) + ' ' + i)

def addToStock(item, brand, amount):
    Stock[item][brand] += amount

def subtractFromStock(item, brand, amount):
    if Stock[item][brand] >= amount:
        Stock[item][brand] -= amount
    else:
        print('\nSo tem '+str(Stock[item][brand])+' itens de '+item+'-'+brand+' no estoque')

def startMenu():
    print('\n\n\nBem-vindo ' + enterpriseName + '! O que você deseja fazer?\n\n')
    print(' Opcao 01: Consultar estoque.')
    print(' Opcao 02: Adicionar items ao estoque.')
    print(' Opcao 03: Remover items do estoque.')
    print(' Opcao 04: Consultar valor de estoque total.')
    print(' Opcao 05: Consultar valor de estoque de um item especifico.')
    print(' Opcao 06: Consultar lucro total.')
    print(' Opcao 07: Consultar lucro de um item especifico.')
    print(' Opcao 08: Buscar valores dos concorrentes mais acessados.')
    print(' Opcao 00: SAIR')

option = 1
while option != 0:

    startMenu()
    
    option = int(input('\n\nDigite a opcao desejada: '))

    if option == 0:
        break
    
    if option == 1:
        print('\n')
        showStock(Stock, 20, 6)
        
    elif option == 2:
        print('\n')
        print('Qual item deseja adicionar?')
        item = input()
        if item.lower() == 'tenis':
            print('Qual marca?')
            brand = input()
            print('Quantidade: ')
            quantity = int(input())
            addToStock(item.lower(), brand.lower(), quantity)
        elif item.lower() == 'camisetas':
            print('Qual marca?')
            brand = input()
            print('Quantidade: ')
            quantity = int(input())
            addToStock(item.lower(), brand.lower(), quantity)
        elif item.lower() == 'calcas':
            print('Qual marca?')
            brand = input()
            print('Quantidade: ')
            quantity = int(input())
            addToStock(item.lower(), brand.lower(), quantity)
            
    elif option == 3:
        print('\n')
        print('Qual item deseja remover?')
        item = input()
        if item.lower() == 'tenis':
            print('Qual marca?')
            brand = input()
            print('Quantidade: ')
            quantity = int(input())
            subtractFromStock(item.lower(), brand.lower(), quantity)
        elif item.lower() == 'camisetas':
            print('Qual marca?')
            brand = input()
            print('Quantidade: ')
            quantity = int(input())
            subtractFromStock(item.lower(), brand.lower(), quantity)
        elif item.lower() == 'calcas':
            print('Qual marca?')
            brand = input()
            print('Quantidade: ')
            quantity = int(input())
            subtractFromStock(item.lower(), brand.lower(), quantity)
        
    #elif option == 4:
    #    print('\n')
    #    
    #elif option == 5:
    #    print('\n')
    #    
    #elif option == 6:
    #    print('\n')
    #    
    #elif option == 7:
    #    print('\n')
    #    
    #elif option == 8:
    #    print('\n')
    #

    else:
        print('\n\nNao existe a opcao escolhida.')
