def zero(func=0): #your code here
    if func == 0:
        return 0
    else:
        if func[0] == "*":
            return 0
        elif func[0] == "+":
            return int(func[1:])
        elif func[0] == "-":
            return int(func[1:])
        else:
            return 0
def one(func=0): #your code here
    if func == 0:
        return 1
    else:
        if func[0] == "*":
            return 1*int(func[1:])
        elif func[0] == "+":
            return 1+int(func[1:])
        elif func[0] == "-":
            return 1-int(func[1:])
        else:
            return 1//int(func[1:])
def two(func =0): #your code here
    if func == 0:
        return 2
    else:
        if func[0] == "*":
            return 2*int(func[1:])
        elif func[0] == "+":
            return 2+int(func[1:])
        elif func[0] == "-":
            return 2-int(func[1:])
        else:
            return 2//int(func[1:])
def three(func=0): #your code here
    if func == 0:
        return 3
    else:
        if func[0] == "*":
            return 3*int(func[1:])
        elif func[0] == "+":
            return 3+int(func[1:])
        elif func[0] == "-":
            return 3-int(func[1:])
        else:
            return 3//int(func[1:])
def four(func=0): #your code here
    if func == 0:
        return 4
    else:
        if func[0] == "*":
            return 4*int(func[1:])
        elif func[0] == "+":
            return 4+int(func[1:])
        elif func[0] == "-":
            return 4-int(func[1:])
        else:
            return 4//int(func[1:])
def five(func=0): #your code here
    if func == 0:
        return 5
    else:
        if func[0] == "*":
            return 5*int(func[1:])
        elif func[0] == "+":
            return 5+int(func[1:])
        elif func[0] == "-":
            return 5-int(func[1:])
        else:
            return 5//int(func[1:])
def six(func=0): #your code here
    if func == 0:
        return 6
    else:
        if func[0] == "*":
            return 6*int(func[1:])
        elif func[0] == "+":
            return 6+int(func[1:])
        elif func[0] == "-":
            return 6-int(func[1:])
        else:
            return 6//int(func[1:])
def seven(func=0): #your code here
    if func == 0:
        return 7
    else:
        if func[0] == "*":
            return 7*int(func[1:])
        elif func[0] == "+":
            return 7+int(func[1:])
        elif func[0] == "-":
            return 7-int(func[1:])
        else:
            return 7//int(func[1:])
def eight(func=0): #your code here
    if func == 0:
        return 8
    else:
        if func[0] == "*":
            return 8*int(func[1:])
        elif func[0] == "+":
            return 8+int(func[1:])
        elif func[0] == "-":
            return 8-int(func[1:])
        else:
            return 8//int(func[1:])
def nine(func=0): #your code here
    if func == 0:
        return 9
    else:
        if func[0] == "*":
            return 9*int(func[1:])
        elif func[0] == "+":
            return 9+int(func[1:])
        elif func[0] == "-":
            return 9-int(func[1:])
        else:
            return 9//int(func[1:])

def plus(f): #your code here
    return "+" + str(f)
def minus(f): #your code here
    return "-" + str(f)
def times(f): #your code here
    return "*"+str(f)
def divided_by(f): #your code here
    return "/"+str(f)

print(seven(plus(five(times(five())))))
print(four(plus(nine())))
print(eight(minus(three())))
print(six(divided_by(two())))