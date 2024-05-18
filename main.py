import logging
import argparse
import mod1
import url2
import scanner

def menu(url):
    if url == None:
        print("""
            URL en uso: "Ninguna"
              
        1. - Scanner de puertos para la IP
        2. - Cambio de pagina por medio de diccionario
        3. - Obtencion de url´s por web scraping
        4. - Buscar vulnerabilidad path traversal
        5. - Verificar la URL con Virus total
        6. - Verificar SSL de la url
        7. - Cambiar url
        8. - Salir
              
            """)
  
    else:
        print(f"""
            URL en uso: {url}
              
        1. - Scanner de puertos para la IP
        2. - Cambio de pagina por medio de diccionario
        3. - Obtencion de url´s por web scraping
        4. - Buscar vulnerabilidad path traversal
        5. - Verificar la URL con Virus total
        6. - Verificar SSL de la url
        7. - Cambiar url
        8. - Salir
      
            """)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Este script esta relacionado con la ciberseguridad en url´s, digite una ip o url para observar las tareas que realiza este script.')
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("--url", type = str, help = "Nombre de URL")
    group.add_argument("--ip", type = str, help = "IP a escanear")
    args = parser.parse_args()
    logging.basicConfig(filename = 'logging.log',level = logging.INFO)

    if args.url is not None:
        logging.info("URL registrada: ")
        logging.info(args.url)

    if args.ip is not None:
        logging.info("IP refistrada: ")
        logging.info(args.ip)

    url_main = args.url
    ip = args.ip
    custom_ports = [80, 443] 


    while True:
        menu(url_main)
        try:
          
            opc = int(input("Digita una opción: "))
          
            if opc == 1:
                url = scanner.check_ports(ip, custom_ports)        
                if url is not None:
                    validar = input("¿Desea usar esta url para seguir con el programa?(Y/N) ")
                    if validar == 'Y' or validar == 'y':
                        url_main = str(url) + "/"
                else:
                    logging.error("No hay conexion con la IP")

                print()

            elif opc == 2: 
                diccionario = input("Digite la ruta donde se encuentra el diccionario: ")
                lista = mod1.vuln_cambio_pag(url_main, diccionario)

                if lista == False:
                    logging.error(f"Fallos en la conexion con: {url}")

                elif lista == True:
                    logging.error(f"Fallo en intentar conectar con la ruta: {diccionario}")

                elif len(lista) == 0:
                    print("No se encontraron palabras con las cuales hacer conexión...")

                else:
                    print("\nRutas con las que se establecio la conexión:\n")
                    for palabra in lista:
                        print(palabra)
                        logging.info("URL registrada: ")
                        logging.info(palabra)
              
                print()
              
            elif opc == 3:
                validar = mod1.enlace(url_main)
                if validar == False:
                    logging.error(f"Fallo la conexion con la URL: {url_main}")
                print("\n")
              
            elif opc == 4:
                respuesta = mod1.path_traversal(url_main)
                if respuesta == False:
                    continue
                else:
                    print(respuesta)
                print("\n")

              
            elif opc == 5:
                validar = url2.verificar_url(url_main)
                if validar == "URL_noescaneada":
                    logging.info(f"La URL {url_main} no a sido escaneada por Virus total")

                elif validar == "Fallo_API":
                    logging.error("Fallo en la API, verificar que sea vigente")

                elif validar == "Fallo_conexion":
                    logging.error(f"Fallo la conexion con la URL: {url_main}")
                print("\n")

            elif opc == 6:
                url2.check_ssl(url_main)
                print()

            elif opc == 7:
                url_main = input("Digite la URL a la que desea cambiar: ")
                print()
              
            elif opc == 8:
                print("Saliendo...")
                print()
                break
              
            else:
                print("\nElige una opción valida...")
                print()

        except ValueError:
            print("\nElige una opción valida...")
            print()

        except KeyboardInterrupt:
            print("\nSaliendo...")
            break
