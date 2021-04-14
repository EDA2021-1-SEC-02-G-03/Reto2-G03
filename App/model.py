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
from DISClib.Algorithms.Sorting import mergesort as mg
assert cf

"""
Se define la estructura de un catálogo de videos. El catálogo tendrá dos listas, una para los videos, otra para las categorias de
los mismos.
"""
def newCatalog():
    #TODO: investigar lo de los números primos porque hacen falta

    catalog = {'videos':None, 
               'categories':None}
    
    #Esta lista contine todos los videos
    #encontrados en los archivos de carga.

    catalog['videos'] = lt.newList(datastructure='ARRAY_LIST')

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

    catalog['tags'] = mp.newMap(2000,
                                maptype='PROBING',
                                loadfactor=0.5)
    return catalog

#|==========================|
#|Funciones para crear datos|
#|==========================|

def addTags(catalog,video):
    tags=catalog['tags']
    tag=video['tags']
    exist_tag=mp.contains(tags,tag)

    if exist_tag:
        entry=mp.get(tags,tag)
        actual_tag=me.getValue(entry)
    else:
        actual_tag=newTag(tag)
        mp.put(tags,tag,actual_tag)
    lt.addLast(actual_tag['videos,'],video)

def newTag(tag):
    entry= {'tag':'','videos':None}
    entry['tag']=tag
    entry['videos']=lt.newList(datastructure='ARRAY_LIST')
    return entry

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
    entry['videos'] = lt.newList(datastructure='ARRAY_LIST')
    return entry

def addCountry(catalog, video):
    countries = catalog['countries']
    country = video['country']
    exist_country = mp.contains(countries, country)

    if exist_country:
        entry = mp.get(countries, country)
        actual_country = me.getValue(entry)
    else:
        actual_country = newCountry(country)
        mp.put(countries, country, actual_country)
    lt.addLast(actual_country['videos'], video)

def newCountry(country):
    entry = {'country': '', 'videos': None}
    entry['country'] = country
    entry['videos'] = lt.newList(datastructure='ARRAY_LIST') 
    return entry

def getVideosByCategory(catalog, category):
    category = mp.get(catalog['categories'], category)
    if category:
        return me.getValue(category)['videos']

def getVideosByCountry(catalog, country):
    country = mp.get(catalog['countries'], country)
    if country:
        return me.getValue(country)['videos']

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

#Funciones de Juan Andrés

def video_most_trending_days_category(catalog,category):
    category=category.strip()
    categoryid=''
    centinela=True
    i=0

    #TODO Encuentre el category id!!!!!!!!!

    
    pos=1
    while pos<=lt.size(catalog['categories_normal']):
        element=lt.getElement(catalog['categories_normal'],pos)
        name=element['name'].strip()
        if category==name:
            categoryid=element['id']
            break
        pos+=1
    
    categoryid=int(categoryid)

    #Esto está bien!
    videos_categoria=mp.get(catalog['categories'],categoryid)
    videos_categoria1=me.getValue(videos_categoria)['videos']
    e=0
    repetidos={}
    while True:
        element=lt.getElement(videos_categoria1,e)
        if element['title'] in repetidos:
            repetidos[element['title']][0]+=1
        else:
            repetidos[element['title']]=[1,e]
        e+=1
        if e>lt.size(videos_categoria1):
           break
    

    mayor=''
    mayorvalor=0
    for i in repetidos:
        listavalor=repetidos[i]
        if listavalor[0]>mayorvalor:
            mayorvalor=listavalor[0]
            mayor=i
    posmayor=repetidos[mayor][1]
    videomayor=lt.getElement(videos_categoria1,posmayor)
    channeltitle=videomayor['channel_title']
    mayorvalor/=2

    return(mayor,channeltitle,categoryid,int(mayorvalor))
    
    

    

