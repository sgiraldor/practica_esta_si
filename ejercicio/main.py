from ejercicio.cola import Persona
import random
from ejercicio.cola import PriorityQueue
from ejercicio.cola import InformacionPersona
from ejercicio.importar import nombres
from ejercicio.importar import apellidos
from ejercicio.importar import problemas_tecnicos

def main(iteracion):
    contador = 1
    cola = PriorityQueue()
    while contador <= iteracion:
        nombre = random.choice(nombres)
        apellido = random.choice(apellidos)
        tecnicos = random.choice(problemas_tecnicos)
        urgencia = random.randint(1,3)
        numero_de_solicitud = random.randint(1, 2500)

        persona = Persona(urgencia, nombre, tecnicos, numero_de_solicitud)
        informacion_persona = InformacionPersona(persona)
        cola.enqueue(informacion_persona)
        contador += 1

    cola = cola.llevar_a_primera_posicion()
    cola.imprimir_cola()

if __name__ == "__main__":
    main(100)


