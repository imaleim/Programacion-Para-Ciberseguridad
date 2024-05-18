import requests
import subprocess
import openpyxl
from openpyxl.styles import Font

API_KEY = 'a141318e5554195cd209510c193cc202716105eafc41862672b407ca1ed24a21'

def verificar_url(url):
    try:
        params = {'apikey': API_KEY, 'resource': url}
        response = requests.get('https://www.virustotal.com/vtapi/v2/url/report', params=params)
        if response.status_code == 200:
            data = response.json()
            if data['response_code'] == 1:
                # Verifica si alguna de las detecciones es positiva
                if any(scan['detected'] for scan in data['scans'].values()):
                    print("¡Advertencia! La URL ha sido identificada como maliciosa:")
                    for engine, result in data['scans'].items():
                        if result['detected']:
                            print(f" - Antivirus de escaneo: {engine}")
                            print(f" - Resultado: {result['result']}")
                else:
                    print("La URL no se ha identificado como maliciosa. Resultados del escaneo:")
                    for engine, result in data['scans'].items():
                        print(f" - Antivirus de escaneo: {engine}")
                        print(f" - Resultado: {result['result']}")
            elif data['response_code'] == 0:
                print("La URL aún no ha sido escaneada.")
                return "URL_noescaneada"
            else:
                print("La URL no se ha identificado como maliciosa.")
        else:
            print("Error al consultar la API:", response.status_code)
            return "Fallo_API"

    except:
        print("URL innacesible")
        return "Fallo_conexion"

#https://pasaporte-gobmx.com/
#https://aduanam.gob.mx.adquirir.site/VH8048


def guardar_txt(salida, nombre_archivo='CertificadoSSL.txt'):
    with open(nombre_archivo, 'w', encoding='utf-8') as archivo:
        archivo.write(salida)
        print(f'Archivo {nombre_archivo} guardado con éxito.')


def check_ssl(url, nombre_archivo='CertificadoSSL'):
    try:
        ps_script = 'C:\\Users\\ajosu\\OneDrive\\Escritorio\\python-codes\\ssl.ps1'
        # Ejecuta el script de PowerShell
        process = subprocess.Popen(['powershell.exe', ps_script, url], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        output, error = process.communicate()

        # Decodifica la salida de bytes a una cadena
        output = output.decode('windows-1252').replace('\r\n', '\n').strip()

        # Imprime la salida
        print(output)

        # Guardar
        guardar_txt(output, nombre_archivo)
    
    except:
        print("Error al intentar crear el archivo .xlsx")


    
#check_ssl(url='www.pandrama.com')
