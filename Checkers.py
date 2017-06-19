from tkinter import *
from time import sleep
from tkinter import messagebox
from random import randint
import winsound
import os
import pickle


#Pantalla Inicio
ventana= Tk()
ventana.title("Checkers")
ventana.geometry("900x660+250+80")
ventana.wm_iconbitmap("iconoprueba.ico")
ventana.resizable(width=False, height=False)
ventana.protocol("WM_DELETE_WINDOW", "onexit")


#Pantalla Jugadores
jugadores=Toplevel(ventana)
jugadores.title("Jugadores")    
jugadores.geometry("900x660+250+80")
jugadores.wm_iconbitmap("iconoprueba.ico")
jugadores.resizable(width=False, height=False)
jugadores.protocol("WM_DELETE_WINDOW", "onexit")
jugadores.iconify()


#Pantalla Juego
juego=Toplevel(ventana)
juego.title("Damas Españolas")
juego.geometry("900x660+250+80")
juego.wm_iconbitmap("iconoprueba.ico")
juego.resizable(width=False, height=False)
juego.protocol("WM_DELETE_WINDOW", "onexit")
p1=Label(juego, bg="DeepSkyBlue3", width=100, height=50) .place(x=50,y=50)
p2=Label(juego, bg="DeepSkyBlue3",width=100, height=50) .place(x=50,y=50)
juego.iconify()

#Pantalla Ajustes
ajustes=Toplevel(ventana)
ajustes.title("Damas Españolas")
ajustes.geometry("900x660+250+80")
ajustes.wm_iconbitmap("iconoprueba.ico")
ajustes.resizable(width=False, height=False)
ajustes.protocol("WM_DELETE_WINDOW", "onexit")
ajustes.iconify()

#Pantalla Acerca De
acercade=Toplevel(ventana)
acercade.title("Damas Españolas")
acercade.geometry("900x660+250+80")
acercade.wm_iconbitmap("iconoprueba.ico")
acercade.resizable(width=False, height=False)
acercade.protocol("WM_DELETE_WINDOW", "onexit")
acercade.configure(bg="DeepSkyBlue3")
acercade.iconify()

#Definicion de imagenes
bsalir=PhotoImage(file="salir.png")
play_img=PhotoImage(file="play-icon.gif")
ajustes_img=PhotoImage(file="settings.png")
acerca_img=PhotoImage(file="acerca.png")
ayuda_img=PhotoImage(file="ayuda.png")
vuelta_img=PhotoImage(file="vuelta.png")
listo_img=PhotoImage(file="listo.png")
check_img=PhotoImage(file="check.png")


#Imagenes de dados
dadoi=PhotoImage(file="dados-inicial.png")
dadot=PhotoImage(file="dados_tira.png")
dado_1=PhotoImage(file="dado1.png")
dado_2=PhotoImage(file="dado2.png")
dado3=PhotoImage(file="dado3.png")
dado4=PhotoImage(file="dado4.png")
dado5=PhotoImage(file="dado5.png")
dado6=PhotoImage(file="dado6.png")


#sonido
#Funciones
tablero=[]

color1="ivory"
color2="brown"
ficha1="black"
ficha2="blue"

def verifica_tablero():
    global tablero
    global turno_jugador
    for i in range(len(tablero)):
        
        for j in range(len(tablero[i])):
            if turno_jugador==1:
                if tablero[i][j]=="J2":
                    return False
            if turno_jugador==2:
                if tablero[i][j]=="J1":
                    return False
    return True

def movimiento_reina(x1,y1,x2,y2,j):
    global tablero
    if abs(x1-x2)==abs(y1-y2):
        tablero[y1][x1]=0
        tablero[y2][x2]=j
    return tablero

def comida_reina_j1(x1,y1,x2,y2):
    global tablero
    if y2>y1:
        dir1="N"
    if y1>y2:
        dir1="S"
    if x2>x1:
        dir2="E"
    if x1>x2:
        dir2="O"
    contador=0
    diferencia=abs(x1-x2)
    if dir1=="N" and dir2=="E":
        for i in range(1,diferencia):
            if y2+1>=0 and x2-i<=7:
                if tablero[y2+1][x2-i]=="J2" or tablero[y2+1][x2-i]=="J2r":
                    tablero[y2+1][x2-i]=0
    if dir1=="N" and dir2=="O":
        for i in range(1,diferencia):
            if y2+1>=0 and x2+i<=7:
                if tablero[y2+1][x2+i]=="J2" or tablero[y2+1][x2+i]=="J2r":
                    tablero[y2+1][x2+i]=0
    if dir1=="S" and dir2=="E":
        for i in range(1,diferencia):
            if y2-1>=0 and x2-i<=7:
                if tablero[y2-1][x2-i]=="J2" or tablero[y2-1][x2-i]=="J2r":
                    tablero[y2-1][x2-i]=0
    if dir1=="S" and dir2=="O":
        for i in range(1,diferencia):
            if y2-1>=0 and x2+i<=7:
                if tablero[y2-1][x2+i]=="J2" or tablero[y2-1][x2+i]=="J2r":
                    tablero[y2-1][x2+i]=0
    return tablero

