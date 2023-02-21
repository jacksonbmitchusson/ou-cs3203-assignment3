
def sumList(arr):
    total = 0
    for i in arr:
        total += i
    return total

def multList(arr):
    total = 1
    for i in arr:
        total *= i
    return total

userInput = ""
list = []
while(userInput != "x"): 
    userInput = input("Enter numbers until you are done, then enter 'x' >")
    if userInput.isnumeric():
        list.append(int(userInput))

print("Input: ", end='')
for i in list:
    print(str(i) + " ", end='')
print("\nSum of list: %d" % (sumList(list)))
print("Product of list: %d" % (multList(list)))
