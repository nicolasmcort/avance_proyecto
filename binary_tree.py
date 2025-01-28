class Nodo:
    def __init__(self, materia, grupo, siguiente=None):
        self.materia = materia  # Nombre de la materia
        self.grupo = grupo      # Grupo de la materia
        self.hijos = []         # Nodos hijos
        self.siguiente = siguiente  # Nodo siguiente para recorrer combinaciones completas

# Función para construir el árbol de combinaciones priorizando grupos
def construir_arbol(materias):
    def agregar_nodos(materia_index, nodo_actual):
        if materia_index == len(materias):
            return
        materia, grupos = materias[materia_index]
        # Ordenar grupos por preferencia (mayor a menor)
        grupos_ordenados = sorted(grupos, key=lambda x: x[1], reverse=True)
        for grupo, _ in grupos_ordenados:
            nuevo_nodo = Nodo(materia, grupo)
            nodo_actual.hijos.append(nuevo_nodo)
            agregar_nodos(materia_index + 1, nuevo_nodo)

    raiz = Nodo("Inicio", None)
    agregar_nodos(0, raiz)
    return raiz

# Función para recorrer el árbol y generar combinaciones con límite
def generar_combinaciones(nodo, limite, combinacion_actual=None, resultados=None):
    if combinacion_actual is None:
        combinacion_actual = []
    if resultados is None:
        resultados = []

    # Detener si alcanzamos el límite
    if len(resultados) >= limite:
        return resultados

    # Si el nodo no tiene hijos, hemos completado una combinación
    if not nodo.hijos:
        resultados.append(combinacion_actual.copy())
        return resultados

    # Recorremos cada hijo del nodo actual
    for hijo in nodo.hijos:
        combinacion_actual.append((hijo.materia, hijo.grupo))
        generar_combinaciones(hijo, limite, combinacion_actual, resultados)
        combinacion_actual.pop()
        # Detener si alcanzamos el límite
        if len(resultados) >= limite:
            break

    return resultados

# Ejemplo de uso
materias = [
    ("Matemáticas", [("Grupo 1", 10), ("Grupo 2", 70)]),  # Grupo con preferencia 90 y 70
    ("Física", [("Grupo A", 80), ("Grupo B", 60)]),       # Grupo con preferencia 80 y 60
    ("Química", [("Grupo X", 85), ("Grupo Y", 50)])      # Grupo con preferencia 85 y 50
]

# Construimos el árbol priorizando los grupos
arbol = construir_arbol(materias)

# Establecemos el límite de combinaciones deseado
limite = 7

# Generamos las combinaciones con límite
combinaciones = generar_combinaciones(arbol, limite)

# Mostramos las combinaciones generadas
print("Combinaciones posibles priorizando las preferencias (limitadas a 5):")
for i, c in enumerate(combinaciones, 1):
    print(f"Horario {i}: {c}")

