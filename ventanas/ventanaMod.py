from tkinter import Label, Entry, Button, messagebox, CENTER, Tk, StringVar, IntVar, DoubleVar
from gestores.Gestor import Gestor

class VentanaModificacion:
    def __init__(self, un_empleado) -> None:
        self.ventana = Tk()
        self.ventana.title('Modificar un empleado')
        self.ventana.geometry('500x400')
        self.ventana.config(padx=10, pady=10)
        self.empleado = un_empleado
        self.gestor = Gestor()
        self.map_tipo = {
            1: 'Obrero',
            2: 'Administrativo',
            3: 'Vendedor'
        }

        self.fuente_12 = ('Book Antiqua', 12)
        self.lbl_title = Label(self.ventana, text=f'Modificar empleado tipo {self.map_tipo[self.empleado.get_tipo_empleado()]}', font=self.fuente_12)
        self.lbl_title.place(relx=0.5, rely=0.1, anchor=CENTER)
        
        Label(self.ventana, text='Legajo:', font=self.fuente_12).place(relx=0.1, rely=0.2, anchor=CENTER)
        self.var_txt_legajo = StringVar(self.ventana)
        self.var_txt_legajo.set(self.empleado.get_legajo())
        self.txt_legajo = Entry(self.ventana, font=self.fuente_12, width=10, textvariable=self.var_txt_legajo)
        self.txt_legajo.place(relx=0.5, rely=0.2, anchor=CENTER)
        
        Label(self.ventana, text='Nombre:', font=self.fuente_12).place(relx=0.1, rely=0.4, anchor=CENTER)
        self.var_txt_nombre = StringVar(self.ventana)
        self.var_txt_nombre.set(self.empleado.get_nombre())
        self.txt_nombre = Entry(self.ventana, font=self.fuente_12, width=25, textvariable=self.var_txt_nombre)
        self.txt_nombre.place(relx=0.5, rely=0.4, anchor=CENTER)
        
        Label(self.ventana, text='Apellido:', font=self.fuente_12).place(relx=0.1, rely=0.5, anchor=CENTER)
        self.var_txt_apellido = StringVar(self.ventana)
        self.var_txt_apellido.set(self.empleado.get_apellido())
        self.txt_apellido = Entry(self.ventana, font=self.fuente_12, width=25, textvariable=self.var_txt_apellido)
        self.txt_apellido.place(relx=0.5, rely=0.5, anchor=CENTER)
        
        Label(self.ventana, text='Sueldo base:', font=self.fuente_12).place(relx=0.1, rely=0.6, anchor=CENTER)
        self.var_txt_sueldo = DoubleVar(self.ventana)
        self.var_txt_sueldo.set(self.empleado.get_sueldo_basico())
        self.txt_sueldo = Entry(self.ventana, font=self.fuente_12, width=25, textvariable=self.var_txt_sueldo)
        self.txt_sueldo.place(relx=0.5, rely=0.6, anchor=CENTER)
        
        self.btn_guardar = Button(self.ventana, text='Guardar', font=self.fuente_12, command=self.guardar_datos)
        self.btn_guardar.place(relx=0.35, rely=0.8, anchor=CENTER)
        
        self.btn_salir = Button(self.ventana, text='Salir', font=self.fuente_12, command=self.salir)
        self.btn_salir.place(relx=0.65, rely=0.8, anchor=CENTER)
                                                     
    def mostrar(self):
        self.ventana.mainloop()
    
    def salir(self):
        self.ventana.destroy()
    
    def guardar_datos(self):
        legajo = self.txt_legajo.get()
        nombre = self.txt_nombre.get()
        apellido = self.txt_apellido.get()
        sueldo_base = float(self.txt_sueldo.get())
        tipo = self.txt_tipo.get()
        
        if self.gestor.modificar_datos_empleado(legajo, nombre, apellido, sueldo_base, tipo):
            messagebox.showinfo('Modificación exitosa', 'Los datos del empleado han sido modificados correctamente.')
            self.salir()
        else:
            messagebox.showerror('Error al modificar', 'Hubo un error al modificar los datos del empleado.')