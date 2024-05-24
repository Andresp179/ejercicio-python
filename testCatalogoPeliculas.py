from Pelicula import Pelicula
from Servicio.catalogo_peliculas import CatalogoPeliculas as cp

opcion= None

while opcion !=4:
    print('Opciones: ')
    print('1. Agregar pelicula')
    print('2. Listar peliculas')
    print('3. Eliminar catalogo')
    print('4. Salir')
    opcion=int(input('Escribe opcion (1-4): '))
    
    if opcion == 1:
        nomnbre_pelicula=input('Nombre de la pelicula: ')
        pelicula= Pelicula(nomnbre_pelicula)
        cp.agregar_pelicula(pelicula)
    elif opcion == 2:
        cp.listar_peliculas
    elif opcion == 3:
        cp.eliminar_peliculas(pelicula)
else:
    print('Salimos del programa')