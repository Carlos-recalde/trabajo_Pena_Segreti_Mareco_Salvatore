def procesar_operaciones_pila(ruta_archivo, length):
    pila = [None] * length
    tope = 0
    
    with open(ruta_archivo, 'r') as archivo:
        for linea in archivo:
            if not linea.strip(): continue
            operacion, valor = linea.strip().split(',')
            
            if operacion == "PUSH":
                if tope == length:
                    print("No se puede agregar más (Overflow)")
                else:
                    pila[tope] = valor
                    tope += 1
                    
            elif operacion == "POP":
                if tope == 0:
                    print("No hay valores en la pila (Underflow)")
                else:
                    tope -= 1
                    pila[tope] = None
                    
    print("Estado final de la Pila (desde la base hasta el tope):")
    for i in range(tope):
        print(pila[i])