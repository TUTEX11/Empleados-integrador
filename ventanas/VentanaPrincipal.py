from tkinter import Tk, Label, CENTER, Listbox, Menu, Button, END, messagebox
from .ventanaAlta import VentanaAlta
from .ventanaBuscar import VentanaBuscar
from .ventanaBaja import VentanaBaja
from .ventanaReporteTipo import VentanaReporteTipo
from gestores.Gestor import Gestor


class VentanaPrincipal:

    gestor = Gestor()
    def __init__(self) -> None:
        self.ventana = Tk()
        self.ventana.title('Ventana Principal')
        self.ventana.geometry('900x700')

        fuente = 'Book Antiqua'
        fuente_12 = ('Book Antiqua', 12) 

        Label(self.ventana, text='Empleados', font=(fuente, 20)).place(relx=0.5, rely=0.1, anchor=CENTER)

        Label(self.ventana, text='Lista de empleados:', font=fuente_12).place(relx=0.5, rely=0.2, anchor=CENTER)

        self.barra_menu = Menu(self.ventana)
        self.empleados = Menu(self.barra_menu)
        self.reportes = Menu(self.barra_menu)
        self.empleados.add_command(label='Mostrar Obreros')
        self.empleados.add_command(label='Mostrar Administrativos')
        self.empleados.add_command(label='Mostrar Vendedores')
        self.empleados.add_separator()
        self.barra_menu.add_cascade(label='Empleados', menu=self.empleados)
        self.reportes.add_command(label='Calcular total sueldos a pagar', command=self.iniciarCalculoTotalSueldos)
        self.barra_menu.add_cascade(label='Reportes', menu=self.reportes)
        self.reportes.add_command(label='Reporte de empleados por puesto', command=self.iniciarReporteEmpleadosPorPuesto)

        self.lst_empleados = Listbox(self.ventana, height=20, width=100)
        self.lst_empleados.place(relx=0.5, rely=0.5, anchor=CENTER)

        self.btn_alta = Button(self.ventana, text='Alta', font=fuente_12, height=3, width=15, command=self.iniciarAlta)
        self.btn_alta.place(relx=0.15, rely=0.9, anchor=CENTER)

        self.btn_baja = Button(self.ventana, text='Baja', font=fuente_12, height=3, width=15, command=self.iniciarBaja)
        self.btn_baja.place(relx=0.3833, rely=0.9, anchor=CENTER)

        self.btn_buscar = Button(self.ventana, text='Buscar', font=fuente_12, height=3, width=15, command=self.iniciarBusqueda)
        self.btn_buscar.place(relx=0.6166, rely=0.9, anchor=CENTER)

        self.btn_salir = Button(self.ventana, text='Salir', font=fuente_12, height=3, width=15, command=self.salir)
        self.btn_salir.place(relx=0.85, rely=0.9, anchor=CENTER)

        self.btn_anterior = Button(self.ventana, text='anterior', font=fuente_12, height=1, width=10)
        self.btn_anterior.place(relx=0.63, rely=0.76, anchor=CENTER)

        self.btn_siguiente = Button(self.ventana, text='siguiente', font=fuente_12, height=1, width=10)
        self.btn_siguiente.place(relx=0.77, rely=0.76, anchor=CENTER)

    def mostrar(self):
        self.ventana.config(menu=self.barra_menu)
        self.ventana.mainloop()
    
    def iniciarAlta(self):
        VentanaAlta().mostrar()
    
    def salir(self):
        self.ventana.destroy()

    def iniciarBusqueda(self):
        self.clearListbox()
        VentanaBuscar(self, self.recibirEmpleado)
    
    def recibirEmpleado(self, empleado):
        self.lst_empleados.insert(END, str(empleado))
    
    def iniciarBaja(self):
        VentanaBaja().mostrar()
    
    def clearListbox(self):
        self.lst_empleados.delete(0, END)

    def iniciarCalculoTotalSueldos(self):
        total_sueldos = self.gestor.calcularTotalSueldos()
        messagebox.showinfo('Total Sueldos', f'El total de sueldos a pagar es: ${total_sueldos:.2f}')
    
    def iniciarReporteEmpleadosPorPuesto(self):
        reporte = self.gestor.reportePorTipo()
        ventanaReporte = VentanaReporteTipo(reporte)
        ventanaReporte.mostrar()