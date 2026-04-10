import multiprocessing
import threading
import time
import random

# --- Funciones de Procesamiento ---

def filtrar_datos(nombre):
    print(f"  [FILTRO] Filtrando datos de {nombre}...")
    time.sleep(random.uniform(0.5, 1.5))

def iluminar_imagen(nombre):
    print(f"  [LUZ] Iluminando {nombre}...")
    time.sleep(random.uniform(0.5, 1.5))

def procesar_imagen(imagen_dict, lista_compartida):
    nombre = f"Img_{imagen_dict['numero_zona']}_{imagen_dict['coordenadas']['x']}_{imagen_dict['coordenadas']['y']}"
    
    print(f"\n>>> Iniciando: {nombre}")
    
    # Llamada a funciones compartidas
    filtrar_datos(nombre)
    iluminar_imagen(nombre)
    
    print(f"✅ {nombre} está lista.")
    
    # Guardamos el resultado en la lista compartida del Manager
    lista_compartida.append(imagen_dict)

# --- Configuración de Tareas ---

def ejecutar_zona(id_zona, lista_compartida):
    # Creamos la lista de diccionarios para esta zona
    imagenes_zona = [
        {
            "coordenadas": {"x": x, "y": random.randint(1, 5)}, 
            "numero_zona": id_zona
        } 
        for x in range(1, 6)
    ]
    
    for img in imagenes_zona:
        procesar_imagen(img, lista_compartida)

# --- Flujo Principal ---

if __name__ == "__main__":
    # El Manager nos permite crear una lista que todos los procesos pueden ver
    with multiprocessing.Manager() as manager:
        resultados_globales = manager.list()
        procesos = []

        # 1. Creamos y lanzamos los Procesos (Zonas)
        for i in range(1, 4):  # Simularemos 3 zonas
            p = multiprocessing.Process(target=ejecutar_zona, args=(i, resultados_globales))
            procesos.append(p)
            p.start()

        # Esperamos a que todos los procesos terminen (Join)
        for p in procesos:
            p.join()

        print("\n" + "="*40)
        print("PROCESAMIENTO MULTIPROCESO COMPLETADO")
        print("="*40 + "\n")

        # 2. Uso de Threading para organizar los resultados por coordenada X
        # Convertimos la lista compartida a una lista normal de Python para el hilo
        datos_finales = list(resultados_globales)
        organizado = {}

        def organizar_por_x(datos):
            for item in datos:
                x_val = item["coordenadas"]["x"]
                if x_val not in organizado:
                    organizado[x_val] = []
                organizado[x_val].append(item)

        hilo_organizador = threading.Thread(target=organizar_por_x, args=(datos_finales,))
        hilo_organizador.start()
        hilo_organizador.join()

        # Mostrar resultados ordenados
        for x, lista in sorted(organizado.items()):
            print(f"Imágenes con Coordenada X = {x}:")
            for img in lista:
                print(f"   - Zona: {img['numero_zona']}, Y: {img['coordenadas']['y']}")

#https://github.com/RodrCarrillo/Ejercicio_satelites_examen/tree/main