def comida_reina_j2(x1,y1,x2,y2):
    global tablero
    if y2>y1:
        dir1="N"
    if y1>y2:
        dir1="S"
    if x2>x1:
        dir2="E"
    if x1>x2:
        dir2="O"
    contador=0
    diferencia=abs(x1-x2)
    if dir1=="N" and dir2=="E":
        for i in range(1,diferencia):
            if 7>=y2+i>=0 and 0<=x2-i<=7:
                if tablero[y2+i][x2-i]=="J1" or tablero[y2+i][x2-i]=="J1r":
                    tablero[y2+i][x2-i]=0
    if dir1=="N" and dir2=="O":
        for i in range(1,diferencia):
            if 7>=y2+i>=0 and 0<=x2+i<=7:
                if tablero[y2+i][x2+i]=="J1" or tablero[y2+i][x2+i]=="J1r":
                    tablero[y2+i][x2+i]=0
    if dir1=="S" and dir2=="E":
        for i in range(1,diferencia):
            if 7>=y2-i>=0 and 0<=x2-i<=7:
                if tablero[y2-i][x2-i]=="J1" or tablero[y2-i][x2-i]=="J1r":
                    tablero[y2-i][x2-i]=0
    if dir1=="S" and dir2=="O":
        for i in range(1,diferencia):
            if 7>=y2-i>=0 and 0<=x2+i<=7:
                if tablero[y2-i][x2+i]=="J1" or tablero[y2-i][x2+i]=="J1r":
                    tablero[y2-i][x2+i]=0
    return tablero




    
def valida_movimiento(posc_ant,posc_actual):
    global p2
    global p1
    #las posiciones tienen valores x,y(columna,fila)en una lista
    global turno_jugador
    x1=posc_ant[0]
    y1=posc_ant[1]
    x2=posc_actual[0]
    y2=posc_actual[1]
    global tablero
    tablero1=tablero
    if tablero1[y2][x2]=="X" or tablero1[y2][x2]=="J1" or tablero1[y2][x2]=="J2" or tablero1[y1][x1]=="X" or tablero1[y1][x1]==0:
        return False
    if tablero1[y1][x1]=="J1":
        if y1<=y2:
            return False
        
    if tablero1[y1][x1]=="J2":
        if y1>=y2: 
            return False

    if turno_jugador==1:
        if tablero[y1][x1]=="J2":
            messagebox.showinfo("Error", "Turno de %s"%nombre2)
            return
    if turno_jugador==2:
        if tablero[y1][x1]=="J1":
            messagebox.showinfo("Error", "Turno de %s"%nombre1)
            return
    if tablero1[y1][x1]=="J1r" or tablero1[y1][x1]=="J2r":
        if tablero[y1][x1]=="J1r":
            tablero=movimiento_reina(x1,y1,x2,y2,"J1r")
            tablero=comida_reina_j1(x1,y1,x2,y2)
        if tablero[y1][x1]=="J2r":
            tablero=movimiento_reina(x1,y1,x2,y2,"J2r")
            tablero=comida_reina_j2(x1,y1,x2,y2)
        
    if not tablero1[y2][x2]=="J1r" or not tablero1[y2][x2]=="J2r":
        if y1+2==y2 or y1-2==y2:
            tablero=comida(x1,y1,x2,y2)
        if (y1+1==y2 or y1-1==y2)and (x1+1==x2 or x1-1==x2):
            for i in range(len(tablero1)):
                for j in range(len(tablero1[i])):
                    if i==y2 and j==x2:
                        if y1+1==y2:
                            tablero1[i][j]="J2"
                        else:
                            tablero1[i][j]="J1"
                    if i==y1 and j==x1:
                        tablero1[i][j]=0

    if tablero1[y2][x2]=="J2":
        if y2==7:
            
            tablero1[y2][x2]="J2r"
    if tablero1[y2][x2]=="J1":
        if y2==0:
            
            tablero1[y2][x2]="J1r"
    tablero_crack()

    if verifica_tablero()==True:
        if turno_jugador==1:
            messagebox.showinfo("Ganador","Felicitaciones, %s has ganado"%nombre2)
            winsound.PlaySound("applause.wav", winsound.SND_FILENAME)

        if turno_jugador==2:
            messagebox.showinfo("Ganador","Felicitaciones, %s has ganado"%nombre1)
            winsound.PlaySound("applause.wav", winsound.SND_FILENAME)
        volver()
            
    if turno_jugador==1:
        Label(juego, bg="DeepSkyBlue3", text="Turno de %s"%nombre1, compound="left", width="50",font="Verdana 18",fg="black") .place(x=50,y=30)
        turno_jugador=2
        return
    if turno_jugador==2:
        Label(juego, bg="DeepSkyBlue3", text="Turno de %s"%nombre2, compound="left",width="50", font="Verdana 18",fg="black") .place(x=50,y=30)
        turno_jugador=1
        return
                    
