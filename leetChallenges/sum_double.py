def sum_double(a, b):
    if int(a) == int(b):
        return 2*(a+2)
    else:
        return a+b


def diff21(n):
    if n <= 21:
        return 21-n
    else:
        return 2*(n-21)


def parrot_trouble(talking, hour):
    if talking == True:
        if hour < 7 or  hour > 20 :
            return True
        else:
            return False
    else:
        if hour < 7 or  hour >= 20 :
            return False
        else:
            return True


def makes10(a, b):
    if a ==10 or b == 10:
        return True
    elif a+b == 10:
        return True
    else:
        return False

def near_hundred(n):
    if abs(100 - n) <= 10 or abs(200-n) <= 10:
        print(abs(100) - n)
        return True
    else:
        return False

def pos_neg(a, b, negative):
    if negative == True:
        if a < 0 and b < 0:
            return True
        else:
            return False
    else:
        if a<0 and b<0:
            return False
        elif a>0 and b>0:
            return False
        else:
            return True


def not_string(str):
    s =str.split(" ")
    if len(s) == 1:
        if s[0] !="not":
            return "not " + str
        else:
            return str
    elif s[0]!="not":
        return "not "+str
    else:
        return str

def missing_char(str, n):
    retStrLis = list(str)
    retStrLis.pop(n)
    return "".join(retStrLis)

def front_back(str):
    strLis = list(str)
    fullLen=len(strLis)
    if fullLen>=2 and fullLen<=3:
        strLis.reverse()
        return "".join(strLis)
    elif fullLen>3:
        last = strLis[0]
        first = strLis[fullLen-1]
        strLis.pop(0)
        strLis.pop(fullLen-2)
        strLis.insert(0,first)
        strLis.insert(fullLen-1, last)
        return "".join(strLis)
    else:
        return str

def front3(str):
    strLen = len(str)
    if strLen>=3:
        return str[0:3]*3
    else:
        return str*3


print(front3("Java"))