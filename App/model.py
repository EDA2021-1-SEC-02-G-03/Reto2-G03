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
assert cf

"""
Se define la estructura de un catálogo de videos. El catálogo tendrá dos listas, una para los videos, otra para las categorias de
los mismos.
"""
def newCatalog():

    catalog = {'videos':None, 
               'categories':None}
    
    catalog['videos'] = lt.newList(datastructure='SINGLE_LINKED')

    catalog['categories_normal'] = lt.newList(datastructure='ARRAY_LIST')

    catalog['categories'] = mp.newMap(2000,
                                     maptype='PROBING',
                                     loadfactor=0.8)
    return catalog

# Construccion de modelos

def addVideo(catalog, video):
    lt.addLast(catalog['videos'], video)
    addCategory(catalog, video)
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

def getVideosByCategory(catalog, category):
    category = mp.get(catalog['categories'], category)
    if category:
        return me.getValue(category)['videos']
    return None

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

# Funciones de consulta

# Funciones utilizadas para comparar elementos dentro de una lista

# Funciones de ordenamiento
