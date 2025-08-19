'''
Exercícios sobre os comandos básicos em Python
'''

def cabecalho(titulo):
    print('========================================')
    print(f'============= {titulo} ===============')
    print('========================================')

#1. Faça um programa que imprima o seu nome.
def q1():
    cabecalho('QUESTÃO 1')
    print('João Paulo')

#2. Faça um programa que imprima o produto dos valores 30 e 27.
def q2():
    cabecalho('QUESTÃO 2')
    print(30*27)

#3. Faça um programa que imprima a média aritmética entre os números 5, 8, 12.
def q3():
    cabecalho('QUESTÃO 3')
    print(f'(5+8+12)/3 = {(5+8+12)/3}')

#4. Faça um programa que leia e imprima um número inteiro.
def q4():
    cabecalho('QUESTÃO 4')
    numero = int(input('Digite um número inteiro: '))
    print(f'O valor digitado foi: {numero}')

#5. Faça um programa que leia dois números reais e os imprima.
def q5():
    cabecalho('QUESTÃO 5')
    num1 = float(input('Digite o primeiro número real: '))
    num2 = float(input('Digite o segundo número real: '))
    print(num1, num2)

#6. Faça um programa que leia um número inteiro e imprima o seu
#   antecessor e o seu sucessor.
def q6():
    cabecalho('QUESTÃO 6')
    num = int(input('Digite um número inteiro: '))
    print(f'Antecessor: {num-1}')
    print(f'Sucessor: {num+1}')

#7. Faça um programa que leia o nome o endereço e o telefone de
#   um cliente e ao final, imprima esses dados.
def q7():
    cabecalho('QUESTÃO 7')
    nome = input('Nome: ')
    endereco = input('Endereço: ')
    telefone = input('Telefone: ')
    resultado = f'''
    Nome: {nome}
    Endereço: {endereco}
    Telefone: {telefone}
    '''
    print(resultado)

#8. Faça um programa que leia dois números inteiros e imprima a
#   subtração deles.
def q8():
    cabecalho('QUESTÃO 8')
    num1 = int(input('Número inteiro: '))
    num2 = int(input('Outro número inteiro: '))
    print(num1-num2)

#9. Faça um programa que leia um número real e imprima ¼ deste número.
def q9():
    cabecalho('QUESTÃO 9')
    num = float(input('Número real: '))
    print(num/4)

#10. Faça um programa que leia três números reais e calcule a
#    média aritmética destes números. Ao final, o programa deve
#    imprimir o resultado do cálculo.
def q10():
    cabecalho('QUESTÃO 10')
    a = float(input('Primeiro Número: '))
    b = float(input('Segundo Número: '))
    c = float(input('Terceiro Número: '))
    media = (a+b+c)/3
    print(f'Média: {media}')

#11. Faça um programa que leia dois números reais e calcule as
#    quatro operações básicas entre estes dois números, adição,
#    subtração,multiplicação e divisão. Ao final, o programa
#    deve imprimir os resultados dos cálculos.
def q11():
    cabecalho('QUESTÃO 11')
    x = float(input('Primeiro número: '))
    y = float(input('Segundo número:'))
    resultado = f'''
    {x} + {y} = {x+y}
    {x} - {y} = {x-y}
    {x} * {y} = {x*y}
    {x} / {y} = {x/y}
    '''
    print(resultado)

#12. Faça um programa que leia um número real e calcule o
#    quadrado deste número. Ao final, o programa deve
#    imprimir o resultado do cálculo.
def q12():
    cabecalho('QUESTÃO 12')
    num = float(input('Número: '))
    print(num*num)

#13. Faça um programa que leia o saldo de uma conta poupança e
#    imprima o novo saldo, considerando um reajuste de 2%.
def q13():
    cabecalho('QUESTÃO 13')
    saldo = float(input('Saldo: R$ '))
    print(saldo*1.02)

#14. Faça um programa que leia a base e a altura de um retângulo
#    e imprima o perímetro (base*2 + altura*2) e a área (base * altura).    
def q14():
    cabecalho('QUESTÃO 14')
    base = int(input('Base do retângulo: '))
    altura = int(input('Altura do retângulo: '))
    print(f'Perímetro: {base*2+altura*2}')
    print(f'Área: {base*altura}')

