from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image
import pygame
import time
import threading
import serial

pygame.mixer.init()
arduinoData = serial.Serial('COM3', 9600)
test = False
musica = False
'''
Esta función se encarga de crear la ventana principal, donde se muestra la consola de comandos y el robot virtual.
Parámetros:
    None
Retorna:
    No retorna 
'''
def ventana():
    ventana = Tk()
    ventana.title('Robot Virtual')
    ventana.minsize(1280, 720)
    ventana.resizable(width=NO, height=NO)
    ventana.configure(background='#C3DFF4')
    
    canvas = Canvas(ventana, width=450, height=400, background='#7293C4')
    canvas.place(x=40, y=150)
    canvas2 = Canvas(ventana, width=650, height=600, background='White')
    canvas2.place(x=600, y=50)
    
    '''
    Objeto Robot
    atributos: ventana, nombre (str), imagen, fecha_creacion (str), felicidad (int), contador (int), anim (boolean)
    metódos:
    hello_ani(): se encarga de crear la animación del robot saludando
    sayhello(): muestra en un messagebox  el nombre del robot y llama a la función hello_ani
    forward_ani(): se encarga de crear la animación del robot caminando hacia adelante
    forward(): cambia la imagen del robot para que este mire hacia adelante
    backward_ani(): se encarga de crear la animación del robot caminando hacia atrás
    backward(): cambia la imagen del robot para que este mire hacia atrás
    stop(): se encarga de detener cualquier animación
    backflip_ani(): se encarga de crear la animación del robot haciendo un backflip
    backflip(): se encarga de llamar a la funcion backflip_ani
    music_on(): carga un archivo mp3 y lo reproduce
    music_off(): detiene la reproducción del archivo mp3 y lo cierra
    '''
    class Robot:
        def __init__(self, ventana, nombre, imagen, contador, anim):
            self.ventana = ventana
            self.nombre = nombre
            self.imagen = imagen
            self.contador = contador
            self.anim = anim

        def hello_ani(self):
            self.anim = True
            canvas2.delete('imgR')
            while self.contador != 12:
                if self.anim == False:
                    break
                nombre = 'Imagenes/wave/wave'+str(self.contador)+'.jpg'
                imgR = ImageTk.PhotoImage(Image.open(nombre).resize((700,400)))
                canvas2.create_image(0,100, image=imgR, anchor=NW, tag='imgR')
                self.contador+=1
                time.sleep(0.15)
                canvas2.delete('imgR')
            self.contador = 1
            canvas2.create_image(0, 100, image=self.imagen, anchor=NW)

        def sayhello(self):
            messagebox.showinfo(title='Nombre:', message='Hola! Mi nombre es ' + str(self.nombre))
            threading.Thread(target=self.hello_ani).start()
        
        def forward_ani(self):
            self.anim = True
            canvas2.delete('imgR')
            while self.contador != 22:
                if self.anim == False:
                    break
                nombre = 'Imagenes/walkF/walkF'+str(self.contador)+'.jpg'
                imgR = ImageTk.PhotoImage(Image.open(nombre).resize((700,400)))
                canvas2.create_image(0, 100, image=imgR, anchor=NW, tag='imgR')
                self.contador+=1
                time.sleep(0.15)
                canvas2.delete('imgR')
            self.contador = 1
            canvas2.create_image(0, 100, image=self.imagen, anchor=NW)

        def forward(self):
            canvas2.delete('imgR')
            self.imagen = ImageTk.PhotoImage(Image.open('Imagenes/defaultF.png').resize((700,400)))
            canvas2.create_image(0,100, image=self.imagen, anchor=NW, tag='imgR')
            threading.Thread(target=self.forward_ani).start()

        def backward_ani(self):
            self.anim = True
            canvas2.delete('imgR')
            while self.contador != 22:
                if self.anim == False:
                    break
                nombre = 'Imagenes/walkB/walkB'+str(self.contador)+'.jpg'
                imgR = ImageTk.PhotoImage(Image.open(nombre).resize((700,400)))
                canvas2.create_image(0, 100, image=imgR, anchor=NW, tag='imgR')
                self.contador+=1
                time.sleep(0.15)
                canvas2.delete('imgR')
            self.contador = 1
            canvas2.create_image(0, 100, image=self.imagen, anchor=NW)

        def backward(self):
            canvas2.delete('imgR')
            self.imagen = ImageTk.PhotoImage(Image.open('Imagenes/defaultB.png').resize((700,400)))
            canvas2.create_image(0,100, image=self.imagen, anchor=NW, tag='imgR')
            threading.Thread(target=self.backward_ani).start()

        def stop(self):
            self.anim = False
        
        def backflip_ani(self):
            self.anim = True
            canvas2.delete('imgR')
            while self.contador != 38:
                if self.anim == False:
                    break
                nombre = 'Imagenes/backflip/backflip ('+str(self.contador)+').jpg'
                imgR = ImageTk.PhotoImage(Image.open(nombre).resize((700,400)))
                canvas2.create_image(0, 100, image=imgR, anchor=NW, tag='imgR')
                self.contador+=1
                time.sleep(0.15)
                canvas2.delete('imgR')
            self.contador = 1
            canvas2.create_image(0, 100, image=self.imagen, anchor=NW)

        def backflip(self):
            threading.Thread(target=self.backflip_ani).start()

        def music_on(self):
            pygame.mixer.music.load('aespa.mp3')
            pygame.mixer.music.play()
        
        def music_off(self):
            pygame.mixer.music.stop()
            pygame.mixer.music.unload()

    '''
    Esta función se encarga de recibir un dato por medio de una entry y devuelve uno de los métodos del objeto robot segun lo que se introdujo en la entry
    Parámetros:
        None
    Retorna:
        No retorna 
    '''        
    def aceptar():
        comando = consola.get()
        if comando == 'sayhello':
            R.sayhello()
        if comando == 'forward':
            R.forward()
        if comando == 'backward':
            R.backward()
        if comando == 'stop':
            R.stop()
        if comando == 'backflip':
            R.backflip()
        if comando == 'music_on':
            R.music_on()
        if comando == 'music_off':
            R.music_off()
    
    '''
    Esta funcion se encarga de cambiar la variable test a un valor boolean True
    Parametros:
        None
    Retorna:
        wait_for_button(test)
    '''
    def test1():
        global test
        test = True
        return wait_for_button(test)

    '''
    Esta funcion se encarga de cambiar la variable test a un valor boolean True
    Parametros:
        test: se encarga de
    Retorna:
        Segun el boton que se presiona, retorna uno de los comandos del robot
    '''
    def wait_for_button(test):
        global musica
        while test == True:
            command = arduinoData.read(2)
            if len(command) == 2:
                if command == b'B1':
                    test = False
                    R.sayhello()
                elif command == b'B2':
                    test = False
                    R.forward()
                elif command == b'B3':
                    test = False
                    R.backward()
                elif command == b'B4':
                    test = False
                    R.backflip()
                elif command == b'B5':
                    if musica == True:
                        test = False
                        musica = False
                        R.music_off()
                    else:
                        test = False
                        musica = True
                        R.music_on()
    
    Label0 = Label(canvas, text='Consola de comandos', bg='#A2C4EC', fg='#383A3D', font=('Baskerville Old Face', 10))
    Label0.place(x=20, y=10)
    Label1 = Label(canvas, text='Los comandos disponibles son: ', bg='#A2C4EC', fg='#383A3D', font=('Baskerville Old Face', 10), width=25)
    Label2 = Label(canvas, text='- sayhello\n- forward\n- backward\n- stop\n- dance\n- music_on\n- music_off', bg='#A2C4EC', width=10, justify=LEFT, fg='#383A3D', font=('Baskerville Old Face', 10), anchor='w')
    Label1.place(x=20, y=120)
    Label2.place(x=110, y=150)

    consola = Entry(canvas, bg='#A2C4EC')
    consola.place(x=20, y=35)
    
    btn = Button(canvas, text='Aceptar', bg='#A2C4EC', fg='#383A3D', font=('Baskerville Old Face', 10), command=test1)
    btn.place(x=60, y=60)

    imgR = ImageTk.PhotoImage(Image.open('Imagenes/defaultF.png').resize((700,400)))
    canvas2.create_image(0,100, image=imgR, anchor=NW, tag='imgR')
    R = Robot(ventana, 'Linaria', imgR, 1, False)
    ventana.mainloop()

ventana()
