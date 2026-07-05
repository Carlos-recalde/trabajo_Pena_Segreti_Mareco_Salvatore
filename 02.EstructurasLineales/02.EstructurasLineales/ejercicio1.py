def procesar_operaciones_cola(ruta_archivo, tamano_max):
    cola = [None] * tamano_max
    frente = 0
    fondo = 0
    cantidad = 0
    
    with open(ruta_archivo, 'r') as archivo:
        for linea in archivo:
            if not linea.strip(): continue
            operacion, valor = linea.strip().split(',')
            
            if operacion == "ENQUEUE":
                if cantidad == tamano_max:
                    print("Error: La cola está llena. No se puede encolar", valor)
                else:
                    cola[fondo] = valor
                    fondo = (fondo + 1) % tamano_max
                    cantidad += 1
                    
            elif operacion == "DEQUEUE":
                if cantidad == 0:
                    print("Error: La cola está vacía. No hay nada para desencolar")
                else:
                    cola[frente] = None
                    frente = (frente + 1) % tamano_max
                    cantidad -= 1
                    
    print("Estado de la Cola:", cola)