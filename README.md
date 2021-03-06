# Proyecto-reservacion-de-boletos
## *Reserva tu boleto Entrega 1* 
<h3><b>pequeña descripcion del proyecto</b></h3><br>
Este proyecto fue pensado como el sistema que se ocupa en un counter en el aeropuerto a la hora de reservar un boleto. Tiene ideas como, la reserva del boleto visual, asistencia de silla de ruedas, reservar un boleto de manera alealtoria y la funcion de una lista por prioridad. (Toma en cuenta a las personas de sillas de ruedas vs las de boletos normales.)<br><br>
  
### Reserva tu boleto es un programa que simula un servicio para reservar boletos aereos. 
Las funciones que este programa ofrece son: 
  - Pregunta cuantos boletos desea reservar y cual es la posicion exacta en la cual quiere reservar sus boletos.
    - Al momento que el cliente ingresa sus datos, se marca con una "X" la posicion o posiciones que el cliente reservo.
  - Pregunta si el cliente es necesitado de servicios especiales. (Es decir, el uso de silla de ruedas)
    - Los guarda en una linked list:
      - En donde la persona o personas que necesiten de cuidados especiales, entran como prioridad en el momento de abordar.  
  - Se puede ver la disponibilidad del avion aun cuando ya se haya hecho una reservacion. 
  - Desocupar asiento
    - Este pregunta la posicion exacta en la cual desea desocupar su asiento para quitar "X".
      - Pregunta si el asiento era de una persona con ncesidades especiales para poder quitarle de igual manera de la linked list.


<b>Las estructuras que fueron usadas en este proyecto: </b>
  - Linked List
  - Array de arrays (Matrices)
  - manipulacion de strings

<h2> Bienvenido al vuelo A138 </h2>


![Bienvenido](https://user-images.githubusercontent.com/71049819/157096508-5e39e5b0-6e25-4747-9fe9-0196b38ad28c.png)

<br> <br>Aaqui puede hacer sus reservaciones de su proximo vuelo! <br> Si usted ocupa una **silla de ruedas** siga este ejemplo <br>

![ejemploSilla](https://user-images.githubusercontent.com/71049819/157097236-6049260f-c6fe-4340-83a9-f89779f23e84.png)

<br> si no ocupa silla siga este otro ejemplo <br>

![Ejemplo](https://user-images.githubusercontent.com/71049819/157097602-804efe1e-342b-4f2a-8753-57502e953921.png)

<br> Usted sera asignado, Personas que requieren de servicios especiales seran los primeros en ser ingresados al avion. <br>

<h3> Gracias por viajar en nuestro vuelo! </h3>


<h2>Pruebas</h2> <br><br>

Unittest
![unittest](https://user-images.githubusercontent.com/71049819/157134992-57f87859-6aab-4324-88c5-85bd2f614b96.png)
Profiling
![profile](https://user-images.githubusercontent.com/71049819/157135055-043be5dd-4c3b-4b98-b71f-ad32e3820188.png)

## *Reserva tu boleto Entrega 2* 
<h3><b>pequeña descripcion del proyecto</b></h3><br>
Este proyecto es la secuela del proyecto anterior, Se le ha agregado un hangar el cual tiene guardados los aviones que no estan en uso, tambien se le implemento una lista de espera la cual tiene los aviones que estan listos para abordar pero no estan en uso aun. Se han agregado mas aviones los cuales pueden ser abordados 1 por 1 y ahora los aviones despegan.

### Reserva tu boleto es un programa que simula un servicio para reservar boletos aereos. 
Las funciones que este programa ofrece son: 
  - A la hora de que despega un avion si hay aviones disponibles en la lista de espera podra mandar a llamar al primero en la lista para abordarlo.
    - En el momento de que el avion sea llamado de la lista de espera el siguiente avion automaticamente se movera a la primera posicion.
  - Tenemos aviones en un hangar los cuales se moveran de manera en que el ultimo en la lista sera el primero en salir del hangar.
    - El hangar tiene aviones que no estan en uso que se pueden mover a la lista de espera si es necesario  


<b>Las estructuras que fueron usadas en este proyecto: </b>
  -Stacks
  -Queue

## *Reserva tu boleto Entrega 3* 
<h3><b>pequeña descripcion del proyecto</b></h3><br>

### Reserva tu boleto es un programa que simula un servicio para reservar boletos aereos. 
Las funciones que este programa ofrece son: 
  - Visualizar de manera grafica en un PDF que abre de forma automatica la distintas rutas que pueden tomar los clientes en el dia deseado.
  - VIsualizar de manera grafica en un PDF las rutas que ofrece la aerolinea (no necesariamente del dia)


<b>Las estructuras que fueron usadas en este proyecto: </b>
  - Se implementaron Grafos para poder mostrar la rutas del dia y la rutas que tiene la aerolinea disponible
  - Se implemento un pequeño search para poder saber que lugar del array se encuentran ocupados. 

# Video de ejecucion

[Video de ejecucion](https://github.com/Tuki1077/Proyecto-reservacion-de-boletos/blob/main/Video%20ejecucion%20Final)

# JMETER para Stress Testing

![sampler 3](https://user-images.githubusercontent.com/71049819/169167235-930f896b-8d5b-4a8b-9027-bfe672b3f14a.jpg)

![Sampler 2](https://user-images.githubusercontent.com/71049819/169167236-86e53222-d167-4a41-a674-ed7d4701355e.jpg)

![sampler](https://user-images.githubusercontent.com/71049819/169167241-4a3ea3ff-8b02-4d4b-9e9f-565fe36cb590.jpg)
  
<h2> Rutas a tomar </h2><br>

![Vancouver](https://user-images.githubusercontent.com/71049819/168942892-3cd71c6f-59cd-496f-8808-fda0cdb0419e.jpg) <br>

![Miami](https://user-images.githubusercontent.com/71049819/168942997-b34acb63-fff3-4bb4-a71b-6e635419c98b.jpg)<br>

![Francia](https://user-images.githubusercontent.com/71049819/168943004-207d661a-b271-4d60-84ca-6b2f8a009337.jpg)<br>

<h2>Tambien estas son las rutas generales que ofrecemos</h2>

![all](https://user-images.githubusercontent.com/71049819/169166815-8102e795-95de-45b6-b474-b5aeaceb081c.jpg)
