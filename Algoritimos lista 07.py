from random import randint



questao = int(input("Número da questão: "))

if questao == 2:
    
    def main():
        ls1a = []
        ls2a = []
    
        while True:
            ls1 = input('Números para a lista 1 (Enter para ir pra lista 2): ')
            if ls1 == "":
                break
            else:
                ls1 = int(ls1)
                ls1a.append(ls1)
                continue
            
        while True:
            ls2 = input('Números para a lista 2 (Enter para exibir resultado): ')
            if ls2 == "":
                break
            else:
                ls2 = int(ls2)
                ls2a.append(ls2)
                continue
            
            
            
        lst = ls1a + ls2a
        lst = list(dict.fromkeys(lst))
        lst.sort()
        print(lst)
    
    if __name__ == "__main__":
        main()


if questao == 3:


    dc = {}

    #builf dict

    while True:
        key = input("Chave do dicionário: ")
        term = input("Termo do dicionário: ")

        if key and term == "out":
            break

        else:
            dc[key] = term
            continue
    #shows the keys
    print(f"Chaves do dicionário: {dc.keys()}")
    print(dc)


if questao == 4:

    morsecode = ""
    morse = {"A": ".-", "B": "-...", "C": "-.-.", "D": "-..", "E": ".", "F": "..-.", "G": "--.", "H": "....", "I": "..", "J": ".---", "K": "-.-",
    "L": ".-..", "M": "--","N": "-.","O": "---","P": ".--.","Q": "--.-","R": ".-.","S": "...","T": "-","U": "..-","V": "...-","W": ".--","X": "-..-","Y": "-.--","Z": "--.."
    ,"0": "-----","1": ".----","2": "..---","3": "...--","4": "....-","5": ".....","6": "-....","7": "--...","8": "---..","9": "----.", " ": ""}
    
    code = input("Texto para codigo morse: ")
    code = code.upper()
    
    while len(code) != 0:
        code1 = code[0]
        coding = morse[code1]
        morsecode = morsecode + " " + coding
        code = code[1:]
    
    
    print(morsecode)


if questao == 5:

    text1 = input("1º palavra: ")
    text1 = "".join(sorted(text1))

    text2 = input("2º palavra: ")
    text2 = "".join(sorted(text2))

    if text1 == text2:
        print(True)

    else:
        print(False)


if questao == 6:



    text1 = input("1º Frase: ")
    text1 = " ".join(text1)
    text1 = "".join(sorted(text1.upper()))
    text1 = " ".join(text1)
    text1 = text1.replace(" ", "")
    
    text2 = input("2º Frase: ")
    text2 = " ".join(text2)
    text2 = "".join(sorted(text2.upper()))
    text2 = text2.replace(" ", "")
    
    if text1 == text2:
        print(True)
    
    else:
        print(False)


if questao == 7:

    def gerarCartela():
        """
        Gera uma cartela de bingo e retorna para o usuário um dicionário com os valores gerados.
        """
        bingo = {'B': 'temp', 'I': 'temp', 'N': 'temp', 'G': 'temp', 'O': 'temp'}
        inicio = 1
        fim = 15
        for letra in bingo:
            valores = []
            while len(valores) < 5:
                valores.append(randint(inicio, fim))
            bingo[letra] = valores
            valores.clear
            inicio = inicio + 15
            fim = fim + 15

        return bingo

    def desenharCartela(dados):
        """
        Retorna uma string com a cartela desenhada
        """
        cartela =            "----------------------\n"
        cartela = cartela + ("| B | I | N | G | O  |")
        for pos in range(0, 5):
            if (dados['B'][pos] < 10):            
                cartela = cartela + (f"\n| {dados['B'][pos]} " + f"| {dados['I'][pos]}"+ f"| {dados['N'][pos]}"+ f"| {dados['G'][pos]}"+ f"| {dados['O'][pos]} |")
            else:             
                cartela = cartela + (f"\n| {dados['B'][pos]}" + f"| {dados['I'][pos]}"+ f"| {dados['N'][pos]}"+ f"| {dados['G'][pos]}"+ f"| {dados['O'][pos]} |")
        cartela = cartela + "\n----------------------"    
        return cartela

    def main():
        bingo = gerarCartela()
        print(bingo)
        print(desenharCartela(bingo))

    if __name__=="__main__":
        main()


