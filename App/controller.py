"""
 * Copyright 2020, Departamento de sistemas y Computación,
 * Universidad de Los Andes
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
import model
import csv
import time
import tracemalloc


"""
El controlador se encarga de mediar entre la vista y el modelo.
"""

# Inicialización del Catálogo de Videos

def initCatalog():
    catalog = model.newCatalog()
    return catalog

def loadData(catalog):
    """
    Carga los datos de los archivos y cargar los datos en la
    estructura de datos
    """

    #Funciones de tiempo
    delta_time = -1.0
    delta_memory = -1.0

    tracemalloc.start()
    start_time = getTime()
    start_memory = getMemory()

    loadVideos(catalog)
    loadCategoriesNormal(catalog)
    loadCategories(catalog)

    stop_memory = getMemory()
    stop_time = getTime()
    tracemalloc.stop()

    delta_time = stop_time - start_time
    delta_memory = deltaMemory(start_memory, stop_memory)

    #Funciones de carga
    
    '''
    loadVideos(catalog)
    loadCategoriesNormal(catalog)
    loadCategories(catalog)
    '''


    return delta_time, delta_memory

def loadVideos(catalog):
    booksfile = cf.data_dir + 'videos/videos-large.csv'
    input_file = csv.DictReader(open(booksfile, encoding='utf-8'))
    for video in input_file:
        model.addVideo(catalog, video)

def loadCategoriesNormal(catalog):
    videos_file = cf.data_dir + 'videos/category-id.csv'
    input_file = csv.DictReader(open(videos_file, encoding='utf-8'), delimiter='\t')
    for category in input_file:
        #ix_category = {category['name']:category['id']}
        model.addCategories(catalog, category)

def loadCategories(catalog):
    videos_file = cf.data_dir + 'videos/category-id.csv'
    input_file = csv.DictReader(open(videos_file, encoding='utf-8'), delimiter='\t')
    for category in input_file:
        model.addCategories(catalog, category)

# Funciones para la carga de datos

# def getVideosCategory(catalog, category):
#     videos = model.getVideosByCategory(catalog, category)
#     return videos

def getVideosPureCountry(catalog, country):
    return model.getVideosByPureCountry(catalog, country)

def getVideosCountry(catalog, country, category):
    videos = model.getVideosByCountry(catalog, country, category)
    return videos

def find_position_category(catalog, category):
    return model.find_position_category(catalog, category)

# Funciones de ordenamiento

def sortVideosByViews(catalog, country, category):
    return model.sortVideosByViews(catalog, country, category)

def sortVideosID(catalog, country):

    return model.sortVideosByID(catalog, country)

def sortVideosLikes(catalog, country):
    return model.sortVideosByLikes(catalog, country)
#def sortVideosCategoryID(catalog, category):


# Funciones de consulta sobre el catálogo

def find_trending_video(list_data):
    return model.find_trending_video(list_data)

def likes_tags(list_data, tag, n_videos):
    return model.likes_tags(list_data, tag, n_videos)

def find_videos_views_country(list_data, n_videos):
    return model.find_videos_views_country(list_data, n_videos)

def videoSize(catalog):
    return model.videoSize(catalog)

def categoriesSize(catalog):
    return model.categoriesSize(catalog)

# Funciones para medir tiempo y almacenamiento usado en pruebas

def getTime():
    """
    devuelve el instante tiempo de procesamiento en milisegundos
    """
    return float(time.perf_counter()*1000)

def getMemory():
    """
    toma una muestra de la memoria alocada en instante de tiempo
    """
    return tracemalloc.take_snapshot()

def deltaMemory(start_memory, stop_memory):
    """
    calcula la diferencia en memoria alocada del programa entre dos
    instantes de tiempo y devuelve el resultado en bytes (ej.: 2100.0 B)
    """
    memory_diff = stop_memory.compare_to(start_memory, "filename")
    delta_memory = 0.0

    # suma de las diferencias en uso de memoria
    for stat in memory_diff:
        delta_memory = delta_memory + stat.size_diff
    # de Byte -> kByte
    delta_memory = delta_memory/1024.0
    return delta_memory

#Funciones de Juan Andrés

def video_most_trending_category(catalog,category):
    return model.video_most_trending_days_category(catalog,category)
