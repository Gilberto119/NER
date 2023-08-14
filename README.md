# Procedimiento de Ejecución 
<br>
Para poder ejecutar la API se toman en cuenta los siguientes pasos 
<ol>
  <li>Tener el entorno de programación ubicado en la carpeta Kosmos</li>
  <li>Ingresar en la terminal el comando "venv\Scripts\activate" con el objetivo de activar la maquina virtual</li>
  <li>Ejecutar la aplicación web con el comando "python app\app.py"</li>
  <li>Asegurarse que la aplicación corra en el puerto "http://127.0.0.1:5000"</li>
</ol>

<br>
Para poder probar el API se utiliza la herramienta POSTMAN, dentro de esta herramienta ponemos lo siguiente:  
<ol>
  <li>Dirección "http://127.0.0.1:5000/ner"</li>
  <li>seleccionamos el método POST</li>
  <li>seleccionamos Body y elegimos formato "raw"</li>
  <li>verificamos que el formato de entrada este en JSON e ingresamos el siguiente texto: </li>
  <br> 
    {
      "oraciones": [
          "Apple está buscando comprar una startup del Reino Unido por mil millones de dólares.",
          "San Francisco considera prohibir los robots de entrega en la acera.",
          "Jon Bloomberg piensa adquirir acciones de wallstreet en New York."
      ]
  }
  <br><br>
  <li> Oprimimos el boton send </li>
</ol>

<br><br>
El resultado deberia ser el siguiente: <br> <br>

{
    "resultado": [
        {
            "entidades": {
                "Apple": "ORG",
                "Reino Unido": "LOC"
            },
            "oracion": "Apple está buscando comprar una startup del Reino Unido por mil millones de dólares."
        },
        {
            "entidades": {
                "San Francisco": "LOC"
            },
            "oracion": "San Francisco considera prohibir los robots de entrega en la acera."
        },
        {
            "entidades": {
                "Jon Bloomberg": "PER",
                "New York": "LOC"
            },
            "oracion": "Jon Bloomberg piensa adquirir acciones de wallstreet en New York."
        }
    ]
}
