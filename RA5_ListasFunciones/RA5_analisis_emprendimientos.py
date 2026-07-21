"""Practica Semana 07: analisis de emprendimientos costarricenses.

Complete los espacios marcados con TODO. El objetivo es generar un reporte por
sede usando listas, diccionarios, funciones, ciclos y condicionales.
"""

from sedes import sedes

def calcular_total(ventas):
    """Recibe una lista y retorna el total de ventas"""
    return sum(ventas)

def calcular_porcentaje_logro(total, meta):
    """Calcula el porcentaje de cumplimiento de un meta"""
    porcentaje = total / meta * 100
    return porcentaje

def calcular_clasificacion (porcentaje):
    if porcentaje >= 100:
        mensaje = "Meta alcanzada, felicitaciones"
    elif porcentaje >= 90:
        mensaje = "ABVERTENCIA, meta no alcanzada"
    else:
        mensaje = "URGENCIA, mtea no alcanzada, revisar perdidas"
        
    return mensaje

def imprimir_reporte(datos_reporte):
    """Imprime el reporte final de ventas por emprendimiento"""
    print("\n---REPORTE FINAL---")
    print("-" * 60)
    
    for fila in datos_reporte:
        print(f"Sede: {fila['nombre']}")
        print(f"Provincia{fila['provincia']}")
        print(f"Tipo{fila['tipo']}")
        
        print(f"Total ventas semanal : ₡{fila['total']:,.2f}")
        #Clasificacion, porcentaje meta y promedio semanal
        print(f"Cuplimiento de meta: {fila['porcentaje']:.2f}%")
        print(f"Clasificacion: {fila['clasificacion']}")
        print(f"Promedio diario: ₡{fila['total']/5:,.2f}")
        print('-' * 60)

reporte = []
for emprendimiento in sedes: 
#print ("La variable sedes es tipo", type(sedes).__name__)
#primer_emprendimiento = sedes[0]
#print("Terminar empredimineto", primer_emprendimiento)
#print("Tipos : ", type(primer_emprendimiento))
#print ("Nombre : ", primer_emprendimiento["nombre"])
#print("Provincia : ", primer_emprendimiento["provincia"])
#print("Ventas : ",primer_emprendimiento["ventas"])

    ventas = emprendimiento["ventas"]
    meta = emprendimiento["meta"]
    nombre = emprendimiento ["nombre"]

    total_ventas = calcular_total(ventas)
    porcentaje_emprendimiento = calcular_porcentaje_logro(total_ventas,meta)
    clasificacion = calcular_clasificacion (porcentaje_emprendimiento)
    
    reporte.append(
        {
            "nombre" :  emprendimiento ["nombre"],
            "provincia" : emprendimiento ["provincia"],
            "tipo":emprendimiento ["tipo"],
            "total": total_ventas,
            "porcentaje": porcentaje_emprendimiento,
            "clasificacion": clasificacion,
        }
        
    )
imprimir_reporte(reporte)

    #print(f"\n---Emprendimiento {nombre} ---")
    #print("total Ventas : ", total_ventas)
    #print("porcentaje de logro", porcentaje_emprendimiento)
    #print(calcular_clasificacion(porcentaje_emprendimiento))