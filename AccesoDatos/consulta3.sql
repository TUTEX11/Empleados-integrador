SELECT t.denominacion, COUNT(e.id_tipo_empleado)
FROM empleados e JOIN tipo_empleado t
WHERE e.id_tipo_empleado = t.id
GROUP BY e.id_tipo_empleado;