Animal
subclases
animal-small
animal-big
Reglas y comportamientos
estado inicial [live]
[big] : consume 1 hp de un [plant-high] o 2 hp de un [plant-low] / [fungi]
[small] : consume 1 hp de un [plant-low] / [fungi] no puede consumir de [plant-high]
si emerge en una celda de agua, no puede moverse a través de otras
se mueve aleatoriamente 1 - 3 celdas en una dirección aleatoria cada tick
consume de una planta aleatoria a su alrededor al final de su movimiento
si no consume en 3 ticks consecutivos, pasa a estado [dead]
a los 12 ticks de existencia se convierte en [animal-big]
cada 6 ticks si tiene otro [animal-big]/[animal-small] al lado 50% de posibilidad de generar un [animal-small]
vida máxima de 24 ticks con desviación de 1 tick
una casilla ocupada por uno no puede ser ocupada por otro ente
al acabar su vida pasa al estado [dead] y no podrá moverse, consumir, no bloqueara movimiento, ni contara para la generación de otro