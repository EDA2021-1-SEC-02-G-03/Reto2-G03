"""
 * Copyright 2020, Departamento de sistemas y Computación, Universidad
 * de Los Andes
 *
 *
 * Desarrolado para el curso ISIS1225 - Estructuras de Datos y Algoritmos
 *
 *
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along withthis program.  If not, see <http://www.gnu.org/licenses/>.
 """

import config as cf
import sys
import controller
from DISClib.ADT import list as lt
from DISClib.ADT import map as mp
assert cf


"""
La vista se encarga de la interacción con el usuario
Presenta el menu de opciones y por cada seleccion
se hace la solicitud al controlador para ejecutar la
operación solicitada
"""

def printMenu():
    print("Bienvenido")
    print("1- Cargar información en el catálogo")
    print("2- Encontrar videos con más views que son tendencia en un determinado país, dada una categoría específica.")
    print('3- Encontrar el video que más días ha sido trending para un país específico.')
    print('4- Encontrar el video que más días ha sido trending para una categoría específica.')
    print('5- Encontrar videos diferentes con más likes en un país y con un tag específico.')
catalog = None

def initCatalog():
    return controller.initCatalog()

def loadData(catalog):
    controller.loadData(catalog)

"""
Menu principal
"""
while True:
    printMenu()
    opcion = int(input('Seleccione una opción para continuar:\n'))
    if opcion == 1:
        pass
    
    elif opcion == 2:
        pass

    elif opcion==3:
        pass

    elif opcion==4:
        pass

    elif opcion==5:
        pass

    else:
        sys.exit(0)
sys.exit(0)
