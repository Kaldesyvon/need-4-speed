import tkinter, random
canvas=tkinter.Canvas(height=500,width=1920,bg="lightgray")
canvas.pack()
z=[]
ciel=[]
p=[0]*15
i=0
finish=["black","white"]
a=1890
b=1
u=1
o=0
for i in range(100):
    canvas.create_rectangle(a,b,a+10,b+10,fill=finish[u])
    u,o=o,u
    canvas.create_rectangle(a+10,b,a+20,b+10,fill=finish[u])
    b+=10
del u,o,a,b,finish
i=0
x=0
y=40
for i in range(15):
    canvas.create_line(x+23,y-3,x+30,y-3,x+30,y+18,x+23,y+18)
    y+=30
i=0
while i!=15:
    cislo=random.randint(0,99)
    if cislo not in z:
        z.append(cislo)
        i+=1
def auto():
    x=0
    y=40
    for i in range(15):
        f=random.choice(("red","white","pink","lime","yellow","magenta","gray","tan","tomato","orange","mediumspringgreen","dodgerblue","azure","khaki","crimson","lightblue","gold","goldenrod","skyblue","aqua","royalblue","steelblue","sandybrown","lightcoral"))
        canvas.create_polygon(x,y+15,x,y+8,x+5,y+8,x+8,y,x+17,y,x+20,y+8,x+25,y+8,x+25,y+15,tag="auta",outline="black",fill=f)
        canvas.create_text(x+12,y+8,text=z[i],tag="pismo")
        y+=30
    auta=canvas.find_withtag("auta")
    pismo=canvas.find_withtag("pismo")
    i=0
    poradie_auticka=0
    poradie_textu=0
    while len(ciel)!=15:
        canvas.update()
        pohyb=random.randint(5,10)
        if p[i]>1890:
            pohyb=0
        canvas.move(auta[poradie_auticka],pohyb,0)
        canvas.move(pismo[poradie_textu],pohyb,0)
        while i!=15:
            p[i]=int(p[i])+pohyb
            if p[i]>1890 and z[i] not in ciel:
                ciel.append(z[i])
                if i==14:
                    i=0
                    poradie_auticka=0
                    poradie_textu=0
                poradie_auticka+=1
                poradie_textu+=1
                i+=1
                break
            elif i==14:
                i=0
                poradie_auticka=0
                poradie_textu=0
                break
            else:
                i=i+1
                poradie_auticka+=1
                poradie_textu+=1
                break
        canvas.after(1)
    print(ciel)
auto()
