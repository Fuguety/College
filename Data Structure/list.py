class List:
    arr = []


def insert(v):
    ls = List()
    ls.arr.insert(0, v)
    print("Inserted to list ", ls.arr)


def printList():
    ls = List()
    print(ls.arr)


def search(v):
    ls = List()
    try:
        x = ls.arr[v]
        print(x)
    except:
        print("List is empty")


def checkArray():
    ls = List()
    if ls.arr[0] == "":
        return True
    else:
        return False


def arrLenght():
    ls = List()
    x = ls.arr.lenght()
    return x


def lastElement():
    ls = List()
    x = arrLenght()
    print(ls.arr[x])


# main
ls = List()
print(" Welcome to List manipulation program \n Please inster a number to choose wich action you want to do")

while (True):
    try:
        print(" 1 - add element to list \n 2 - search element on list \n 3 - check if list is empty \n 4 - get the size of the list \n 5 - get the last element \n Enter - Exit program")

        print(f"\nCurrent list: {ls.arr}")

        x = input()

        if (x == "1"):
            print("Element you want to add:")
            element = input()
            insert(element)

        elif (x == "2"):
            quantity = arrLenght()
            print(f"The current list has {quantity} elements")
            
            print("Wich element you want to see? ")
            element = input()

            search(element)
        
        elif (x == "3"):
            print(checkArray())
        
        elif (x == "4"):
            print(arrLenght)
        
        elif (x == "5"):
            lastElement()
            
        elif(x == ""):
            break

        else:
            print("Please insert a valid option")

    except:
        print("Error")
        break