def matriz_tablero():
    global tablero
    tablero=[0]*8
    for i in range(0,8):
        tablero[i]=[0]*8
    for fila in range(0,8):
        for columna in range (0,8):
            if fila%2==0:
                if columna%2==0:
                    tablero[fila][columna]="X"
                if fila==0 or fila==2:
                    if columna==1 or columna==3 or columna==5 or columna==7:
                        tablero[fila][columna]="J2"
                if fila==6:
                    if columna==1 or columna==3 or columna==5 or columna==7:
                        tablero[fila][columna]="J1"
            if fila%2!=0:
                if columna%2!=0:
                    tablero[fila][columna]="X"
                if fila==1:
                    if columna==0 or columna==2 or columna==4 or columna==6:
                        tablero[fila][columna]="J2"
            
                if fila==5 or fila==7:
                    if columna==0 or columna==2 or columna==4 or columna==6:
                        tablero[fila][columna]="J1"

##def hacer_ficha(fila,columna):
##    global tablero
##    if tablero[fila][columna]=="J1":
##        jugador1=w.create_oval(0+50*columna,0+50*fila,50+50*columna,50+50*fila,fill=ficha1)
##    return jugador1
posicion_x=0
posicion_y=0
x2=0
y2=0


def jugada_inicial(event):
    global posicion_x, posicion_y
    posicion_x = event.x
    posicion_y = event.y
    posicion_x=posicion_x//50
    posicion_y=posicion_y//50

    
dadomayor=0
turno_jugador=0   
def jugada_final(event):
    global tablero
    global x2, y2
    global posicion_x, posicion_y
    global turno_jugador
    x2= event.x
    y2= event.y
    x2=x2//50
    y2=y2//50
    valida_movimiento([posicion_x, posicion_y],[x2,y2])
    
    
    
    
        
def tablero_crack():
    w=Canvas(juego, width=400, height=400)
    w.place(x=300,y=150)
    global tablero
    contador=0
    tag_F="F"
    tag_C="C"
    for i in range(len(tablero)):
        for j in range(len(tablero[i])):
            if i%2==0:
                if j%2==0:
                    rect1=w.create_rectangle(0+50*j,0+50*i,50+50*j,50+50*i,fill=color1, tags=tag_C+str(contador))
                    w.tag_bind(rect1, "<1>", jugada_final)
                if j%2==1:
                    rect2=w.create_rectangle(0+50*j,0+50*i,50+50*j,50+50*i,fill=color2, tags=tag_C+str(contador))
                    w.tag_bind(rect2, "<1>", jugada_final)
                    if tablero[i][j]=="J1":
                        jugador1=w.create_oval(0+50*j,0+50*i,50+50*j,50+50*i,fill=ficha1, tags=tag_F+str(contador))
                        w.tag_bind(jugador1, "<1>", jugada_inicial)
                        
                    if tablero[i][j]=="J1r":
                        jugador1_r=w.create_oval(0+50*j,0+50*i,50+50*j,50+50*i,fill=ficha1, tags=tag_F+str(contador))
                        jugador1r=w.create_rectangle(15+50*j,15+50*i,35+50*j,35+50*i,fill="yellow", tags=tag_F+str(contador))
                        w.tag_bind(jugador1_r, "<1>", jugada_inicial)
                        w.tag_bind(jugador1r, "<1>", jugada_inicial)

                    if tablero[i][j]=="J2":
                        jugador2=w.create_oval(0+50*j,0+50*i,50+50*j,50+50*i,fill=ficha2, tags=tag_F+str(contador))
                        w.tag_bind(jugador2, "<1>", jugada_inicial)
                        
                    if tablero[i][j]=="J2r":
                        jugador2_r=w.create_oval(0+50*j,0+50*i,50+50*j,50+50*i,fill=ficha2, tags=tag_F+str(contador))
                        jugador2r=w.create_rectangle(15+50*j,15+50*i,35+50*j,35+50*i,fill="yellow", tags=tag_F+str(contador))
                        w.tag_bind(jugador2_r, "<1>", jugada_inicial)
                        w.tag_bind(jugador2r, "<1>", jugada_inicial)

            if i%2!=0:
                if j%2==0:
                    rect1=w.create_rectangle(0+50*j,0+50*i,50+50*j,50+50*i,fill=color2, tags=tag_C+str(contador))
                    w.tag_bind(rect1, "<1>", jugada_final)
                    if tablero[i][j]=="J1":
                        jugador1=w.create_oval(0+50*j,0+50*i,50+50*j,50+50*i,fill=ficha1, tags=tag_F+str(contador))
                        w.tag_bind(jugador1, "<1>", jugada_inicial)

                    if tablero[i][j]=="J1r":
                        jugador1_r=w.create_oval(0+50*j,0+50*i,50+50*j,50+50*i,fill=ficha1, tags=tag_F+str(contador))
                        jugador1r=w.create_rectangle(15+50*j,15+50*i,35+50*j,35+50*i,fill="yellow", tags=tag_F+str(contador))
                        w.tag_bind(jugador1_r, "<1>", jugada_inicial)
                        w.tag_bind(jugador1r, "<1>", jugada_inicial)
                        
                    if tablero[i][j]=="J2":
                        jugador2=w.create_oval(0+50*j,0+50*i,50+50*j,50+50*i,fill=ficha2, tags=tag_F+str(contador))
                        w.tag_bind(jugador2, "<1>", jugada_inicial)

                    if tablero[i][j]=="J2r":
                        jugador2_r=w.create_oval(0+50*j,0+50*i,50+50*j,50+50*i,fill=ficha2, tags=tag_F+str(contador))
                        jugador2r=w.create_rectangle(15+50*j,15+50*i,35+50*j,35+50*i,fill="yellow", tags=tag_F+str(contador))
                        w.tag_bind(jugador2_r, "<1>", jugada_inicial)
                        w.tag_bind(jugador2r, "<1>", jugada_inicial)
                        
                    
                if j%2==1:
                    w.create_rectangle(200+50*j,100+50*i,250+50*j,150+50*i,fill=color1, tags=tag_C+str(contador))
                    w.tag_bind(rect2, "<1>", jugada_final)
            contador+=1
    

