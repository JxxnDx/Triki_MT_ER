from tkinter import *
from MaquinaTuring import *
from PIL import Image, ImageTk

class TrikiGui:

    raiz = Tk()
    raiz.title('Triki')
    miFrame = Frame(bg='lightgreen')
    paginaJuego = Frame(bg = 'lightgreen')
    estado = Label(paginaJuego, text='Turno del jugador A(X)', font=('ARCADE', 18), bg='lightgreen', fg='blue')

    triki = False
    movimientos = 0
    turno = 'X'
    cadena_X = ''
    cadena_O = ''

    maquina = Turing()

    def frame(self):
        self.miFrame.pack(fill='both', expand='True')
        self.raiz.resizable(False, False)

        imagen = Image.open('trikiimage.png')
        imagen = imagen.resize((200, 100))
        img = ImageTk.PhotoImage(imagen)
        
        menuBar = Menu(self.miFrame)
        menu_info = Menu(menuBar, tearoff=0)
        menu_info.add_command(label='Sobre nosotros', command=self.showInfo)
        menu_info.add_command(label='Versión', command=self.showVersion)

        menuBar.add_cascade(label='Info', menu=menu_info)
        self.raiz.config(menu = menuBar)

        titulo = Label(self.miFrame, text='T R I K I', font=('HIRO MISAKE', 42), bg='lightgreen')
        imgn = Label(self.miFrame, image=img, bg='lightgreen')
        titulo.pack(pady=(50, 5), padx=50)
        imgn.pack(padx=50)

        self.botonJugar = Button(self.miFrame, text='Jugar', command=self.jugar)
        self.botonJugar.pack(pady=(5, 5), padx=50)
        self.botonJugar.config(font=('ARCADE', 20), bg='lightblue')

        self.botonCerrar = Button(self.miFrame, text=' Salir ', command=lambda: self.raiz.destroy())
        self.botonCerrar.pack(padx=50, pady=(5, 50))
        self.botonCerrar.config(font=('ARCADE', 20), bg='lightblue')

        mainloop()

    #
    def jugar(self):
        tablero = Frame(self.paginaJuego)

        self.buttons = [[None for _ in range(3)] for _ in range(3)]
        for i in range(3):
            for j in range(3):
                self.buttons[i][j] = Button(tablero, text="", font=("Arial", 24), width=5, height=2,
                                              command=lambda row=i, col=j: self.marcar_casilla(row, col))
                self.buttons[i][j].grid(row=i, column=j)

        tablero.config(pady=50, padx=50, bg='lightgreen')
        tablero.pack(side='bottom')

        texto = Label(self.paginaJuego, text='A jugar!')
        texto.config(font=('HIRO MISAKE', 25), fg='purple', bg='lightgreen', pady=20)
        texto.pack(side='top')

        self.estado.pack(side='top', pady=(10, 2), padx=50)
        self.miFrame.pack_forget()
        self.paginaJuego.pack()

    #
    def marcar_casilla(self, row, col):        
        self.buttons[row][col].config(state='disabled')
        self.movimientos += 1

        if(self.turno == 'X'):
            self.cadena_X = self.generar_cadena(self.cadena_X, row, col)

            self.estado.config(text= 'Turno del jugador B(O)')
            self.check_winner(self.cadena_X)
            self.buttons[row][col].config(text=self.turno)
            self.turno = 'O'

        else:
            self.cadena_O = self.generar_cadena(self.cadena_O, row, col)

            self.estado.config(text= 'Turno del jugador A(X)')
            self.check_winner(self.cadena_O)
            self.buttons[row][col].config(text=self.turno)
            self.turno = 'X'

    def generar_cadena(self, cadena, row, col):
        if(row == 0 and col == 0):
            cadena = cadena + '1'
        elif(row == 0 and col == 1):
            cadena = cadena + '01'
        elif(row == 0 and col == 2):
            cadena = cadena + '001'
        elif(row == 1 and col == 0):
            cadena = cadena + '0001'
        elif(row == 1 and col == 1):
            cadena = cadena + '00001'
        elif(row == 1 and col == 2):
            cadena = cadena + '000001'
        elif(row == 2 and col == 0):
            cadena = cadena + '0000001'
        elif(row == 2 and col == 1):
            cadena = cadena + '00000001'
        else:
            cadena = cadena + '000000001'

        return cadena

    def check_winner(self, cadena):
        if(self.maquina.probar_cadena(cadena)):
            self.triki = True
            for row in self.buttons:
                for button in row:
                    button.config(state = 'disabled')

            if(self.turno == 'X'):
                self.estado.config(text = 'FIN DEL JUEGO \n HA GANADO EL JUGADOR A!', fg = 'black')
            else:
                self.estado.config(text = 'FIN DEL JUEGO \n HA GANADO EL JUGADOR O!', fg = 'black')

        if(self.movimientos == 9 and self.triki != True):
            self.estado.config(text = 'FIN DEL JUEGO \n HA SIDO UN EMPATE!', fg = 'black')


    #Funciones para el menú 
    def showInfo(self):
        info = Toplevel(self.raiz)
        info.title('About us')

        texto_info = Label(info, text = 'Proyecto autómatas \n Daniel Sebastián Badillo \n Juan David Pallares')
        texto_info.pack(pady=20, padx=20)

    def showVersion(self):
        version = Toplevel(self.raiz)
        version.title('Version')

        info_version = Label(version, text = 'Versión 1.0')
        info_version.pack(padx=20, pady=20)


ventana = TrikiGui()
ventana.frame()
