import requests
import sqlite3
import os

# Obtener información de Pokémon desde la PokeAPI
def obtener_info_pokemon(nombre_pokemon):
    url = f'https://pokeapi.co/api/v2/pokemon/{nombre_pokemon.lower()}'
    respuesta = requests.get(url)
    if respuesta.status_code == 200:
        return respuesta.json()
    else:
        print("Pokémon no encontrado.")
        return None

# Agregar Pokémon a la base de datos
def agregar_pokemon_bd(nombre, info, poseidos):
    conn = sqlite3.connect("pokemontam.db")
    cursor = conn.cursor()
    
    # Verificar si el Pokémon ya existe
    cursor.execute('SELECT * FROM pokemones WHERE nombre = ?', (nombre.lower(),))
    pokemon_existente = cursor.fetchone()
    
    if pokemon_existente:
        # Actualizar el número de Pokémon poseídos si ya existe
        cursor.execute('''
            UPDATE pokemones
            SET poseidos = poseidos + ?
            WHERE nombre = ?
        ''', (poseidos, nombre.lower()))
    else:
        # Insertar nuevo registro de Pokémon
        cursor.execute('''
            INSERT INTO pokemones (id, nombre, altura, peso, tipos, habilidades, poseidos)
            VALUES (?, ?, ?, ?, ?, ?, ?)
        ''', (
            info['id'],
            nombre.lower(),  # Almacenar nombres en minúsculas para garantizar consistencia
            info['height'],
            info['weight'],
            ', '.join([t['type']['name'] for t in info['types']]),
            ', '.join([a['ability']['name'] for a in info['abilities']]),
            poseidos
        ))
    
    conn.commit()
    conn.close()

# Eliminar Pokémon de la base de datos
def eliminar_pokemon_bd(nombre):
    conn = sqlite3.connect("pokemontam.db")
    cursor = conn.cursor()
    cursor.execute('DELETE FROM pokemones WHERE nombre = ?', (nombre.lower(),))
    conn.commit()
    conn.close()

# Crear la base de datos y la tabla de Pokémon
def iniciar_bd():
    if not os.path.exists("pokemontam.db"):
        conn = sqlite3.connect("pokemontam.db")
        cursor = conn.cursor()
        cursor.execute('DROP TABLE IF EXISTS pokemones')
        cursor.execute('''
            CREATE TABLE pokemones (
                id INTEGER PRIMARY KEY,
                nombre TEXT UNIQUE,
                altura INTEGER,
                peso INTEGER,
                tipos TEXT,
                habilidades TEXT,
                poseidos INTEGER
            )
        ''')
        conn.commit()
        conn.close()

# Obtener todos los nombres de Pokémon de la base de datos
def obtener_todos_nombres_pokemon():
    conn = sqlite3.connect("pokemontam.db")
    cursor = conn.cursor()
    cursor.execute('SELECT nombre FROM pokemones')
    resultado = cursor.fetchall()
    conn.close()
    return [nombre[0] for nombre in resultado]

# Buscar un Pokémon en la base de datos
def buscar_pokemon_bd(nombre_pokemon):
    conn = sqlite3.connect("pokemontam.db")
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM pokemones WHERE nombre = ?', (nombre_pokemon.lower(),))
    resultado = cursor.fetchone()
    conn.close()
    return resultado

# Limpiar la pantalla del terminal
def limpiar_pantalla():
    os.system('cls' if os.name == 'nt' else 'clear')

# Mostrar el menú principal y manejar las opciones del usuario
def principal():
    iniciar_bd()
    
    while True:
        limpiar_pantalla()
        print("\nSelecciona una opción:")
        print("1. Buscar un Pokémon (PokeAPI)")
        print("2. Ver Pokémon poseídos (Base de datos)")
        print("3. Salir")
        eleccion = input("Ingresa tu elección: ")

        if eleccion == "1":
            limpiar_pantalla()
            nombre_pokemon = input("Ingresa el nombre del Pokémon: ")
            info_pokemon = obtener_info_pokemon(nombre_pokemon)
            if info_pokemon:
                print(f"Nombre: {info_pokemon['name'].capitalize()}")
                print(f"Altura: {info_pokemon['height']}")
                print(f"Peso: {info_pokemon['weight']}")
                print(f"Tipos: {', '.join([t['type']['name'] for t in info_pokemon['types']])}")
                print(f"Habilidades: {', '.join([a['ability']['name'] for a in info_pokemon['abilities']])}")
                guardar = input("¿Quieres agregar este Pokémon a tu Pokédex? (si/no): ").lower()
                if guardar == 'si':
                    poseidos = int(input("Ingresa el número de poseídos: "))
                    agregar_pokemon_bd(nombre_pokemon, info_pokemon, poseidos)
                    print("Pokémon agregado a tu Pokédex.")
                else:
                    print("Regresando al menú principal.")
                input("Presiona Enter para regresar al menú principal...")

        elif eleccion == "2":
            limpiar_pantalla()
            print("\nSelecciona una opción:")
            print("1. Mostrar lista de nombres de todos los Pokémon")
            print("2. Buscar por nombre de Pokémon")
            print("3. Eliminar un Pokémon")
            eleccion_bd = input("Ingresa tu elección: ")

            if eleccion_bd == "1":
                limpiar_pantalla()
                nombres = obtener_todos_nombres_pokemon()
                if nombres:
                    print("Pokémon en tu Pokédex:")
                    for nombre in nombres:
                        print(nombre.capitalize())
                else:
                    print("No se encontraron Pokémon en tu Pokédex.")
                input("Presiona Enter para regresar al menú principal...")

            elif eleccion_bd == "2":
                limpiar_pantalla()
                nombre = input("Ingresa el nombre del Pokémon a buscar: ")
                resultado = buscar_pokemon_bd(nombre)
                if resultado:
                    print(f"Nombre: {resultado[1].capitalize()}")
                    print(f"Altura: {resultado[2]}")
                    print(f"Peso: {resultado[3]}")
                    print(f"Tipos: {resultado[4]}")
                    print(f"Habilidades: {resultado[5]}")
                    print(f"Poseídos: {resultado[6]}")
                    eliminar = input("¿Quieres eliminar este Pokémon de tu Pokédex? (si/no): ").lower()
                    if eliminar == 'si':
                        eliminar_pokemon_bd(nombre)
                        print("Pokémon eliminado de tu Pokédex.")
                else:
                    print("Pokémon no encontrado en tu Pokédex.")
                input("Presiona Enter para regresar al menú principal...")

            elif eleccion_bd == "3":
                limpiar_pantalla()
                nombre = input("Ingresa el nombre del Pokémon a eliminar: ")
                if buscar_pokemon_bd(nombre):
                    eliminar_pokemon_bd(nombre)
                    print(f"Pokémon {nombre.capitalize()} eliminado de tu Pokédex.")
                else:
                    print("Pokémon no encontrado en tu Pokédex.")
                input("Presiona Enter para regresar al menú principal...")

            else:
                print("Elección inválida. Regresando al menú principal.")
                input("Presiona Enter para regresar al menú principal...")

        elif eleccion == "3":
            limpiar_pantalla()
            print("Saliendo de la aplicación.")
            break

        else:
            limpiar_pantalla()
            print("Elección inválida. Por favor, intenta de nuevo.")
            input("Presiona Enter para regresar al menú principal...")

if __name__ == "__main__":
    principal()