def comida(x1,y1,x2,y2):
    global tablero
    for i in range(len(tablero)):
        for j in range(len(tablero[i])):
            if y1<i<y2 or y1>i>y2:
                
                if j+1==x2 or j-1==x2:
                    if tablero[i][j]!=tablero[y1][x1] and tablero[i][j]!=0:
                        tablero[y2][x2]=tablero[y1][x1]
                        tablero[y1][x1]=0
                        tablero[i][j]=0
                        return tablero
                        
    return tablero

def config():
    ventana.iconify()
    ajustes.deiconify()

def acerca_de():
    ventana.iconify()
    acercade.deiconify()
    
def pantalla():
    ventana.iconify()
    jugadores.deiconify()

##def tiempo(n):
##    sec=n
##    min=0
##    hor=0
##    if n>=60:
##        min=sec//60
##        sec=sec%60
##        hor=min//60
##        min=min%60
##    return hor,":",min,":",sec
##def cronometro():
##    contador=0
##    while True:
##        sleep(1)
##        contador=contador+1
##        x=tiempo(contador)
##        print (x)
##    return
    
def reinicia_cron():
    global sec, minute, hor
    sec=0
    minute=0
    hor=0
    contador=0
    return

variable = 1
def listo():
    global respuesta_reloj
    global variable
    global pausa
    global reloj
    pausa=False
    
    if nombre1=="" or nombre2=="":
        messagebox.showerror("Error", "Escoja ambos nombres de jugadores primero")
        return
    if dado1==0 or dado2==0:
        messagebox.showerror("Error", "Debe tirar los dados primero")
        return
    
    juego.deiconify()
    reinicia_cron()
    #cronometro()
    pausa = False
    jugadores.iconify()
    matriz_tablero()
    tablero_crack()
    if respuesta_reloj==1:
        if (variable == 1):
            variable = 2
            cronometro()



def volver():
    global pausa
    pausa = True
    global entrada1
    global entrada2
    global respuesta_reloj
    
    ventana.deiconify()
    jugadores.iconify()
    ajustes.iconify()
    acercade.iconify()
    juego.iconify()
    global dado1
    global dado2
    global nombre1
    global nombre2
    nombre1=""
    nombre2=""
    dado1=0
    dado2=0
    
    Label(jugadores, image=dadoi, bg="DeepSkyBlue3") .place(x=90,y=100)
    Label(jugadores, image=dadoi, bg="DeepSkyBlue3") .place(x=90,y=300)

def quit1():
    global pausa
    pausa = True
    answer=messagebox.askyesno("Salida", "Seguro que deseas salir?", default="no")
    if answer==True:
        winsound.PlaySound("abucheo.wav", winsound.SND_FILENAME)
        ventana.destroy()

