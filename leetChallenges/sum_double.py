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
    if abs(100) - n <=10 or abs(200-n)<=10:
        return True
    else:
        return False

print(near_hundred(111))