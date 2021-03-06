#I decided to challenge myself by making functions without using the actual operator characters,
#but I found that float cases were more work than I felt like doing right now. If I have time, I'll add those.

def add(a, b):
    if a > 0 and b > 0:
        for i in range(b):
            a += 1
        print(a)
    else:
        print(a + b)
    
def subtract(a, b):
    if a > 0 and b > 0:
        for i in range(b):
            a -= 1
    else:
        print(a - b)
        
def multiply(a, b):
    if b > 0:
        product = 0
        for i in range(b):
            product += a
        print(product)
    else:
        print(a * b)

def divide(a, b):
    if a < 0 and b < 0 or a < 0 and b > 0:
        a = 0 - a
        b = 0 - b
    quotient = 0
    if a >= 0 and b > 0:
        while True:
            a = a - b
            if a < 0:
                print(str(quotient) + ", remainder: " + str(a + b))
                break
            quotient += 1
    elif b == 0:
        print("Imagine that you have cookies, and you split them evenly among zero friends. How many cookies does each person get? See? It doesn't make sense. And Cookie Monster is sad that there are no cookies, and you are sad that you have no friends.")
    else:
        while True:
            a = a + b
            if a < 0:
                print(str(quotient) + ", remainder: " + str(0 - a + b))
                break
            quotient -= 1

#This function is quite confusing, but I'll try to explain the jist of it. This does not work for negative bases, but it does take negative exponents.
def power(a, b):
    exponential = a
    old_exponential = a
    count = 1
    if b > 0:
        while count < b:
            #You need to add a to itself 1 minus a times, and the value grows each time, so I added old_exponential instead of a.
            for i in range(a - 1):
                exponential += old_exponential
            old_exponential = exponential
            count += 1
        print(exponential)
    elif b == 0:
        print(1)
    elif b < 0:
        b = 0 - b
        while count < b:
            for i in range(a - 1):
                exponential += old_exponential
            old_exponential = exponential
            count += 1
        print("1 / " + str(exponential))


def calculator():
    print('Hello! Welcome to the Integer Calculator. Please only use integers.')
    while True:
        calc = input('Would you like to calculate something? Type "yes" or "no". ')
        if calc.lower() == 'no':
            break
        x = input('What is your first number? ')
        op = input('What operation would you like to perform? Type "add", "subtract, "multiply", "divide," or "power." ')
        y = input('What is your second number? ')
        if op.lower() == 'add':
            add(int(x), int(y))
        elif op.lower() == 'subtract':
            subtract(int(x), int(y))
        elif op.lower() == 'multiply':
            multiply(int(x), int(y))
        elif op.lower() == 'divide':
            divide(int(x), int(y))
        elif op.lower() == 'power':
            power(int(x), int(y))
        else:
            print('I\'m sorry, I didn\'t understand your request.')
            
calculator()