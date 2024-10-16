from tkinter import Label, Entry, Button, messagebox, Tk, CENTER
from gestores.Gestor import Gestor

class VentanaBuscar:
    def __init__(self, parent, callback) -> None: # TODO: Eliminar parametro parent y probar
        
        self.ventana = Tk()
        self.ventana.title('Buscar un empleado')
        self.ventana.geometry('500x400')
        self.ventana.config(padx=10, pady=10)
        self.gestor = Gestor()
        self.callback = callback
        
        self.fuente_12 = ('Book Antiqua', 12)
        self.lbl_title = Label(self.ventana, text='Buscar empleado', font=self.fuente_12)
        self.lbl_title.place(relx=0.5, rely=0.1, anchor=CENTER)

        Label(self.ventana, text='Ingrese el legajo del empleado:', font=self.fuente_12).place(relx=0.3, rely=0.4, anchor=CENTER)
        self.txt_legajo = Entry(self.ventana, font=self.fuente_12, width=16, validate='key', validatecommand=(self.ventana.register(self.validar_numero), '%S'))
        self.txt_legajo.place(relx=0.7, rely=0.4, anchor=CENTER)

        self.btn_buscar = Button(self.ventana, text='Buscar', font=self.fuente_12, command=self.iniciarbuscarEmpleado)
        self.btn_buscar.place(relx=0.4, rely=0.6, anchor=CENTER)

        self.btn_cancelar = Button(self.ventana, text='Cancelar', font=self.fuente_12, command=self.ventana.destroy)
        self.btn_cancelar.place(relx=0.6, rely=0.6, anchor=CENTER)

    def mostrar(self):
        self.ventana.mainloop()
    
    def iniciarbuscarEmpleado(self):
        if (legajo := self.txt_legajo.get()) != '':
            if (empleado := self.gestor.buscarEmpleado(int(legajo))) is None:
                messagebox.showerror('Error', 'Empleado no encontrado.')
                self.salir()
                return
            messagebox.showinfo('Empleado encontrado', str(empleado))
            self.callback(empleado)
            self.salir()
        else:
            messagebox.showerror('Error', 'Tenes que ingresar algun numero')
            
    def validar_numero(self, entrada):
        return entrada.isdigit()
    
    def salir(self):
        self.ventana.destroy()


