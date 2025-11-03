'''
PROVA PRÁTICA DE PYTHON
Ao término enviar e-mail conforme modelo:
Para: preti.joao@ifmt.edu.br
Assunto: Prova 1 de Laboratório de Programação 2025/2
Mensagem: Coloque seu nome completo na mensagem do e-mail
Anexo: prova.py
'''

#1. Faça um programa que leia o saldo de uma conta corrente,
#   o juros de rendimento mensal e imprima o valor em reais do
#   rendimento referente a 1 mês de juros. (2,5pt)
def q1():
    saldo = float(input('Saldo: R$ '))
    juros = float(input('Juros mês (%): '))
    print(f'Rendimento: R$ {saldo*juros/100}')

#2. Complemente a questão 1 da prova, para que o cálculo do
#   rendimento só ocorra se o saldo da conta for positivo.
#   Caso contrário, deverá exibir uma mensagem informando que o
#   rendimento não pode ser calculado para valores negativos ou sem
#   saldo em conta corrente. (2,5pt)
def q2():
    saldo = float(input('Saldo: R$ '))
    if saldo <= 0:
        print('Não é possível calcular rendimento para saldo <= 0')
    else:
        juros = float(input('Juros mês (%): '))
        print(f'Rendimento: R$ {saldo*juros/100}')

#3. Complemente a questão 1 ou 2 da prova, para que não seja aceito juros
#   negativo. O programa deve reiteradamente informar o usuário do erro
#   e solicitar novo valor para o juros. (2,5pt)
def q3():
    saldo = float(input('Saldo: R$ '))
    while True:
        print('Informe um juros positivo')
        juros = float(input('Juros mês (%): '))
        if juros > 0:
            break
    print(f'Rendimento: R$ {saldo*juros/100}')

#4. Complemente a questão 1, 2 ou 3 da prova, para que o cálculo
#    do rendimento suporte um prazo maior do que 1 mês. (2,5pt)
#    O programa deverá solicitar do usuário também prazo do
#    investimento em meses.
#    Atenção: trata-se de uma operação de juros composto.
def q4():
    saldo = float(input('Saldo: R$ '))
    juros = float(input('Juros mês (%): '))
    prazo = int(input('Prazo em meses da aplicação: '))
    for _ in range(prazo):
        saldo += saldo*juros/100
    print(f'Rendimento: R$ {saldo}')

