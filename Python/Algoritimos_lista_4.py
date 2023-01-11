

from cmath import sqrt
from random import randint
from math import pi
from math import sqrt
from timeit import repeat
print('''       ⣠⣶⣿⣿⢳⣿⡇⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢸⣶⣭⣻⢿⢯⣞⡝⣿⣿⣫⢃⣛⣵⣾⣿        ⢀⣾    
      ⣰⣿⣿⣿⣏⣿⣿⡇⣿⣿⣿⣿⣿⣿⣿⡿⣟⣯⣷⣾⢸⣿⣿⣿⣷⣿⡏⠁⣿⣿⡀⢸⣿⣿⣿⣿        ⣼⣿    
     ⣼⣿⣿⣿⡟⣼⣿⣿⡇⣿⣿⣿⣿⡿⣟⣽⣾⣿⣿⣿⣿⡏⣿⣿⣿⣿⣿⣷⡴⠿⢟⣛⣭⣭⣭⣭⣝⣀      ⢠⣿⣿⡀   
    ⣸⣿⣿⣿⣿⢱⣿⣿⣿⡇⣿⣿⡿⣫⣾⣿⣿⡿⣻⣵⣶⣿⣿⣷⣶⣶⣶⣶⣶⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣦⡀   ⢸⣿⣿⡇   
   ⢰⣿⣿⣿⣿⡟⣾⣿⣿⣿⣧⠹⣫⣾⣿⣿⣿⣫⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣆  ⢸⣿⣿⣿   
   ⣿⣿⣿⣿⣿⡇⣿⣿⣿⣿⣿⣎⢿⣿⣿⣿⣳⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣆ ⢸⣿⣿⣿⡇  
  ⢸⣿⣿⣿⣿⣿⢹⣿⣿⣿⣿⣿⣿⣦⡻⣿⢧⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢹⣿⣿⣿⣿⣿⣿⣿⣿⣇⢿⣿⣿⣿⣿  
  ⣾⣿⣿⣿⣿⣿⢸⣿⣿⣿⣿⣿⣿⣿⣿⡆⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠸⣿⣿⣿⣿⣿⣿⣿⠿⣿⡎⣿⣿⣿⣿⡇ 
  ⣿⣿⣿⣿⣿⣿⡜⣿⣿⣿⣿⣿⣿⣿⡿⣹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡏⣿⣿⣿⣿⣿⣿⣿⣿⣿⢀⢻⣿⣿⣿⡿⠛⣡⣾⣿⣿⡜⣿⣿⣿⣇ 
 ⢸⣿⣿⣿⣿⣿⣿⡇⣿⣿⣿⣿⣿⣿⢟⣵⣟⣼⣿⣟⠻⣿⣿⣿⣿⣿⣿⣿⢁⢿⣿⣿⣿⣿⣿⣿⣿⡿⣼⣎⢿⠿⢋⣴⣿⣿⣿⣿⣿⣷⡹⣿⣿⣿ 
 ⢸⣿⣿⣿⣿⣿⣿⣧⢻⣿⣿⣿⣟⣑⣚⢍⣾⣿⣿⣿⣷⣦⣙⠻⣿⣿⣿⢧⣿⡸⣿⣿⣿⣿⣿⣿⣿⢇⣿⠟⣀⢶⣿⣿⣿⣿⣿⣿⣿⣿⣿⣜⠿⡟ 
 ⢸⣿⣿⣿⣿⣿⣿⣿⡘⣿⣿⣿⡿⢟⣵⣿⣿⣿⣿⣿⣿⣿⣿⣷⣦⡙⠣⣿⣿⣧⢻⣿⣿⣿⣿⣿⠏⠜⡡⠞⠛⠃⠙⠿⠿⣿⣿⣿⢿⣿⣿⠿⣫⠇ 
 ⠈⣿⣿⣿⣿⣿⣿⡟⣷⢜⣫⣽⢞⣿⣿⣿⣿⣿⣿⣿⣿⡿⣿⣿⠟⠵⠷⢬⡙⢿⡜⣿⢹⣿⣿⢏⣴⠊⣠⠶⠿⢷⣦⣄⠈⢙⣛⡛⣃⣐⣶⣾⠏  
  ⣿⣿⣿⣿⣿⣿⣧⣿⣿⣔⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠂⣠⡤⠴⠦⢤⣙⣿⣧⠛⣼⠟⣡⣾⣿⣾⣿⡗  ⠹⣿⣆⠈⣙⡇⣿⣿⡿⠋   
  ⢸⣿⣿⣿⣿⣿⣿⢉⣾⣿⣿⣿⣿⣿⣿⣿⡿⠿⠟⠃⢠⣾⣿⡷   ⠻⣿⣿⣴⣷⣿⣿⣿⣿⡇⠉    ⢻⣿⡆⢿⣇⠛⠉     
  ⠘⣿⣿⣿⣿⣿⣿⢸⣿⣿⣿⣿⣿⣶⣤⣲⣶⣾⠿⢀⣿⣿⠙⠁   ⡀⢻⣿⣿⣿⣿⣿⣿⣿⣧⠰⣄⣀⣠⡇⢸⣿⣧⢺⣿⡄      
   ⣿⣿⣿⣿⣿⣿⡏⣿⣿⣿⣿⣿⣿⣿⢻⣿⣿⡇⢸⣿⣷⠠⣄⡀⢀⣰⡇⣸⣿⣿⣿⣿⣿⣿⣿⣿⣦⡙⠿⠿⣡⣿⢿⣿⡏⣿⣷⡀     
   ⢻⣿⣿⣿⣿⣿⣿⣹⣿⣿⣿⣿⢏⣽⢸⣿⣿⣧⠘⣿⣿⣆⠙⠿⠿⢟⣵⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣶⣶⢲⢮⡿⣽⣷⣿⣿⣷     
   ⣸⣿⣿⣿⣿⣿⣿⣧⢿⣿⣿⡏⣾⣯⡍⣿⣿⣿⡼⣯⣟⣛⣻⢶⢼⣟⣿⣿⣿⣿⣿⣿⣿⠿⠿⣿⣿⣿⠿⣫⣏⣾⢳⢳⢇⣿⣿⡿⡇    
   ⣿⣟⣿⣿⣿⣿⣿⣿⣎⢿⣿⡇⣿⡿⡇⢻⣿⣿⣷⣝⠳⠷⢯⢏⣟⣾⡏⣙⣛⢛⣋⣥⣶⣶⣦⣄⡀⠐⠆⣿⣿⣿⣟⣫⢾⣿⣿⡇⠃    
  ⡸⠋⣼⣿⣿⣿⣿⣿⣿⣿⣯⢿⣿⡜⠋⢀⡌⣿⣿⣿⣮⡩⢾⣯⣾⣿⣿⡇⣧⣣⣾⣿⣿⣿⣿⣿⣿⣿⣦ ⣿⣿⣿⣿⢏⣿⣿⠟⠁     
   ⣸⣿⣿⣿⣿⣿⣿⣿⣿⢟⣽⣿⠃ ⣾⣿⡘⢿⣿⣿⣿⣷⡮⣹⣿⣿⡇⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⢱⣿⣿⣿⣋⠚⣩⡵⣸      
  ⢠⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣶⢦⣇ ⣿⣿⣿⣤⠓⠈⢽⣭⣾⣿⣿⣿⣷⡘⣿⣿⣿⣿⣿⣿⣿⣿⠟⣡⣿⣿⡿⢛⡁⠘⢛⣱⡇      
  ⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡱⢿⣿⣦⡘⠿⠿⢟⣱⣶⣤⣽⡻⢿⣿⣿⣿⣿⣮⣙⠻⠿⠿⠟⣋⣡⣾⠿⢛⣥⣶⣿⣧⡀ ⠛       
 ⢰⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣾⣿⣶⣻⣿⣿⡏⠛⠿⡟⣫⠁⠸⢭⣝⣛⣛⣛⠿⡟⠛⢋⣭⣥⣶⣾⡟⠛⠋⢉⣁ 
 ⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢛⣛⠓⠉⠛⠇⣀⣤⠶⢎⠠⠇ ⣀⠈⢉⡉⠉⢀⡀⠰ ⠉⠉⠉⠉
 ⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡎⡳⠂ ⣠⡾⣫⣶⣿⣿⣷⣦⣄⣉⣀⣈⣁⣀⣠⣤⣾⣶⣦⣄⡀ 
 ⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢟⠋⡱⠁ ⡰⡟⠑⠿⠿⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡦\n\n\n
Bem vindo prof\n''')


