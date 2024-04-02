variavel = int(6)#definindo uma variavel 
num1 = 0 #contador 1
num2 = 1 #contador 2
lista = [] #criando uma lista vazia

while num1 <= variavel:#enquando o num for menor ou igual que a variavel
    lista.append(num1)#add o num da sequencia de fibonascci na lista
    num1, num2 = num2, num1 + num2  #num1 vai virar o num2 e num2 vai virar num1+num2   

if variavel == lista[-1]:#se a var for igual ao ultimo elemento da lista pertence 
    print('Pertence')

else:#se não
    print('Não pertence')