
def sumList(ls):
    total = 0
    for i in ls:
        total += i
    return total

def multList(ls):
    total = 1
    for i in ls:
        total *= i
    return total

def reverseList(ls):
    lsNew = []
    for i in range(len(ls)):
        lsNew.append(ls[-i - 1])
    return lsNew 

def printList(ls, msg):
    print(msg, end = '');
    for i in ls:
        print(str(i) + " ", end = '')

userInput = ""
list = []
while(userInput != "x"): 
    userInput = input("Enter numbers until you are done, then enter 'x' >")
    if userInput.isnumeric():
        list.append(int(userInput))

        
printList(list, "\n\nInput: ")
printList(reverseList(list), "\nReversed Input: ")

print("\nSum of list: %d" % (sumList(list)))
print("Product of list: %d" % (multList(list)))
