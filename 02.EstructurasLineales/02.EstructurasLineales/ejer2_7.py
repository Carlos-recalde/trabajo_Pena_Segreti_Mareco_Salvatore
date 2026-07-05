from collections import defaultdict, deque

def sort_topologico_basico(ruta_archivo):
    nodos = set()
    adyacencia = defaultdict(list)
    grado_entrada = defaultdict(int)

    with open(ruta_archivo, 'r') as archivo:
        for linea in archivo:
            if not linea.strip(): continue
            origen, destino = linea.strip().split(',')
            
            nodos.add(origen)
            nodos.add(destino)
            adyacencia[origen].append(destino)
            grado_entrada[destino] += 1
            if origen not in grado_entrada:
                grado_entrada[origen] = 0

    q = deque()
    ot = [] 

    for nodo in list(nodos):
        if grado_entrada[nodo] == 0:
            q.append(nodo)

    while q:
        x = q.popleft()
        ot.append(x)
        
        nodos.remove(x)

        for vecino in adyacencia[x]:
            grado_entrada[vecino] -= 1
            
            if grado_entrada[vecino] == 0 and vecino in nodos:
                q.append(vecino)

    print("El Sort Topológico es:", ot)