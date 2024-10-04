from tkinter import Tk, Label, Button, CENTER

class VentanaReporteTipo:

    def __init__(self, reporte: dict) -> None:
        self.ventana = Tk()
        self.ventana.title('Reporte Cantidad de Empleados por tipo')
        self.ventana.geometry('300x300')

        texto = f''
        for tipo, cantidad in reporte.items():
            texto += f'{tipo}: {cantidad}\n'
        
        Label(self.ventana, text=texto, font=('Book Antiqua', 12)).place(relx=0.5, rely=0.5, anchor=CENTER)

        self.btn_cerrar = Button(self.ventana, text='Cerrar', font=('Book Antiqua', 12), width=10, command=self.cerrar)
        self.btn_cerrar.place(relx=0.5, rely=0.8, anchor=CENTER)
    
    def mostrar(self):
        self.ventana.mainloop()
    
    def cerrar(self):
        self.ventana.destroy()
    