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

    catalog['videos'] = lt.newList(datastructure='ARRAY_LIST')

    #Esta lista contiene todas las categorias
    #encontradas en los archivos de carga.

    catalog['categories_normal'] = lt.newList(datastructure='ARRAY_LIST')

    #Este indice crea un map cuya llave son los paises

    
    catalog['pure_country'] = mp.newMap(400,
                                     maptype='PROBING',
                                     loadfactor=0.5)

    #Este indice crea un map en el cual las llaves son 
    #paises y los valores que tiene cada país son un 
    #mapa en el cual las llaves son las diferentes
    #categorias y los valores son una lista de videos


    catalog['categories'] = mp.newMap(64,
                                     maptype='PROBING',
                                     loadfactor=0.5)

    #Este indice crea un map cuya llave es el país

    catalog['countries'] = mp.newMap(400,
                                    maptype='PROBING',
                                    loadfactor=0.5)

    return catalog

#Funciones de Creación de Datos

def addVideo(catalog, video):
    lt.addLast(catalog['videos'], video)
    addPureCountry(catalog, video)
    addCountry(catalog, video)
    addCategory(catalog, video)
    #addCountry(catalog, video)

def addCategories(catalog, category):
    lt.addLast(catalog['categories_normal'], category)

def addCategory(catalog, video):
    categories = catalog['categories']
    category = video['category_id']
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

def addPureCountry(catalog, video):
    countries = catalog['pure_country']
    country = video['country']
    exist_country = mp.contains(countries, country)

    if exist_country:
        entry = mp.get(countries, country)
        actual_country = me.getValue(entry)
    else:
        actual_country = newPureCountry(country)
        mp.put(countries, country, actual_country)
    lt.addLast(actual_country['videos'], video)

def newPureCountry(country):
    entry = {'country': '', 'videos': None}
    entry['country'] = country
    entry['videos'] = lt.newList(datastructure='ARRAY_LIST')
    return entry

def addCountry(catalog, video):
    countries = catalog['countries']
    country = video['country']
    category = video['category_id']
    exist_country = mp.contains(countries, country)

    if exist_country:
        entry = mp.get(countries, country)
        actual_country = me.getValue(entry)
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
    lt.addLast(actual_category['videos'], video)




def newCountry(country):
    entry = {'country': '', 'cateogories_country': None}
    entry['country'] = country
    entry['categories_country'] = mp.newMap(64, 
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

def getVideosByPureCountry(catalog, country):
    country = mp.get(catalog['pure_country'], country)
    if country:
        return me.getValue(country)['videos']

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

#Funciones de Ordenamiento

def sortVideosByViews(catalog, country, category):

    videos_country = getVideosByCountry(catalog, country, category)
    vc_sortedByViews = ms.sort(videos_country, compareViews)

    return vc_sortedByViews

def sortVideosByID(catalog, country):

    videos_id = getVideosByPureCountry(catalog, country)
    vc_sortedByCategory = ms.sort(videos_id, compareVideoID)

    return vc_sortedByCategory

def sortVideosBycategID(catalog, category):
    videos_id = getVideosByCategory(catalog, category)
    category_id = ms.sort(videos_id, compareVideoID)

    return category_id

def sortVideosByLikes(catalog, country):
    videos_likes = getVideosByPureCountry(catalog, country)
    likes = ms.sort(videos_likes, compareLikes)

    return likes

#Compare Functions

def compareViews(views1, views2):

    return int(views1['views']) > int(views2['views'])

def compareCategory(category1, category2):

    return int(category1['category_id']) > int(category2['category_id'])

def compareVideoID(videoId1, videoId2):

    return (videoId1['video_id'] > videoId2['video_id'])

def compareLikes(like1, like2):

    return int(like1['likes']) > int(like2['likes'])

#Requerimiento 2

def find_trending_video(list_data):
    bigger_moment, actual_winner, counter = 0, 0, 0
    actual_video = ''
    for video in lt.iterator(list_data):
        if video['video_id'] != actual_video:
            actual_video = video['video_id']
            bigger_moment = 0
        bigger_moment += 1
        if bigger_moment >= actual_winner:
            actual_winner = bigger_moment
            video_winner = counter
    counter += 1
    return lt.getElement(list_data, video_winner), actual_winner

#Requerimiento 4

def likes_tags(list_data, tag, n_videos):
    counter = 0
    for video in lt.iterator(list_data):
        if tag in video['tags']:
            counter += 1
            if counter > int(n_videos):
                break
            print(video['title'],video['channel_title'],video['publish_time'],video['views'],video['likes'],video['dislikes'],video['tags'])

#Requerimiento 1

def find_videos_views_country(list_data, n_videos):
    counter = 0
    for video in lt.iterator(list_data):
        counter += 1
        if counter > int(n_videos):
            break
        print(video['trending_date'],video['title'],video['channel_title'],video['publish_time'],video['views'],video['likes'],video['dislikes'])

#Requerimiento 3

def video_most_trending_days_category(catalog,category):
    category=category.strip()
    categoryid=''
    centinela=True
    i=0
    pos=1
    while pos<=lt.size(catalog['categories_normal']):
        element=lt.getElement(catalog['categories_normal'],pos)
        name=element['name'].strip()
        if category==name:
            categoryid=element['id']
            break
        pos+=1
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
    return(mayor,channeltitle,categoryid,int(mayorvalor))
    
    

    