questao = input('Número da questão: ')
questao = questao.lower()

if questao == '1' or questao == 'todas':
    print('Questão 1')
    m = 0
    n = 0
    while True:
        x = input('Número (enter para sair): ')
        if x == '0' and n == 0:
            print('Erro')
            
        if x == '':
            print('Média:', z)
            break

        y = int(x)
    
        m = m + y  
        
        n = n + 1   
        z = m / n
        
        
elif questao == '2' or questao == 'todas':
    print('Questão 2')
    while True:
        x =  float(input('Valor (0 para sair): '))
        y = x - (x * 0.6)
        a = "{:.2f}".format(x)
        b = "{:.2f}".format(y)
        if x != 0:
            print(f'Vallor: {a} Desconto: 60% Valor com desconto: {b}')
        elif x == 0:
            print('ERRO_Somente valores diferentes de 0 são aceitos')
            break

elif questao == '3' or questao == 'todas':
    print('Questão 3')
    print('Celsiuss\tFireheght\n 0\t\t 32\n 10\t\t 50\n 20\t\t 68\n 30\t\t 86\n 40\t\t 104\n 50\t\t 122\n 60\t\t 140\n 70\t\t 158\n 80\t\t 176\n 90\t\t 194\n 100\t\t 212')

elif questao == '4' or questao == 'todas':    
    print('Questão 4')
    

    au = 0
    a = 0
    d = 0
    coord = 0
    coord2 = 0
    cd1 = 0
    cd2 = 0

    coord = float(input('Coordenada x: '))
    coord2 = float(input('Coordenada y: '))
    au = float(coord)
    a = float(coord2)
    while cd1 != '':
        cd1 = input('Coordenada x (enter para sair): ')
        if cd1 != '':
            cd2 = input('Coordenada y:')
            a1 = float(cd1)
            a2 = float(cd2)
            d = d + sqrt(((a2 - a)* 2) + ((a1 - au)**2))
            au = float(a1)
            a = float(a2)

    else:
        d = d + sqrt(((a2 - coord2) *2) + ((a1 - coord)**2))
        print(d)

