#1:

def func(string):
    print(string[:8])
    print(string[-6:])
    print(string[::3])
    print(string[:len(string)//4])
    print(string.upper())
    print(string[::-1])

#2:

def lettersCount(string):
    count = {}
    for char in string:
        if char not in count:
            count[char] = 1
        else:
            count[char]+=1
    return count

#3:

def newString(string):
    if len(string) < 2:
        return ""
    else:
        return string[:2] + string[-2:]
    
#4:

def first_middle_last(string):
    if len(string) < 3:
        pass
    else:
        middle = len(string) // 2
        print(string[0] + string[middle] + string[-1])
        print(string[(len(string)//2)-1]+string[len(string)//2]+string[(len(string)//2)+1])

#5:

def term(n):
    term = 2
    sum = 0
    for i in range(n):
        sum += term
        term = term * 10 + 2
    return term

#6:

def remove(list):
    num = [0, 4, 5]
    new_list = []

    for i in range(len(list)):
        if i not in num:
            new_list.append(list[i])

    print(new_list)

#7:
def containsA(list):
    new_list = []
    for item in list:
        if "a" in item:
            new_list.append(item) 
    return new_list

#9:
def fibonacci(n):
    sequence = [0, 1]
    for i in range(2, n):
        term = sequence[i-1] + sequence[i-2]
        sequence.append(term)
    return sequence

#10:
def sqrDic():
    squares = {}
    for i in range(1, 16):
        squares[i] = i**2

    print(squares) 

sqrDic()
    
    

