estoque = {
    'frutas':{
        'uvas':
              {'quantidade':30,
               'preço':10.55,
               },
        'bananas':{
                'quantidade':20,
                'preço':15.25

        },
     
        },
    'eletronicos':{
        'fone':{
                'quantidade':10,
                'preço':500.55
        },
        'iphone':{
                'quantidade':5,
                'preço':17000
        }

    }
    
    }


carrinho =  []
total =  []

senha =  '74651456.9'
login = '37485'

dig_senha =  input('Digite sua senha: ')
dig_login =  input('Digite seu login: ')

if dig_login == login and dig_senha == senha:
    print('Seja bem vindo(a))')
    pedir  =  input('Deseja fazer o pedido: sim ou não?')
    if pedir == 'sim':
        print('estoque: ', 'estoque, escolha se produto: ')
        secao = input('Digite a seção -  frutas ou eletronicos')
        produto =  input(f'escolha o produto{estoque[secao]} ')
        print('Produto:', estoque[secao][produto])
        carrinho.append(produto)
        total.append(estoque[secao][produto]['preço'])
        
        estoque[secao][produto]['quantidade'] - 1
        print(estoque)

        print('CArrinho', carrinho)
        print('R$', total)
        print('------------------------')
        formapag = ['1 PIX', '2 - CC', '3 - CD']
        pag =  int(input('Digite a forma de pagamento: '))
        print('FORMA DE PAGAMENTO', formapag[pag])

    else:
        print('Obrigada volte sempre')    
else:
    print('Algo foi digitado errado... tente novamente')    







