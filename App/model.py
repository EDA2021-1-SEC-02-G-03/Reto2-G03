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
 *
 * Contribuciones:
 *
 * Dario Correal - Version inicial
 """


import config as cf
from DISClib.ADT import list as lt
from DISClib.ADT import map as mp
from DISClib.DataStructures import mapentry as me
from DISClib.Algorithms.Sorting import shellsort as sa
from DISClib.Algorithms.Sorting import mergesort as ms
assert cf

"""
Se define la estructura de un catálogo de videos. El catálogo tendrá dos listas, una para los videos, otra para las categorias de
los mismos.
"""
def newCatalog():

    catalog = {'videos':None, 
               'categories':None}
    
    #Esta lista contine todos los videos
    #encontrados en los archivos de carga.

    catalog['videos'] = lt.newList(datastructure='SINGLE_LINKED')

    #Esta lista contiene todas las categorias
    #encontradas en los archivos de carga.

    catalog['categories_normal'] = lt.newList(datastructure='ARRAY_LIST')

    #Este indice crea un map cuya llave es la categoría del video
    
    catalog['categories'] = mp.newMap(2000,
                                     maptype='PROBING',
                                     loadfactor=0.5)

    #Este indice crea un map cuya llave es el país

    catalog['countries'] = mp.newMap(200,
                                    maptype='PROBING',
                                    loadfactor=0.5)
    return catalog

#|==========================|
#|Funciones para crear datos|
#|==========================|

def addVideo(catalog, video):
    lt.addLast(catalog['videos'], video)
    addCategory(catalog, video)
    addCountry(catalog, video)
    #mp.put(catalog['categories'], int(video['category_id']), video)

def addCategories(catalog, category):
    #c = newCategory(category['id'], category['name'])
    lt.addLast(catalog['categories_normal'], category)

def addCategory(catalog, video):
    categories = catalog['categories']
    category = int(video['category_id'])
    exist_category = mp.contains(categories, category)

    if exist_category:
        entry = mp.get(categories, category)
        actual_category = me.getValue(entry)
    else:
        actual_category = newCategory(category)
        mp.put(categories, category, actual_category)
    lt.addLast(actual_category['videos'], video)

def newCategory(category):
    entry = {'category': '', 'videos': None}
    entry['category'] = category
    entry['videos'] = lt.newList(datastructure='SINGLE_LINKED')
    return entry

def addCountry(catalog, video):
    countries = catalog['countries']
    country = video['country']
    category = video['category_id']
    exist_country = mp.contains(countries, country)

    if exist_country:
        entry = mp.get(countries, country)
        #ct_entry = mp.get(countries, category)
        actual_country = me.getValue(entry)
        #exist_category = me.getValue(ct_entry)
        #if exist_category:
            #entry = mp.get(entry['categories_country'])
    else:
        actual_country = newCountry(country)
        mp.put(countries, country, actual_country)
    
    exist_category = mp.contains(actual_country['categories_country'], category)

    if exist_category:
        entry_ct = mp.get(actual_country['categories_country'], category)
        actual_category = me.getValue(entry_ct)
    
    else:
        actual_category = newCategory_from_country(category)
        mp.put(actual_country['categories_country'], category, actual_category)
    #mp.put(actual_country, country, actual_country['categories_country'])
    lt.addLast(actual_category['videos'], video)
    #addData(catalog, actual_country)

# def addData(catalog, actual_country):
#     categories = entry['categories_country']
#     pass

def newCountry(country):
    #entry = {'country': '', 'videos': None}
    entry = {'country': '', 'cateogories_country': None}
    entry['country'] = country
    #entry['videos'] = lt.newList(datastructure='ARRAY_LIST')
    entry['categories_country'] = mp.newMap(65, 
                                maptype='PROBING',
                                loadfactor=0.5) 
    return entry

def newCategory_from_country(category):

    entry = {'category': '', 'videos': None}
    entry['category'] = category
    entry['videos'] = lt.newList(datastructure='ARRAY_LIST')

    return entry

def getVideosByCategory(catalog, category):
    category = mp.get(catalog['categories'], category)
    if category:
        return me.getValue(category)['videos']

#Accede al mapa en donde las llaves son paises y 
#los valores son una lista con videos

def getVideosByCountry(catalog, country, category):
    country = mp.get(catalog['countries'], country)
    if country:
        country_data = me.getValue(country)['categories_country']
        categories = mp.get(country_data, category)
        if categories:
            return me.getValue(categories)['videos']

def find_position_category(catalog, category):
    for runner in range(lt.size(catalog)):
        element = lt.getElement(catalog, runner)
        if element['name'].strip() in category.strip():
            return element['id']
    return False

def videoSize(catalog):
    return lt.size(catalog['videos'])

def categoriesSize(catalog):
    return lt.size(catalog['categories_normal'])

# Funciones para agregar informacion al catalogo

# Funciones para creacion de datos

#|======================|
#| Funciones de consulta|
#|======================|

def sortVideosByViews(catalog, country, category):

    videos_country = getVideosByCountry(catalog, country, category)
    vc_sortedByViews = ms.sort(videos_country, compareViews)

    return vc_sortedByViews

def sortVideosByCategoryID(catalog, list_country_views):

    vc_sortedByCategory = ms.sort(list_country_views, compareCategory)

    return vc_sortedByCategory

# Funciones utilizadas para comparar elementos dentro de una lista

def compareViews(views1, views2):

    return int(views1['views']) > int(views2['views'])

def compareCategory(category1, category2):

    return int(category1['category_id']) > int(category2['category_id'])

# Funciones de ordenamiento
