# Prueba 1. Organizador de horarios sin colisiones
from typing import List, Tuple, Set

class Materia:
    def __init__(self, nombre: str, grupo: int, profesor: str, horario: Tuple[int, int], dias: List[str]) -> None:
        self.nombre = nombre
        self.grupo = grupo
        self.profesor = profesor
        self.horario = horario  # (inicio, fin)
        self.dias = dias  # Lista de días (ejemplo: ['L', 'M'])

    def __str__(self) -> str:
        return f"Materia: {self.nombre} \n" \
               f"\tProfesor: {self.profesor} \n" \
               f"\tGrupo: {self.grupo} \n" \
               f"\tHorario: {self.horario[0]} - {self.horario[1]}\n" \
               f"\tDías: {', '.join(self.dias)}"
    

# Función para seleccionar materias sin conflictos de horarios
def OrganizadorHorario(materias: list[list[Materia]]) -> list[Materia]:
    seleccionadas = []  # Lista para almacenar las materias seleccionadas
    horarios_ocupados = set()  # Conjunto para almacenar horarios ocupados
    
    for lista_materias in materias:
        # Ordenamos las materias por horario para optimizar la asignación
        lista_materias.sort(key=lambda materia: materia.horario)
        
        for materia in lista_materias:
            # Verificamos si el horario de la materia ya está ocupado
            if materia.horario not in horarios_ocupados:
                seleccionadas.append(materia)
                horarios_ocupados.add(materia.horario)  # Añadimos el horario al conjunto de ocupados
                break  # Si se encuentra un horario libre, se pasa a la siguiente lista de materias
            # Si el horario ya está ocupado, buscamos la siguiente opción
    
    return seleccionadas


# Instancias de las materias
algebra_lineal_basica = [
    Materia("Algebra lineal basica", 1, "Sandra Carolina García", (7, 9), ["Ma", "J"]),
    Materia("Algebra lineal basica", 2, "Carolina Neira Jimenez", (7, 9), ["Ma", "J"])
]

calculo_ecuaciones_diferenciales = [
    Materia("Cálculo de ecuaciones diferenciales ordinarias", 1, "Mauricio Lopez Hernandez", (14, 16), ["L", "Mi"]),
    Materia("Cálculo de ecuaciones diferenciales ordinarias", 2, "Juan Carlos Hernandez Rincón", (14, 16), ["L", "Mi"]),
    Materia("Cálculo de ecuaciones diferenciales ordinarias", 3, "Victor Manuel Ardilla", (14, 16), ["L", "Mi"])
]

calculo_diferencial = [
    Materia("Cálculo Diferencial", 1, "Natalia Camila Pinzón Cortes", (9, 11), ["Mi", "V"]),
    Materia("Cálculo Diferencial", 2, "Nicolás Martinez Alba", (9, 11), ["Mi", "V"]),
    Materia("Cálculo Diferencial", 3, "Gustavo Adolfo Nieto Clavijo", (9, 11), ["Mi", "V"]),
    Materia("Cálculo Diferencial", 4, "Leonardo Rendon Arbelaez", (9, 11), ["Mi", "V"])
]

calculo_integral = [
    Materia("Cálculo Integral", 1, "Omar Duque Gomez", (9, 11), ["Mi", "V"]),
    Materia("Cálculo Integral", 2, "Mauricio Bogoya Lopez", (9, 11), ["Mi", "V"]),
    Materia("Cálculo Integral", 3, "Martha Cecilia Moreno Penagos", (9, 11), ["Mi", "V"]),
    Materia("Cálculo Integral", 4, "Herbert Alonso Dueñas Ruiz", (9, 11), ["Mi", "V"])
]

