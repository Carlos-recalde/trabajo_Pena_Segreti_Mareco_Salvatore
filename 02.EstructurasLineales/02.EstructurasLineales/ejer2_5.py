from collections import defaultdict, deque

def tsort_con_deteccion_de_ciclos(ruta_archivo):
    p = set()
    r = defaultdict(list)
    grado_entrada = defaultdict(int)
    
    with open(ruta_archivo, 'r') as archivo:
        for linea in archivo:
            if not linea.strip(): continue
            origen, destino = linea.strip().split(',')
            
            p.add(origen)
            p.add(destino)
            r[origen].append(destino)
            grado_entrada[destino] += 1
            if origen not in grado_entrada:
                grado_entrada[origen] = 0

    q = deque()
    secuencia_tsort = []
    
    for x in list(p):
        if grado_entrada[x] == 0:
            q.append(x)            
    while q:
        x = q.popleft()
        secuencia_tsort.append(x)
        p.remove(x) 
        
        # E = E|_P 
        for vecino in r[x]:
            grado_entrada[vecino] -= 1
            if grado_entrada[vecino] == 0:
                q.append(vecino)
                
    if p:
        print("Atención: La estructura es cíclica. No es posible calcular el T-Sort.")
    else:
        print("Secuencia generada por T-Sort:", secuencia_tsort)