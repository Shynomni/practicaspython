import random
import matplotlib.pyplot as plt

def simular_galton(num_canicas, num_niveles):
    contenedores = [0] * (num_niveles + 1)  # Inicializar los contenedores con 0 canicas

    for _ in range(num_canicas):
        nivel = 0  # Comenzar en el nivel superior
        for _ in range(num_niveles):
            lado = random.choice(['Izquierda', 'Derecha'])  # Elegir al azar izquierda o derecha
            if lado == 'Derecha':
                nivel += 1  # Avanzar al siguiente nivel a la derecha
        contenedores[nivel] += 1  # Incrementar el contador del contenedor correspondiente

    return contenedores

def graficar_histograma(contenedores):
    num_contenedores = len(contenedores)
    niveles = list(range(num_contenedores))
    cantidad_canicas = contenedores

    plt.bar(niveles, cantidad_canicas)
    plt.xlabel('Contenedor')
    plt.ylabel('Cantidad de canicas')
    plt.title('Máquina de Galton - Histograma de canicas en cada contenedor')
    plt.show()

# Simular la máquina de Galton con 3000 canicas y 12 niveles
num_canicas = 3000
num_niveles = 12

contenedores = simular_galton(num_canicas, num_niveles)
graficar_histograma(contenedores)

# Agregar un encabezado adicional al gráfico
plt.title("Histograma de canicas en cada contenedor - Máquina de Galton") 



