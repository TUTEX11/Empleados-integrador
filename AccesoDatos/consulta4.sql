SELECT e.legajo, e.nombre, e.apellido, e.sueldo_basico,
       CASE 
           WHEN o.cant_dias_trabajados IS NOT NULL THEN o.cant_dias_trabajados
           WHEN a.presentismo IS NOT NULL THEN a.presentismo
           WHEN v.ventas IS NOT NULL THEN v.ventas
       END AS detalle, e.id_tipo_empleado
FROM empleados e
LEFT JOIN dias_trabajados_obreros o ON e.legajo = o.legajo
LEFT JOIN presentismo_administrativos a ON e.legajo = a.legajo
LEFT JOIN ventas_vendedores v ON e.legajo = v.legajo
LIMIT ?
OFFSET ?;