dado1=0
dado2=0

def dados():
    global nombre1
    global nombre2
    global dado1
    global dado2
    global turno_jugador
    if nombre1=="" or nombre2=="":
        messagebox.showerror("Error", "Escoja ambos nombres de jugadores primero")
        return
    if dado1==0 and dado2==0:
        dado1=randint(1,6)
        dado2=randint(1,6)
        while dado1==dado2:
            dado2=randint(1,6)
        if dado1==1:
            Label(jugadores, image=dado_1, bg="DeepSkyBlue3") .place(x=90,y=300)
        if dado1==2:
            Label(jugadores, image=dado_2, bg="DeepSkyBlue3") .place(x=90,y=300)
        if dado1==3:
            Label(jugadores, image=dado3, bg="DeepSkyBlue3") .place(x=90,y=300)    
        if dado1==4:
            Label(jugadores, image=dado4, bg="DeepSkyBlue3") .place(x=90,y=300)
        if dado1==5:
            Label(jugadores, image=dado5, bg="DeepSkyBlue3") .place(x=90,y=300)
        if dado1==6:
            Label(jugadores, image=dado6, bg="DeepSkyBlue3") .place(x=90,y=300)
        if dado2==1:
            Label(jugadores, image=dado_1, bg="DeepSkyBlue3") .place(x=90,y=100)
        if dado2==2:
            Label(jugadores, image=dado_2, bg="DeepSkyBlue3") .place(x=90,y=100)
        if dado2==3:
            Label(jugadores, image=dado3, bg="DeepSkyBlue3") .place(x=90,y=100)    
        if dado2==4:
            Label(jugadores, image=dado4, bg="DeepSkyBlue3") .place(x=90,y=100)
        if dado2==5:
            Label(jugadores, image=dado5, bg="DeepSkyBlue3") .place(x=90,y=100)
        if dado2==6:
            Label(jugadores, image=dado6, bg="DeepSkyBlue3") .place(x=90,y=100)
        if dado1>dado2:
            messagebox.showinfo("Ganador","%s ha ganado"%nombre2)
            turno_jugador=1
        if dado2>dado1:
            turno_jugador=2
            messagebox.showinfo("Ganador","%s ha ganado"%nombre1)
    else:
        messagebox.showerror("Error", "Solo puede tirar una vez")
def r_con():
    global respuesta_reloj
    text_reloj=str(respuesta_reloj.get())
    reloj_config= open("reloj_configure.txt", "w")
    reloj_config.write(text_reloj)
    reloj_config.close()
    

def empatar():
    global pausa
    pausa = True
    empate=messagebox.askyesno("Empatar","¿Seguro que desea empatar?", default="no")
    if empate==True:
        ok=messagebox.showinfo("Empate", "El juego queda empate por acuerdo entre jugadores" )
        winsound.PlaySound("applause.wav", winsound.SND_FILENAME)
        volver()

def retirar():
    global pausa
    pausa = True
    pregunta=messagebox.askyesno("Retirar", "Seguro que desea retirarse?")
    if pregunta==True:
        if turno_jugador==1:
            messagebox.showinfo("Ganador","Felicitaciones, %s has ganado"%nombre1)
            winsound.PlaySound("applause.wav", winsound.SND_FILENAME)
        if turno_jugador==2:
            messagebox.showinfo("Ganador","Felicitaciones, %s has ganado"%nombre2)
            winsound.PlaySound("applause.wav", winsound.SND_FILENAME)
        
        volver()

nombre1=""
nombre2=""
contraseña1=""
contraseña2=""
def checkeo_1():
    global nombre1
    global contraseña1
    nombre1=nombre_p_1.get()
    contraseña1=Contraseña_p1.get()
    if len(nombre1)<1 or len(nombre1)>20:
        messagebox.showerror("Error nombre", "El nombre debe tener entre 1 y 20 carecteres")
        nombre1=""
    if len(Contraseña1)<5 or len(Contraseña1)>10:
        messagebox.showerror("Error Contraseña", "La contraseña debe tener entre 5 y 10 carecteres")
        Contraseña1=""
    if revisa_usuario(nombre1,contraseña1)=="Si cont":
        cambio_cont=messagebox.askyesno("Cambio Contraseña", "Desea Cambiar su Contraseña?")        
        if cambio_cont==True:
            Entry(jugadores, textvariable=contraseña1,bg="gray", fg="black", show="*").place(x=200,y=288)
            Label(jugadores, fg="black", text="Nueva Contraseña:", font="Chalkduster 18", bg="DeepSkyBlue3") .place(x=10,y=280)
    if revisa_usuario(nombre1,contraseña1)==True:
        user=pickle.load(open("tablero2017jugadores.txt","rb"))
        user[nombre1]=contraseña1
        pickle.dump(user,open("tablero2017jugadores.txt", "wb"))
    return