if questao == 8:

    def gerarCartela():
        """
        Gera uma cartela de bingo e retorna para o usuário um dicionário com os valores gerados.
        """
        bingo = {'B': 'temp', 'I': 'temp', 'N': 'temp', 'G': 'temp', 'O': 'temp'}
        inicio = 1
        fim = 16
        for letra in bingo:
            valores = []
            while len(valores) < 5:
                valores.append(randint(inicio, fim))
            bingo[letra] = valores
            valores.clear
            inicio = inicio + 15
            fim = fim + 15

        return bingo

    def desenharCartela(dados):
        """
        Retorna uma string com a cartela desenhada
        """
        cartela =            "----------------------\n"
        cartela = cartela + ("| B | I | N | G | O  |")
        for pos in range(0, 5):
            if (dados['B'][pos] < 10):            
                cartela = cartela + (f"\n| {dados['B'][pos]} " + f"| {dados['I'][pos]}"+ f"| {dados['N'][pos]}"+ f"| {dados['G'][pos]}"+ f"| {dados['O'][pos]} |")
            else:             
                cartela = cartela + (f"\n| {dados['B'][pos]}" + f"| {dados['I'][pos]}"+ f"| {dados['N'][pos]}"+ f"| {dados['G'][pos]}"+ f"| {dados['O'][pos]} |")
        cartela = cartela + "\n----------------------"    
        return cartela

    def verificarCartela(valores, bingo):
        """
        Verifica se um cartela de bingo é vencedora ou não. Retornando True caso sim.
        valores = conjunto com os números sorteados


        bingo = cartela a ser verificada 
        """
        items = set()
        valores = set(valores)
        for pos in range (0, 5):                    #Verifica todas as linhas
            for letra in bingo:
                items.add(bingo[letra][pos])
            if (items.issubset(valores)):
                return True
            items.clear()

        items.clear()
        for letra in bingo:                         #Verifica todas as colunas
            for pos in range(0, 5):
                items.add(bingo[letra][pos])
            if (items.issubset(valores)):
                return True
            items.clear()

        items.clear()                               #Verificam as diagonais
        inicio = -1
        for letra in bingo:
            inicio = inicio + 1
            items.add(bingo[letra][inicio])
        if (items.issubset(valores)):
            return True

        items.clear()
        inicio = -1
        for letra in "OGNIB":
            inicio = inicio + 1
            items.add(bingo[letra][inicio])
        if (items.issubset(valores)):
            return True

        return False

    def main():

        #Aqui serão testadas todas as possibilidades de vitória no bingo (as tabelas estarão tortas pois o número de teste é menor que 10)

        #Cartela diagonal
        bingo = {'B': [15, 3, 4, 11, 0], 'I': [16, 9, 20, 0, 30], 'N': [43, 8, 0, 42, 39], 'G': [47, 0, 49, 2, 49], 'O': [0, 73, 64, 66, 6]}
        print(bingo)
        print(desenharCartela(bingo))
        if (verificarCartela({0}, bingo)):
            print("Cartela vencedora")
        else:
            print("Cartela perdedora")

        #Cartela diagonal
        bingo = {'B': [0, 3, 4, 11, 75], 'I': [16, 0, 20, 0, 30], 'N': [43, 8, 0, 42, 39], 'G': [47, 16, 49, 0, 49], 'O': [8, 73, 64, 66, 0]}
        print(bingo)
        print(desenharCartela(bingo))
        if (verificarCartela({0}, bingo)):
            print("Cartela vencedora")
        else:
            print("Cartela perdedora")

        #Cartela horizontal
        bingo = {'B': [1, 3, 1, 11, 65], 'I': [0, 9, 2, 59, 30], 'N': [0, 8,3, 42, 39], 'G': [0, 26, 4, 2, 49], 'O': [0, 73, 5, 66, 6]}
        print(bingo)
        print(desenharCartela(bingo))
        if (verificarCartela({5,2,3,1,4}, bingo)):
            print("Cartela vencedora")
        else:
            print("Cartela perdedora")

        #Cartela vertical
        bingo = {'B': [0, 0, 0, 0, 0], 'I': [16, 9, 20, 65, 30], 'N': [43, 8, 12, 42, 39], 'G': [47, 58, 49, 2, 49], 'O': [6, 73, 64, 66, 6]}
        print(bingo)
        print(desenharCartela(bingo))
        if (verificarCartela({0}, bingo)):
            print("Cartela vencedora")
        else:
            print("Cartela perdedora")

        #Cartela aleatória
        bingo = gerarCartela()
        print(bingo)
        print(desenharCartela(bingo))
        if (verificarCartela({0}, bingo)):
            print("Cartela vencedora")
        else:
            print("Cartela perdedora")

    if __name__=="__main__":
        main()


