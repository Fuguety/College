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
    if v < 0:
        print("please insert a value higher or equal to 0")
    
    else:
        try:
            print(ls.arr[v - 1])
        except:
            print("Element not found")


def checkArray():
    ls = List()
    try:
        if ls.arr[0] == "":
            return False
        else:
            return True
    except:
        return False


def arrLenght():
    ls = List()
    x = len(ls.arr)
    return x


def lastElement():
    ls = List()
    check = checkArray()
    try:
        if(check == False):
            print("The list is empty")
        
        else:
            x = arrLenght() - 1
            print(f"Last element of the list is: {ls.arr[x]}")
                    
    except:
        print("Error")


# main
ls = List()
print(" Welcome to List manipulation program \n Please inster a number to choose wich action you want to do")

while (True):
    try:
        print("\n 1 - add element to list \n 2 - search element on list \n 3 - check if list is empty \n 4 - get the size of the list \n 5 - get the last element \n Enter - Exit program")

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

            search(int(element))
        
        elif (x == "3"):
            check = checkArray()
            print(check)
        
        elif (x == "4"):
            getSize = arrLenght()
            print(f"Size of the List: {getSize}")
        
        elif (x == "5"):
            lastElement()
            
        elif(x == ""):
            break

        else:
            print("Please insert a valid option")

    except:
        print("Error")
        break
