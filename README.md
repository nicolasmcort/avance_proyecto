# avance_proyecto

Algoritmo principal de ordenamiento del sistema
``` mermaid
graph TD
    A[Inicio] --> B[Ordenar materias por preferencia]
    B --> C[Inicializar horario vacío]
    C --> D[Iterar sobre las materias ordenadas]
    D --> E{¿Grupo disponible sin colisión?}
    E -- Sí --> F[Añadir grupo al horario]
    E -- No --> G[Omitir materia temporalmente]
    F --> H[¿Se recorrieron todas las materias?]
    G --> H
    H -- No --> D
    H -- Sí --> I[Convertir horario a estructura única]
    I --> J{¿Horario es único?}
    J -- Sí --> K[Añadir horario a la lista de válidos]
    J -- No --> L[Descartar horario]
    K --> M{¿Se alcanzó el límite de horarios?}
    L --> M
    M -- No --> N[Generar nueva combinación aleatoria]
    N --> C
    M -- Sí --> O[Finalizar y devolver horarios]

```