elif questao == '5' or questao == 'todas':
    print('Questão 5')    
    n = 0
    while True:
        idade = int(input('Idade da pessoa (0 para finalizar): '))
        if idade <= 2 and idade > 0:
            valor = 0
        elif idade >= 3 and idade <= 12:
            valor = 14.00
        elif idade > 65:
            valor = 18.00
        elif idade == 0:
            n = "{:.2f}".format(n)
            print(f'Valor total: R${n}')
            break 
        else:
            valor = 23.00
        n = n + valor
            
elif questao == '6' or questao == 'todas':
    print('Questão 6')
    bit = input('Bit: ')
    x = bit.count('1')
    y = x % 2
    while bit != '':
        if y == 0:
            print('O Byte é ímpar')
            break
        elif y != 0:   
            print('O Byte é par')
            break
    else:
        print('Erro')

elif questao == '7' or questao == 'todas':
    print('Questão 7')
    x = pi
    y = int(x)
    x1 = "{:.1f}".format(x)
    x2 = "{:.2f}".format(x)    
    x3 = "{:.3f}".format(x)
    x4 = "{:.4f}".format(x)
    x5 = "{:.5f}".format(x)
    x6 = "{:.6f}".format(x)
    x7 = "{:.7f}".format(x)
    x8 = "{:.8f}".format(x)
    x9 = "{:.9f}".format(x)
    x10 = "{:.10f}".format(x)
    x11 = "{:.11f}".format(x)
    x12 = "{:.12f}".format(x)
    x13 = "{:.13f}".format(x)
    x14 = "{:.14f}".format(x)
    x15 = "{:.15f}".format(x)
    print(y,x1,x2,x3,x4,x5,x6,x7,x8,x9,x10,x11,x12,x13,x14,x15)

