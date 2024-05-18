#DESCRIPCIÓN DEL PROYECTO

Proyecto Integrador de Aprendizaje para finalizar la unidad de Programación para Ciberseguridad enfocado en un script con 6 tareas relacionadas con la ciberseguridad.

#Índice
**Contenido**

[TOCM]






# FUNCIONALIDAD

Ofrece diferentes funcionalidades que permiten a los usuarios realizar escaneo de puertos (443 y 80), cambios de página mediante un diccionario, obtención de urls mediante web scraping, búsqueda de la vulnerabilidad path traversal, utilización de API VIRUS TOTAL para la verificación de urls, comprobación de información de certificados SSL. Básicamente está enfocado en la seguridad web y obtención de vulnerabilidades de estas.


#INSTALACIÓN
Al descargar el proyecto obtendrás los siguientes archivos:

	main.py
	mod1.py
	scanner.py
	url2.py
	ssl.ps1
	requirements.txt
	ejemplo.txt

Para su optima ejecución puedes hacer una instalación masiva de los módulos utilizados con el archivo requirements.txt desde CMD de la siguiente manera:

   `pip install -r requirements.txt`

#USO

Preferentemente ejecutar desde CMD y movernos a la ruta donde estén los archivos del proyecto. Podemos hacer uso de –h para ver que argumentos son requeridos para ejecutar.

*Se debe ejecutar el main.py

Para ejecutar con URLS:
`python main.py --url www.ejemplo.com`

Para ejecutar con IP:
`python main.py --ip 192.168.1.1`

Instrucciones para saber el uso que se le puede dar a las tareas:

####1.	Scanner de puertos para la IP 

En base a una IP dada realiza un escaneo de los puertos 80 (HTTP) o 443 (HTTPS). Si se encuentra alguno abierto imprime un mensaje y pregunta si se quiere hacer un escaneo mas “intrusivo” con nmap. 

En caso de ejecutar el escaneo intrusivo imprime el protocolo y el estado de cada puerto, si se encuentra abierto te devuelve una URL correspondiente.

Como reporte genera un Excel llamado ***Python_nmap.xlsx***

****NOTA IMPORTANTE:** este tipo de escaneos con nmap pueden ser posiblemente ilegal si se realiza sin permiso. Debes hacer uso correcto de nmap ya que en algunos casos pueden afectar a la red y a los dispositivos que se están escaneando. De preferencia no hacer uso en:
	 •	Redes ajenas sin ningún permiso
	 •	Sistemas de terceros 
	 •	Propósito maliciosos
	 •	Entornos corporativos o educativos

####2.	Cambio de pagina por medio de diccionario:

El proyecto te proporciona un archivo txt con una lista para probar esta opción. 
Mediante una URL ingresada se construye una nueva URL que es la base de la URL ingresada hasta el último “/”. Después del ultimo “/” se agregaran las del diccionario. 

Si el código estado de la respuesta de la solicitud HTTP es 200 significa que la pagina existe y esta accesible, se repite ese procedimiento con toda la lista del diccionario. Por ultimo devuelve una lista nueva con URLs que respondieron con 200.

**** NOTA IMPORTANTE:** Esta tipo de escaneo también es considerado malicioso si se realiza sin permiso en sitios web.



####3.	Obtención de Urls con web scraping ****

Con la URL ingresada sigue los enlaces encontrados en esta. Las recolecta y esta te regresa un documento Excel con las URLS encontradas llamado ***Enlaces_Encontrados.xlsx***

**** NOTA IMPORTANTE: **Debemos tener permisos de la web que se va a utilizar de preferencia ya que también se considera un poco intrusivo.


####4.	Buscar vulnerabilidad Path Traversal 

Esta opción busca identificar la vulnerabilidad de path traversal con la URL dada.
Para su uso la URL proporcionada debe tener algún “=”. Si encuentra un signo igual, asume que puede haber una vulnerabilidad y procede a modificar la URL para intentar explotarla.
Elimina todo después del signo igual y añade la cadena “/…/…/…/…/…/…/etc/passwd” a la URL.
Si la solicitud es exitosa devuelve si la página es vulnerable o en lo contrario que no lo es.

****NOTA IMPORTANTE:** Debe realizarse solo en entornos controlados y con permiso. Realizar pruebas de seguridad en sistemas que no te pertenecen sin autorización puede ser ilegal y tener consecuencias graves.

####5.	Verificar la url con VIRUS TOTAL 

Para su uso debes obtener una API KEY de Virus Total e ingresarla en el código.
Si la URL ha sido escaneada previamente y detectada como maliciosa por algún motor de antivirus, la función imprimirá una advertencia y los detalles de la detección.
Si la URL no ha sido identificada como maliciosa, imprimirá los resultados del escaneo de cada motor de antivirus.

####6.	Verificar SSL de URL 

Esta opción importa un script de powershell a Python y obtiene todos los detalles de un certificado SSL de una URL ingresada. 

Imprime la información del certificado, incluyendo el sujeto, el emisor, las fechas de validez, el algoritmo de firma, el número de serie y el thumbprint (hash del certificado).

Verifica si el certificado está caducado comparando la fecha de expiración con la fecha actual y formatea la salida para indicar si el certificado es válido o ha caducado.
Por utimo te genera un archivo txt con los resultados llamado ***CertificadoSSL.txt***

Para su uso recuerda que el scrip de Python y powershell deben estar en la misma ruta. También para ejecutar scripts de PowerShell en tu sistema, es posible que necesites **cambiar la política de ejecución **de scripts. Puedes hacerlo con el siguiente comando en PowerShell ejecutado como administrador:

`Set-ExecutionPolicy RemoteSigned`

****NOTA IMPORTANTE:** Tener permiso para verificar los certificados SSL de los sitios web que no te pertenecen y de seguir las políticas de seguridad aplicables.

####7.	Cambiar URL 
La opción es útil para cambiar de URL si quieres seguir probando diferentes sin salir del programa.

####8.	Salir
Termina la ejecución.


#CRÉDITOS


[http://https://axarnet.es/blog/web-scrapping#](http://https://axarnet.es/blog/web-scrapping#)

[http:/https://owasp.org/www-community/attacks/Path_Traversal/](http:/https://owasp.org/www-community/attacks/Path_Traversal/)

[http://https://www.redeszone.net/tutoriales/configuracion-puertos/nmap-escanear-puertos-comandos/](http://https://www.redeszone.net/tutoriales/configuracion-puertos/nmap-escanear-puertos-comandos/)
