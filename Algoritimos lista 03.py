#Ciência da Computação

questao = int(input('Numero da questao: '))

#questao 1
if questao == 1:
    num = int(input('Numero: '))
    x = num % 2
    if x == 0:
        print('Par')
    else:
        print('impar')

#qeustao 2
if questao == 2:
    idade = int(input('idade do cão: '))
    idade2 = idade - 2
    idd = idade2 * 4
    idd2 = 2 + idd
    
    if idade > 2:
        print('idade humana: ',idd2)

    elif idade <= 2 and idade > 0:
        id = idade * 10.5
        print('Idade: ', id)
    elif idade <= 0:
        print('Serião que você tetou dar uma idade negativa?????????????? kkkkkkkkkkk')
    
#questao 3
if questao == 3:
    ltr = input('LETRA: ')
    v = ['a','e','i','o','u','A','E','I','O','U']

    if ltr in v:
        print('Vogal')

    else:
        print('Constoante')

#questao 4
if questao == 4:
    num = int(input('número de lados: '))
    if num == 3:
        print('triângulo')
    elif num == 4:
        print('quadrado') 
    elif num == 5:
        print('pentágono')
    elif num == 6:
        print('hexágono')
    elif num == 7:
        print('septágono')
    elif num == 8:
        print('octágono')
    elif num == 9:
        print('noneágono')
    elif num == 10:
        print('decágono')
    else:
        print('E eu sei la po ;-;')

#questao 5
if questao == 5:
    mes = input('mês: ')
    
    m31 = ['janeiro','março','maio','julho','agosto','outubro','dezembro']
    m30 = ['abril','junho','setembro','novembro']
    if mes in m31:
        print('esse mês tem 31 dias')
    elif mes in m30:
        print('esse mês tem 30 dias')
    elif mes == 'fevereiro':
        print('esse mês pode ter 28 ou 29 dias')
    else:
        print('Somente meses sao aceitos')

#questao 6
if questao == 6:
    l1 = int(input('lado 1: '))
    l2 = int(input('lado 2: '))
    l3 = int(input('lado 3: '))
    if l1 == l2 == l3:
        print('equilátero')
    elif l1 == l2 or l1 == l3 or l2 == l3:
        print('isóceles')
    else:
        print('escaleno')
    
#questao 7
if questao == 7:
    barulho = int(input('nível decibéis: '))
    if barulho == 130:
        print('britadeira')
    elif barulho == 106:
        print('cortador de grama')
    elif barulho == 70:
        print('despertador')
    elif barulho == 40:
        print('sala silenciosa')
    elif barulho < 130 and barulho > 106:
        print('Entre britadeira e cortador de grama')
    elif barulho < 106 and barulho > 70:
        print('entre cortador de grama e despertador')
    elif barulho < 70 and barulho > 40:
        print('entre despertador e sala sileciosa')
    elif barulho < 40 and barulho > 130:
        print('So tem decibeis entre 130 e 40')

