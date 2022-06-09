SELECT  b.id
       ,p.nombre AS pasajero
       ,p.nombre AS conductor
       ,e.fecha
       ,v.fecha
       ,v.silla
       ,v.placa
       ,v.tarifa
       ,c.tipo   AS origen
       ,c.tipo AS destino
FROM boleto AS b, persona AS p, expedicion AS e, viaje AS v, ciudad AS c
WHERE p.identificacion = b.ident_pasajero
AND p.identificacion = b.ident_conductor
AND e.id = b.id_expedicion
AND v.numero = b.num_viaje
AND c.id = v.id_ciudad_origen
AND c.id = v.id_ciudad_destino

SELECT 
       a.id, a.pasajero, b.conductor, a.expedicion, b.viaje, a.silla, a.placa, a.tarifa, a.origen, b.destino

FROM (
    SELECT b.id, e.fecha AS expedicion, v.silla, v.placa, v.tarifa, c.tipo AS origen, CONCAT(p.nombre, ' ', p.apellido) AS pasajero
    FROM persona AS p
    INNER JOIN boleto AS b ON p.identificacion = b.ident_pasajero
    INNER JOIN expedicion AS e ON b.id_expedicion = e.id
    INNER JOIN viaje AS v ON b.num_viaje = v.numero
    INNER JOIN ciudad AS c ON v.id_ciudad_origen = c.id
) a
INNER JOIN (
    SELECT b.id, c.tipo AS destino, v.fecha AS viaje, CONCAT(p.nombre, ' ',p.apellido) AS conductor
    FROM persona AS p
    INNER JOIN boleto AS b ON p.identificacion = b.ident_conductor
    INNER JOIN viaje AS v ON b.num_viaje = v.numero
    INNER JOIN ciudad AS c ON v.id_ciudad_destino = c.id
) b ON a.id = b.id

SELECT b.id, p.nombre AS pasajero, p.nombre AS conductor, v.fecha, v.silla, v.placa, v.tarifa 
FROM boleto AS b, persona AS p, viaje AS v
WHERE b.ident_pasajero = p.identificacion
AND b.ident_pasajero = p.identificacion
AND b.num_viaje = v.numero

UPDATE persona SET id_tipo_per = 1 WHERE identificacion = 9

UPDATE persona SET nombre = 'Diego', apellido = 'Torres', email = 'diego@gmail.com', telefono = 321145525, id_tipo_per = 2, id_tipo_doc = 2 WHERE identificacion = 9

UPDATE persona SET nombre = 'Diego', apellido = 'Torres', email = 'diego@gmail.com', telefono = 321145525, id_tipo_per = 2, id_tipo_doc = 2 WHERE identificacion = 9

SELECT o.numero, o.fecha, o.silla, o.placa, o.tarifa, o.ciudad AS origen, d.ciudad AS destino
FROM (
    SELECT v.numero, c.tipo AS ciudad, v.fecha, v.silla, v.placa, v.tarifa 
    FROM viaje AS v
    INNER JOIN ciudad AS c ON v.id_ciudad_origen = c.id
) o
INNER JOIN (
    SELECT v.numero, c.tipo AS ciudad
    FROM viaje AS v
    INNER JOIN ciudad AS c ON v.id_ciudad_destino = c.id
) d ON o.numero = d.numero 
AND o.numero = 1

SELECT * FROM viaje WHERE numero = 1;

UPDATE viaje SET placa = 'DCG234' WHERE numero = 1
