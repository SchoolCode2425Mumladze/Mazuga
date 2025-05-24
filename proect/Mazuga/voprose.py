import random as r
import time
import turtle as t
from codgame import tipe
voprosis=[]
index=[]
voprosis_tape=["какой формы фигура номер один?","какой формы фигура номер два?","какой формы фигура номер три?","какой формы фигура номер четыре?","какой формы фигура номер пять?","какой формы фигура номер шесть?"]
index_tipe=[0,1,2,3,4,5]
a=''
def zadaha():
    while len(voprosis)<4:
        q = r.randint(1, len(voprosis_tape)-1)
        a = voprosis_tape[q]
        voprosis.append(a)
        voprosis_tape.pop(voprosis_tape.index(a))
    print(voprosis)
    for u in voprosis:
        if u=="какой формы фигура номер один?":
            index.append(0)
        if u=="какой формы фигура номер два?":
            index.append(1)
        if u=="какой формы фигура номер три?":
            index.append(2)
        if u=="какой формы фигура номер четыре?":
            index.append(3)
        if u=="какой формы фигура номер пять?":
            index.append(4)
        if u=="какой формы фигура номер шесть?":
            index.append(5)
    print(index)
def otvet():
    def onKey1():
        a="квадрат"

    def onKey2():
        a="треуольник"

    def onKey3():
        a="круг"

    screen = t.Screen()
    screen.onkey(onKey1, "1")
    screen.listen()

    screen = t.Screen()
    screen.onkey(onKey2, "2")
    screen.listen()

    screen = t.Screen()
    screen.onkey(onKey3, "3")
    screen.listen()
for i in range(4):
    if a==tipe[index]:
        print(1)
