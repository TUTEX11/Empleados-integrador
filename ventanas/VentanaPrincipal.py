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
        self.paginaActual = 0

        fuente = 'Book Antiqua'
        fuente_12 = ('Book Antiqua', 12) 

        Label(self.ventana, text='Empleados', font=(fuente, 20)).place(relx=0.5, rely=0.1, anchor=CENTER)

        Label(self.ventana, text='Lista de empleados:', font=fuente_12).place(relx=0.5, rely=0.2, anchor=CENTER)

        self.barra_menu = Menu(self.ventana)

        self.empleados = Menu(self.barra_menu)
        self.barra_menu.add_cascade(label='Empleados', menu=self.empleados)
        self.empleados.add_command(label='Mostrar Obreros')
        self.empleados.add_command(label='Mostrar Administrativos')
        self.empleados.add_command(label='Mostrar Vendedores')

        self.reportes = Menu(self.barra_menu)
        self.barra_menu.add_cascade(label='Reportes', menu=self.reportes)
        self.reportes.add_command(label='Calcular total sueldos a pagar', command=self.iniciarCalculoTotalSueldos)
        self.reportes.add_command(label='Reporte de empleados por puesto', command=self.iniciarReporteEmpleadosPorPuesto)

        self.lst_empleados = Listbox(self.ventana, height=20, width=120)
        self.lst_empleados.place(relx=0.5, rely=0.5, anchor=CENTER)

        self.menu_lista = Menu(self.lst_empleados, tearoff=0)
        self.menu_lista.add_command(label='Eliminar')
        self.menu_lista.add_command(label='Modificar')
        self.menu_lista.add_command(label='Calcular sueldo total', command=self.mostrarSueldoTotalEmpleado)
        self.lst_empleados.bind('<Button-3>', self.mostrar_menu_lista)

        self.btn_alta = Button(self.ventana, text='Alta', font=fuente_12, height=3, width=15, command=self.iniciarAlta)
        self.btn_alta.place(relx=0.15, rely=0.9, anchor=CENTER)

        self.btn_baja = Button(self.ventana, text='Baja', font=fuente_12, height=3, width=15, command=self.iniciarBaja)
        self.btn_baja.place(relx=0.3833, rely=0.9, anchor=CENTER)

        self.btn_buscar = Button(self.ventana, text='Buscar', font=fuente_12, height=3, width=15, command=self.iniciarBusqueda)
        self.btn_buscar.place(relx=0.6166, rely=0.9, anchor=CENTER)

        self.btn_salir = Button(self.ventana, text='Salir', font=fuente_12, height=3, width=15, command=self.salir)
        self.btn_salir.place(relx=0.85, rely=0.9, anchor=CENTER)

        self.btn_anterior = Button(self.ventana, text='<', font=fuente_12, height=1, width=4, command=self.anterior_pagina)
        self.btn_anterior.place(relx=0.74, rely=0.76, anchor=CENTER)

        self.btn_siguiente = Button(self.ventana, text='>', font=fuente_12, height=1, width=4, command=self.siguiente_pagina)
        self.btn_siguiente.place(relx=0.81, rely=0.76, anchor=CENTER)

        self.max_paginas = self.gestor.getMaxPageCount()

        self.obtenerEmpleadosPagina()

    def mostrar(self):
        self.ventana.config(menu=self.barra_menu)
        self.ventana.mainloop()
    
    def obtenerEmpleadosPagina(self):
        self.clearListbox()
        empleados_pagina = self.gestor.generarPaginaEmpleados(self.paginaActual)
        for empleado in empleados_pagina:
            self.lst_empleados.insert(END, empleado)
    
    def siguiente_pagina(self):
        if self.paginaActual < self.max_paginas:
            self.paginaActual += 1
            self.obtenerEmpleadosPagina()

    def anterior_pagina(self):
        if self.paginaActual > 0:
            self.paginaActual -= 1
            self.obtenerEmpleadosPagina() 
    
    def mostrar_menu_lista(self, event):
        try:
            self.lst_empleados.selection_clear(0, END)
            index = self.lst_empleados.nearest(event.y)
            self.lst_empleados.selection_set(index)
            self.menu_lista.tk_popup(event.x_root, event.y_root)
        finally:
            self.menu_lista.grab_release()
    
    def iniciarAlta(self):
        VentanaAlta().mostrar()
    
    def salir(self):
        self.ventana.destroy()

    def iniciarBusqueda(self):
        self.clearListbox()
        VentanaBuscar(self, self.recibirEmpleado)
    
    def recibirEmpleado(self, empleado):
        self.lst_empleados.insert(END, empleado)
    
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
    
    def mostrarSueldoTotalEmpleado(self):
        seleccion = self.lst_empleados.curselection()
        if seleccion:
            indice = seleccion[0]
            empleado = self.gestor.devolverEmpleadoLista(indice)
            messagebox.showinfo('Sueldo de empleado', f'El sueldo total de este empleado es de: $ {empleado.calcularSueldo():.2f}')
        else:
            messagebox.showerror('ERROR', 'Seleccione un empleado')