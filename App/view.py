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
import time
import tracemalloc


"""
La vista se encarga de la interacción con el usuario
Presenta el menu de opciones y por cada seleccion
se hace la solicitud al controlador para ejecutar la
operación solicitada
"""

def printMenu():
    print("Bienvenido")
    print("1- Cargar información en el catálogo")
    print("2- Requerimiento número 1")
    print("3- Requerimiento número 2")
    print("4- Requerimiento número 3")
    print("5- Requerimiento número 4")

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
    inputs = input('Seleccione una opción para continuar\n')
    if int(inputs[0]) == 1:
        print("Cargando información de los archivos ....")
        catalog = controller.initCatalog()
        data = controller.loadData(catalog)
        print('Videos cargados: ' + str(controller.videoSize(catalog)))
        print('Categorias cargadas: ' + str(controller.categoriesSize(catalog)))
        print('Tiempo [ms]: ', f"{data[0]:.3f}", "-", "Memoria [kB]: ", f"{data[1]:.3f}")
        #car = mp.get(catalog['categories'], 1)
        #car = catalog['categories']
        #print(car)

    elif int(inputs[0]) == 2:
        country = input('Ingrese el pais del cual desea saber información \n')
        n_videos = input('ingrese el numero de videos a listar\n')
        category_name = input('Escriba una categoría\n')

        delta_time = -1.0
        delta_memory = -1.0

        tracemalloc.start()
        start_time = controller.getTime()
        start_memory = controller.getMemory()

        id_number = controller.find_position_category(catalog['categories_normal'], category_name)
        country_v_c = controller.sortVideosByViews(catalog, country, id_number)
        controller.find_videos_views_country(country_v_c, n_videos)

        stop_memory = controller.getMemory()
        stop_time = controller.getTime()
        tracemalloc.stop()

        delta_time = stop_time - start_time
        delta_memory = controller.deltaMemory(start_memory, stop_memory)
        print('Tiempo[ms]: ', f"{delta_time:.3f}", "-", "Memoria [kB]: ", f"{delta_memory:.3f}")

    elif int(inputs[0]) == 3:
        country = input('Ingrese el pais del cual desea saber información \n')
        delta_time = -1.0
        delta_memory = -1.0

        tracemalloc.start()
        start_time = controller.getTime()
        start_memory = controller.getMemory()

        country_videos = controller.sortVideosID(catalog, country)
        video_trending = controller.find_trending_video(country_videos)
        winner, trending_days = video_trending[0], video_trending[1]
        print(winner['title'], winner['channel_title'], winner['country'], trending_days)

        stop_memory = controller.getMemory()
        stop_time = controller.getTime()
        tracemalloc.stop()

        delta_time = stop_time - start_time
        delta_memory = controller.deltaMemory(start_memory, stop_memory)
        print('Tiempo[ms]: ', f"{delta_time:.3f}", "-", "Memoria [kB]: ", f"{delta_memory:.3f}")
    
    elif int(inputs[0]) == 4:
        category_name = input('Escriba una categoría\n')
        id_number = controller.find_position_category(catalog['categories_normal'], category_name)
        pass
    elif int(inputs[0]) == 5:
        country = input('Ingrese el pais del cual desea saber información \n')
        n_videos = input('ingrese el numero de videos a listar\n')
        tag = input('Ingrese el tag del video: ')

        delta_time = -1.0
        delta_memory = -1.0

        tracemalloc.start()
        start_time = controller.getTime()
        start_memory = controller.getMemory()
        
        sorted_likes = controller.sortVideosLikes(catalog, country)
        controller.likes_tags(sorted_likes, tag, n_videos)

        stop_memory = controller.getMemory()
        stop_time = controller.getTime()
        tracemalloc.stop()

        delta_time = stop_time - start_time
        delta_memory = controller.deltaMemory(start_memory, stop_memory)
        print('Tiempo[ms]: ', f"{delta_time:.3f}", "-", "Memoria [kB]: ", f"{delta_memory:.3f}")
    
    else:
        sys.exit(0)
sys.exit(0)
