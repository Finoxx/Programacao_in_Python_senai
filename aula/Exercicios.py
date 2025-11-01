import random

# print('Exercicio1')

# n = int(input('Digite um número: '))

# if n > 0:
#     print("Esse número é positivo")

# elif n == 0:
#     print('Esse número é igual a 0')

# elif n < 0:
#     print('Esse número é negativo')

# print('Exercicio2')

# i = int(input('Digite sua idade: '))
# t = str(input('Possui titulo de eleitor?'))

# if i >= 16 and t == 'Sim':
#     print('Você pode votar')
    
# else: 
#     print('Você não pode votar')


# print ('Exercicio3')

# n = random.randrange(0,7894467851213487)

# d = n%2  

# if d == 0:
#     print(n)
#     print('Esse número é par')
# else:
#     print(n)
#     print('Esse número é impar')

# print ('Exercicio4')

# n = int(input('Digite o primeiro número para gerar um triangulo: '))
# n1 = int(input('Digite o segundo número para gerar um triangulo: '))
# n2 = int(input('Digite o terceiro número para gerar um triangulo: '))

# if  n == n1 == n2 :
#     print('Esse triangulo é equilatero')

# elif n==n1 or n==n2 or n1==n2:
#     print('Esse triangulo é isosceles')

# elif n !=n1 or n!=n2 or n1!=n2:
#     print('Esse triangulo é escaleno')

# print('Exercicio5')

# n = int(input('Digite um número'))

# d = n% 5
# e = n% 7

# if e and d == 0:
#     print('seu número é divisel por 5 e 7')
# elif d == 0:
#     print('Seu numero é multiplo por 5')
# elif e == 0:
#     print("Seu número é multiplo de 7")
# else:
#     print('Seu número não é multiplo numero 5 ou 7')

# print ('Exercico6')

# n = int(input('Digite um número'))

# if n > 0:
#     if n > 10:
#         print('Seu número é positivo e maior que 10')
# else:
#     print ('Seu número é negativo e menor que 10')

print('Exercicio7')

n = int(input('Digite um número'))

d = n% 3
e = n% 5

if d == 0 and e  == 0:
    print('seu número é divisel por 3 e 5')
elif d == 0:
    print('Seu numero é divisivel por 3')
elif e == 0:
    print("Seu número é divisivel de 5")
else:
    print('Seu número não é divisivel numero 3 ou 5')