if questao == 9:

    def gerarCartela():
        """
        Gera uma cartela de bingo e retorna para o usuário um dicionário com os valores gerados.
        """
        bingo = {'B': 'temp', 'I': 'temp', 'N': 'temp', 'G': 'temp', 'O': 'temp'}
        inicio = 1
        fim = 16
        for letra in bingo:
            valores = []
            while len(valores) < 5:
                valores.append(randint(inicio, fim))
            bingo[letra] = valores
            valores.clear
            inicio = inicio + 15
            fim = fim + 15
        
        return bingo
    
    def desenharCartela(dados):
        """
        Retorna uma string com a cartela desenhada
        """
        cartela =            "----------------------\n"
        cartela = cartela + ("| B | I | N | G | O  |")
        for pos in range(0, 5):
            if (dados['B'][pos] < 10):            
                cartela = cartela + (f"\n| {dados['B'][pos]} " + f"| {dados['I'][pos]}"+ f"| {dados['N'][pos]}"+ f"| {dados['G'][pos]}"+ f"| {dados['O'][pos]} |")
            else:             
                cartela = cartela + (f"\n| {dados['B'][pos]}" + f"| {dados['I'][pos]}"+ f"| {dados['N'][pos]}"+ f"| {dados['G'][pos]}"+ f"| {dados['O'][pos]} |")
        cartela = cartela + "\n----------------------"    
        return cartela
    
    def verificarCartela(valores, bingo):
        """
        Verifica se um cartela de bingo é vencedora ou não. Retornando True caso sim.
        valores = conjunto com os números sorteados
        
        
        bingo = cartela a ser verificada 
        """
        items = set()
        valores = set(valores)
        for pos in range (0, 5):                    #Verifica todas as linhas
            for letra in bingo:
                items.add(bingo[letra][pos])
            if (items.issubset(valores)):
                return True
            items.clear()
    
        items.clear()
        for letra in bingo:                         #Verifica todas as colunas
            for pos in range(0, 5):
                items.add(bingo[letra][pos])
            if (items.issubset(valores)):
                return True
            items.clear()
        
        items.clear()                               #Verificam as diagonais
        inicio = -1
        for letra in bingo:
            inicio = inicio + 1
            items.add(bingo[letra][inicio])
        if (items.issubset(valores)):
            return True
    
        items.clear()
        inicio = -1
        for letra in "OGNIB":
            inicio = inicio + 1
            items.add(bingo[letra][inicio])
        if (items.issubset(valores)):
            return True
        
        return False
    
    def main():
        minimo = 9999999
        maximo = 0
        qtdJogos = 1000
        totalChamadas = 0
    
        for rodadas in range(1, 1001):
            numerosDisponiveis = []
            for i in range(1,76):
                numerosDisponiveis.append(i)
            cartela = gerarCartela()
            NumerosSorteados = set()
            chamadas = 1
            while True:
                IndexSorteado = randint(0, len(numerosDisponiveis))
                if (IndexSorteado == len(numerosDisponiveis)):
                    try:    
                        NumerosSorteados.add(numerosDisponiveis.pop())
                    except:
                        break
                else:
                    NumerosSorteados.add(numerosDisponiveis[IndexSorteado]) 
                    del numerosDisponiveis[IndexSorteado]  
    
                if (chamadas >= 5) and (verificarCartela(NumerosSorteados, cartela)):
                    print("Cartela vencedora: ")
                    print(desenharCartela(cartela))
                    print("Quantidade de números sorteados:", len(NumerosSorteados))
                    print("Números sorteados:", NumerosSorteados)
                    if (chamadas < minimo):
                        minimo = chamadas
                    if (chamadas > maximo):
                        maximo = chamadas
                    totalChamadas = totalChamadas + chamadas   
                    break
                chamadas = chamadas + 1
        
        media = totalChamadas / qtdJogos
        print("Média: %.1f" % (media))
        print("Máximo:", maximo)
        print("Mínimo:", minimo)
    
    if __name__=="__main__":
        main()