def checkeo_2():
    global nombre2
    global contraseña2
    nombre2=nombre_p_2.get()
    contraseña2=Contraseña_p2.get()
    if len(nombre2)<1 or len(nombre2)>20:
        messagebox.showerror("Error nombre", "El nombre debe tener entre 1 y 20 carecteres")
        nombre2=""
    if len(contraseña2)<5 or len(contraseña2)>10:
        messagebox.showerror("Error Contraseña", "La contraseña debe tener entre 5 y 10 carecteres")
        contraseña2=""
    if revisa_usuario(nombre2,contraseña2)=="Si cont":
        cambio_cont=messagebox.askyesno("Cambio Contraseña", "Desea Cambiar su Contraseña?")        
        if cambio_cont==True:
            Entry(jugadores, textvariable=contraseña2,bg="gray", fg="black", show="*").place(x=200,y=288)
            Label(jugadores, fg="black", text="Nueva Contraseña:", font="Chalkduster 18", bg="DeepSkyBlue3") .place(x=10,y=280)
    if revisa_usuario(nombre2,contraseña2)==True:
        user=pickle.load(open("tablero2017jugadores.txt","rb"))
        user[nombre2]=contraseña2
        pickle.dump(user,open("tablero2017jugadores.txt", "wb"))
    
    return
def revisa_usuario(usuario,contraseña):
    user=pickle.load(open("tablero2017jugadores.txt","rb"))
    if usuario in user:
        if contraseña!=user[usuario]:
            return "No cont"    
        if contraseña==user[usuario]:
            return "Si cont"
    else:
        return True
        

        
    

def c_con():
    global respuesta_comida
    text_comida=str(respuesta_comida.get())
    comida_config= open("comida_configure.txt", "w")
    comida_config.write(text_comida)
    comida_config.close()

def cant_con():
    global respuesta_cantidad
    text_cantidad=str(respuesta_cantidad.get())
    cantidad_config= open("cantidad_configure.txt", "w")
    cantidad_config.write(text_cantidad)
    cantidad_config.close()

sec=0
minute=0
hor=0
contador=0
def cronometro():
    global sec
    global minute
    global hor
    global cron
    global contador
    global pausa
    if pausa == False:
        if contador == 1:
            cron=Label(juego, font="Arial 28", width="10",bg="DeepSkyBlue3", fg="black")
        
            cron['text']=str(hor)+"  "+":"+str(minute)+"  "+":"+str(sec)
        
            cron.place(x=20,y=200)
            

        else:
            contador += 1
        if contador==2:
            contador=0
        
        sec+=1
        if sec==60:
            minute+=1
            sec=0
        if minute==60:
            hor+=1
            minute=0
            
        cron=Label(juego, font="Arial 28", bg="DeepSkyBlue3", width="10",fg="black")
        
        cron['text']=str(hor)+"  "+":"+str(minute)+"  "+":"+str(sec)
        
        cron.place(x=20,y=200)
        
    cron.after(1000, cronometro)

def pausar():
    global pausa
    if pausa:
        pausa = False
    else:
        pausa = True
    
def ayuda_i():
    os.startfile("Manual de Usuario.pdf")

def imprimir_tablero():
    os.startfile("Tablero Impresion.pdf")

def guardar_juego():
    global respuesta_reloj
    global tablero
    global turno_jugador
    global lee_cantidad
    global sec, minute, hor, pausa, contador
    global nombre1,nombre2,contraseña1,contraseña2
    pickle.dump({"tablero":tablero, "turno":turno_jugador, "movidas":lee_cantidad, "reloj": respuesta_reloj, "tiempo_detalles": [sec, minute, hor, pausa, contador], "usuarios":{"j1":[nombre1,contraseña1], "j2":[nombre2,contraseña2]}}, open("tablero2017juegoactual.dat", "wb"))
def cargar_juego():
    global tablero
    global turno_jugador
    global lee_cantidad
    global respuesta_reloj
    global sec, minute, hor, pausa, contador
    global nombre1,nombre2,contraseña1,contraseña2
    if solicita_usuario_clave()==True:
        carga=pickle.load(open("tablero2017juegoactual.dat", "rb"))
        tablero=carga["tablero"]
        turno_jugador=carga["turno_jugador"]
        lee_cantidad=carga["movidas"]
        respuesta_reloj=carga["reloj"]
        tiempo=carga["tiempo_detalles"]
        sec, minute, hor, pausa, contador=tiempo
        usuario1=carga["j1"]
        usuario2=carga["j2"]
        nombre1,contraseña1=usuario1
        nombre2,contraseña2=usuario2
    else:
        messagebox.showerrror("Error de Usuarios", "EL usuario o contraseña ingresados no son los registrados en el juego a cargar")


