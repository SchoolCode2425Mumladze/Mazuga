import random as r
import turtle as t
voprosis=[]
voprosis_nomber=["Где был жёлтый квадрат?","Где был синий квадрат?","Где был красный квадрат?","Где был жёлтый треугольник?","Где был синий треугольник","Где был красный треугольник?","Где был жёлтый круг?","Где был синий круг?","Где был красный круг?"]
voprosis_color=["какого цвета фигура номер один?","какого цвета фигура номер два?","какого цвета фигура номер три?","какого цвета фигура номер четыре?","какого цвета фигура номер пять?","какого цвета фигура номер шесть?"]
voprosis_tape=["какая фигура номер один?","какая фигура номер два?","какая фигура номер три?","какая фигура номер четыре?","какая фигура номер пять?","какая фигура номер шесть?"]
a=''
while len(voprosis)<10:
    var=r.randint(1,3)
    if var==1:
        b = len(voprosis_color)-1
        if len(voprosis_color) <= 2:
            a = voprosis_color[0]
        else:
            q = r.randint(1,b)
            a=voprosis_color[q]
            voprosis.append(a)
        voprosis_color.pop(voprosis_color.index(a))
    elif var==2:
        b = len(voprosis_nomber)-1
        if len(voprosis_nomber) <= 2:
            a = voprosis_nomber[0]
        else:
            q = r.randint(1,b)
            a=voprosis_nomber[q]
            voprosis.append(a)
        voprosis_nomber.pop(voprosis_nomber.index(a))
    else:
        b = len(voprosis_tape) - 1
        if len(voprosis_tape) <= 2:
            a = voprosis_tape[0]
        else:
            q = r.randint(1, b)
            a = voprosis_tape[q]
            voprosis.append(a)
        voprosis_tape.pop(voprosis_tape.index(a))