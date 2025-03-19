# UML (Unified Modeling Language) Cheatsheet

## Visión General de UML

UML (Unified Modeling Language) es un lenguaje estándar para visualizar, especificar, construir y documentar sistemas de software. Proporciona una forma de comunicar ideas sobre diseño de software utilizando diagramas y notaciones estándar.

### Etapas de Desarrollo donde UML es Útil

1. **Fase de Análisis**:
   - Capturar requisitos
   - Modelar procesos de negocio
   - Definir casos de uso

2. **Fase de Diseño**:
   - Arquitectura del sistema
   - Relaciones entre componentes
   - Interfaces de componentes

3. **Fase de Implementación**:
   - Guía para programadores
   - Documentación del código
   - Mapeo entre diseño y código

4. **Fase de Pruebas**:
   - Validación de comportamiento
   - Verificación de flujos

5. **Fase de Mantenimiento**:
   - Documentación actualizada
   - Guía para cambios

## Elementos Comunes de UML

### Frames (Marcos)
- **Definición**: Contenedores que encapsulan elementos de un diagrama
- **Sintaxis**: Rectángulo con una etiqueta en la esquina superior izquierda
- **Uso**: Define el tipo de diagrama y el ámbito

### Classifiers (Clasificadores)
- **Definición**: Abstracciones que representan conceptos en un dominio
- **Tipos principales**:
  - Clases
  - Interfaces
  - Componentes
  - Nodos
  - Casos de uso
  - Actores

### Comments and Notes (Comentarios y Notas)
- **Definición**: Texto explicativo para clarificar elementos del diagrama
- **Sintaxis**: Rectángulo con esquina doblada y línea punteada al elemento
- **Uso**: Proporcionar información adicional

### Dependencies (Dependencias)
- **Definición**: Relaciones donde un cambio en un elemento afecta a otro
- **Sintaxis**: Flecha discontinua
- **Tipos**:
  - Uso (use)
  - Abstracción (abstraction)
  - Permiso (permission)
  - Sustitución (substitution)

### Features and Properties (Características y Propiedades)
- **Atributos**: Representan los datos asociados a un clasificador
- **Operaciones**: Representan los comportamientos de un clasificador
- **Visibilidad**:
  - `+` Público
  - `-` Privado
  - `#` Protegido
  - `~` Paquete

## Tipos de Diagramas UML

### Diagramas Estructurales
- Muestran la estructura estática del sistema
- Tipos principales:
  - **Diagrama de Clases**: Clases, atributos, operaciones y relaciones
  - **Diagrama de Objetos**: Instancias de clases y relaciones
  - **Diagrama de Componentes**: Componentes físicos del software
  - **Diagrama de Despliegue**: Hardware y distribución del software
  - **Diagrama de Paquetes**: Organización y dependencias entre paquetes
  - **Diagrama de Estructura Compuesta**: Estructura interna de clases

### Diagramas de Comportamiento
- Muestran el comportamiento dinámico del sistema
- Tipos principales:
  - **Diagrama de Actividad**: Flujo de trabajo o proceso
  - **Diagrama de Casos de Uso**: Funcionalidades y actores
  - **Diagrama de Estados**: Estados y transiciones
  - **Diagrama de Secuencia**: Intercambio de mensajes temporales
  - **Diagrama de Comunicación**: Intercambio de mensajes entre objetos
  - **Diagrama de Tiempo**: Cambios de estado a lo largo del tiempo

## Diagrama de Clases

### Elementos del Diagrama de Clases
- **Clase**: Rectángulo con tres compartimentos (nombre, atributos, operaciones)
  ```
  +---------------------+
  |      Nombre         |
  +---------------------+
  | - atributo1: tipo   |
  | + atributo2: tipo   |
  +---------------------+
  | + operación1(): tipo|
  | # operación2(): tipo|
  +---------------------+
  ```

- **Interfaces**: Similar a una clase con estereotipo «interface»
  ```
  <<interface>>
  +---------------------+
  |    NombreInterfaz   |
  +---------------------+
  | + método1(): tipo   |
  | + método2(): tipo   |
  +---------------------+
  ```

### Relaciones en Diagramas de Clases

- **Asociación**: Conexión estructural entre clases
  - Línea sólida entre clases
  - Puede incluir multiplicidad y nombre de la asociación
  ```
  Clase1 ───────── Clase2
         1     *
  ```

- **Agregación**: Relación "tiene un" (todo-parte débil)
  - Línea con diamante vacío en el extremo "todo"
  ```
  Todo ◇───── Parte
  ```