def solicita_usuario_clave():                                                                                                                                                                                                                                                               

    

#Fondo Pantalla Ajustes
Label(ajustes, bg="DeepSkyBlue3", width=900, height=660) .place(x=0,y=0)
Button(ajustes, text="Salir",image=bsalir, compound="left", command=quit1, font="Arial 28", fg="white", bg="gray", cursor="pirate").place(x=20,y=580)
Button(ajustes, text="Volver",image=vuelta_img, compound="left", command=volver, font="Chalkduster 28", fg="white", bg="gray", cursor="gumby") .place(x=20,y=500)
respuesta_reloj=IntVar()
Label(ajustes, bg="bisque4", width=20, height=10) .place(x=80,y=60)
Label(ajustes, bg="bisque4", text="Reloj", font="Verdana 18") .place(x=80,y=60)
reloj1=Radiobutton(ajustes, activebackground="bisque4",bg="bisque4",text="Si",  font="Verdana 12",variable=respuesta_reloj, value=1,command=r_con) .place(x=100,y=100)
reloj2=Radiobutton(ajustes, activebackground="bisque4",bg="bisque4",text="No",  font="Verdana 12",variable=respuesta_reloj, value=2,command=r_con) .place(x=100,y=140)
reloj3=Radiobutton(ajustes, activebackground="bisque4", bg="bisque4",text="Por jugador", font="Verdana 12", variable=respuesta_reloj, value=3,command=r_con) .place(x=100,y=180)
Label(ajustes, bg="bisque4", width=40, height=8) .place(x=350,y=60)
Label(ajustes, bg="bisque4", text="Comer Piezas", font="Verdana 18") .place(x=380,y=60)
respuesta_comida=StringVar()
comer_obligatorio=Radiobutton(ajustes, activebackground="bisque4",bg="bisque4",text="Obligatoria",  font="Verdana 12",variable=respuesta_comida, value="obligatorio",command=c_con) .place(x=480,y=100)
comer_opcional=Radiobutton(ajustes, activebackground="bisque4",bg="bisque4",text="Opcional",  font="Verdana 12",variable=respuesta_comida, value="opcional",command=c_con) .place(x=480,y=140)
Label(ajustes, bg="bisque4", text="Cantidad permitida de jugadas sin acciones", font="Verdana 18") .place(x=50,y=260)
respuesta_cantidad=IntVar()
cantidad_movidas=Entry(ajustes, textvariable=respuesta_cantidad, bg="bisque4", fg="black", width=5). place(x=580,y=270)
Button(ajustes, image=check_img, bg="DeepSkyBlue3", cursor="pirate", command=cant_con) .place(x=620,y=270)

#Fondo Pantalla Jugadores
Label(jugadores, bg="DeepSkyBlue3", width=900, height=660) .place(x=0,y=0)
Label(jugadores, fg="black", text="Jugador 1:", font="Chalkduster 18", bg="DeepSkyBlue3") .place(x=70,y=50)
Label(jugadores, fg="black", text="Contraseña:", font="Chalkduster 18", bg="DeepSkyBlue3") .place(x=55,y=80)
nombre_p_1=StringVar()
Contraseña_p1=StringVar()
Entry(jugadores, textvariable=nombre_p_1,bg="gray", fg="black").place(x=200,y=58)
Entry(jugadores, textvariable=Contraseña_p1,bg="gray", show="*", fg="black").place(x=200,y=88)
Label(jugadores, fg="black", text="Jugador 2:", font="Chalkduster 18", bg="DeepSkyBlue3") .place(x=70,y=250)
Label(jugadores, fg="black", text="Contraseña:", font="Chalkduster 18", bg="DeepSkyBlue3") .place(x=55,y=280)
nombre_p_2=StringVar()
Contraseña_p2=StringVar()
Entry(jugadores, textvariable=nombre_p_2,bg="gray", fg="black").place(x=200,y=258)
Entry(jugadores, textvariable=Contraseña_p2,bg="gray", fg="black", show="*").place(x=200,y=288)
Label(jugadores, bg="DeepSkyBlue3", image=dadot) .place(x=530, y=100)
Label(jugadores, image=dadoi, bg="DeepSkyBlue3") .place(x=90,y=120)
Label(jugadores, image=dadoi, bg="DeepSkyBlue3") .place(x=90,y=320)
Button(jugadores, text="Tira Dados", font="Chalkduster 20", bg="gray", cursor="pirate", command=dados) .place(x=500, y=200)
Button(jugadores, text="Salir",image=bsalir, compound="left", command=quit1, font="Arial 28", fg="white", bg="gray", cursor="pirate").place(x=20,y=580)
Button(jugadores, text="Volver",image=vuelta_img, compound="left", command=volver, font="Chalkduster 28", fg="white", bg="gray", cursor="gumby") .place(x=20,y=500)
Button(jugadores, text="Listo", image=listo_img, compound="left", font="Chalkduster 28", bg="gray", cursor="pirate",fg="white", command=listo) .place(x=20,y=420)
Button(jugadores, image=check_img, bg="DeepSkyBlue3", cursor="pirate", command=checkeo_1) .place(x=340,y=50)
Button(jugadores, image=check_img, bg="DeepSkyBlue3", cursor="pirate", command=checkeo_2) .place(x=340,y=250)

