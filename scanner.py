import socket
import nmap
from openpyxl import Workbook

def check_ports(ip_host, custom_ports = None):  


    try:
        ip = socket.gethostbyname(ip_host)
    except:
        print("No se pudo resolver la dirección IP.")
        return

    if custom_ports is None:
        custom_ports = ''

    open_ports = ''
    for port in custom_ports:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)  
        result = sock.connect_ex((ip, port))
        if result == 0:
            open_ports += str(port)
        sock.close()

    if open_ports:
        print(f"La IP: {ip_host} tiene el puerto {open_ports} abierto.")
        si = input('¿Desea hacer un escaneo más intrusivo con nmap? (Y / N) ')
        if si == 'Y' or si == 'y':
            return escanear_url_desde_ip(ip_host, open_ports)

    else:
        print(f"No se encontraron puertos abiertos en {ip_host}.")

def escanear_url_desde_ip(ip, port):
    nm = nmap.PortScanner()
    nm.scan(ip, arguments = f' -sCV - p{port}')

    for host in nm.all_hosts():
        print(f"Resultado del escaneo para {host}:")
        for proto in nm[host].all_protocols():
            print(f"Protocolo : {proto}")

            lport = nm[host][proto].keys()
            for port in lport:
                estado = nm[host][proto][port]['state']
                if estado == 'open':
                    if port == 80:
                        print(f"URL HTTP encontrada: http://{host}")
                        lista = [[ip, port, f"http://{host}"]]
                        guardar_resultados_excel(lista)
                        return f"http://{host}"

                    elif port == 443:
                        print(f"URL HTTPS encontrada: https://{host}")
                        lista = [[ip, port, f"http://{host}"]]
                        guardar_resultados_excel(lista)
                        return f"https://{host}"

def guardar_resultados_excel(resultados):
    try:
        if not resultados:
            print("No hay resultados para guardar.")
            return

        wb = Workbook()
        ws = wb.active
        ws.title = "Resultados de Escaneo"

        headers = ["IP", "Puertos Abiertos", "URL Encontrada"]
        ws.append(headers)

        for resultado in resultados:
            if len(resultado) != 3:
                print("Error: formato incorrecto de resultado.")
                continue
            ws.append(resultado)

        wb.save("resultados_escaneo.xlsx")
        print("Los resultados se han guardado en resultados_escaneo.xlsx")

    except:
        print("Error al crear el archivo .xlsx")
        return False