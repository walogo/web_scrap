from scrapthor import scrap,filtros

url='https://en.wikipedia.org/wiki/Conor_McGregor'

#Profundidad a la que se va a scrapear
profundidad=2

#Parametros es un diccionario,cree una clase que es muy util para  manejar las keys que el programa puede leer

##Con la clase de ayuda (filtros)
parametros=filtros()
parametros.ig_formato(['html'])
##Sin la clase de ayuda
parametros={'ig_formato':['html']}
### ig = diminutivo de ignorar ; formato = formato del archivo

#Permite que se descarguen los archivos
descargar_archivos=True
#Permite escribir un archivo con todos los links encontrados
guardar_links=True
#Permite crear un archivo .json con fingerprints (hash) de cada archivo encontrado
guardar_hashes=True

#scrap(url, profundidad=1, parametros={}, descargar_archivos=True, guardar_links=True, guardar_hashes=True)
scrap(url,profundidad,parametros,descargar_archivos,guardar_links,guardar_hashes)