- **Composición**: Relación "contiene un" (todo-parte fuerte)
  - Línea con diamante relleno en el extremo "todo"
  ```
  Todo ◆───── Parte
  ```

- **Herencia/Generalización**: Relación "es un"
  - Línea sólida con triángulo vacío apuntando a la superclase
  ```
  SuperClase
     △
     │
  SubClase
  ```

- **Dependencia**: Una clase depende de otra
  - Línea discontinua con flecha
  ```
  Clase1 - - - -> Clase2
  ```

- **Realización**: Implementación de interfaz
  - Línea discontinua con triángulo vacío
  ```
  <<interface>>
  Interface
     △
     ┊
   Clase
  ```

### Multiplicidad en Asociaciones
- `1`: Exactamente uno
- `0..1`: Cero o uno
- `*`: Cero o más
- `1..*`: Uno o más
- `5..10`: Entre 5 y 10

### Navegabilidad
- Flecha en un extremo: Navegación unidireccional
- Sin flechas: Navegación bidireccional
- `X` en un extremo: No navegable

## Ejemplo: Diseñar Twitter con Diagrama de Clases

```
+---------------+       *     +-----------------+
|    Usuario    |<>------------|     Tweet      |
+---------------+       1      +-----------------+
| - id: int     |              | - id: int       |
| - username: str|              | - contenido: str|
| - email: str   |              | - fecha: Date   |
+---------------+              +-----------------+
| + seguir()    |              | + like()        |
| + tuitear()   |              | + retweet()     |
+---------------+              | + responder()   |
       △                       +-----------------+
       |                               △
       |                               |
+---------------+             +-----------------+
|   Seguidor    |             |     Retweet     |
+---------------+             +-----------------+
| - fechaInicio |             | - fecha: Date   |
+---------------+             +-----------------+
       |                               |
       |                               |
+---------------+             +-----------------+
|   Seguido     |             |    Respuesta    |
+---------------+             +-----------------+
                              | - contenido: str|
                              +-----------------+
```

## Diagrama de Actividad

### Elementos del Diagrama de Actividad

- **Nodo Inicial**: Círculo negro sólido
  ```
  ●
  ```

- **Nodo Final**: Círculo negro con un anillo alrededor
  ```
  ◉
  ```

- **Acción**: Rectángulo con esquinas redondeadas
  ```
  +-------------+
  | Hacer algo  |
  +-------------+
  ```

- **Decisión/Fusión**: Diamante
  ```
       ◇
      / \
     /   \
    /     \
  ```

- **Fork/Join**: Barra negra (para paralelismo)
  ```
  ───────
  ```

- **Swimlanes**: Divisiones para mostrar responsabilidades
  ```
  +-------------------+-------------------+
  | Actor1            | Actor2            |
  +-------------------+-------------------+
  |                   |                   |
  | +-------------+   |                   |
  | | Actividad 1 |   |                   |
  | +-------------+   |                   |
  |        |          |                   |
  |        ▼          |                   |
  |        ◇          |                   |
  |       / \         |                   |
  |      /   \        |                   |
  |     /     \       |                   |
  |    ▼       ▼      |                   |
  |    |       |      |                   |
  |    |       |      |                   |
  |    ▼       |      |                   |
  |            |      |                   |
  |            ▼      | +-------------+   |
  |                   | | Actividad 2 |   |
  |                   | +-------------+   |
  |                   |                   |
  +-------------------+-------------------+
  ```

### Ejemplo: Diseño de Sistema de Calificación en Línea

```
●
│
▼
+-------------------+
| Iniciar sesión    |
+-------------------+
       │
       ▼
       ◇
      / \
     /   \
Si  /     \ No
   /       \
  ▼         ▼
+--------+ +----------------+
| Acceso | | Mostrar error  |
| docente| | de login       |
+--------+ +----------------+
    │              │
    │              │
    ▼              │
+---------------+  │
| Ver cursos    |  │
+---------------+  │
    │              │
    ▼              │
+---------------+  │
| Seleccionar   |  │
| estudiante    |  │
+---------------+  │
    │              │
    ▼              │
+---------------+  │
| Ingresar      |  │
| calificación  |  │
+---------------+  │
    │              │
    ▼              │
    ◇<-------------+
   / \
  /   \
 /     \
▼       ▼
+----------------+ +----------------+
| Guardar        | | Cancelar       |
| calificación   | | calificación   |
+----------------+ +----------------+
       │                │
       │                │
       ▼                │
+----------------+      │
| Notificar al   |      │
| estudiante     |      │
+----------------+      │
       │                │
       ▼                ▼
       ◉
```
