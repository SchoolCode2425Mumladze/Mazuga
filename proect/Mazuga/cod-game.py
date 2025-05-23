import turtle as t
import random as r
import time
import paint
from voprose import zadaha
t.bgcolor('grey')
t.speed(0)
t.ht()
kartohka=[]
cx = [-250,0,250,-250,0,250]
cy = [250,250,250,-250,-250,-250]
figyres=['жёлтый квадрат','жёлтый треугольник','жёлтый круг','синий квадрат','синий круг','синий треугольник','красный круг','красный квадрат',"красный треугольник"]
while len(kartohka)<6:
    a=figyres[r.randint(0, len(figyres) - 1)]
    kartohka.append(a)
    figyres.pop(figyres.index(a))
print(kartohka)
b = 0
tipe=[]
i=0
while len(kartohka)>i:
    t.penup()
    t.goto(cx[b],cy[b])
    t.pendown()

    if kartohka[i]=="жёлтый квадрат":
        tipe.append("квадрат")
        paint.kvadrat('yellow')
    if kartohka[i]=="красный квадрат":
        tipe.append("квадрат")
        paint.kvadrat('red')
    if kartohka[i]=="синий квадрат":
        tipe.append("квадрат")
        paint.kvadrat('blue')
    if kartohka[i]=="жёлтый треугольник":
        tipe.append("треугольник")
        paint.treugolnik("yellow")
    if kartohka[i]=="синий треугольник":
        tipe.append("треугольник")
        paint.treugolnik("blue")
    if kartohka[i]=="красный треугольник":
        tipe.append("треугольник")
        paint.treugolnik("red")
    if kartohka[i]=="жёлтый круг":
        tipe.append("круг")
        paint.krug("yellow")
    if kartohka[i]=="синий круг":
        tipe.append("круг")
        paint.krug("blue")
    if kartohka[i]=="красный круг":
        tipe.append("круг")
        paint.krug("red")
    i+=1
    t.write(b+1, font=('Arial', 50, 'normal'))
    b += 1
print(tipe)
# t.title("осталось 7")
# time.sleep(1)
# t.title("осталось 6")
# time.sleep(1)
# t.title("осталось 5")
# time.sleep(1)
# t.title("осталось 4")
# time.sleep(1)
t.title("осталось 3")
time.sleep(1)
t.title("осталось 2")
time.sleep(1)
t.title("осталось 1")
time.sleep(1)
t.title("осталось 0")
t.clear()
zadaha()