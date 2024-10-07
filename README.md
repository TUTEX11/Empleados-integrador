## ABM de empleados

Programar un abm de empleados según las consignas del ejercicio de la unidad 2.

Leer todo el archivo de empleados. El mismo posee los siguientes datos:

* Tipo de empleado (1: obrero, 2: administrativo, 3: vendedor).
* Legajo
* Nombre
* Apellido
* Sueldo básico
* La tercera columna depende del tipo de empleado, en el caso de los obreros indica la cantidad de días trabajados en el mes, en el caso de los administrativos indica si le corresponde cobrar presentismo y en el caso de los vendedores indica el importe total de ventas realizadas en mes.

Por cada tipo de empleados el sueldo se calcula de una forma diferente:

* En el caso de los obreros, el sueldo básico corresponde a un mes de 20 días laborables, y el sueldo a cobrar debe ser un propocional a la cantidad de días efectivamente trabajados.
* En el caso de los administrativos, el sueldo a cobrar es igual al básico, pero se incrementa en 13% si le corresponde cobrar el presentismo.
* Los vendedores cobrar el sueldo básico más un 1% del total vendido.

Luego de la carga:

* Calcular el total a pagar de sueldos
* Contar los empleados por tipo (tres totales)
* Buscar un empleado por legajo y mostrar el sueldo a pagar

Funcionalidades para terminar con la v1.0

Acoplar funcionalidades a los botones del menu right click -> TERMINADO
Implementar la funcionalidad de mostrar empleados por páginas -> TERMINADO

* Iniciar refactor con dataclasses y modulo logging

** FECHA FINAL DE LANZAMIENTO DE LA 1.0: 13/10/2024