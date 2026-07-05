import random

def gestion_ocupacion_universitaria(param_e, param_p, param_bh, bh_buscado):
    tamano_max = 85000
    inscriptos = [0] * tamano_max
    capacidad = [0] * tamano_max
    
    for idx in range(tamano_max):
        inscriptos[idx] = random.randint(0, 40)
        capacidad[idx] = random.randint(40, 60)
        
    max_porcentaje = -1
    mejor_indice = -1
    
    for idx in range(tamano_max):
        porcentaje = inscriptos[idx] / capacidad[idx]
        if porcentaje > max_porcentaje:
            max_porcentaje = porcentaje
            mejor_indice = idx
            
    edificio = mejor_indice // 21250
    resto = mejor_indice % 21250
    num_piso = resto // 4250
    resto %= 4250
    ala = resto // 2125
    resto %= 2125
    aula = resto // 85
    bloque = resto % 85
    
    print(f"Mayor ocupación en Aula: {aula} - Bloque: {bloque}")
    print(f"(Edificio: {edificio} Piso: {num_piso} Ala: {ala})")
    print("-" * 30)
    
    suma_por_piso = [0, 0, 0, 0, 0] 
    aulas_por_piso = 4 * 2 * 25 
    
    for idx in range(bh_buscado, tamano_max, 85):
        piso_actual = (idx % 21250) // 4250
        suma_por_piso[piso_actual] += inscriptos[idx]
        
    for p in range(5):
        promedio = suma_por_piso[p] / aulas_por_piso
        print(f"Promedio en Piso {p}: {promedio}")
    print("-" * 30)
        
    total_norte = 0
    total_sur = 0
    
    base_formula = (param_e * 21250) + (param_p * 4250) + param_bh
    
    inicio_norte = base_formula + (0 * 2125)
    inicio_sur = base_formula + (1 * 2125)
    
    for aula in range(25):
        total_norte += inscriptos[inicio_norte + (aula * 85)]
        total_sur += inscriptos[inicio_sur + (aula * 85)]
        
    print(f"Total Ala Norte: {total_norte}")
    print(f"Total Ala Sur: {total_sur}")


#gestion_ocupacion_universitaria(param_e=0, param_p=1, param_bh=10, bh_buscado=10)