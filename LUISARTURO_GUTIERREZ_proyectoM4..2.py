import requests
import json
import os

def buscar_pokemon(nombre):
    url = f"https://pokeapi.co/api/v2/pokemon/{nombre.lower()}"
    response = requests.get(url)

    if response.status_code == 404:
        print("El Pokémon no fue encontrado.")
        return None

    data = response.json()
    imagen = data["sprites"]["front_default"]
    peso = data["weight"]
    altura = data["height"]
    movimientos = [movimiento["move"]["name"] for movimiento in data["moves"]]
    habilidades = [habilidad["ability"]["name"] for habilidad in data["abilities"]]
    tipos = [tipo["type"]["name"] for tipo in data["types"]]

    pokemon = {
        "nombre": nombre,
        "imagen": imagen,
        "peso": peso,
        "altura": altura,
        "movimientos": movimientos,
        "habilidades": habilidades,
        "tipos": tipos
    }

    return pokemon

def guardar_pokemon(pokemon):
    carpeta_pokedex = "pokedex"
    if not os.path.exists(carpeta_pokedex):
        os.makedirs(carpeta_pokedex)

    nombre_archivo = f"{carpeta_pokedex}/{pokemon['nombre']}.json"
    with open(nombre_archivo, "w") as archivo:
        json.dump(pokemon, archivo, indent=4)

def mostrar_info_pokemon(pokemon):
    print("Nombre:", pokemon["nombre"])
    print("Imagen:", pokemon["imagen"])
    print("Peso:", pokemon["peso"])
    print("Altura:", pokemon["altura"])
    print("Movimientos:", ", ".join(pokemon["movimientos"]))
    print("Habilidades:", ", ".join(pokemon["habilidades"]))
    print("Tipos:", ", ".join(pokemon["tipos"]))

# Ciclo principal del programa
while True:
    # Obtener el nombre del Pokémon desde el usuario
    nombre_pokemon = input("Ingrese el nombre de un Pokémon (o 'q' para salir): ")

    # Verificar si se quiere salir del programa
    if nombre_pokemon.lower() == "q":
        break

    # Buscar el Pokémon en la Pokédex
    pokemon = buscar_pokemon(nombre_pokemon)

    if pokemon:
        mostrar_info_pokemon(pokemon)
        guardar_pokemon(pokemon)

