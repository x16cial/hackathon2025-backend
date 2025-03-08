Plant
subclases
plant-low
plant-high
Reglas y comportamientos
estado inicial [live]
no puede surgir en celdas [rock]
inicia con 5 hp as [plant-low]
no se mueve
tras 24 ticks o 16 si se encuentra en una celda [soil+] se convierte en [plant-high]
vida maxima de 30 ticks desviacion de 3 ticks
[plant-high] bloquea movimiento [plant-low] no
cada 8 ticks 30% de generar una [plant-low] en una celda del rededor que no tenga una [plant-low]/[plant-high]
al morir una [plant-high] o perder todo su hp degrada la celda de su ciclo de tierra, su vida pasa al estado [dead] ,no bloqueara movimiento, ni contara para la generación de otro, una [plant-low] no degradara la tierra