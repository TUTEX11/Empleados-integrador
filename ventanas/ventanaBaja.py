from tkinter import Tk, Button, Entry, Label, CENTER, messagebox
from gestores.Gestor import Gestor


class VentanaBaja:

    gestor = Gestor()

    def __init__(self):
        self.ventana = Tk()
        self.ventana.title("Dar de baja un empleado")
        self.ventana.geometry("400x300")

        self.fuente = ('Book Antiqua', 12)

        Label(self.ventana, text='Dar de baja un empleado', font=('Book Antiqua', 16)).place(relx=0.5, rely=0.1, anchor=CENTER)
    
        self.label = Label(self.ventana, text="Ingrese legajo:", font=self.fuente)
        self.label.place(relx=0.3, rely=0.5, anchor=CENTER)

        self.txt_legajo = Entry(self.ventana, font=self.fuente, width=10, validate='key', validatecommand=(self.ventana.register(self.validar_numero), '%S'))
        self.txt_legajo.place(relx=0.65, rely=0.5, anchor=CENTER)

        self.btn_cancelar = Button(self.ventana, text='Cancelar', font=self.fuente, width=10, command=self.cancelar)
        self.btn_cancelar.place(relx=0.25, rely=0.8, anchor=CENTER)

        self.btn_baja = Button(self.ventana, text='Dar de baja', font=self.fuente, width=10, command=self.iniciarBaja)
        self.btn_baja.place(relx=0.75, rely=0.8, anchor=CENTER)
    
    def validar_numero(self, entrada):
        return entrada.isdigit()
    
    def iniciarBaja(self):
        if self.validar_campo_vacio():
            legajo_dar_baja = int(self.txt_legajo.get())
            if (empleado := self.gestor.buscarEmpleado(legajo_dar_baja)) is None:
                messagebox.showerror('Error', 'Empleado no encontrado.')
                self.clear_entry()
                return
            if messagebox.askyesno('Empleado encontrado', f'Empleado encontrado: {str(empleado)} \nDesea darlo de baja del sistema?'):
                if self.gestor.eliminar(empleado):
                    messagebox.showinfo('Empleado dado de baja', 'Empleado dado de baja exitosamente.')
                    self.clear_entry()
                else:
                    messagebox.showerror('Error', 'No se pudo dar de baja al empleado.')
            self.clear_entry()
        else:
            messagebox.showerror('Error', 'Debe ingresar un legajo.')
        self.clear_entry()
        self.cancelar()

    def mostrar(self):
        self.ventana.mainloop()
    
    def cancelar(self):
        self.ventana.destroy()
    
    # clear the Entry
    def clear_entry(self):
        self.txt_legajo.delete(0, 'end')
    
    # validate Entry is not empty
    def validar_campo_vacio(self):
        return self.txt_legajo.get() != ''
    



