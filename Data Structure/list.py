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
    try:
        if ls.arr[0] == "":
            return True
        else:
            return False
    except:
        return True

def arrLenght():
    ls = List()
    x = len(ls.arr)
    return x


def lastElement():
    ls = List()
    check = checkArray()
    try:
        if (check != False):
            print("The list is empty")

        else:
            x = arrLenght() - 1
            print(f"Last element of the list is: {ls.arr[x]}")

    except:
        print("Error")


def remove(v):
    ls = List()
    x = False
    for i in ls.arr:
        if(i == v):
            ls.arr.remove(v)
            print(f"Element {v} removed")
            x = True
            break
        else:
            continue
    
    if(x != True):
        print("Element not found")
        
def insertEnd(element):
    ls = List()
    check = checkArray()
    if (check != True):
        ls.arr.append(element)
    
    else:
        print("List is empty, just adding element as first element")
        ls.arr.insert(0, element)
    
def freeList():
    ls = List()
    ls.arr.clear()
    print("List is now empty")


# main
ls = List()
print(" Welcome to List manipulation program \n Please inster a number to choose wich action you want to do")

while (True):
    try:
        print(" 1 - add element to list \n 2 - search element on list \n 3 - check if list is empty \n 4 - get the size of the list \n 5 - get the last element \n 6 - Remove a specific element \n 7 - Insert a element to end of the list \n 9 - Clean list\n Enter - Exit program")

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
            print(arrLenght())

        elif (x == "5"):
            lastElement()
        
        elif(x == "6"):
            print("Please type the element you want to remove:")
            v = input()
            remove(v)
        
        elif(x == "7"):
            print("Insert element you want to add to the end of the list")
            element = input()
            insertEnd(element)
            
        elif(x == "9"):
            freeList()

        elif (x == ""):
            break

        else:
            print("Please insert a valid option")

    except:
        print("Error")
        break

