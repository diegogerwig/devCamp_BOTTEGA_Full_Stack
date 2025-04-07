# UML (UNIFIED MODELING LANGUAGE)

## 1. FUNDAMENTOS DEL UML

### ¿Qué es UML?
- Lenguaje visual estándar para modelar y documentar sistemas de software
- Desarrollado por Grady Booch, Ivar Jacobson y James Rumbaugh
- Administrado por el Object Management Group (OMG)
- Versión actual: UML 2.5

### Etapas del desarrollo donde se utiliza UML
- Análisis de requisitos
- Diseño de arquitectura
- Implementación
- Pruebas
- Documentación
- Mantenimiento

### Componentes comunes y elementos de UML
- **Frames**: Contenedores que delimitan un diagrama o una parte de él
- **Clasificadores**: Descripciones de conjuntos de objetos con características y comportamientos similares
- **Comentarios y notas**: Proporcionan información adicional o aclaraciones
- **Dependencias**: Relaciones donde un cambio en un elemento puede afectar a otro
- **Características y propiedades**: Atributos y operaciones de los elementos modelados

## 2. TIPOS DE DIAGRAMAS UML

### Diagramas estructurales

Modelan la estructura estática del sistema:

1. **Diagrama de Clases**: Muestra la estructura estática del sistema, con clases, atributos, métodos y relaciones entre clases.

2. **Diagrama de Objetos**: Representa instancias específicas de clases y sus relaciones en un momento determinado.

3. **Diagrama de Componentes**: Ilustra cómo los componentes de software se organizan y dependen entre sí.

4. **Diagrama de Despliegue**: Muestra la arquitectura física del hardware y software en el sistema.

5. **Diagrama de Paquetes**: Organiza elementos del modelo en grupos lógicos mostrando dependencias entre ellos.

6. **Diagrama de Estructura Compuesta**: Describe la estructura interna de una clase y las colaboraciones que esta estructura hace posibles.

7. **Diagrama de Perfiles**: Extensión del mecanismo estándar de UML para adaptar el lenguaje a dominios específicos.

### Diagramas de comportamiento

Modelan aspectos dinámicos del sistema:

1. **Diagrama de Casos de Uso**: Muestra la funcionalidad proporcionada por un sistema desde la perspectiva del usuario.

2. **Diagrama de Actividades**: Representa flujos de trabajo, procesos y algoritmos como una serie de acciones.

3. **Diagrama de Máquina de Estados**: Muestra los estados de un objeto y las transiciones entre estos estados.

4. **Diagrama de Secuencia**: Muestra interacciones entre objetos en una secuencia temporal específica.

5. **Diagrama de Comunicación**: Similar al de secuencia, pero enfatiza las relaciones entre objetos en lugar del tiempo.

6. **Diagrama de Tiempos**: Muestra el comportamiento de objetos en un periodo de tiempo específico.

7. **Diagrama de Interacción Global**: Combina elementos de diagramas de actividad y secuencia para mostrar múltiples interacciones.

## 3. DIAGRAMA DE CLASES

### Elementos principales
- **Clase**: Representación de un conjunto de objetos con atributos y métodos similares
- **Interfaz**: Colección de operaciones que especifican un servicio
- **Tipos de datos**: Valores que no tienen identidad
- **Enumeraciones**: Conjunto de literales nombrados

### Asociaciones, multiplicidad y navegabilidad
- **Asociación**: Relación entre clases
  - Unidireccional: Navegable en una dirección
  - Bidireccional: Navegable en ambas direcciones
- **Multiplicidad**: Especifica cuántas instancias de una clase se relacionan con otra
  - 1: Exactamente una instancia
  - 0..1: Cero o una instancia
  - *: Cero o más instancias (0..*)
  - 1..*: Una o más instancias
- **Tipos de relaciones**:
  - Generalización (herencia)
  - Realización (implementación)
  - Dependencia
  - Agregación (relación "tiene un")
  - Composición (relación "parte de" más fuerte)

### Ejemplo práctico: Modelado de Twitter
- Clases principales: Usuario, Tweet, Mensaje, Seguidor, Hashtag
- Relaciones entre entidades
- Atributos y métodos clave

## 4. DIAGRAMA DE ACTIVIDAD

