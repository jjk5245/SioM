
def getInput(x,y):
    x = input("Enter a number")
    y = input("Enter a number")
    return x,y

def add(x,y):
    return x + y

def printNums(t):
    print(t)

t = 0
m = 0
n = 0

m,n = getInput(m,n)

t = add(m,n)

printNums(t)