#Falta agregar sonido
#Fondo Pantalla Juego
Label(juego, bg="DeepSkyBlue3", width=900, height=660) .place(x=0,y=0)
Button(juego, bg="DeepSkyBlue3", image=vuelta_img, compound="left", text="Pantalla Inicio", command=volver,relief="sunken") .place(x=20,y=500)
Button(juego, text="Salir",image=bsalir, compound="left", command=quit1,bg="DeepSkyBlue3", font="Arial 20", fg="black", cursor="pirate",relief="sunken").place(x=20,y=580)
Button(juego, text="Retiro",command=retirar, bg="DeepSkyBlue3", font="Arial 20", fg="black", cursor="pirate",relief="sunken").place(x=780,y=500)
Button(juego, text="Tablas",command=empatar, bg="DeepSkyBlue3", font="Arial 20", fg="black", cursor="pirate",relief="sunken").place(x=780,y=580)
lee_config=open("comida_configure.txt", "r"). read()
Label(juego, bg="DeepSkyBlue3", text="Comida es %s"%lee_config, font="Verdana 18", fg="black") .place(x=50,y=100)
lee_cantidad=open("cantidad_configure.txt", "r"). read()
Label(juego, bg="DeepSkyBlue3", text="Cantidad de movidas sin comidas %s"%lee_cantidad, font="Verdana 18", fg="black") .place(x=20,y=70)
Button(juego, text="Pausa",command=pausar, bg="DeepSkyBlue3", font="Arial 20", fg="black", cursor="pirate",relief="sunken").place(x=80,y=280)
Button(juego, text="Guardar", command=guardar_juego, bg="DeepSkyBlue3", font="Arial 20", fg="black", cursor="pirate",relief="sunken").place(x=80,y=380)




#Fondo de Pantalla Inicio
img=PhotoImage(file="imagen.gif")
Label(ventana,bg="black",width=900, height=660) .place(x=0,y=0)
Label (ventana,image=img,bg="black") .place(x=125,y=140)
imgtablero=PhotoImage(file="movimiento.gif")
Label (ventana,image=imgtablero,bg="black" ) .place(x=600,y=390)

#Titulo
Label(ventana,bg="black",fg="white", text="Damas Españolas", font="Chalkduster 45") .place(x=250,y=45)



#Fondo Pantalla Acerca de
Button(acercade, text="Volver",image=vuelta_img, compound="left", command=volver, font="Chalkduster 28", fg="white", bg="gray", cursor="gumby") .place(x=20,y=500)
Button(acercade, text="Salir",image=bsalir, compound="left", command=quit1, font="Arial 28", fg="white", bg="gray", cursor="pirate").place(x=20,y=580)
acerca_progra= open("acerca_de_archivo.txt", "r"). read()
info=Label(acercade, text=acerca_progra, bg="DeepSkyBlue3", fg="black")
info.pack()


    
    
#Botones Ventana Principal
boton1=Button(ventana, text="Salir",image=bsalir, compound="left", command=quit1, font="Arial 28", fg="white", bg="gray", cursor="pirate").place(x=20,y=580)
boton=Button(ventana, text="Jugar",image=play_img, compound="left", command=lambda: pantalla(), font="Chalkduster 28", fg="white", bg="gray", cursor="gumby")
boton.place(x=49,y=200)
Button(ventana, text="Ajustes", image=ajustes_img, compound="left", bg="gray", font="Chalkduster 28", fg="white", cursor="spraycan", command=config) .place(x=49, y=300)
Button(ventana, text="Acerca de", image=acerca_img, compound="left", command=acerca_de,bg="gray", font="Chalkduster 28", fg="white", cursor="tcross") .place(x=49, y=390)
Button(ventana, text="Ayuda", image=ayuda_img, compound="left", bg="gray", command=ayuda_i, font="Chalkduster 28", fg="white", cursor="diamond_cross") .place(x=49, y=480)
Button(ventana, text="Impresion", bg="gray", command=imprimir_tablero, font="Chalkduster 28", fg="white", cursor="diamond_cross") .place(x=660, y=180)


ventana.mainloop()

#Logica

    

#Link para iconos: http://www.iconarchive.com/search?q=exit

    
