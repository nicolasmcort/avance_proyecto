class Materia:
    def __init__(self, nombre: str, grupo: int, profesor: str, horario: int, dias: str) -> None:
        self.nombre = nombre
        self.grupo = grupo
        self.profesor = profesor
        self.horario = horario
        self.dias = dias

    def __str__(self) -> str:
        return f"""Materia: {self.nombre} 
        \t Profesor: {self.profesor} 
        \t Grupo: {self.grupo} 
        \t Horario: {self.horario}
        \t Días: {self.dias}"""
    
# Función para seleccionar materias sin conflictos de horarios
def organizar_horario(materias: list[list[Materia]]) -> list[Materia]:
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
    Materia("Algebra lineal basica", 1, "Sandra Carolina García", 7, "mj"),
    Materia("Algebra lineal basica", 2, "Carolina Neira Jimenez", 7, "mj")
]

calculo_ecuaciones_diferenciales = [
    Materia("Cálculo de ecuaciones diferenciales ordinarias", 1, "Mauricio Lopez Hernandez", 14, "lM"),
    Materia("Cálculo de ecuaciones diferenciales ordinarias", 2, "Juan Carlos Hernandez Rincón", 14, "lM"),
    Materia("Cálculo de ecuaciones diferenciales ordinarias", 3, "Victor Manuel Ardilla", 14, "lM")
]

calculo_diferencial = [
    Materia("Cálculo Diferencial", 1, "Natalia Camila Pinzón Cortes", 9, "Mv"),
    Materia("Cálculo Diferencial", 2, "Nicolás Martinez Alba", 9, "Mv"),
    Materia("Cálculo Diferencial", 3, "Gustavo Adolfo Nieto Clavijo", 9, "Mv"),
    Materia("Cálculo Diferencial", 4, "Leonardo Rendon Arbelaez", 9, "Mv")
]

calculo_integral = [
    Materia("Cálculo Integral", 1, "Omar Duque Gomez", 9, "Mv"),
    Materia("Cálculo Integral", 2, "Mauricio Bogoya Lopez", 9, "Mv"),
    Materia("Cálculo Integral", 3, "Martha Cecilia Moreno Penagos", 9, "Mv"),
    Materia("Cálculo Integral", 4, "Herbert Alonso Dueñas Ruiz", 9, "Mv")
]

poo = [
    Materia("POO", 1, "Jorge Enrique Amaya Cala", 18, "lM"),
    Materia("POO", 10, "Fernando Ospina Marín", 7, "lM"),
    Materia("POO", 11, "Fernando Ospina Marín", 9, "lM"),
    Materia("POO", 12, "Paula Ximena Rodríguez Nempeque", 6, "mj"),
    Materia("POO", 13, "Edgar Miguel Vargas Chaparro", 14, "lM"),
    Materia("POO", 2, "Cristhian Fernando Lara Espejo", 9, "mj"),
    Materia("POO", 3, "Néstor Germán Bolívar Pulgarín", 14, "mj"),
    Materia("POO", 4, "Felipe González Roldán", 14, "lM"),
    Materia("POO", 5, "Rafael Antonio Acosta Rodríguez", 7, "mj"),
    Materia("POO", 6, "Paula Ximena Rodríguez Nempeque", 7, "lM"),
    Materia("POO", 7, "Jorge Enrique Amaya Cala", 7, "lM"),
    Materia("POO", 8, "Néstor Germán Bolívar Pulgarín", 16, "mj"),
    Materia("POO", 9, "David Alberto Herrera Álvarez", 11, "lM")
]

sistemas_numericos = [
    Materia("Sistemas Numéricos", 1, "German Preciado López", 9, "mj"),
    Materia("Sistemas Numéricos", 2, "Ricardo Ariel Pastrán Ramírez", 9, "mj"),
    Materia("Sistemas Numéricos", 3, "John Jaime Rodríguez Vega", 9, "mj")
]

probabilidad = [
    Materia("Probabilidad", 1, "Carlos Eduardo Alonso Malaver", 11, "Mv")
]

introduccion_al_analisis_real = [
    Materia("Introducción al Análisis Real", 1, "Mauricio Bogoya López", 11, "Mv")
]

introduccion_a_cc = [
    Materia("Introducción a CC", 1, "Arles Ernesto Rodríguez Portela", 11, "mj"),
    Materia("Introducción a CC", 2, "Juan Carlos Galvis Arrieta", 9, "mj")
]

introduccion_a_teoria_de_conjuntos = [
    Materia("Introducción a Teoría de Conjuntos", 1, "Pedro Hernán Zambrano Ramírez", 9, "mj"),
    Materia("Introducción a Teoría de Conjuntos", 2, "Yeison Alexander Sánchez Rubio", 14, "mj")
]

fundamentos_de_matematicas = [
    Materia("Fundamentos de Matemáticas", 1, "Mauro Artigiani", 7, "mj"),
    Materia("Fundamentos de Matemáticas", 2, "Sergio Alejandro Carrillo Torres", 7, "mj"),
    Materia("Fundamentos de Matemáticas", 3, "Oscar Guillermo Riaño Castañeda", 7, "mj"),
    Materia("Fundamentos de Matemáticas", 4, "Daniel Nuñez Alarcón", 7, "mj")
]

estructuras_de_datos = [
    Materia("Estructuras de Datos", 1, "Edwin Andres Niño Velasquez", 14, "mj"),
    Materia("Estructuras de Datos", 3, "Jhon Alexander Lopez Fajardo", 16, "mj"),
    Materia("Estructuras de Datos", 4, "Jhon Alexander Lopez Fajardo", 9, "mj"),
    Materia("Estructuras de Datos", 5, "David Alberto Herrera Alvarez", 7, "lM"),
    Materia("Estructuras de Datos", 2, "David Alberto Herrera Alvarez", 9, "lM")
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
seleccionadas = organizar_horario(materias)

# Mostrar la selección final
print("Materias seleccionadas sin colisiones de horario:")
for materia in seleccionadas:
    print("_" * 40)
    print(materia)
