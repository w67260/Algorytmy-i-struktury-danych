#DO DOKONCZENIA

from Zadanie1 import Stack
def parChecker(symobolString):
    s=Stack()
    balanced=True
    index=0
    while index<len(symobolString) and balanced:
        symobol=symobolString[index]
        if symobol=="(":
            s.push(symobol)
        else:
            if s.isEmpty():
                balanced=False
            else:
                s.pop()
        index+=1
    if balanced and s.isEmpty():
        return True
    else:
        return False

print(parChecker('((()))'))
print(parChecker('((())'))
print(parChecker('(())(())'))