from random import randint
import math

#Lucas de Azevedo
#BCC1
questao = (input('Número da questão: '))


if questao == '1': #questão 1
    print('Questão 1')
    
    def hip(l1, l2):
        h = (l1 * l1) + (l2 * l2)
        h = math.sqrt(h)
        return h
    
    
    
    def main():
        l1 = float(input('L1: '))
        l2 = float(input('L2: '))

        
        sss = hip(l1, l2)
        print(sss)
        

    if __name__ == "__main__":
        main()        


elif questao == '2': #questão 2
    print('Questão 2')
    
    def tarifa(dis):
        
        exes = 4.00
        disprice = (dis / 140) * 0.25
        price = exes + disprice
        return price
    
    def main():
        distance = int(input('Distância em metros: '))

        total = tarifa(distance)
        print(f'Total a pagar: R${total}')
    
    if __name__ == "__main__":
        main()


elif questao == '3': #questão 3
    print('Questão 3')

    def delivery(items):
        if items == 1:
            value = 10.95
            return value

        else:
            value = 10.95 + ((items - 1) * 2.95)
            return value

    def main():
        item = int(input('Quantidade de itens desejados: '))
        item = delivery(item)
        print(f'O valor total de entrega foi de R${item}')
    
    if __name__ == "__main__":
        main()


elif questao == '4': #quetsão 4
    print('Quetsão 4')

    def main():
        n1 = float(input('Número 1: '))
        n2 = float(input('Número 2: '))
        n3 = float(input('Número 3: '))

        mediana = [n1 , n2 , n3]
        med = mediana.sort()
        

        print(mediana)
        print(med)

    if __name__ == "__main__":
        main()


elif questao == '5': #questão 5
    print('Questão 5')

    def num(num):
        if num == '1':
            num = 'primeiro'
            return num

        elif num == '2':
            num = 'segundo'
            return num

        elif num == '3':
            num = 'terceiro'
            return num

        elif num == '4':
            num = 'quarto'
            return num

        elif num == '5':
            num = 'quinto'
            return num

        elif num == '6':
            num = 'sexto'
            return num

        elif num == '7':
            num = 'sétimo'
            return num

        elif num == '8':
            num = 'oitavo'
            return num

        elif num == '9':
            num = 'nono'
            return num

        elif num == '10':
            num = 'décimo'
            return num

        elif num == '11':
            num = 'décimo primeiro'
            return num

        elif num == '12':
            num = 'décimo segundo'
            return num
        
        elif num == 'todas':
            num = 'primeiro segundo terceiro quarto quinto sexto sétimo oitavo nono décimo décimo primeiro décimo segundo'
            return num
        
        else:
            print('Número não achado na biblioteca')

    def main():
        numero = input('Número para ordinal (`todas` para exibit todas): ')
        numero = numero.lower()
        numero = num(numero)
        print(numero)
    
    if __name__ == "__main__":
        main()


elif questao == '6': #questão 6

    def central(cen):
        centro = '\t\t\t\t\t\t\t\t\t\t ' + cen
        return centro



    def main():
        x = input('Insira seu texto aqui: ')
        y = central(x)
        print(y)
    
    if __name__ == "__main__":
        main()


elif questao == '7': #questao 7

    def triangulo(tri):
        l1 = tri[0]
        l2 = tri[1]
        h = tri[2]

        
        if h > l1 + l2:
            return('Não forma um triangulo') 
        else:
            return('É um trigas')

    def main():
        x = int(input('Lado 1: '))
        y = int(input('Lado 2: '))
        z = int(input('Lado 3: '))

        aaaaaaaaaaaaaaaa = [x, y, z]
        aaaaaaaaaaaaaaaa.sort()
        a = triangulo(aaaaaaaaaaaaaaaa)
        print(a)

    if __name__ == "__main__":
        main()


elif questao == '8': #questão 8
    def caps(cts):
        if cts.find('. ') > 0:
            cts = cts.split('. ')
            ls1 = cts[0]
            ls2 = cts[1]


            up1 = ls1[0]
            up1 = up1.upper() + ls1[1:]

            up2 = ls2[0]
            up2 = up2.upper() + ls2[1:]

            joint = up1 + '. ' + up2
            return(joint)



        elif cts.find('! ') > 0:
            cts = cts.split('! ')
            ls1 = cts[0]
            ls2 = cts[1]


            up1 = ls1[0]
            up1 = up1.upper() + ls1[1:]

            up2 = ls2[0]
            up2 = up2.upper() + ls2[1:]

            joint = up1 + '! ' + up2
            return(joint)



        elif cts.find('? ') > 0:
            cts = cts.split('? ')
            ls1 = cts[0]
            ls2 = cts[1]


            up1 = ls1[0]
            up1 = up1.upper() + ls1[1:]

            up2 = ls2[0]
            up2 = up2.upper() + ls2[1:]

            joint = up1 + '? ' + up2
            return(joint)

        else:
            up = cts[0]
            up = up.upper() + cts[1:]
            return(up)
    
    def main():
       a = input('Escreva sua frase: ')

       print(caps(a)) 


    if __name__ == "__main__":
        main()


