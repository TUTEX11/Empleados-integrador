from tkinter import Label, Entry, Button, messagebox, Tk, CENTER, Checkbutton
from tkinter.ttk import Combobox
from gestores.Gestor import Gestor

class VentanaAlta:

    gestor = Gestor()

    def __init__(self) -> None:
        self.ventana = Tk()
        self.ventana.title('Dar de alta un empleado')
        self.ventana.geometry('900x700')
        self.opciones = {
            0 : self.mostrar_obrero,
            1 : self.mostrar_administrativo,
            2 : self.mostrar_vendedor
        }
        

        self.vcmd = (self.ventana.register(self.solo_numeros), '%P')

        self.fuente_12 = ('Book Antiqua', 12)

        Label(self.ventana, text='Dar de alta empleado en el sistema', font=('Book Antiqua', 20)).place(relx=0.5, rely=0.1, anchor=CENTER)

        Label(self.ventana, text='Selecciona tipo de empleado:', font=self.fuente_12).place(relx=0.3, rely=0.2, anchor=CENTER)

        self.cmb_tipo = Combobox(self.ventana, font=self.fuente_12, width=25, state='readonly', values=('Obrero', 'Administrativo', 'Vendedor'))
        self.cmb_tipo.place(relx=0.545, rely=0.2, anchor=CENTER)
        self.cmb_tipo.bind("<<ComboboxSelected>>", self.selection_changed)

        Label(self.ventana, text='Ingrese el nombre:', font=self.fuente_12).place(relx=0.344, rely=0.3, anchor=CENTER)

        self.txt_nombre = Entry(self.ventana, width=25, font=self.fuente_12)
        self.txt_nombre.place(relx=0.545, rely=0.3, anchor=CENTER)

        Label(self.ventana, text='Ingrese el apellido:', font=self.fuente_12).place(relx=0.344, rely=0.4, anchor=CENTER)

        self.txt_apellido = Entry(self.ventana, width=25, font=self.fuente_12)
        self.txt_apellido.place(relx=0.545, rely=0.4, anchor=CENTER)

        Label(self.ventana, text='Ingrese el sueldo base:', font=self.fuente_12).place(relx=0.332, rely=0.5, anchor=CENTER)

        self.txt_sueldoBase = Entry(self.ventana, width=25, font=self.fuente_12, validate="key", validatecommand=self.vcmd)
        self.txt_sueldoBase.place(relx=0.545, rely=0.5, anchor=CENTER)

        self.btn_guardar = Button(self.ventana, text='Guardar', font=self.fuente_12, width=12, command=self.validarDatosEmpleado)
        self.btn_guardar.place(relx=0.4, rely=0.9, anchor=CENTER)

        self.btn_salir = Button(self.ventana, text='Salir', font=self.fuente_12, width=12, command=self.salir)
        self.btn_salir.place(relx=0.6, rely=0.9, anchor=CENTER)

        self.lbl_diasTrabajados = Label(self.ventana, text='Ingrese la cantidad de dias trabajados:', font=self.fuente_12)
        self.txt_diasTrabajados = Entry(self.ventana, font=self.fuente_12, width=10, validate="key", validatecommand=self.vcmd)

        self.chk_presentismo = Checkbutton(self.ventana, font=self.fuente_12, text='Presentismo')

        self.lbl_ventas = Label(self.ventana, text='Ingrese el monto de ventas:', font=self.fuente_12)
        self.txt_ventas = Entry(self.ventana, font=self.fuente_12, width=10, validate="key", validatecommand=self.vcmd)

        self.ocultar_todos()

    def validarDatosEmpleado(self):
        if self.cmb_tipo.current() == -1:
            messagebox.showerror('ERROR', 'Seleccione un tipo de empleado')
            return
        if self.validarCamposVacios():
            messagebox.showerror('ERROR', 'Debe completar todos los campos')
            return
        self.inciarGuardado()
    
    def inciarGuardado(self):
        datos = [self.txt_nombre.get(), self.txt_apellido.get(), float(self.txt_sueldoBase.get())]
        if self.cmb_tipo.current() == 0:
            datos.append(int(self.txt_diasTrabajados.get()))
            datos.append(1)
        elif self.cmb_tipo.current() == 1:
            datos.append(1 if self.chk_presentismo.get() else 0)
            datos.append(2)
        else:
            datos.append(float(self.txt_ventas.get()))
            datos.append(3)
        resultado = self.gestor.guardarEmpleado(datos)
        if resultado:
            messagebox.showinfo('Info', 'parece que se guardó bien perro fijate')
        else:
            messagebox.showerror('ERROR', 'pifiaste para la bosta nero no se guardio ni mierda')
        

    def solo_numeros(self, char):
        return char.isdigit() or char == ""

    def validarCamposVacios(self):
        return not(self.txt_nombre.get() and self.txt_apellido.get() and self.txt_sueldoBase.get())

    def selection_changed(self, event):
        indice_selected = self.cmb_tipo.current()
        self.opciones[indice_selected]()

    def mostrar_obrero(self):
        self.lbl_diasTrabajados.place(relx=0.273, rely=0.7, anchor=CENTER)
        self.txt_diasTrabajados.place(relx=0.489, rely=0.7, anchor=CENTER)

        self.ocultar_administrativo()
        self.ocultar_vendedor()

    def mostrar_administrativo(self):
        self.chk_presentismo.place(relx=0.5, rely=0.7, anchor=CENTER)

        self.ocultar_obrero()
        self.ocultar_vendedor()

    def mostrar_vendedor(self):
        self.lbl_ventas.place(relx=0.325, rely=0.7, anchor=CENTER)
        self.txt_ventas.place(relx=0.489, rely=0.7, anchor=CENTER)
        
        self.ocultar_obrero()
        self.ocultar_administrativo()
    
    def ocultar_obrero(self):
        self.lbl_diasTrabajados.place_forget()
        self.txt_diasTrabajados.place_forget()
    
    def ocultar_administrativo(self):
        self.chk_presentismo.place_forget()
    
    def ocultar_vendedor(self):
        self.lbl_ventas.place_forget()
        self.txt_ventas.place_forget()
    
    def ocultar_todos(self):
        self.ocultar_obrero()
        self.ocultar_administrativo()
        self.ocultar_vendedor()

    def mostrar(self):
        self.ventana.mainloop()
    
    def salir(self):
        self.ventana.destroy()

