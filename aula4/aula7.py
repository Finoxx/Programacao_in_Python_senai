lista_  =  [1,2,3]

print(lista_)               
lista_[0] = 100
print(lista_)


# funções
# nomeDaFunção(lista)

# alteram 
# funções atribuir valores a lista 

lista_.append(10)
print(lista_)

lista_.insert(1,200)
print(lista_)

lista_.extend([10,20,30,10,20])
print(lista_)

lista_+=(10,20,50,55,5)
print(lista_)

# remover os dados

lista_.pop()
print(lista_)

lista_.pop(5)
print(lista_)

lista_.remove(200)
print(lista_)

del lista_[0]
print(lista_)


# verificam um dado:



# tamanho

print(len(lista_))

# menor numero

print(min(lista_))

# maior numero

print(max(lista_))

# quanto tem de um dado 

print(lista_.count(10))

# ordenar a lista 

lista_.sort()
print(lista_)

# reverter a sequencia da lista 

lista_.sort(reverse = True)
print(lista_)

# copiar a lista 


x  =  lista_.copy()
print(x)

# limpar a lista
lista_.clear()
print(lista_)

# métodos
# nome.nomeMétodo