#15. Faça um programa que leia o valor de um produto, o percentual
#    do desconto desejado e imprima o valor do desconto e o valor
#    do produto subtraindo o desconto.
def q15():
    cabecalho('QUESTÃO 15')
    valor = float(input('Valor do produto: R$ '))
    perc_desconto = int(input('Percentual do desconto: '))
    desconto = valor * perc_desconto/100
    valor_final = valor - desconto
    print(f'Desconto: R$ {desconto}')
    print(f'Valor final: R$ {valor_final}')

#16. Faça um programa que calcule o reajuste do salário de um
#    funcionário. Para isso, o programa deverá ler o salário atual
#    do funcionário e ler o percentual de reajuste. Ao final imprimir
#    o valor do novo salário.
def q16():
    cabecalho('QUESTÃO 16')
    salario = float(input('Salário: '))
    perc_reajuste = float(input('Percentual de reajuste: '))
    print(f'Novo Salário: R$ {salario*perc_reajuste/100+salario}')

#17. Faça um programa que calcule a conversão entre graus centígrados
#    e Fahrenheit. Para isso, leia o valor em centígrados e calcule
#    com base na fórmula a seguir. Após calcular o programa deve
#    imprimir o resultado da conversão.
#    F = (9 x C + 160) / 5
def q17():
    cabecalho('QUESTÃO 17')
    c = float(input('Graus Centígrados: '))
    print(f'Fahrenheit: {(9*c+160)/5}')

#18. Faça um programa que calcule a quantidade de litros de combustível
#    consumidos em uma viagem, sabendo-se que o carro tem autonomia de
#    12 km por litro de combustível. O programa deverá ler o tempo
#    decorrido na viagem e a velocidade média e aplicar as fórmulas:
#    D = T x V       L = D / 12
#    Em que:
#    • D = Distância percorrida
#    • T = Tempo
#    • V = Velocidade média
#    • L = Litros de combustível consumidos
#    Ao final, o programa deverá imprimir a distância percorrida e a
#    quantidade de litros consumidos na viagem.
def litros_consumidos(distancia, media_consumo):
    return distancia/media_consumo

def distancia_percorrida(tempo, velocidade):
    return tempo*velocidade

def q18():
    cabecalho('QUESTÃO 18')
    tempo = float(input('Tempo decorrido na viagem(horas): '))
    velocidade = int(input('Velocidade média (km/h): '))
    print(f'Distância percorrida: {distancia_percorrida(tempo,velocidade)}')
    print(f'Litros consumidos: {litros_consumidos(distancia_percorrida(tempo,velocidade),12)}')


#19. Faça um programa que calcule o valor de uma prestação em atraso.
#    Para isso, o programa deve ler o valor da prestação vencida, a
#    taxa periódica de juros e o período de atraso. Ao final, o
#    programa deve imprimir o valor da prestação atrasada, o período
#    de atraso, os juros que serão cobrados pelo período de atraso, o
#    valor da prestação acrescido dos juros. Considere juros simples.
def q19():
    cabecalho('QUESTÃO 19')

#20. Faça um programa que efetue a apresentação do valor da conversão
#    em real (R$) de um valor lido em dólar (US$). Para isso, será
#    necessário também ler o valor da cotação do dólar.
def q20():
    cabecalho('QUESTÃO 20')

menu = '''
[1] - Imprimir nome
[2] - Imprimir produto
[3] - Imprimir média
[4] - Imprimir inteiro
[5] - Ler e imprimir números reais
[6] - Antecessor e Sucessor
[7] - Dados de cliente
[8] - Subtração
[9] - 1/4
[10] - Média Aritmética
[11] - Operações aritméticas básicas
[12] - Quadrado de um número
[13] - Saldo de poupança
[14] - Área e perímetro de um retângulo
[15] - Desconto em produto
[16] - Reajuste Salarial
[17] - Conversão de temperatura
[18] - Consumo de veículo
[19] - Juros de prestação atrasada
[20] - Conversão dólar-real

Digite a opção a ser executada: 
'''

opcao = input(menu)
eval(f'q{opcao}()')
