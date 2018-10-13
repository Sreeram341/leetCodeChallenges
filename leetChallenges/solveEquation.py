class Solution:
    def solveEquation(self, equation):
        symb = ['+', '-', '*', '/']
        spliElem = equation.split('=')
        inSplitLis = []
        outerCntr = 0
        for i in spliElem:
            currStrLis = list(i)
            currStr=i
            cntr=0
            newCntr=0
            innerSplitLis = []
            newLis = []
            XDict = {"x": 0, "Num": 0}
            for j in currStrLis:
                newCntr += 1
                if j in symb:
                    innerSplitLis.append(currStr[cntr:newCntr-1])
                    cntr = newCntr
                    innerSplitLis.append(currStr[cntr-1])
            innerSplitLis.append(currStr[cntr:newCntr])
            strtCntr, endCntr = 0, 0

            for k in range(len(innerSplitLis)):
                if innerSplitLis[k] in symb:
                    if strtCntr == 0 and endCntr == 0:
                        strtCntr = k
                        endCntr = k
                    elif strtCntr > 0:
                        endCntr = k
                        s = "".join(innerSplitLis[strtCntr:endCntr])
                        newLis.append(s)
                        strtCntr = k
                elif strtCntr < 1:
                    s = "".join(innerSplitLis[:k+1])
                    newLis.append(s)
            else:
                if strtCntr > 0:
                    s = "".join(innerSplitLis[endCntr:len(innerSplitLis)])
                    newLis.append(s)

            for j in newLis:
                inLis = list(j)

                if 'x' in inLis:

                    if '-' in inLis:
                        try:
                            val = int("".join(inLis[1:len(inLis)-1]))
                            XDict["x"] -= val
                        except:
                            #val = int("".join(inLis[1:len(inLis)-1]))
                            XDict["x"] -= 1
                    elif '+' in inLis:
                        try:
                            val = int("".join(inLis[1:len(inLis)-1]))
                            XDict["x"] += val
                        except:
                            #val = int("".join(inLis[0:len(inLis) - 1]))
                            XDict["x"] += 1
                    else:
                        try:
                            if len(inLis) == 1:
                                XDict["x"] += 1
                            else:
                                val = int("".join(inLis[0:len(inLis)-1]))
                                XDict["x"] += val
                        except:
                            val = int("".join(inLis[0:len(inLis)-1]))
                            XDict["x"] += val
                else:
                    if '-' in inLis:
                        try:
                            val = int("".join(inLis[1:]))
                            XDict["Num"] -= val
                        except:
                            val = int(inLis[0])
                            XDict["Num"] -= val
                    elif '+' in inLis:
                        try:
                            val = int("".join(inLis[1:]))
                            XDict["Num"] += val
                        except:
                            val = int(inLis[0])
                            XDict["Num"] += val
                    else:
                        try:
                            val = int("".join(inLis[:]))
                            XDict["Num"] += val
                        except:
                            if len(inLis) > 0:
                                val = int(inLis[1])
                                XDict["Num"] -= val
            inSplitLis.insert(outerCntr, XDict)
            outerCntr += 1
        x1, Num1, x2, Num2 = inSplitLis[0].get("x"), inSplitLis[0].get("Num"), inSplitLis[1].get("x"), inSplitLis[1].get("Num")
        if x1-x2 ==0 and Num2-Num1 == 0:
            return "Infinite solutions"
        elif x1-x2 ==0 and Num2-Num1 != 0:
            return "No solution"
        elif x1 - x2 != 0 and Num2 - Num1 == 0:
            return "x=0"
        else:
            # print(x1, x2)
            # print(Num2, Num1)
            val = str(int((Num2 - Num1) / (x1 - x2)))
            return "x="+val


sol = Solution()

print(sol.solveEquation("2x=x"))
print(sol.solveEquation("x=x+2"))
print(sol.solveEquation("2x+3x-6x=x+2"))
print(sol.solveEquation("2x+3x-6x+1=2+x"))
print(sol.solveEquation("5x+5-3-2x=6+x-2"))
print(sol.solveEquation("x+5-3+x=6+x-2"))
print(sol.solveEquation("-x=-1"))
print(sol.solveEquation("3x=33+22+11"))
print(sol.solveEquation("99x=99"))
print(sol.solveEquation("x=x"))
