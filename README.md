# IntroDevOps-Proyecto
Desarrollado por: Ana Valentina Dinardi, Javier Salvatierra y Fabricio Quintana

## Instrucciones para instalar Flask:

Se debe contar con python instalado, se puede verificar con python --version o py --version

En Windows:
```bash
py -3 -m venv .venv
.venv\Scripts\activate
pip install Flask
```

En Linux:
```bash
pip install flask
```

##  Cómo correr la API:
Para correr la API, se debe ejecutar el siguiente comando en la terminal:
```bash
python app.py o py app.py
```

## Ejemplos de uso de los Endpoints

Se detallan los ejemplos para consumir la API utilizando `curl` desde la terminal o mediante peticiones HTTP estándar.
También se puede utilizar herramientas como Postman para realizar las peticiones.

---

### 1. Obtener todos los Pokémon

Devuelve la lista completa de Pokémons.

* **Método:** `GET`
* **Ruta:** `/pokemons`
* **Código de respuesta:** `200 OK`

#### Ejemplo de Petición (cURL):
```bash
curl -X GET [http://127.0.0.1:5000/pokemons](http://127.0.0.1:5000/pokemons)
```

### 2. Obtener un Pokémon por ID

Busca y devuelve los datos de un Pokémon específico utilizando su ID único.

* **Método:** `GET`
* **Ruta:** `/pokemons/<pokemon_id>`
* **Parámetros de URL:** `pokemon_id` (Entero) — El ID del Pokémon a buscar.
* **Código de respuesta:** `200 OK` si se encuentra el Pokémon, `404 Not Found` si no se encuentra.

#### Ejemplo de Petición Exitosa (cURL):

```bash
curl -X GET [http://127.0.0.1:5000/pokemons/1](http://127.0.0.1:5000/pokemons/1)
```

### 3. Crear un nuevo Pokémon

Agrega un nuevo objeto Pokémon a la lista. Debe enviarse un cuerpo JSON con la estructura correcta y un `id` que no exista previamente.

* **Método:** `POST`
* **Ruta:** `/pokemons`
* **Headers:** `Content-Type: application/json`
* **Código de respuesta:** `201 Created`

#### Ejemplo de Petición (cURL):
```bash
curl -X POST [http://127.0.0.1:5000/pokemons](http://127.0.0.1:5000/pokemons) \
  -H "Content-Type: application/json" \
  -d '{
    "id": 3,
    "nombre": "Squirtle",
    "imagen": "https://link_a_imagen_de_squirtle.jpg",
    "caracteristicas": {
      "peso": 9.0,
      "altura": 0.5,
      "fuerza": 48,
      "edad": 3
    },
    "habilidades": ["Pistola Agua", "Burbuja"],
    "tipo": "Agua",
    "habitat": "Lagos"
  }'
```


### 4. Actualizar un Pokémon existente

Modifica los atributos de un Pokémon existente especificando su `id` en la URL. No permite modificar el campo `id`.

* **Método:** `PUT`
* **Ruta:** `/pokemons/<pokemon_id>`
* **Parámetros de URL:** `pokemon_id` (Entero) — ID del Pokémon a actualizar.
* **Headers:** `Content-Type: application/json`
* **Código de respuesta:** `200 OK`

#### Ejemplo de Petición (cURL):

```bash
curl -X PUT [http://127.0.0.1:5000/pokemons/1](http://127.0.0.1:5000/pokemons/1) \
  -H "Content-Type: application/json" \
  -d '{
    "nombre": "Pikachu Editado",
    "caracteristicas": {
      "peso": 6.5,
      "altura": 0.4,
      "fuerza": 60,
      "edad": 6
    },
    "habitat": "Ciudad"
  }'
```


### 5. Eliminar un Pokémon

Elimina de la base de datos el Pokémon asociado al `id` especificado.

* **Método:** `DELETE`
* **Ruta:** `/pokemons/<pokemon_id>`
* **Parámetros de URL:** `pokemon_id` (Entero) — ID del Pokémon a eliminar.
* **Código de respuesta:** `200 OK`

#### Ejemplo de Petición (cURL):

```bash
curl -X DELETE [http://127.0.0.1:5000/pokemons/2](http://127.0.0.1:5000/pokemons/2)
```