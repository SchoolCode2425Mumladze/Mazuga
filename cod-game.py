import turtle as t
import random as r
import time
import paint
t.bgcolor('grey')
t.speed(0)
t.ht()
kartohka=[]
figyres=['жёлтый квадрат','жёлтый треугольник','жёлтый круг','синий квадрат','синий круг','синий треугольник','красный круг','красный квадрат',"красный треугольник"]
while len(kartohka)<6:
    a=figyres[r.randint(0, len(figyres) - 1)]
    kartohka.append(a)
    figyres.pop(figyres.index(a))
print(kartohka)
i=0
while len(kartohka)>i:
    if kartohka[i]=="жёлтый квадрат":
        paint.kvadrat('yellow')
    if kartohka[i]=="красный квадрат":
        paint.kvadrat('red')
    if kartohka[i]=="синий квадрат":
        paint.kvadrat('blue')
    if kartohka[i]=="жёлтый треугольник":
        paint.treugolnik("yellow")
    if kartohka[i]=="синий треугольник":
        paint.treugolnik("blue")
    if kartohka[i]=="красный треугольник":
        paint.treugolnik("red")
    if kartohka[i]=="жёлтый круг":
        paint.krug("yellow")
    if kartohka[i]=="синий круг":
        paint.krug("blue")
    if kartohka[i]=="красный круг":
        paint.krug("red")
    i+=1
t.title("осталось 7")
time.sleep(1)
t.title("осталось 6")
time.sleep(1)
t.title("осталось 5")
time.sleep(1)
t.title("осталось 4")
time.sleep(1)
t.title("осталось 3")
time.sleep(1)
t.title("осталось 2")
time.sleep(1)
t.title("осталось 1")
time.sleep(1)
t.title("осталось 0")