elif questao == '9': #questão 9
    def isIntegre(ctx):
        strip = ctx.strip(' ')
        rest = strip[1:]

        if strip.isdigit() == True:
            return "Inteiro"

        elif rest.isdigit() == True and strip.find('+') >= 0:
            return "Número Inteiro"

        elif rest.isdigit() == True and strip.find('-') >= 0:
            return "Número Inteiro"

        else:
            return("Não é um numero inteiro")

    def main():
        vava = input('Digite seu texto para verificar se é um número: ')
        print(isIntegre(vava))

    if __name__ == "__main__":
        main()


elif questao == '10': #questão 10
    print('Questão 10')
    
    def prime(num):
        x2 = num % 2
        x3 = num % 3
        x5 = num % 5
        x7 = num % 7
        if x2 == 0 or x3 == 0 or x5 == 0 or x7 == 0:
            num = 'Não primo'
        
        elif num == 1 or num == 2 or num == 3 or num == 5 or num == 7:
           num = 'Primo'

        else:
            num = 'Número primo'

        return num

    def main():
        numero = int(input('Número: '))
        numero = prime(numero)
        print(numero)

    if __name__ == "__main__":
        main()


elif questao == '11': #questão 11
    def main():
        key = ''
        ran = randint(7,10)
        
        for i in range(ran):
            
            x = chr(randint(33,126))
            key = key + x
            if i >= 7:
                print(f'Senha: {key}')
            
            else:
                continue
                
    if __name__ == "__main__":
        main()


elif questao == '12': #questão 12
    def main():
        key = input('Digite sua senha: ')
        keylen = len(key)
        x = any(key.isdigit() for key in key) #verifica se tem apenas números

        if keylen < 8:
            print('Sua senha deve conter pelo menos 8 caracteres.')
        else:
            if key.isdigit() == True:
                print('Sua senha não pode conter apenas números')
            elif x == False:
                print('Sua senha precisa conter pelo menos um número.')
            else:
                if key.lower() == key:
                    print('Sua senha precisa ter pelo menos uma letra maiúscula')
                elif key.upper() == key:
                    print('Sua senha precisa ter pelo menos uma letra minúscula')
                else:
                    if x == True:
                        print('senha válida.')

    if __name__ == "__main__":
        main()


elif questao == '13': #questão 13

    def month(date):
        #days of months
        d31 = [1, 3, 5, 7, 8, 10, 12]

        d30 = [4, 6, 9, 11]

        dfe = [2]

        date = date.split('/')
        month = int(date[0])
        year = int(date[1])

        if month in d31:
            return'Esse mes tem 31 dias'

        elif month in d30:
            return 'Esse mês tem 30 dias' 

        elif month in dfe and year % 4 == 0:
            return 'O mês de fevereiro tem 29 dias' 

        elif month in dfe and year % 4 != 0:
            return 'O mês de fevereiro tem 28 dias' 
        
        else:
            return 'Favor bote uma data válida'


    def main():

        date = input('Mês e Ano(exemplo:01/22): ')
        if date.find('/') <= 0:
            print('Erro 404, por favor bote o ´/´')

        else:
            print(month(date))


    if __name__ == "__main__":
        main()


elif questao == '14': #questão 14
    def main():

        date = input('Data(Dia/mes/ano(00/00/00)): ')
        date = date.split('/')


        day = int(date[0])    
        month = int(date[1])    
        year = int(date[2])

        if day * month == year:
        
            print('A data é magica')

        else:
        
            print('Data não é magica')

    if __name__ == "__main__":
        main()


elif questao == '15': #questão 15
    def hex2dec(hexa):

        hexd = int(hexa, 16)

        return hexd

    def dec2hex(dec):

        deci = hex(int(dec))
        deci = deci.replace('0x','')

        return deci

    def main():

        hexas = ['0','1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F']

        num = input('Número: ')
        num = num.upper()

        if num.isdigit() == True:
            print('Decimal para Hexadecimal:', dec2hex(num))

        elif len(num) == 1 and num in hexas:
            print('Hexadecimal para decimal:', hex2dec(num))

        else:
            print('Número invalido')

    if __name__ == "__main__":
        main()


elif questao == '16': #questão 16

    def main():
        
        x = input('Número: ')
        base = int(input('Base do número (se quiser base 10 so botar 10): '))
        print(int(x, base))

    if __name__ == "__main__":
        main()


else:
    print('Erro questao_NotFound')