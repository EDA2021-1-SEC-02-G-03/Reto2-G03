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
    print("2- Requerimiento número 1")

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
        id_number = controller.find_position_category(catalog['categories_normal'], category_name)
        #print(mp.get(catalog['countries'], 'USA'))
        #country_videos = controller.sortVideosByViews(catalog, country)
        #country_v_c = controller.sortVideosByCategoryID(catalog, country_videos)
        country_v_c = controller.sortVideosByViews(catalog, country, id_number)
        #country_videos = controller.sortVideosByViews(catalog, country)
        card = 0
        for video in lt.iterator(country_v_c):
            card += 1
            print(video['country'], video['title'], video['views'], video['channel_title'], video['views'])
            if card >= 3:
                break

        # id_number = controller.find_position_category(catalog['categories_normal'], category_name)
        # videos = controller.getVideosCategory(catalog, int(id_number))
        # no_rep = []
        # for max_liked in range(int(n_videos)):
        #     actual_max = 0
        #     actual_id = ''
        #     title_max = ''
        #     for video in lt.iterator(videos):
        #         if int(video['likes']) > int(actual_max) and video['video_id'] not in no_rep:
        #             actual_max = video['likes']
        #             actual_id = video['video_id']
        #             title_max = video['title']
        #     no_rep.append(actual_id)
        #     print(title_max, actual_max)

    else:
        sys.exit(0)
sys.exit(0)
