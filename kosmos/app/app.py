from flask import Flask, request, jsonify
import spacy

app = Flask(__name__)
nlp = spacy.load("es_core_news_sm")



def result(oraciones):
    """
    Al definir una funcion result que retonarna un diccionario con el resultado de la extracción de entidades,
    debemos tomar en cuenta la siguiente estructura: 

        {
            "oraciones": [
                "Apple está buscando comprar una startup del Reino Unido por mil millones de dólares.",
                "San Francisco considera prohibir los robots de entrega en la acera."
            ]
        }

    por ende el resultado debe ser un diccionario con la siguiente estructura:

        {
            "resultado": [
                    {
                    "oración": "Apple está buscando comprar una startup del Reino Unido por mil millones
                    de dólares.",
                    "entidades": {
                    "Apple": "ORG",
                    "Reino Unido": "LOC",
                    }
                },
                    {
                    "oración": "San Francisco considera prohibir los robots de entrega en la acera.",
                    "entidades": {
                    "San Francisco": "LOC"
                    }
                }
            ]
        }



    """

    resultado = [] # Creamos una lista vacía para almacenar los resultados

    for oracion in oraciones: # Iteramos sobre la lista de oraciones  para poder tener el formato de salida deseado
            doc = nlp(oracion) #Se procesa la oracion con el modelo es_core_news_sm
            entidad = {} # Creamos un diccionario vacío para almacenar las entidades

            for ent in doc.ents: # Iteramos sobre las entidades de la oración
                entidad[ent.text] = ent.label_
            
            resultado.append({ # se junta la oracion y las entidades en un diccionario
                'oracion': oracion,
                'entidades': entidad
                
                
            })



            respuesta = { # se retorna todo en un diccionario 
                'resultado': resultado
            }

    return respuesta

@app.route('/ner', methods=['POST'])
def recognize_entities():
    data = request.get_json() # El request del get_json() es el body de la petición
    oraciones = data.get('oraciones', '') # El get() es para obtener el valor de la llave 'oraciones' del diccionario data

    entities = result(oraciones) # Llamamos a la función result() y le pasamos como parámetro la variable oraciones la cual retorna un diccionario con el resultado

    return jsonify(entities) # Retornamos el resultado en formato JSON

if __name__ == '__main__':
    app.run(debug=True)
