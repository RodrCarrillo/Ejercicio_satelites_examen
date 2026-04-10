# Ejercicio_satelites_examen
Basicamente mi promt y un poco del pseudocodigo:

Vamos a hacer un trabajo de multiprocessing en Python, simularemos que estamos recibiendo y procesando imágenes satelitales y que el proceso es lento y complejo. No vamos a procesar ninguna imagen, solo fingirlo. Crea una función que diga procesando imagen y el nombre de la imagen, luego llame a funciones compartidas (vamos a usar `.manager`) que digan cosas como `print(f"filtrando datos de {nombre_imagen}")`, `print(f"Iluminando {nombre_imagen}")`, finalmente diga `f"{nombre_imagen esta lista}"` que ha terminado. Quiero que el tiempo que se tarda en procesar cada imagen sea aleatorio.

Nuestros multiprocesos van a ser divididos en zonas, les pondremos nombres como `zona1 = multiprocessing.Process()` y que cada proceso contenga una lista de diccionarios que digan cosas como `imagen1 = {"coordenadas": {"x": 0, "y": 0}, "numero_zona": 1}` el número de zona es el mismo que el del proceso llamado zona, "x" e "y" toman valores del 1 al 5.
Finalmente, juntamos todos los procesos y los ordenamos con threading en listas con la misma "x" en el diccionario


Necesitas instalar:
import multiprocessing
import threading
import time
import random

