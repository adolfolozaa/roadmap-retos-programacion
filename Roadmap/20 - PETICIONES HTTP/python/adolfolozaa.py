'''
* EJERCICIO:
 * Utilizando un mecanismo de peticiones HTTP de tu lenguaje, realiza
 * una petición a la web que tú quieras, verifica que dicha petición
 * fue exitosa y muestra por consola el contenido de la web.
 *
'''
import requests
import json



'''response = requests.get("https://google.com/hdhdhdhd")
if response.status_code == 200:
    print(response.text)
else:
    print(f"Error con código {response.status_code} al realizar la petición.")'''

'''
* DIFICULTAD EXTRA (opcional):
 * Utilizando la PokéAPI (https://pokeapi.co), crea un programa por
 * terminal al que le puedas solicitar información de un Pokémon concreto
 * utilizando su nombre o número.
 * - Muestra el nombre, id, peso, altura y tipo(s) del Pokémon
 * - Muestra el nombre de su cadena de evoluciones
 * - Muestra los juegos en los que aparece
 * - Controla posibles errores
'''

pokemon = input('introduce el nombre del pokemon a buscar:  ').lower()
response = requests.get(f"https://pokeapi.co/api/v2/pokemon/{pokemon}/")
if response.status_code == 200:
    data = response.json()
    print('Nombre: ', data['name'])
    print('ID: ', data['id'])
    print('Peso: ', data['weight'])
    print('Altura: ', data['height'])
    for type in data['types']:
        print('Tipo(s): ', type['type']['name'])
    for game in data["game_indices"]:
        print(game["version"]["name"])
    
    response = requests.get(
        f"https://pokeapi.co/api/v2/pokemon-species/{pokemon}/")

    if response.status_code == 200:
        url = response.json()['evolution_chain']['url']

        response = requests.get(url)

        if response.status_code == 200:
            data = response.json()

            print('Cadena de evolucion')
        
            def get_evolves(data):
                 print(data['species']['name'])
                 if 'evolves_to' in data:
                     for evolve in data['evolves_to']:
                        get_evolves(evolve)

            get_evolves(data['chain'])

        else:
            print(f"Error con código {response.status_code} aobteniendo evoluciones")
        
    else:
        print(f"Error con código {response.status_code} aobteniendo evoluciones")
    
else:
        print(f"Error  {response.status_code} Pokemon no encontrado")

