from tkinter import *
from customtkinter import *
from PIL import Image, ImageTk
from src.words_list import palabras_faciles, palabras_expertas
import random
import os
import time
from tkinter import messagebox


class MindDash:
    def __init__(self):
        self.root = Tk()
        self.root.resizable(False, False)
        self.root.title('MindDash')
        self.window_width = 600
        self.window_height = 600
        self.root.geometry(f"{self.window_width}x{self.window_height}")
        self.root.config(bg='#f5f7fc')
        icon_path = r'D:/Usuario/Desktop/PROGRAMACIÓN/PROYECTOS/MindDash/src/assets/icon.ico'
        self.root.iconbitmap(default=icon_path)

        self.imagen_tk = None
        self.question_imagen_tk = None
        self.cartel_ganador = None
        self.cartel_perdedor = None
        self.button_frame_main = None
        self.button_frame_dificultad = None
        
        self.azul='#0047ff'
        self.fondo='#f5f7fc'
        self.hover='#002aff'
        self.txt_palabra = None
        self.btn_volver = None
        self.btn_reiniciar = None
        self.btn_enviar = None
        self.option_buttons = None
        self.palabras_ingresadas = []
        
        self.setup_window()

    def setup_window(self):
        self.setup_main_frame()
        self.setup_logo()
        self.setup_question_logo()
        self.setup_buttons()

    def setup_main_frame(self):
        self.main_frame = Frame(self.root, bg='#f5f7fc', width=self.window_width, height=self.window_height)
        self.main_frame.pack(expand=True, fill="both")

    def setup_logo(self):
        ruta_imagen = 'D:/Usuario/Desktop/PROGRAMACIÓN/PROYECTOS/MindDash/src/assets/menu_logo.png'
        nuevo_ancho = 402
        nuevo_alto = 281

        logo_image = Image.open(ruta_imagen)
        imagen_redimensionada = logo_image.resize((nuevo_ancho, nuevo_alto))
        self.imagen_tk = ImageTk.PhotoImage(imagen_redimensionada)

        self.canvas = Canvas(self.main_frame, width=nuevo_ancho, height=nuevo_alto, highlightthickness=0, bd=0, bg='#f5f7fc')
        self.canvas.place(relx=0.5, rely=0.3, anchor=CENTER)
        self.canvas.create_image(0, 0, anchor="nw", image=self.imagen_tk)

    def setup_question_logo(self):
        ruta_question_imagen = 'D:/Usuario/Desktop/PROGRAMACIÓN/PROYECTOS/MindDash/src/assets/question_logo.png'
        nuevo_question_ancho = 402
        nuevo_question_alto = 281

        question_imagen = Image.open(ruta_question_imagen)
        question_redimensionada = question_imagen.resize((nuevo_question_ancho, nuevo_question_alto))
        self.question_imagen_tk = ImageTk.PhotoImage(question_redimensionada)

    def setup_ganador(self):
        ruta_ganador_imagen = 'D:/Usuario/Desktop/PROGRAMACIÓN/PROYECTOS/MindDash/src/assets/ganador.png'

        ganador_imagen = Image.open(ruta_ganador_imagen)
        ganador_redimensionada = ganador_imagen.resize((412, 291))
        self.ganador_imagen_tk = ImageTk.PhotoImage(ganador_redimensionada)
    def setup_perdedor(self):
        ruta_perdedor_imagen = 'D:/Usuario/Desktop/PROGRAMACIÓN/PROYECTOS/MindDash/src/assets/perdedor.png'

        perdedor_imagen = Image.open(ruta_perdedor_imagen)
        perdedor_redimensionada = perdedor_imagen.resize((412, 291))
        self.perdedor_imagen_tk = ImageTk.PhotoImage(perdedor_redimensionada)
        
    def setup_buttons(self):
        button_frame = Frame(self.main_frame, bg='#f5f7fc')
        button_frame.place(relx=0.5, rely=0.75, anchor=CENTER)

        btn_comenzar = CTkButton(button_frame,
                                text="\uf04b Comenzar",
                                font=("Tektur", 32),
                                bg_color='#f5f7fc',
                                fg_color='#0047ff',
                                text_color='white',
                                border_width=0,
                                corner_radius=50,
                                border_spacing=5,
                                hover_color='#002aff',
                                command=lambda: self.menu_dificultad())
        btn_comenzar.grid(row=0, column=0, pady=5, sticky=EW)

        btn_ajustes = CTkButton(button_frame,
                                text="\uf013 Ajustes",
                                font=("Tektur", 32),
                                bg_color='#f5f7fc',
                                fg_color='#0047ff',
                                text_color='white',
                                border_width=0,
                                corner_radius=50,
                                border_spacing=5,
                                hover_color='#002aff',
                                command=lambda: self.menu_ajustes())
        btn_ajustes.grid(row=1, column=0, pady=5, sticky=EW)

        btn_salir = CTkButton(button_frame,
                             text="\uf00d Salir",
                             font=("Tektur", 32),
                             bg_color='#f5f7fc',
                             fg_color='#0047ff',
                             text_color='white',
                             border_width=0,
                             corner_radius=50,
                             border_spacing=5,
                             hover_color='#002aff',
                             command=lambda: self.press_salir())
        btn_salir.grid(row=2, column=0, pady=5, sticky=EW)


    #------------------- MENU AJUSTES -------------------#
    def menu_ajustes(self):
        self.main_frame.pack_forget()
        self.setup_main_frame()
        self.button_frame = Frame(self.main_frame, bg='#f5f7fc')
        self.button_frame.place(relx=0.5, rely=0.5, anchor=CENTER)

    #------------------- MENU DIFICULTAD -------------------#
    def menu_dificultad(self):
        self.main_frame.pack_forget()
        self.setup_main_frame()
        self.button_frame = Frame(self.main_frame, bg='#f5f7fc')
        self.button_frame.place(relx=0.5, rely=0.5, anchor=CENTER)

        lbl_choose_difficulty = Label(self.button_frame,
                                      text='Elige una Dificultad',
                                      font=('Tektur', 30),
                                      bg='#f5f7fc',
                                      fg='#0047ff')
        lbl_choose_difficulty.grid(row=0, column=0, pady=30, sticky=EW)

        btn_facil = CTkButton(self.button_frame,
                              text="Fácil",
                              font=("Tektur", 35),
                              bg_color='#f5f7fc',
                              fg_color='#0047ff',
                              text_color='white',
                              border_width=0,
                              corner_radius=50,
                              border_spacing=5,
                              hover_color='#002aff',
                              command=lambda: self.nivel_facil())
        btn_facil.grid(row=1, column=0, pady=5, sticky=EW)

        btn_intermedio = CTkButton(self.button_frame,
                                   text="Intermedio",
                                   font=("Tektur", 35),
                                   bg_color='#f5f7fc',
                                   fg_color='#0047ff',
                                   text_color='white',
                                   border_width=0,
                                   corner_radius=50,
                                   border_spacing=5,
                                   hover_color='#002aff',
                                   command=lambda: self.nivel_intermedio())
        btn_intermedio.grid(row=2, column=0, pady=5, sticky=EW)

        btn_avanzado = CTkButton(self.button_frame,
                                 text="Avanzado",
                                 font=("Tektur", 35),
                                 bg_color='#f5f7fc',
                                 fg_color='#0047ff',
                                 text_color='white',
                                 border_width=0,
                                 corner_radius=50,
                                 border_spacing=5,
                                 hover_color='#002aff',
                                 command=lambda: self.nivel_avanzado())
        btn_avanzado.grid(row=3, column=0, pady=5, sticky=EW)

        btn_experto = CTkButton(self.button_frame,
                                text="Experto",
                                font=("Tektur", 35),
                                bg_color='#f5f7fc',
                                fg_color='#0047ff',
                                text_color='white',
                                border_width=0,
                                corner_radius=50,
                                border_spacing=5,
                                hover_color='#002aff',
                                command=lambda: self.nivel_experto())
        btn_experto.grid(row=4, column=0, pady=5, sticky=EW)
        
        btn_reresar = CTkButton(self.button_frame,
                                text="\uf104 Volver",
                                font=("Tektur", 25),
                                bg_color='#f5f7fc',
                                fg_color='#0047ff',
                                text_color='white',
                                border_width=0,
                                corner_radius=50,
                                border_spacing=5,
                                hover_color='#002aff',
                                command=lambda: self.volver())
        btn_reresar.grid(row=5, column=0, pady=5, sticky=EW)


    #------------------- NIVELES -------------------#
    def nivel_facil(self):
        self.main_frame.pack_forget() 
        self.setup_main_frame()
        
        palabras_mostradas = random.sample(palabras_faciles, 4)

        def inicio_juego():
            palabra_label = Label(self.main_frame, bg=self.fondo, font=("Tektur", 50), fg=self.azul)
            palabra_label.place(relx=0.5, rely=0.5, anchor=CENTER)
            palabra_label.config(text=palabras_mostradas[0])
            for palabra in palabras_mostradas:
                palabra_label.config(text=palabra)
                self.root.update()
                time.sleep(2)
                palabra_label.config(text="")
                self.root.update()
            palabra_label.destroy()

            
            #------------------- QUESTION LOGO -------------------#
            question_logo = Canvas(self.main_frame, width=402, height=281,
                                   highlightthickness=0, bd=0, bg=self.fondo)
            question_logo.place(relx=0.5, rely=0.4, anchor=CENTER)
            question_logo.create_image(0, 0, anchor="nw", image=self.question_imagen_tk)

            nivel_juego = Frame(self.main_frame, bg=self.fondo)
            nivel_juego.place(relx=0.5, rely=0.7, anchor=CENTER)

            self.entry_var = StringVar()
            self.txt_palabra = Entry(nivel_juego, highlightthickness=1, relief='flat', font=('Tektur', 16), width=30)
            self.txt_palabra.grid(row=0, columnspan=2, pady=10)
            self.txt_palabra.focus()
            def convertir_a_mayusculas(event):
                texto_ingresado = self.txt_palabra.get().upper()
                self.txt_palabra.delete(0, 'end')
                self.txt_palabra.insert(0, texto_ingresado) 
            # Vincular el evento <Key> para convertir a mayúsculas mientras se escribe
            self.txt_palabra.bind('<KeyRelease>',convertir_a_mayusculas)
            self.txt_palabra.bind('<Return>', lambda event=None: enviar_palabras())

            #------------------- BOTONES PARA VOLVER, REINICIAR Y ENVIAR VALORES -------------------#
            self.option_buttons = Frame(nivel_juego, bg=self.fondo)
            self.option_buttons.grid(row=1, sticky=EW)

            self.btn_volver = CTkButton(self.option_buttons,
                                        text="\uf104 Volver",
                                        font=("Tektur", 15),
                                        bg_color=self.fondo,
                                        fg_color=self.azul,
                                        text_color='white',
                                        border_width=0,
                                        corner_radius=5,
                                        hover_color=self.hover,
                                        command=lambda:self.volver())
            self.btn_volver.grid(row=0, column=0, padx=3)
            self.btn_reiniciar = CTkButton(self.option_buttons,
                                           text="\uf01e Reiniciar",
                                           font=("Tektur", 15),
                                           bg_color=self.fondo,
                                           fg_color=self.azul,
                                           text_color='white',
                                           border_width=0,
                                           corner_radius=5,
                                           hover_color=self.hover,
                                           command=lambda:reiniciar_nivel_facil())
            self.btn_reiniciar.grid(row=0, column=1, padx=3)
            self.btn_enviar = CTkButton(self.option_buttons,
                                        text="\uf064 Enviar",
                                        font=("Tektur", 15),
                                        bg_color=self.fondo,
                                        fg_color=self.azul,
                                        text_color='white',
                                        border_width=0,
                                        corner_radius=5,
                                        hover_color=self.hover,
                                        command=lambda:enviar_palabras())
            self.btn_enviar.grid(row=0, column=2, padx=3)
        
        
        def setup_ganador():
            ruta_ganador_imagen = 'D:/Usuario/Desktop/PROGRAMACIÓN/PROYECTOS/MindDash/src/assets/ganador.png'

            ganador_imagen = Image.open(ruta_ganador_imagen)
            ganador_redimensionada = ganador_imagen.resize((512, 391))
            self.ganador_imagen_tk = ImageTk.PhotoImage(ganador_redimensionada)
        def setup_perdedor():
            ruta_perdedor_imagen = 'D:/Usuario/Desktop/PROGRAMACIÓN/PROYECTOS/MindDash/src/assets/perdedor.png'

            perdedor_imagen = Image.open(ruta_perdedor_imagen)
            perdedor_redimensionada = perdedor_imagen.resize((512, 391))
            self.perdedor_imagen_tk = ImageTk.PhotoImage(perdedor_redimensionada)        
        
        def GANADOR():
            setup_ganador()
            self.cartel_ganador = Canvas(self.main_frame, width=512, height=391, highlightthickness=0, bd=0)
            self.cartel_ganador.place(relx=0.5, rely=0.5, anchor=CENTER)
            self.cartel_ganador.create_image(0, 0, anchor="nw", image=self.ganador_imagen_tk) 
            self.cartel_ganador.after(3000, self.cartel_ganador.destroy)      
            self.cartel_ganador.bind("<Button-1>", lambda event: self.cartel_ganador.destroy())

        def PERDEDOR():
            setup_perdedor()
            self.cartel_perdedor = Canvas(self.main_frame, width=512, height=391, highlightthickness=0, bd=0)
            self.cartel_perdedor.place(relx=0.5, rely=0.5, anchor=CENTER)
            self.cartel_perdedor.create_image(0, 0, anchor="nw", image=self.perdedor_imagen_tk)           
            self.cartel_perdedor.after(3000, self.cartel_perdedor.destroy)      
            self.cartel_perdedor.bind("<Button-1>", lambda event: self.cartel_perdedor.destroy())
        
        
        def enviar_palabras():
            palabra_usuario = self.txt_palabra.get()

            if len(self.palabras_ingresadas) < len(palabras_mostradas):
                self.palabras_ingresadas.append(palabra_usuario)
                self.txt_palabra.delete(0, 'end')
                if len(self.palabras_ingresadas) == len(palabras_mostradas):
                    # Lista de palabras generadas por el algoritmo
                    palabras_generadas = [p.upper() for p in palabras_mostradas]

                    # Lista de palabras ingresadas por el usuario
                    palabras_usuario = [p.upper() for p in self.palabras_ingresadas]

                    # Verificar si las listas son iguales
                    if palabras_usuario == palabras_generadas:
                        GANADOR()
                    else:
                        PERDEDOR()
                    # Configurar el Entry en modo de solo lectura
                    self.txt_palabra.config(state='readonly')
                    self.palabras_ingresadas = []  
        inicio_juego()

        #------------------- BOTON REINICIAR -------------------#
        def reiniciar_nivel_facil():
            for widget in self.main_frame.winfo_children():
                widget.destroy()
            self.nivel_facil()

    def nivel_intermedio(self):
        self.main_frame.pack_forget() 
        self.setup_main_frame()
        
        palabras_mostradas = random.sample(palabras_faciles, 5)

        def inicio_juego():
            palabra_label = Label(self.main_frame, bg=self.fondo, font=("Tektur", 50), fg=self.azul)
            palabra_label.place(relx=0.5, rely=0.5, anchor=CENTER)
            palabra_label.config(text=palabras_mostradas[0])
            for palabra in palabras_mostradas:
                palabra_label.config(text=palabra)
                self.root.update()
                time.sleep(1.3)
                palabra_label.config(text="")
                self.root.update()
            palabra_label.destroy()

            
            #------------------- QUESTION LOGO -------------------#
            question_logo = Canvas(self.main_frame, width=402, height=281,
                                   highlightthickness=0, bd=0, bg=self.fondo)
            question_logo.place(relx=0.5, rely=0.4, anchor=CENTER)
            question_logo.create_image(0, 0, anchor="nw", image=self.question_imagen_tk)

            nivel_juego = Frame(self.main_frame, bg=self.fondo)
            nivel_juego.place(relx=0.5, rely=0.7, anchor=CENTER)

            self.entry_var = StringVar()
            self.txt_palabra = Entry(nivel_juego, highlightthickness=1, relief='flat', font=('Tektur', 16), width=30)
            self.txt_palabra.grid(row=0, columnspan=2, pady=10)
            self.txt_palabra.focus()
            def convertir_a_mayusculas(event):
                texto_ingresado = self.txt_palabra.get().upper()
                self.txt_palabra.delete(0, 'end')
                self.txt_palabra.insert(0, texto_ingresado) 
            # Vincular el evento <Key> para convertir a mayúsculas mientras se escribe
            self.txt_palabra.bind('<KeyRelease>',convertir_a_mayusculas)
            self.txt_palabra.bind('<Return>', lambda event=None: enviar_palabras())

            #------------------- BOTONES PARA VOLVER, REINICIAR Y ENVIAR VALORES -------------------#
            self.option_buttons = Frame(nivel_juego, bg=self.fondo)
            self.option_buttons.grid(row=1, sticky=EW)

            self.btn_volver = CTkButton(self.option_buttons,
                                        text="\uf104 Volver",
                                        font=("Tektur", 15),
                                        bg_color=self.fondo,
                                        fg_color=self.azul,
                                        text_color='white',
                                        border_width=0,
                                        corner_radius=5,
                                        hover_color=self.hover,
                                        command=lambda:self.volver())
            self.btn_volver.grid(row=0, column=0, padx=3)
            self.btn_reiniciar = CTkButton(self.option_buttons,
                                           text="\uf01e Reiniciar",
                                           font=("Tektur", 15),
                                           bg_color=self.fondo,
                                           fg_color=self.azul,
                                           text_color='white',
                                           border_width=0,
                                           corner_radius=5,
                                           hover_color=self.hover,
                                           command=lambda:reiniciar_nivel_intermedio())
            self.btn_reiniciar.grid(row=0, column=1, padx=3)
            self.btn_enviar = CTkButton(self.option_buttons,
                                        text="\uf064 Enviar",
                                        font=("Tektur", 15),
                                        bg_color=self.fondo,
                                        fg_color=self.azul,
                                        text_color='white',
                                        border_width=0,
                                        corner_radius=5,
                                        hover_color=self.hover,
                                        command=lambda:enviar_palabras())
            self.btn_enviar.grid(row=0, column=2, padx=3)
        
        
        def setup_ganador():
            ruta_ganador_imagen = 'D:/Usuario/Desktop/PROGRAMACIÓN/PROYECTOS/MindDash/src/assets/ganador.png'

            ganador_imagen = Image.open(ruta_ganador_imagen)
            ganador_redimensionada = ganador_imagen.resize((512, 391))
            self.ganador_imagen_tk = ImageTk.PhotoImage(ganador_redimensionada)
        def setup_perdedor():
            ruta_perdedor_imagen = 'D:/Usuario/Desktop/PROGRAMACIÓN/PROYECTOS/MindDash/src/assets/perdedor.png'

            perdedor_imagen = Image.open(ruta_perdedor_imagen)
            perdedor_redimensionada = perdedor_imagen.resize((512, 391))
            self.perdedor_imagen_tk = ImageTk.PhotoImage(perdedor_redimensionada)        
        
        def GANADOR():
            setup_ganador()
            self.cartel_ganador = Canvas(self.main_frame, width=512, height=391, highlightthickness=0, bd=0)
            self.cartel_ganador.place(relx=0.5, rely=0.5, anchor=CENTER)
            self.cartel_ganador.create_image(0, 0, anchor="nw", image=self.ganador_imagen_tk) 
            self.cartel_ganador.after(3000, self.cartel_ganador.destroy)      
            self.cartel_ganador.bind("<Button-1>", lambda event: self.cartel_ganador.destroy())

        def PERDEDOR():
            setup_perdedor()
            self.cartel_perdedor = Canvas(self.main_frame, width=512, height=391, highlightthickness=0, bd=0)
            self.cartel_perdedor.place(relx=0.5, rely=0.5, anchor=CENTER)
            self.cartel_perdedor.create_image(0, 0, anchor="nw", image=self.perdedor_imagen_tk)           
            self.cartel_perdedor.after(3000, self.cartel_perdedor.destroy)      
            self.cartel_perdedor.bind("<Button-1>", lambda event: self.cartel_perdedor.destroy())
        
        
        def enviar_palabras():
            palabra_usuario = self.txt_palabra.get()

            if len(self.palabras_ingresadas) < len(palabras_mostradas):
                self.palabras_ingresadas.append(palabra_usuario)
                self.txt_palabra.delete(0, 'end')
                if len(self.palabras_ingresadas) == len(palabras_mostradas):
                    # Lista de palabras generadas por el algoritmo
                    palabras_generadas = [p.upper() for p in palabras_mostradas]

                    # Lista de palabras ingresadas por el usuario
                    palabras_usuario = [p.upper() for p in self.palabras_ingresadas]

                    # Verificar si las listas son iguales
                    if palabras_usuario == palabras_generadas:
                        GANADOR()
                    else:
                        PERDEDOR()
                    # Configurar el Entry en modo de solo lectura
                    self.txt_palabra.config(state='readonly')
                    self.palabras_ingresadas = []  
        inicio_juego()

        #------------------- BOTON REINICIAR -------------------#
        def reiniciar_nivel_intermedio():
            for widget in self.main_frame.winfo_children():
                widget.destroy()
            self.nivel_intermedio()

    def nivel_avanzado(self):
        self.main_frame.pack_forget() 
        self.setup_main_frame()
        
        palabras_mostradas = random.sample(palabras_expertas, 5)

        def inicio_juego():
            palabra_label = Label(self.main_frame, bg=self.fondo, font=("Tektur", 50), fg=self.azul)
            palabra_label.place(relx=0.5, rely=0.5, anchor=CENTER)
            palabra_label.config(text=palabras_mostradas[0])
            for palabra in palabras_mostradas:
                palabra_label.config(text=palabra)
                self.root.update()
                time.sleep(1.2)
                palabra_label.config(text="")
                self.root.update()
            palabra_label.destroy()

            
            #------------------- QUESTION LOGO -------------------#
            question_logo = Canvas(self.main_frame, width=402, height=281,
                                   highlightthickness=0, bd=0, bg=self.fondo)
            question_logo.place(relx=0.5, rely=0.4, anchor=CENTER)
            question_logo.create_image(0, 0, anchor="nw", image=self.question_imagen_tk)

            nivel_juego = Frame(self.main_frame, bg=self.fondo)
            nivel_juego.place(relx=0.5, rely=0.7, anchor=CENTER)

            self.entry_var = StringVar()
            self.txt_palabra = Entry(nivel_juego, highlightthickness=1, relief='flat', font=('Tektur', 16), width=30)
            self.txt_palabra.grid(row=0, columnspan=2, pady=10)
            self.txt_palabra.focus()
            def convertir_a_mayusculas(event):
                texto_ingresado = self.txt_palabra.get().upper()
                self.txt_palabra.delete(0, 'end')
                self.txt_palabra.insert(0, texto_ingresado) 
            # Vincular el evento <Key> para convertir a mayúsculas mientras se escribe
            self.txt_palabra.bind('<KeyRelease>',convertir_a_mayusculas)
            self.txt_palabra.bind('<Return>', lambda event=None: enviar_palabras())

            #------------------- BOTONES PARA VOLVER, REINICIAR Y ENVIAR VALORES -------------------#
            self.option_buttons = Frame(nivel_juego, bg=self.fondo)
            self.option_buttons.grid(row=1, sticky=EW)

            self.btn_volver = CTkButton(self.option_buttons,
                                        text="\uf104 Volver",
                                        font=("Tektur", 15),
                                        bg_color=self.fondo,
                                        fg_color=self.azul,
                                        text_color='white',
                                        border_width=0,
                                        corner_radius=5,
                                        hover_color=self.hover,
                                        command=lambda:self.volver())
            self.btn_volver.grid(row=0, column=0, padx=3)
            self.btn_reiniciar = CTkButton(self.option_buttons,
                                           text="\uf01e Reiniciar",
                                           font=("Tektur", 15),
                                           bg_color=self.fondo,
                                           fg_color=self.azul,
                                           text_color='white',
                                           border_width=0,
                                           corner_radius=5,
                                           hover_color=self.hover,
                                           command=lambda:reiniciar_nivel_intermedio())
            self.btn_reiniciar.grid(row=0, column=1, padx=3)
            self.btn_enviar = CTkButton(self.option_buttons,
                                        text="\uf064 Enviar",
                                        font=("Tektur", 15),
                                        bg_color=self.fondo,
                                        fg_color=self.azul,
                                        text_color='white',
                                        border_width=0,
                                        corner_radius=5,
                                        hover_color=self.hover,
                                        command=lambda:enviar_palabras())
            self.btn_enviar.grid(row=0, column=2, padx=3)
        
        
        def setup_ganador():
            ruta_ganador_imagen = 'D:/Usuario/Desktop/PROGRAMACIÓN/PROYECTOS/MindDash/src/assets/ganador.png'

            ganador_imagen = Image.open(ruta_ganador_imagen)
            ganador_redimensionada = ganador_imagen.resize((512, 391))
            self.ganador_imagen_tk = ImageTk.PhotoImage(ganador_redimensionada)
        def setup_perdedor():
            ruta_perdedor_imagen = 'D:/Usuario/Desktop/PROGRAMACIÓN/PROYECTOS/MindDash/src/assets/perdedor.png'

            perdedor_imagen = Image.open(ruta_perdedor_imagen)
            perdedor_redimensionada = perdedor_imagen.resize((512, 391))
            self.perdedor_imagen_tk = ImageTk.PhotoImage(perdedor_redimensionada)        
        
        def GANADOR():
            setup_ganador()
            self.cartel_ganador = Canvas(self.main_frame, width=512, height=391, highlightthickness=0, bd=0)
            self.cartel_ganador.place(relx=0.5, rely=0.5, anchor=CENTER)
            self.cartel_ganador.create_image(0, 0, anchor="nw", image=self.ganador_imagen_tk) 
            self.cartel_ganador.after(3000, self.cartel_ganador.destroy)      
            self.cartel_ganador.bind("<Button-1>", lambda event: self.cartel_ganador.destroy())

        def PERDEDOR():
            setup_perdedor()
            self.cartel_perdedor = Canvas(self.main_frame, width=512, height=391, highlightthickness=0, bd=0)
            self.cartel_perdedor.place(relx=0.5, rely=0.5, anchor=CENTER)
            self.cartel_perdedor.create_image(0, 0, anchor="nw", image=self.perdedor_imagen_tk)           
            self.cartel_perdedor.after(3000, self.cartel_perdedor.destroy)      
            self.cartel_perdedor.bind("<Button-1>", lambda event: self.cartel_perdedor.destroy())
        
        
        def enviar_palabras():
            palabra_usuario = self.txt_palabra.get()

            if len(self.palabras_ingresadas) < len(palabras_mostradas):
                self.palabras_ingresadas.append(palabra_usuario)
                self.txt_palabra.delete(0, 'end')
                if len(self.palabras_ingresadas) == len(palabras_mostradas):
                    # Lista de palabras generadas por el algoritmo
                    palabras_generadas = [p.upper() for p in palabras_mostradas]

                    # Lista de palabras ingresadas por el usuario
                    palabras_usuario = [p.upper() for p in self.palabras_ingresadas]

                    # Verificar si las listas son iguales
                    if palabras_usuario == palabras_generadas:
                        GANADOR()
                    else:
                        PERDEDOR()
                    # Configurar el Entry en modo de solo lectura
                    self.txt_palabra.config(state='readonly')
                    self.palabras_ingresadas = []  
        inicio_juego()

        #------------------- BOTON REINICIAR -------------------#
        def reiniciar_nivel_intermedio():
            for widget in self.main_frame.winfo_children():
                widget.destroy()
            self.nivel_intermedio()

    def nivel_experto(self):
        self.main_frame.pack_forget() 
        self.setup_main_frame()
        
        palabras_mostradas = random.sample(palabras_expertas, 4)

        def inicio_juego():
            palabra_label = Label(self.main_frame, bg=self.fondo, font=("Tektur", 50), fg=self.azul)
            palabra_label.place(relx=0.5, rely=0.5, anchor=CENTER)
            palabra_label.config(text=palabras_mostradas[0])
            for palabra in palabras_mostradas:
                palabra_label.config(text=palabra)
                self.root.update()
                time.sleep(1)
                palabra_label.config(text="")
                self.root.update()
            palabra_label.destroy()

            
            #------------------- QUESTION LOGO -------------------#
            question_logo = Canvas(self.main_frame, width=402, height=281,
                                   highlightthickness=0, bd=0, bg=self.fondo)
            question_logo.place(relx=0.5, rely=0.4, anchor=CENTER)
            question_logo.create_image(0, 0, anchor="nw", image=self.question_imagen_tk)

            nivel_juego = Frame(self.main_frame, bg=self.fondo)
            nivel_juego.place(relx=0.5, rely=0.7, anchor=CENTER)

            self.entry_var = StringVar()
            self.txt_palabra = Entry(nivel_juego, highlightthickness=1, relief='flat', font=('Tektur', 16), width=30)
            self.txt_palabra.grid(row=0, columnspan=2, pady=10)
            self.txt_palabra.focus()
            def convertir_a_mayusculas(event):
                texto_ingresado = self.txt_palabra.get().upper()
                self.txt_palabra.delete(0, 'end')
                self.txt_palabra.insert(0, texto_ingresado) 
            # Vincular el evento <Key> para convertir a mayúsculas mientras se escribe
            self.txt_palabra.bind('<KeyRelease>',convertir_a_mayusculas)
            self.txt_palabra.bind('<Return>', lambda event=None: enviar_palabras())

            #------------------- BOTONES PARA VOLVER, REINICIAR Y ENVIAR VALORES -------------------#
            self.option_buttons = Frame(nivel_juego, bg=self.fondo)
            self.option_buttons.grid(row=1, sticky=EW)

            self.btn_volver = CTkButton(self.option_buttons,
                                        text="\uf104 Volver",
                                        font=("Tektur", 15),
                                        bg_color=self.fondo,
                                        fg_color=self.azul,
                                        text_color='white',
                                        border_width=0,
                                        corner_radius=5,
                                        hover_color=self.hover,
                                        command=lambda:self.volver())
            self.btn_volver.grid(row=0, column=0, padx=3)
            self.btn_reiniciar = CTkButton(self.option_buttons,
                                           text="\uf01e Reiniciar",
                                           font=("Tektur", 15),
                                           bg_color=self.fondo,
                                           fg_color=self.azul,
                                           text_color='white',
                                           border_width=0,
                                           corner_radius=5,
                                           hover_color=self.hover,
                                           command=lambda:reiniciar_nivel_intermedio())
            self.btn_reiniciar.grid(row=0, column=1, padx=3)
            self.btn_enviar = CTkButton(self.option_buttons,
                                        text="\uf064 Enviar",
                                        font=("Tektur", 15),
                                        bg_color=self.fondo,
                                        fg_color=self.azul,
                                        text_color='white',
                                        border_width=0,
                                        corner_radius=5,
                                        hover_color=self.hover,
                                        command=lambda:enviar_palabras())
            self.btn_enviar.grid(row=0, column=2, padx=3)
        
        
        def setup_ganador():
            ruta_ganador_imagen = 'D:/Usuario/Desktop/PROGRAMACIÓN/PROYECTOS/MindDash/src/assets/ganador.png'

            ganador_imagen = Image.open(ruta_ganador_imagen)
            ganador_redimensionada = ganador_imagen.resize((512, 391))
            self.ganador_imagen_tk = ImageTk.PhotoImage(ganador_redimensionada)
        def setup_perdedor():
            ruta_perdedor_imagen = 'D:/Usuario/Desktop/PROGRAMACIÓN/PROYECTOS/MindDash/src/assets/perdedor.png'

            perdedor_imagen = Image.open(ruta_perdedor_imagen)
            perdedor_redimensionada = perdedor_imagen.resize((512, 391))
            self.perdedor_imagen_tk = ImageTk.PhotoImage(perdedor_redimensionada)        
        
        def GANADOR():
            setup_ganador()
            self.cartel_ganador = Canvas(self.main_frame, width=512, height=391, highlightthickness=0, bd=0)
            self.cartel_ganador.place(relx=0.5, rely=0.5, anchor=CENTER)
            self.cartel_ganador.create_image(0, 0, anchor="nw", image=self.ganador_imagen_tk) 
            self.cartel_ganador.after(3000, self.cartel_ganador.destroy)      
            self.cartel_ganador.bind("<Button-1>", lambda event: self.cartel_ganador.destroy())

        def PERDEDOR():
            setup_perdedor()
            self.cartel_perdedor = Canvas(self.main_frame, width=512, height=391, highlightthickness=0, bd=0)
            self.cartel_perdedor.place(relx=0.5, rely=0.5, anchor=CENTER)
            self.cartel_perdedor.create_image(0, 0, anchor="nw", image=self.perdedor_imagen_tk)           
            self.cartel_perdedor.after(3000, self.cartel_perdedor.destroy)      
            self.cartel_perdedor.bind("<Button-1>", lambda event: self.cartel_perdedor.destroy())
        
        
        def enviar_palabras():
            palabra_usuario = self.txt_palabra.get()

            if len(self.palabras_ingresadas) < len(palabras_mostradas):
                self.palabras_ingresadas.append(palabra_usuario)
                self.txt_palabra.delete(0, 'end')
                if len(self.palabras_ingresadas) == len(palabras_mostradas):
                    # Lista de palabras generadas por el algoritmo
                    palabras_generadas = [p.upper() for p in palabras_mostradas]

                    # Lista de palabras ingresadas por el usuario
                    palabras_usuario = [p.upper() for p in self.palabras_ingresadas]

                    # Verificar si las listas son iguales
                    if palabras_usuario == palabras_generadas:
                        GANADOR()
                    else:
                        PERDEDOR()
                    # Configurar el Entry en modo de solo lectura
                    self.txt_palabra.config(state='readonly')
                    self.palabras_ingresadas = []  
        inicio_juego()

        #------------------- BOTON REINICIAR -------------------#
        def reiniciar_nivel_intermedio():
            for widget in self.main_frame.winfo_children():
                widget.destroy()
            self.nivel_intermedio()

    #------------------- BOTON VOLVER -------------------#
    def volver(self):
        for widget in self.main_frame.winfo_children():
            widget.destroy()
        # Vuelve a configurar el frame principal con el menú principal
        self.setup_logo()
        self.setup_buttons()
    
    def press_salir(self):
            self.root.destroy()   
   
    def mainloop(self):
        self.root.mainloop()

if __name__ == "__main__":
    mind_dash = MindDash()
    mind_dash.mainloop()