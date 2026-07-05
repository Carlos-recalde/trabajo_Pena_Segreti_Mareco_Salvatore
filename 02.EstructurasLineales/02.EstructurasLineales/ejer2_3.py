class Celda:
    def __init__(self, info):
        self.info = info
        self.link = None

def procesar_lista_enlace_simple(ruta_archivo):
    cabecera = None
    
    with open(ruta_archivo, 'r') as archivo:
        for linea in archivo:
            if not linea.strip(): continue
            partes = linea.strip().split(',')
            operacion = partes[0]
            valor = partes[1] if len(partes) > 1 else None
            
            if operacion == "INSERTAR":
                nueva_celda = Celda(valor)
                if cabecera is None:
                    cabecera = nueva_celda
                else:
                    aux = cabecera
                    while aux.link is not None:
                        aux = aux.link
                    aux.link = nueva_celda
                    
            elif operacion == "ELIMINAR":
                if cabecera is None:
                    print("Error: La lista ya está vacía")
                else:
                    celda_a_borrar = cabecera
                    cabecera = cabecera.link
                    del celda_a_borrar 

    print("Estado final de la Lista Enlazada:")
    aux = cabecera
    while aux is not None:
        print(aux.info)
        aux = aux.link