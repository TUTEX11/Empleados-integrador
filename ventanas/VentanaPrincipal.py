from tkinter import *


class VentanaPrincipal:
    def __init__(self) -> None:
        self.ventana = Tk()
        self.ventana.title('Ventana Principal')
        self.ventana.geometry('900x700')

        fuente = 'Book Antiqua'

        Label(self.ventana, text='Empleados', font=(fuente, 20)).place(relx=0.5, rely=0.1, anchor=CENTER)

        Label(self.ventana, text='Lista de empleados:', font=(fuente, 12)).place(relx=0.5, rely=0.2, anchor=CENTER)

        self.barra_menu = Menu(self.ventana)
        self.empleados = Menu(self.barra_menu)
        self.empleados.add_command(label='Mostrar Obreros')
        self.empleados.add_command(label='Mostrar Administrativos')
        self.empleados.add_command(label='Mostrar Vendedores')
        self.empleados.add_separator()
        self.barra_menu.add_cascade(label='Empleados', menu=self.empleados)

        self.lst_empleados = Listbox(self.ventana, height=20, width=100)
        self.lst_empleados.place(relx=0.5, rely=0.5, anchor=CENTER)

        self.btn_alta = Button(self.ventana, text='Alta', font=(fuente, 12), height=3, width=15)
        self.btn_alta.place(relx=0.15, rely=0.85, anchor=CENTER)

        self.btn_baja = Button(self.ventana, text='Baja', font=(fuente, 12), height=3, width=15)
        self.btn_baja.place(relx=0.3833, rely=0.85, anchor=CENTER)

        self.btn_buscar = Button(self.ventana, text='Buscar', font=(fuente, 12), height=3, width=15)
        self.btn_buscar.place(relx=0.6166, rely=0.85, anchor=CENTER)

        self.btn_salir = Button(self.ventana, text='Salir', font=(fuente, 12), height=3, width=15, command=self.salir)
        self.btn_salir.place(relx=0.85, rely=0.85, anchor=CENTER)

    def mostrar(self):
        self.ventana.config(menu=self.barra_menu)
        self.ventana.mainloop()
    
    def salir(self):
        self.ventana.destroy()
    
VentanaPrincipal().mostrar()