elif questao == '8' or questao == 'todas':
    print('Questão 8')
    text = ''
    while True:
        word = input('Digite um caractere por vez (Enter para exibir resultado): ')
        if word != '':
            y = ord(word)
            key = int(input('Quantas casas você deseja pular? '))
            msg = y + key
            msg_text = str(chr(msg))
            text = text + msg_text
        else:
            print(text)
            break

elif questao == '9' or questao == 'todas':
    print('Questão 9')
    x = int(input('Número: '))

    raiz = x / 2
    while raiz * raiz > 0.1 ** -12:
        raiz = (raiz + (raiz / 2)) / 2
        
    else:
        print('raiz:', raiz)

elif questao == '10' or questao == 'todas':
    print('Questão 10')
    while True:
        word = input('Palavra (Enter para sair): ')
        out = ''
        reword = word[::-1]   #reverse word
        if word == reword and word != out:
            print('Palíndromo')
        elif word == out:
            print('Exit')
            break
        else:
            print('Não é um Palíndromo')
    
elif questao == '11' or questao == 'todas':
    print('Questão 11')
    while True:
        out = ''
        frase = input('Frase (Enter para sair): ')
        frase = frase.upper()
        frase = frase.replace(' ', '')          # Removes the ' '
        frase = frase.replace(',', '')          # Removes the ,
        frase = frase.replace('.', '')          # Removes the .
        frase = frase.replace('!', '')          # Removes the !
        frase = frase.replace('?', '')          # Removes the ?
        reverse = frase[::-1]
        
        if reverse == frase and frase != out:
            print('Palíndromo')
        
        elif frase == out:
            break
        
        else:
            print('Não é um Palíndromo')
    
elif questao == '12' or questao == 'todas':
    print('Questão 12')
    tabela = ('''\t1   2   3   4   5   6   7   8   9   10
    1   1   2   3   4   5   6   7   8   9   10
    2   2   4   6   8   10  12  14  16  18  20
    3   3   6   9   12  15  18  21  24  27  30
    4   4   8   12  16  20  24  28  32  36  40
    5   5   10  15  20  25  30  35  40  45  50
    6   6   12  18  24  30  36  42  48  54  60
    7   7   14  21  28  35  42  49  56  63  70
    8   8   16  24  32  40  48  56  64  72  80
    9   9   18  27  36  45  54  63  72  81  90
    10  10  20  30  40  50  60  70  80  90  100 ''')
    print(tabela)

elif questao == '13' or questao == 'todas':
    print('Questão 13')
    x = int(input('Número (maior ou igual a 2): '))
    fator = 2
    
    if x < 2:
        print('Erro')
    
    while x >= fator:
        if x % fator == 0:
            x = x / fator
            print(fator)
        else:
            fator = fator + 1
    
elif questao == '14' or questao == 'todas':  
    print('Questão 14')

    bit = input('Número em binário: ' )
    readbit = bit[::-1]
    
    while readbit != 0:
        num = int(readbit[0] * 2)
        readbit = readbit - str(readbit[-1])

elif questao == '15' or questao == 'todas':
    print('Questão 15')
    
    result = ''
    num = int(input('Número para transformar em binário: '))
    
    while num != 0:
        rest = num % 2
        r = str(rest)
        result = result + r
        num = num // 2

    else:
        print(result)

elif questao == '16' or questao == 'todas':
    print('Questão 16')

    out = 0
    coins = ''
    mais = 0


    while mais <= 10:
        coins = ''
        out = 0
        while out <= 10:
        
            out = out + 1
            num = randint(0, 1)    # 0 = cara      1 = coroa
            coin = str(num)


            if coin == '0':          # 0 para A
                coin = 'A'    
            elif coin == '1':        # 1 para O
                coin = 'O'


            coins = coins + coin


            xxx = coins.find('AAA')
            yyy = coins.find('OOO') 


            if xxx >= 0:
                print(f'{coins} ({out} sorteios)')
                break
            
            elif yyy >= 0:
                print(f'{coins} ({out} sorteios)')
                break
        mais = mais + 1 
    
else:
    print('Erro')    

