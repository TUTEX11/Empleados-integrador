from tkinter import *
from tkinter.ttk import Combobox

class VentanaAlta:
    def __init__(self) -> None:
        self.ventana = Tk()
        self.ventana.title('Dar de alta un empleado')
        self.ventana.geometry('900x700')

        fuente = 'Book Antiqua'
        fuente_12 = ('Book Antiqua', 12) 

        Label(self.ventana, text='Dar de alta empleado en el sistema', font=(fuente, 20)).place(relx=0.5, rely=0.1, anchor=CENTER)

        self.lbl_tipo = Label(self.ventana, text='Selecciona tipo de empleado:', font=fuente_12)
        self.lbl_tipo.place(relx=0.3, rely=0.2, anchor=CENTER)

        self.cmb_tipo = Combobox(self.ventana, font=fuente_12, width=25)
        self.cmb_tipo.place(relx=0.545, rely=0.2, anchor=CENTER)


    
    def mostrar(self):
        self.ventana.mainloop()

VentanaAlta().mostrar()

