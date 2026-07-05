def altura(arreglo, k):
    
    n = len(arreglo)
    
    altura = 0
    nodos_en_nivel = 1
    nodos_contados = 1
    
    while nodos_contados < n:
        nodos_en_nivel = nodos_en_nivel * k
        nodos_contados = nodos_contados + nodos_en_nivel  #esto es para saber si aun quedan nodos
        altura = altura + 1                               #por contar    
    return altura





def preorden(arreglo, k):
    
    if len(arreglo) == 0:
        return
    
    pila = []
    pila.append(1)                
    
    while len(pila) > 0:
        x = pila.pop() 
        print(arreglo[x - 1])  # vale 1, por eso le resto 1 para tener la pocicion 0
        
        primer_hijo = k * (x - 1) + 2    #ecuacion 
        
        for i in range(k - 1, -1, -1):
            hijo = primer_hijo + i
            if hijo <= len(arreglo):      
                pila.append(hijo)

arreglo = ['A', 'B', 'C', 'D', 'E', 'F', 'G']
k = 3

preorden(arreglo, k)