### Elementos principales
- **Actividad**: Comportamiento parametrizado
- **Acciones**: Pasos fundamentales en una actividad
- **Flujos de control**: Conectan acciones mostrando el orden de ejecución
- **Nodos de decisión**: Representan puntos de ramificación condicional
- **Nodos de bifurcación/unión**: Representan paralelismo
- **Nodos iniciales y finales**: Indican dónde comienza y termina el flujo

### Ejemplo práctico: Sistema de calificación en línea
- Flujo de trabajo para calificar tareas
- Bifurcaciones para aprobación/rechazo
- Notificaciones y actualizaciones de estado

## 5. DIAGRAMA DE CASOS DE USO

### Elementos principales
- **Actor**: Entidad externa que interactúa con el sistema
- **Caso de uso**: Funcionalidad proporcionada por el sistema
- **Relaciones**:
  - Include: Un caso de uso incluye la funcionalidad de otro
  - Extend: Un caso de uso extiende otro en situaciones específicas
  - Generalización: Relación entre casos de uso generales y específicos

### Ejemplo práctico: Sistema de automatización de marketing
- Actores: Administrador, Usuario de marketing, Cliente
- Casos de uso: Crear campaña, Segmentar audiencia, Enviar correos

## 6. DIAGRAMA DE DESPLIEGUE

### Elementos principales
- **Nodo**: Recurso computacional físico o virtual
- **Artefacto**: Elemento físico de información
- **Dispositivo**: Hardware específico
- **Entorno de ejecución**: Software que proporciona servicios
- **Comunicación**: Enlaces entre nodos

### Ejemplo práctico: Motor de solicitud de canciones
- Servidores y bases de datos
- Interfaces de usuario
- Conexiones de red

## 7. DIAGRAMA DE PAQUETES

### Elementos principales
- **Paquete**: Mecanismo de agrupación de elementos relacionados
- **Dependencia**: Relación entre paquetes
- **Importación**: Un paquete requiere elementos de otro
- **Fusión**: Combinación de contenido de paquetes

### Ejemplo práctico: Sistema de automatización de marketing
- Paquetes: Interfaz de usuario, Lógica de negocio, Persistencia
- Dependencias entre componentes

## 8. DIAGRAMA DE SECUENCIA

### Elementos principales
- **Línea de vida**: Representa un participante en la interacción
- **Mensaje**: Comunicación entre participantes
- **Fragmentos combinados**: Grupos de mensajes con condiciones específicas
- **Marcas de tiempo**: Indican eventos temporales

### Ejemplo práctico: Motor de comisiones CRM
- Interacción entre objetos para calcular comisiones
- Flujo de mensajes y respuestas
- Condiciones y bucles

## 9. DIAGRAMA DE MÁQUINA DE ESTADOS

### Elementos principales
- **Estado**: Condición durante la vida de un objeto
- **Transición**: Cambio de un estado a otro
- **Evento**: Ocurrencia significativa que desencadena transiciones
- **Acción**: Comportamiento ejecutado durante una transición
- **Actividad**: Comportamiento ejecutado mientras se está en un estado

### Ejemplo práctico: Máquina de estados CRM
- Estados de un cliente: Prospecto, Activo, Inactivo
- Transiciones basadas en interacciones
- Eventos que desencadenan cambios de estado

## 10. PROYECTOS DE APLICACIÓN

### Diseño de Twitter
- Diagrama de casos de uso
- Diagrama de clases

### Diseño de aplicación de comercio electrónico
- Diagrama de actividad
- Diagrama de clases

### Modelado de biblioteca de código para análisis de números telefónicos
- Diagrama de paquetes
- Diagrama de secuencia

### Diseño de sistema de gestión de flotas empresariales
- Diagrama de actividad
- Diagrama de paquetes
- Diagrama de despliegue
- Diagrama de clases

### Diseño del sistema de viajes compartidos Uber
- Diagrama de actividad
- Diagrama de paquetes
- Diagrama de casos de uso
- Diagrama de despliegue

### Modelado de sistema de evaluación educativa
- Diagrama de actividad
- Diagrama de clases
- Diagrama de máquina de estados
- Diagrama de despliegue

### Diseño de sistema de automatización de marketing
- Diagrama de casos de uso
- Diagrama de actividad
- Diagrama de paquetes
- Diagrama de despliegue
- Diagrama de máquina de estados
- Diagrama de clases
