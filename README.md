# PROYECTO POKEMON - PYTHON!!

-----------------------
## Descripción

"PROYECTO POKEMON - PYTHON!!" es una aplicación desarrollada con Django que permite gestionar información relacionada con el mundo Pokémon. La aplicación ofrece las siguientes funcionalidades:

    - **Agregar Pokemones:**  Los usuarios pueden agregar Pokemones a la base de datos utilizando un formulario que recopila información como el nombre, el tipo y el ataque del Pokémon.

    - **Crear Entrenadores Pokémon:** Los usuarios pueden crear perfiles de Entrenadores Pokémon, proporcionando detalles como el nombre, el apellido y su tipo de Pokémon favorito.

    - **Crear Gimnasios Pokémon:** La aplicación permite crear gimnasios Pokémon, con información como el nombre, el tipo y el líder del gimnasio.

    - **Búsqueda de Pokémon:** Los usuarios pueden buscar Pokémon por nombre y ver sus detalles.

    - **Listado de Clases:** La aplicación muestra un listado completo de todos los elementos en las tres clases: Pokémon, Entrenadores Pokémon y Gimnasios Pokémon.

## Servidor
[!IMPORTANT]
La aplicación sigue la arquitectura MVT (Model-View-Template) de Django y se ejecuta en el servidor local utilizando el comando:

    > $ py manage.py runserver

## Rutas Principales

    - **Panel de Administración:** http://localhost:8000/admin - Accede al panel de administración de Django para gestionar los datos de la aplicación.

    - **Página de Inicio:** http://localhost:8000/PokeApp - Página de inicio de la aplicación.

    - **Gestión de Pokemones:** http://localhost:8000/PokeApp/pokemon/ - Gestiona y agrega Pokemones.

    - **Gestión de Entrenadores:** http://localhost:8000/PokeApp/master/ - Gestiona y crea perfiles de Entrenadores Pokémon.

    - **Gestión de Gimnasios:** http://localhost:8000/PokeApp/gym/ - Gestiona y crea Gimnasios Pokémon.

    - **Búsqueda de Pokémon:** http://localhost:8000/PokeApp/pokemon_search/ - Realiza búsquedas de Pokémon por nombre y muestra los resultados.