#questao 8 eu fiquei bravo com a questao ent decidi fazer para todos os valores, perdao Kkkkkjk
if questao == 8:
    nota = input('Nota musical: ')
    c = ['C0', 'c0', 'C1', 'c1', 'C2', 'c2', 'C3', 'c3', 'C4', 'c4', 'C5', 'c5', 'C6', 'c6', 'C7', 'c7', 'C8', 'c8'] #Funçoes de C
    d = ['D0', 'd0', 'D1', 'd1', 'D2', 'd2', 'D3', 'd3', 'D4', 'd4', 'D5', 'd5', 'D6', 'd6', 'D7', 'd7', 'D8', 'd8']
    e = ['E0', 'e0', 'E1', 'e1', 'E2', 'e2', 'E3', 'e3', 'E4', 'e4', 'E5', 'e5', 'E6', 'e6', 'E7', 'e7', 'E8', 'e8']
    f = ['F0', 'f0', 'F1', 'f1', 'F2', 'f2', 'F3', 'f3', 'F4', 'f4', 'F5', 'f5', 'F6', 'f6', 'F7', 'f7', 'F8', 'f8']
    g = ['G0', 'g0', 'G1', 'g1', 'G2', 'g2', 'G3', 'g3', 'G4', 'g4', 'G5', 'g5', 'G6', 'g6', 'G7', 'g7', 'G8', 'g8']
    a = ['A0', 'a0', 'A1', 'a1', 'A2', 'a2', 'A3', 'a3', 'A4', 'a4', 'A5', 'a5', 'A6', 'a6', 'A7', 'a7', 'A8', 'a8']
    b = ['B0', 'b0', 'B1', 'b1', 'B2', 'b2', 'B3', 'b3', 'B4', 'b4', 'B5', 'b5', 'B6', 'b6', 'B7', 'b7', 'B8', 'b8']
    
    if nota in c:
        notastring = str(nota)[1] #pega o Número de CX
        notav = int(notastring)
        freq = 261.63 / (2 ** (4 - notav))
        print(f'Frequencia de {nota}: {freq}')
        
        print('Frequência (Hz) de C4: 261.63 ')
    
    elif nota in d:
        notastring = str(nota)[1]
        notav = int(notastring)
        freq = 293.66 / (2 ** (4 - notav))
        print(f'Frequencia de {nota}: {freq}')
        print('Frequência (Hz) de D4: 293.66')
    
    elif nota in e:
         notastring = str(nota)[1]
         notav = int(notastring)
         freq = 329.63 / (2 ** (4 - notav))
         print(f'Frequencia de {nota}: {freq}')
         print('Frequência (Hz) de E4: 329.63')
    
    elif nota in f:
         notastring = str(nota)[1]
         notav = int(notastring)
         freq = 349.23 / (2 ** (4 - notav))
         print(f'Frequencia de {nota}: {freq}')
         print('Frequência (Hz) de F4: 349.23')
    
    elif nota in g:
         notastring = str(nota)[1]
         notav = int(notastring)
         freq = 392.00 / (2 ** (4 - notav))
         print(f'Frequencia de {nota}: {freq}')
         print('Frequência (Hz) de G4: 392.00')
    
    elif nota in a:
         notastring = str(nota)[1]
         notav = int(notastring)
         freq = 440.00 / (2 ** (4 - notav))
         print(f'Frequencia de {nota}: {freq}')
         print('Frequência (Hz) de A4: 440.00')
    
    elif nota in b:
         notastring = str(nota)[1]
         notav = int(notastring)
         freq = 493.88 / (2 ** (4 - notav))
         print(f'Frequencia de {nota}: {freq}')
         print('Frequência (Hz) de B4: 493.88')

#questao 9
if questao == 9:
    dia = input('Diga o dia e mes (DDMM): ')
    if dia == '0101':
        print('Confraternização universal')
    elif dia == '2104':
        print('Tiradentes')
    elif dia == '0105':
        print('Dia do trabalho')
    elif dia == '0709':
        print('Independência do Brasil')
    elif dia == '1210':
        print('Nossa Senhora Aparecida')
    elif dia == '0211':
        print('Finados')
    elif dia == '1511':
        print('Proclamação da República')
    elif dia == '2512':
        print('Natal')
    else:
        print('F no chat, não tem feriado')

#questao 10
if questao == 10:
    quadradinho = int(input('Diga o numero da posição da peça no tabuleiro de xadrez: '))
    quadradinho1 = input('Diga a letra: ')
    l = ['a', 'c', 'e', 'g']
    l2 = ['b', 'd', 'f', 'h']
    n = [1, 3, 5, 7]
    n2 = [2, 4, 6, 8]
    if quadradinho in n and quadradinho1 in l:
        print('quadrado preto')
    elif quadradinho in n2 and quadradinho1 in l2:
        print('quadrado branco')
    else:
        print('Erro 404: NotFound')

#questao 11
if questao == 11:
    a = int(input('Valor de a: '))
    b = int(input('Valor de b: '))
    c = int(input('Valor de c: '))
    delta = b ** 2 - (4 * a * c)
    if a == 0:
        print('Não existe valor de x para quando a for 0')
    
    elif delta < 0:
        print('Não possui raizes reais')
    
    else:
        x1 = (-b + delta ** (1 / 2)) / (2 * a)
        x2 = (-b - delta ** (1 / 2)) / (2 * a)
        print(f'Valor de x1 {x1}, Valor de x2 {x2}')

#questao 12
if questao == 12:
    ano = int(input('Qual ano: '))
    ano400 = ano % 400
    ano4 = ano % 4
    if ano400 == 0 or ano4 == 0:
        print('O ano é bissexto')
    else:
        print('O ano não é bissexto')

#questao else
if questao >= 13:
    print(f'Erro Questao{questao}DontExist')
