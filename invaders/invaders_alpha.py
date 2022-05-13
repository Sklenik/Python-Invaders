#potrebne moduly
import turtle
import math
import winsound

#globalni promenne
vystreleno = 'ne'
skore = 0
rychlost_invaderu = 0.05
invader_mrtvej = 0
invader_sprite = 0

def PythonInvaders():
    
    #promenne
    '''
    Dokud sem nevytvoril funkci pro restart, vsecko fungovalo skvele,
    ale ted musim nevim proc presunout tyto promenne mimo kod,
    a pak je deklarovat jako globalni, aby kod fungoval jak ma.
    Zvlastni ale nestezuju si.
    '''

    global vystreleno
    global skore
    global rychlost_invaderu
    global invader_mrtvej
    global invader_sprite

    #nastaveni okynka

    wn = turtle.Screen()
    wn.setup(width = 600,height = 600)
    wn.bgcolor('black')
    wn.title('Python Invaders')
    wn.tracer(0)                    #VELMI citlive

    #import ikonek
    turtle.register_shape("Sprites/Hrac/Laser_Cannon.gif")
    turtle.register_shape("Sprites/Invader1/Invader1.gif")
    turtle.register_shape("Sprites/Invader2/Invader2.gif")
    turtle.register_shape("Sprites/Invader3/Invader3.gif")

    #hrac
    hrac = turtle.Turtle()
    hrac.shape("Sprites/Hrac/Laser_Cannon.gif")
    hrac.up()
    hrac.speed(0)
    hrac.setposition(0, -250)

    #ovladani hrace

    def doleva():
        x = hrac.xcor()-15
        hrac.setx(x)
        if x < - 270:
            hrac.setpos(-270,-250)

    def doprava():
        x = hrac.xcor()+15
        hrac.setx(x)
        if x > 270:  
            hrac.setpos(270,-250)


    #nastaveni a mechanika strileni, zbytek je v hlavnim while cyklu
    vystrel = turtle.Turtle()
    vystrel.color('white')
    vystrel.shape('square')
    vystrel.shapesize(.25,.75)
    vystrel.up()
    vystrel.speed(0)
    vystrel.setposition(0,-300)
    vystrel.setheading(90)
    vystrel.hideturtle()

    def vystrelit():
        global vystreleno
        if vystreleno == 'ne':
            winsound.PlaySound("Sound/laser.wav", winsound.SND_ASYNC)
            vystreleno = 'ano'
            x = hrac.xcor()
            y = hrac.ycor()
            vystrel.setposition(x,y+15)
            vystrel.showturtle()


    #Invaders - tohle dalo hodne prace
    invaders = []
    pocet = 40


    for i in range(pocet):
        invaders.append(turtle.Turtle())

    cislo_invadera = 0
    invaderX = -250
    invaderY = 200

    for invader in invaders:
        invader.shape("Sprites/Invader2/Invader2.gif")
        invader.penup()
        invader.speed(0)

        x = invaderX + 51 * (cislo_invadera%10)
        y = invaderY - 40 * int(cislo_invadera/10)
        invader.setposition(x,y)
        cislo_invadera += 1
        invader_sprite +=1
        if cislo_invadera == 10:
            invaderY -= 50
            cislo_invadera = 0
    
    
        if 10 < invader_sprite <31:
                invader.shape("Sprites/Invader1/Invader1.gif")
        if 30 < invader_sprite <=40:
                invader.shape("Sprites/Invader3/Invader3.gif")

    #pocitadlo
    pocitadlo = turtle.Turtle()
    pocitadlo.color('white')
    pocitadlo.speed(0)
    pocitadlo.penup()
    pocitadlo.setposition(-290,280)
    pocitadlo.write('Score: {}'.format(skore),False, align='left')
    pocitadlo.hideturtle()


    #bum1
    bum1 = turtle.Turtle()
    bum1.shape('circle')
    bum1.color('white')
    bum1.up()
    bum1.speed(0)
    bum1.hideturtle()

    #bum2
    bum2 = turtle.Turtle()
    bum2.shape('circle')
    bum2.color('white')
    bum2.shapesize(1.5)
    bum2.up()
    bum2.speed(0)
    bum2.hideturtle()

    #kolize
    '''
    Asi tyden sem si lamal hlavu s tim proc moje funkce na kolizi nefunguji,
    nakonec sem se rozhodl vygooglit reseni protoze sem nechtel ztracet cas vymyslenim neceho,
    co nefunguje a ja nevim proc.
    '''

    def kolize(objekt1,objekt2):
        vzdalenost = math.sqrt(math.pow(objekt1.xcor()-objekt2.xcor(),2)+math.pow(objekt1.ycor()-objekt2.ycor(),2))
        if vzdalenost < 25 :
            return True
        else:
            return False

    #vypinani a restartovani hry
    def vypnout():
        turtle.bye()

    def restart():
        global skore
        skore = 0
        global invader_mrtvej
        invader_mrtvej = 0
        global rychlost_invaderu
        rychlost_invaderu = 0.05
        global invader_sprite
        invader_sprite = 0
        wn.clearscreen()
        PythonInvaders()

    wn.listen()
    wn.onkey(vypnout,'Escape')
    wn.onkey(restart, 'r')

    #vitezstvi

    def win():
        wn.clear()
        wn.bgcolor('black')
        win = turtle.Turtle()
        win.color('white')
        win.speed(0)
        win.penup()
        win.hideturtle()
        win.setposition(0,0)
        win.write('Vyhral jsi!',False, align='center')
        win.setposition(0,-30)
        win.write('Tve skore: {}'.format(skore),False, align='center')
        win.setposition(0,-60)
        win.write('(stiskni "Esc" pro ukonceni)',False, align='center')
        win.setposition(0,-90)
        win.write('Chces si zahrat jeste jednou? Stiskni R pro novou hru!',False, align='center')
        
        wn.listen()
        wn.onkey(vypnout,'Escape')
        wn.onkey(restart, 'r')

        turtle.mainloop()

    #prohra

    def fail():
        wn.clear()
        wn.bgcolor('black')
        fail = turtle.Turtle()
        fail.color('white')
        fail.speed(0)
        fail.penup()
        fail.hideturtle()
        fail.setposition(0,120)
        fail.write('Ale ne! Mimozemstani se dostali na zem!',False, align='center')
        fail.setposition(0,90)
        fail.write('Nedal jsi se ale bez boje! Tve skore je: {}'.format(skore),False, align='center')
        fail.setposition(0,60)
        fail.write('Neni vsak vse ztraceno! Zrestartuj hru stisktnutim R a poradne jim to nandej :D!',False, align='center')
        fail.setposition(0,30)
        fail.write('Pokud si prejes hru ukoncit, stiskni Esc',False, align='center')
        
        wn.listen()
        wn.onkey(vypnout,'Escape')
        wn.onkey(restart, 'r')

        turtle.mainloop()


    #ovladani
    turtle.listen()
    turtle.onkey(doleva,'Left')
    turtle.onkeypress(doleva,'Left')
    turtle.onkey(doprava,'Right')
    turtle.onkeypress(doprava,'Right')
    turtle.onkey(vystrelit,'space')


    #exploze        #nefunkcni a vyrazene z provozu
    def exploze(x):
        bum1.setposition(x,250)
        bum1.showturtle()

    #cara
    cara = turtle.Turtle()
    cara.shape('square')
    cara.color('white')
    cara.shapesize(.3,29)
    cara.penup()
    cara.setposition(0,-200)

    #loop

    while True:
        wn.update()

        if invader_mrtvej == pocet:
            win()
            break

        for invader in invaders:
            invx = invader.xcor()
            invx += rychlost_invaderu
            invader.setx(invx)
            
            if invader.xcor() >= 260:
                for inv in invaders:
                    invy = inv.ycor()
                    invy -= 50
                    inv.sety(invy)
                rychlost_invaderu *= -1.2

            if invader.xcor() <= -260:
                for inv in invaders:
                    invy = inv.ycor()
                    invy -= 50
                    inv.sety(invy)
                rychlost_invaderu *= -1.2

            if kolize(invader,vystrel):
                vystrel.speed(0)
                vystrel.hideturtle()
                vystrel.setposition(0,-250)
                vystreleno = 'ne'
                winsound.PlaySound("Sound/velkybum.wav", winsound.SND_ASYNC)
                invader.hideturtle()
                invader.speed(0)
                invader.setposition(0,-300)
                skore += 10
                pocitadlo.clear()
                pocitadlo.write('Score: {}'.format(skore),False, align='left')
                invader_mrtvej += 1

            if invader.ycor() == -200:
                fail()
                break

            
            '''
            ################################################################################
            Pod timto komentarem lezi zakomentovany kod mnou vytvoreny pro detekci kolize.
            Fungoval do chvile, nez sem zavedl vice invaderu jako seznam.
            Pak i po predelani odmital fungovat podle mych predstav, proto byl
            v ramci uspory casu a nervu, nahrazen.
            ################################################################################


            if abs(vystrel.xcor() - invader.xcor()) < 20 and abs(vystrel.ycor() - invader.ycor()) < 20:
                vystrel.speed(0)
                vystrel.hideturtle()
                vx = vystrel.xcor()
                vystreleno = 'ne'
                invader.hideturtle()
                invader.speed(0)
                invader.setposition(0,-300)
                skore += 10
                pocitadlo.clear()
                pocitadlo.write('Score: {}'.format(skore),False, align='left')
                
            '''

        if vystreleno == 'ano':
            vy = vystrel.ycor()
            vy += 2
            vystrel.sety(vy)
            
            if vystrel.ycor() == 250:
                vystrel.speed(0)
                winsound.PlaySound("Sound/malybum.wav", winsound.SND_ASYNC)
                vystrel.hideturtle()
                vystrel.setposition(0,-250)
                #vx = vystrel.xcor()
                #bum1.setposition(vx,250)       #stary kod na zobrazovani animace pro vybuch,
                #bum1.showturtle()              #ktery se rozbil kdyz sem zavedl wn.update().
                #bum1.hideturtle()
                #exploze(vx)
                vystreleno = 'ne'

PythonInvaders()