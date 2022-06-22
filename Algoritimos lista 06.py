from random import randint
from gettext import find

questao = int(input("Número da questão: "))

if questao == 1:
    ls = []
    while True:
        num = int(input("Insira seu número aqui: "))
        ls.append(num)
        if num == 0:
            ls.sort()
            print(ls)
            break
        else:
            ls.append(num)
            continue

elif questao == 2:
    ls = []
    while True:
        num = int(input("Insira seu número aqui: "))

        if num == 0:
            ls.sort()
            ls.reverse()
            print(ls)
            break
        else:
            ls.append(num)
            continue

elif questao == 3:
    
    ls = []

    while True:
        num = int(input("Insira seu número aqui: "))

        if num == 0:
            ls.sort()
            ls.pop(0)
            ls.reverse()
            ls.pop(0)
            ls.reverse()
            print(ls)
            break
        else:
            ls.append(num)
            continue

elif questao == 4:

    ls = []

    while True:
        text = input("Insira seu número aqui: ")

        if text == "":
            ls = list(dict.fromkeys(ls))
            print(ls)
            break
        else:
            ls.append(text)
            continue


elif questao == 5:

    ls = []
    ls1 = []
    ls2 = []
    ls3 = []
    while True:
        num = input("Insira seu número aqui: ")

        if num == "":

            ls = ls1 + ls2

            print(ls)
            break

        else:
            number = int(num)
            if number < 0:
                ls1.append(number)

                continue
            
            
            elif number > 0:
                ls2.append(number)

                continue
            
            continue


elif questao == 6:
    def divisores(div):
        htot = []

        for n in range(1, div + 1):
            if div % n == 0:
                h = [n]
                htot = htot + h

        return htot


    def main():
        exes = int(input("Número: "))
        print(divisores(exes))

    if __name__ == "__main__":
        main()


elif questao == 7:
    def divisores(div):
        htot = 0

        for n in range(1, div):
            if div % n == 0:
                h = n
                htot = htot + h
        if htot == div:
            return "É um numero perfeito"
        else:
            return "Não é um número perfeito"


    def main():
        exes = int(input("Número: "))
        print(divisores(exes))

    if __name__ == "__main__":
        main()


elif questao == 8:
    
    def textoooo(elton):

        eder = elton.replace(" ", "$$")
        eder = eder.replace("!", "$$")
        eder = eder.replace("?", "$$")
        eder = eder.replace(".", "$$")
        eder = eder.replace(",", "$$")
        eder = eder.replace("/", "$$")
        eder = eder.replace(":", "$$")
        eder = eder.replace(";", "$$")
        eder = eder.replace("-", "$$")
        eder = eder.split("$$")
        return eder


    def main():
        exes = input("Text: ")
        print(textoooo(exes))

    if __name__ == "__main__":
        main()


elif questao == 9:

    def order(ls, media):
        out = 0
        lslen = len(ls)
        alta = []
        abajo = []
        mediaaa = []

        while out != lslen:
            out = out + 1
            thingy = ls[0]
            thingy = int(thingy)

            if thingy < media:
                thingy = [thingy]
                abajo = abajo + thingy

            elif thingy == media:                
                thingy = [thingy]
                mediaaa = mediaaa + thingy

            elif thingy > media:    
                thingy = [thingy]            
                alta = alta + thingy      

            ls.pop(0)

        return f"notas abaixo da média: {abajo} \nnotas na média:{mediaaa} \nnotas acima da média: {alta}"



    def main():
        ls = []
        m = 0
        n = 0

        while True:
            num = input('Número (enter para sair): ')

            if num == '':
                print(order(ls, media))

                break
            
            else:
            
                num = int(num)

                y = num

                m = m + y  

                n = n + 1   
                media = m / n

                x = [num]
                ls = ls + x


    if __name__ == "__main__":
        main()


elif questao == 10:

    ls = []
    lse = ['e']
    lsr = []
    ls1 = []
    string = " "

    while True:
        item = [input("Texto: ")]

        
        if item[0] == "":

            if len(ls) > 2:
                ls.reverse()
                ls1 = [ls[0]]
                ls.pop(0)
                ls.reverse()
                ls = ls + lse + ls1
                x = string.join(ls)
                x = x.replace(" ", ", ")
                x = x.replace("e, ", "e ")
                if x.find(", e ") >= 1:
                    x = x.replace(", e ", " e ")
                print(x)
                break
            elif len(ls) == 2:
                ls1 = [ls[1]]
                ls.pop(1)
                ls = ls + lse + ls1
                x = string.join(ls)
                print(x)
                break
            elif len(ls) == 1:
                print(ls[0])
                break
            else:
                print("Insira um texto")

        else:
            ls = ls + item
            continue


elif questao == 11:
    
    sorteio = []
    for numeiro in range(6):
        rand = [randint(1, 60)]
        sorteio = sorteio + rand
        sorteio.sort()

    print(sorteio)


elif questao == 12:

    def main():
        ls =[]
        while True:
            term = input("Termo: ")

            if term == "":
                aaa = ls
                aaa = aaa.sort()

                if aaa == ls:
                    print("True")
                    break
                
                else:
                    print("False")
                    break
                
            else:
                term = int(term)
                term = [term]
                ls = ls + term
                continue



    if __name__ == "__main__":
        main()


elif questao == 13:
    def countRange(ls, mini, maxi):

        values = []
        ls.sort()
        lente = len(ls)
        for x in range(lente):
            if ls[0] >= mini and ls[0] < maxi:
                ls1 = [ls[0]]
                values = values + ls1
                ls.pop(0)

            else:
                ls.pop(0)
        return values



    def main():

        ls = []
        while True:
            term = input("Número(Enter para continuar): ")
            if term == "":
                break
            
            else: 
                term = int(term)
                term = [term]
                ls = ls + term
                continue
            
        termmax = int(input("Valor máximo: "))
        termmin = int(input("Valor mínimo: "))


        print(countRange(ls, termmin, termmax))



    if __name__ == "__main__":
        main()


elif questao == 14:
    
    def precedencia(x):
        if x.find('-') >= 0 or x.find("+") >= 0:
            return 1

        elif x.find("*") >= 0 or x.find("/") >= 0:
            return 2

        elif x.find("^") >= 0:
            return 3

        else:
            return -1, "não é uma precedência"

    def main():
        x = input("Precedência: ")
        print(precedencia(x))

    if __name__ == "__main__":
        main()


elif questao == 15:

    def main():
        expres = input("Expressão matemática: ")


        if expres.find("+ ") >= 0:

            expres = expres.replace("+ ", ", + , ")


        if expres.find("- ") >= 0:
            expres = expres.replace("- ", ", - , ")

        if expres.find("/") >= 0:
            expres = expres.replace("/", ", / , ")

        if expres.find("*") >= 0:
            expres = expres.replace("*", ", * , ")

        if expres.find("^") >= 0:
            expres = expres.replace("^", "^ , ")

        expres = expres.split(",")

        print(f"tokens: {expres}")

    if __name__  == "__ main__":
        main()



