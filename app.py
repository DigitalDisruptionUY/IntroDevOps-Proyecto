from flask import Flask, jsonify, request

app = Flask(__name__)

# Base de datos en memoria para almacenar los Pokémon
pokemons = [
    {
        "id": 1,
        "nombre": "Pikachu",
        "imagen": "https://link_a_imagen_de_pikachu.jpg",
        "caracteristicas": {
            "peso": 6.0,
            "altura": 0.4,
            "fuerza": 55,
            "edad": 5
        },
        "habilidades": ["Impactrueno", "Cola férrea"],
        "tipo": "Eléctrico",
        "habitat": "Bosques"
    },
    {
        "id": 2,
        "nombre": "Charmander",
        "imagen": "https://link_a_imagen_de_charmander.jpg",
        "caracteristicas": {
            "peso": 8.5,
            "altura": 0.6,
            "fuerza": 52,
            "edad": 4
        },
        "habilidades": ["Llamarada", "Arañazo"],
        "tipo": "Fuego",
        "habitat": "Montañas"
    }
]

@app.route('/pokemons', methods=['GET'])
def get_pokemons():
    """
    Obtiene la lista de todos los Pokémon.
    """
    return jsonify(pokemons), 200

@app.route('/pokemons', methods=['POST'])
def create_pokemon():
    """
    Crea un nuevo Pokémon.
    """
    
    # Obtener los datos del cuerpo de la solicitud
    data = request.get_json()

    #Validar que hayan datos
    if not data:
        return jsonify({"error": "No se proporcionaron datos"}), 400
    
    #Validar que el id no existe previamente
    if any(pokemon['id'] == data['id'] for pokemon in pokemons):
        return jsonify({"error": "El Pokémon con este ID ya existe"}), 400

    #Agregar el nuevo Pokémon a la lista
    pokemons.append(data)

    # Devolver una respuesta exitosa con el Pokémon creado
    return jsonify({
        "message": "Pokémon creado exitosamente",
        "pokemon": data
    }), 201
  
#Obtener por id
@app.route('/pokemons/<pokemon_id>', methods=['GET'])
def get_pokemon_by_id(pokemon_id):
    """
    Obtiene un Pokémon por su ID.
    """
    # Recorre la lista de Pokémon y hasta el que tenga el ID especificado, sino ninguno
    pokemon = next((p for p in pokemons if p["id"] == int(pokemon_id)), None)
    if pokemon:
        return jsonify(pokemon), 200
    else:
        return jsonify({"error": "Pokémon no encontrado"}), 404

#modificar por id
@app.route('/pokemons/<pokemon_id>', methods=['PUT'])
def update_pokemon(pokemon_id):
    """
    Modifica un Pokémon existente por su ID.
    """
    # Obtener los datos del cuerpo de la solicitud
    data = request.get_json()

    # Validar que hayan datos
    if not data:
        return jsonify({"error": "No se proporcionaron datos"}), 400

    # Buscar el Pokémon por ID
    pokemon = next((p for p in pokemons if p["id"] == int(pokemon_id)), None)

    if not pokemon:
        return jsonify({"error": "Pokémon no encontrado"}), 404

    # Actualizar los campos del Pokémon (evitando cambiar el id)
    for key, value in data.items():
        if key != "id":
            pokemon[key] = value

    return jsonify({
        "message": "Pokémon actualizado exitosamente",
        "pokemon": pokemon
    }), 200


#Borrar por id
@app.route('/pokemons/<pokemon_id>', methods=['DELETE'])
def delete_pokemon(pokemon_id):
    """
    Elimina un Pokémon por su ID.
    """
    # Buscar el Pokémon por ID
    pokemon = next((p for p in pokemons if p["id"] == int(pokemon_id)), None)

    if not pokemon:
        return jsonify({"error": "Pokémon no encontrado"}), 404

    # Eliminarlo de la lista
    pokemons.remove(pokemon)

    return jsonify({
        "message": "Pokémon eliminado exitosamente",
        "pokemon": pokemon
    }), 200

if __name__ == '__main__':
    # Ejecuta la aplicación en modo debug para desarrollo
    app.run(debug=True)