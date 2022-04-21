#Nome: Lucas de Azevedo
#Curso: Ciência da Computação

import datetime

questao = int(input('Qual o número da questão?\n---> '))

if questao == 1:
    dias = int(input('Numero de Dias: '))
    hora = int(input('Horas: '))
    minutes = int(input('Minutos: '))
    seconds = int(input('Segundos: '))

    dias1 = dias * 24 * 60 * 60
    horas1 = hora * 60 * 60 
    minutes1 = minutes * 60
    Totaltime = dias1 + horas1 + minutes1 + seconds

    print('Tempo total em segundos: ', Totaltime)

if questao == 2:

    segundos = int(input('numero de segundos: '))

    diasSobra = segundos % 86400
    horassobra = segundos % (60 * 60)
    segundossobra = horassobra % 60
    minutos = horassobra / 60
    horas = diasSobra // 3600
    dias = segundos / (24 * 60 * 60)
    dias1 = int(dias)
    horas1 = int(horassobra)
    minutos1 = int(minutos)
    
    print("O tempo deu: ",("%02d" % dias1),":",( "%02d" % (horas)),":", ("%02d" % minutos1),":", ("%2d" % segundossobra))

if questao == 3:
    print('O dia e horário no seu computador é: ', datetime.datetime.now())

if questao == 4:
    x = int(input('Primeiro numero: '))
    y = int(input('Segundo numero: '))
    z = int(input('Terceiro numero: '))

    maior = max(x, y, z)
    menor = min(x, y ,z)
    meio = x + y + z - maior - menor 
    print(menor, meio, maior)

if questao == 5:

    x = int(input('Troco a dar ao cliente: '))

    naosei = x  / 50
    y = x % 50
    naosei1 = y / 25
    z = y % 25
    naosei2 =  z / 10
    s = z % 10

    variavel = int(naosei)
    variavel1 = int(naosei1)
    variavel2 = int(naosei2)


    print('Quantidade de moedas que tem que dar')
    print('50:', variavel, '25:', variavel1, '10:', variavel2, '1:', s)

if questao == 6:
    num = int(input('Digite um numero de 4 digitos: '))
    
    x1 = str(num)[0]
    x2 = str(num)[1]
    x3 = str(num)[2]
    x4 = str(num)[3]

    y1 = int(x1)
    y2 = int(x2)
    y3 = int(x3)
    y4 = int(x4)

    y = y1 + y2 + y3 + y4 
    
    print('A soma dos 4 digitos deu: ', y)

if questao == 7:
    x = int(input('Diga um numero de 3 digitos: '))

    x1 = str(x)[0]
    x2 = str(x)[1]
    x3 = str(x)[2]
    
    print('Centenas:', x1, '\nDezenas:', x2, '\nUnidades:', x3)

if questao == 8:
    x = int(input('Diga um numero de 3 digitos: '))

    x1 = str(x)[0]
    x2 = str(x)[1]
    x3 = str(x)[2]

    y = x3 + x2 + x1
    print('O ordem do numero na forma invertida é', y)

if questao == 9:
    x = int(input('Dia mes e ano: '))


    dia = int(x / 10000)
    mes = int(x / 100)
    ano = int(x)

    alemao = (mes  - dia * 100)

    socrates = (ano - (dia * 10000) - (alemao * 100))



    print("ano", ("%02d"%socrates),"mes", ("%02d" %alemao),"dia", ("%02d"%dia))

if questao == 10:
    x = int(input('Informe o numero de sua matrícula: '))

    x1 = str(x)[0]
    x2 = str(x)[1]
    x3 = str(x)[2]
    x4 = int(x3)
    if x4 == 1:
        z = 1
    if x4 == 2:
        z = 2
    if x4 > 2:
        z = 'Error_SemesteNotFound'
        print('Erro')

    ano = x1 + x2
   
    print('Ano de matrícula', ano, ' e semestre', z)

if questao >= 11:
    print('Erro ao achar questão')