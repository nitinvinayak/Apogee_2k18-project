#HANGMAN
#By Nitin
import random

def low(n):
    m=n.lower()
    return m
t=0
import turtle
turtle.bgcolor("light blue")
turtle.pu()
turtle.bk(200)
turtle.lt(90)
turtle.fd(150)
turtle.lt(90)
turtle.fd(50)
turtle.rt(90)
turtle.fd(50)
turtle.pd()
turtle.pencolor("black")
turtle.fd(20)
turtle.rt(90)
turtle.fd(100)
turtle.rt(90)
turtle.fd(400)
turtle.rt(90)
turtle.fd(170)
turtle.bk(340)
turtle.pu()
turtle.home()
turtle.pd()
def head():
    turtle.pu()
    turtle.bk(200)
    turtle.lt(90)
    turtle.fd(150)
    turtle.pd()
    turtle.pencolor("black")
    turtle.pensize(10)
    turtle.circle(50)
    turtle.pu()
    turtle.home()
    turtle.pd()
    
def body():
    turtle.pu()
    turtle.bk(200)
    turtle.lt(90)
    turtle.fd(150)
    turtle.lt(90)
    turtle.fd(50)
    turtle.lt(90)
    turtle.fd(50)
    turtle.pd()
    turtle.pencolor("blue")
    turtle.pensize(10)
    turtle.fd(150)
    turtle.pu()
    turtle.home()
    turtle.pd()
def hand1():
    turtle.pu()
    turtle.bk(200)
    turtle.lt(90)
    turtle.fd(150)
    turtle.lt(90)
    turtle.fd(50)
    turtle.lt(90)
    turtle.fd(125)
    turtle.lt(135)
    turtle.pd()
    turtle.pensize(10)
    turtle.pencolor("red")
    turtle.fd(100)
    turtle.pu()
    turtle.home()
    turtle.pd()
def hand2():
    turtle.pu()
    turtle.bk(200)
    turtle.lt(90)
    turtle.fd(150)
    turtle.lt(90)
    turtle.fd(50)
    turtle.lt(90)
    turtle.fd(125)
    turtle.rt(135)
    turtle.pd()
    turtle.pensize(10)
    turtle.pencolor("red")
    turtle.fd(100)
    turtle.pu()
    turtle.home()
    turtle.pd()
def leg1():
    turtle.pu()
    turtle.bk(200)
    turtle.lt(90)
    turtle.fd(150)
    turtle.lt(90)
    turtle.fd(50)
    turtle.lt(90)
    turtle.fd(50)
    turtle.pd()
    turtle.fd(150)
    turtle.lt(45)
    turtle.pensize(10)
    turtle.pencolor("red")
    turtle.fd(100)
    turtle.pu()
    turtle.home()
    turtle.pd()
def leg2():
    turtle.pu()
    turtle.bk(200)
    turtle.lt(90)
    turtle.fd(150)
    turtle.lt(90)
    turtle.fd(50)
    turtle.lt(90)
    turtle.fd(50)
    turtle.pd()
    turtle.pensize(10)
    turtle.pencolor("red")
    turtle.fd(150)
    turtle.rt(45)
    turtle.fd(100)
    turtle.pu()
    turtle.home()
#dictionary containing all the names of movies
aa={1:['superman'],2:['batman'],3:['spiderman'],4:['hulk'],5:["wolverine"],6:["xmen"],7:["thor"],8:["antman"],9:["krrish"],10:["aquaman"],11:["deadpool"],12:["flash"],13:["watchmen"],14:["daredevil"],15:["hellboy"],16:["superwoman"]}
bb={1:["dilwale"],2:["raone"],3:["don"],4:["raees"],5:["fan"],6:["baazigar"],7:["darr"],8:["pardes"],9:["baadshah"],10:["devdas"],11:["swades"],12:["bhoothnath"],13:["billu"],14:["ashoka"],15:["mohabbatein"]}
cc={1:["kick"],2:["veer"],3:["sultan"],4:['dabangg'],5:["ready"],6:["partner"],7:["bodyguard"],8:["wanted"],9:["hello"],10:["yuvvraaj"],11:["saawariya"],12:["baghban"]}
dd={1:['pk'],2:["dangal"],3:["ghajini"],4:["dhoom3"],5:["lagaan"],6:["talaash"],7:["fanaa"],8:["3idiots"]}
ee={1:["airlift"],2:["baby"],3:["robot2"],4:["holiday"],5:["khiladi"],6:["gabbar"],7:["shaukeens"],8:["housefull3"],9:['brothers'],10:["boss"],11:["joker"],12:["omg"],13:["blue"],14:["tashan"],15:["welcome"],16:["waqt"],17:["khakee"],18:["special26"]}
name=raw_input("ENTER YOUR NAME: ")
print "SUPERHERO MOVIE -      aa"
print "SRK's MOVIE -          bb"
print "SALMAN KHAN's MOVIE -  cc"
print "AAMIR KHAN's MOVIE -   dd"
print "AKSHAY KUMAR's MOVIE - ee"
choose=raw_input("ENTER YOUR CHOICE: ")
c=low(choose)
if c=="aa":
    c=aa
elif c=="bb":
    c=bb
elif c=="cc":
    c=cc
elif c=="dd":
    c=dd
elif c=="ee":
    c=ee    
else:
    print "PLEASE ENTER THE RIGHT KEYWORD"
n=len(c)
k=0
w=c[random.randint(1,n)]
print "HINT:",len(w[0]),"- LETTER WORD"
turtle.begin_fill()
for i in range(0,100):
    f=0
    S=raw_input("ENTER THE LETTER:")
    s=low(S)
    for j in range(len(w[0])):
        if s==w[0][j]:
            turtle.pensize(1)
            turtle.pencolor("black")
            turtle.home()
            turtle.fd(j*20)
            turtle.write(s,font=("Arial",15,"normal"))
            f=100
            k=k+1
            turtle.home()
    
        
    if f==0:
        if t==0:
            head()
            t=1
        elif t==1:
            body()
            t=2
        elif t==2:
            hand1()
            t=3
        elif t==3:
            hand2()
            t=4
        elif t==4:
            leg1()
            t=5
        elif t==5:
            leg2()
            t=6
        
    if k==len(w[0]):
        print name.upper(),"YOU WIN !!!!"
        break
    if t==6:
        print name.upper(),"YOU LOSE....","WORD IS",w
        break
    