poo = [
    Materia("POO", 1, "Jorge Enrique Amaya Cala", (18, 20), ["L", "Mi"]),
    Materia("POO", 10, "Fernando Ospina Marín", (7, 9), ["L", "Mi"]),
    Materia("POO", 11, "Fernando Ospina Marín", (9, 11), ["L", "Mi"]),
    Materia("POO", 12, "Paula Ximena Rodríguez Nempeque", (6, 8), ["Ma", "J"]),
    Materia("POO", 13, "Edgar Miguel Vargas Chaparro", (14, 16), ["L", "Mi"]),
    Materia("POO", 2, "Cristhian Fernando Lara Espejo", (9, 11), ["Ma", "J"]),
    Materia("POO", 3, "Néstor Germán Bolívar Pulgarín", (14, 16), ["Ma", "J"]),
    Materia("POO", 4, "Felipe González Roldán", (14, 16), ["L", "Mi"]),
    Materia("POO", 5, "Rafael Antonio Acosta Rodríguez", (7, 9), ["Ma", "J"]),
    Materia("POO", 6, "Paula Ximena Rodríguez Nempeque", (7, 9), ["L", "Mi"]),
    Materia("POO", 7, "Jorge Enrique Amaya Cala", (7, 9), ["L", "Mi"]),
    Materia("POO", 8, "Néstor Germán Bolívar Pulgarín", (16, 18), ["Ma", "J"]),
    Materia("POO", 9, "David Alberto Herrera Álvarez", (11, 1), ["L", "Mi"])
]

sistemas_numericos = [
    Materia("Sistemas Numéricos", 1, "German Preciado López", (9, 11), ["Ma", "J"]),
    Materia("Sistemas Numéricos", 2, "Ricardo Ariel Pastrán Ramírez", (9, 11), ["Ma", "J"]),
    Materia("Sistemas Numéricos", 3, "John Jaime Rodríguez Vega", (9, 11), ["Ma", "J"])
]

probabilidad = [
    Materia("Probabilidad", 1, "Carlos Eduardo Alonso Malaver", (11, 1), ["Mi", "V"])
]

introduccion_al_analisis_real = [
    Materia("Introducción al Análisis Real", 1, "Mauricio Bogoya López", (11, 1), ["Mi", "V"])
]

introduccion_a_cc = [
    Materia("Introducción a CC", 1, "Arles Ernesto Rodríguez Portela", (11, 1), ["Ma", "J"]),
    Materia("Introducción a CC", 2, "Juan Carlos Galvis Arrieta", (9, 11), ["Ma", "J"])
]

introduccion_a_teoria_de_conjuntos = [
    Materia("Introducción a Teoría de Conjuntos", 1, "Pedro Hernán Zambrano Ramírez", (9, 11), ["Ma", "J"]),
    Materia("Introducción a Teoría de Conjuntos", 2, "Yeison Alexander Sánchez Rubio", (14, 16), ["Ma", "J"])
]

fundamentos_de_matematicas = [
    Materia("Fundamentos de Matemáticas", 1, "Mauro Artigiani", (7, 9), ["Ma", "J"]),
    Materia("Fundamentos de Matemáticas", 2, "Sergio Alejandro Carrillo Torres", (7, 9), ["Ma", "J"]),
    Materia("Fundamentos de Matemáticas", 3, "Oscar Guillermo Riaño Castañeda", (7, 9), ["Ma", "J"]),
    Materia("Fundamentos de Matemáticas", 4, "Daniel Nuñez Alarcón", (7, 9), ["Ma", "J"])
]

estructuras_de_datos = [
    Materia("Estructuras de Datos", 1, "Edwin Andres Niño Velasquez", (14, 16), ["Ma", "J"]),
    Materia("Estructuras de Datos", 3, "Jhon Alexander Lopez Fajardo", (16, 18), ["Ma", "J"]),
    Materia("Estructuras de Datos", 4, "Jhon Alexander Lopez Fajardo", (9, 11), ["Ma", "J"]),
    Materia("Estructuras de Datos", 5, "David Alberto Herrera Alvarez", (7, 9), ["L", "Mi"]),
    Materia("Estructuras de Datos", 2, "David Alberto Herrera Alvarez", (9, 11), ["L", "Mi"])
]

# Lista que contiene todas las materias
materias = [
    algebra_lineal_basica, 
    calculo_ecuaciones_diferenciales, 
    calculo_diferencial,
    calculo_integral,
    poo,
    sistemas_numericos,
    probabilidad,
    introduccion_al_analisis_real,
    introduccion_a_cc,
    introduccion_a_teoria_de_conjuntos,
    fundamentos_de_matematicas,
    estructuras_de_datos
]

# Organizar el horario sin colisiones
seleccionadas = OrganizadorHorario(materias)

print("Materias seleccionadas sin colisiones de horario:")
for materia in seleccionadas:
    print("_" * 40)
    print(materia)
