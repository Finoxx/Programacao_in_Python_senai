import os
import shutil



with open('q','w') as arq:
    os.mkdir('u')



os.rename('t','t2')



with os.scandir('t2') as entr:
     for dados in entr:
          print(dados.name)
        
with os.scandir('t2') as entr:
     for dados in entr:
          if dados.is_dir():
             print(dados.name)
        


with os.scandir('C:/Users/Aluno/Downloads/Nova pasta/t2') as entr:
     for dados in entr:
          if 'arq.txt':
             with open('arq.txt','r') as conte:
                  conte.read()


with os.scandir('teste') as entrada :
       for n in entrada:
              print(n) 
              if 'teste.txt':
                  with open('C:/Users/Aluno/Downloads/Nova pasta/teste/teste.txt', 'r')  as t:
                    content = t.read()



print(content)
print(dados.name)



l =  []


with open('teste.txt','r') as arqui:
    conteudo   =  arqui.read()
    for n in conteudo:
        l.append(n)
        print(n)
    print(l)



shutil.rmtree('x')


shutil.copytree('C:/Users/Aluno/Downloads/Nova pasta/teste', 'teste2.py')

