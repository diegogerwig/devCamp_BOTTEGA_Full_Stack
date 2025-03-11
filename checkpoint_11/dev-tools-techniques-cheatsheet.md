# HERRAMIENTAS DE DESARROLLO Y TÉCNICAS DE ESTUDIO

## Técnicas de Estudio para Desarrolladores

### Reverse Note Taking (Toma de Notas Inversa)

**Proceso:**
1. **Leer/estudiar el material** sin tomar notas inicialmente
2. **Cerrar el material** y escribir lo que recuerdas
3. **Verificar tus notas** contra el material original
4. **Corregir y completar** las notas basadas en lo que olvidaste

**Beneficios:**
- Mejora la retención activa vs. copia pasiva
- Identifica rápidamente lagunas en la comprensión
- Fortalece las conexiones cerebrales para la memoria a largo plazo
- Más efectivo que subrayar o tomar notas mientras lees

### Speed Reading (Lectura Rápida) para Desarrolladores

**Técnicas:**
1. **Evitar la subvocalización** (no "pronunciar" palabras en tu mente)
2. **Usar un marcador/dedo** como guía visual
3. **Leer en bloques** (grupos de palabras) en lugar de palabra por palabra
4. **Escanear primero** títulos, subtítulos, imágenes y conclusiones
5. **Ajustar velocidad** según el contenido (código vs. explicación)

**Para lectura de código:**
- Enfocarse primero en la estructura general
- Identificar patrones y componentes clave
- Profundizar solo en las secciones relevantes
- Usar herramientas de desglose de código (outline) cuando sea posible

## VS Code y Extensiones de Desarrollo

### Instalación de devCamp VS Code Extension

1. Abrir VS Code
2. Ir a la pestaña de Extensiones (Ctrl+Shift+X)
3. Buscar "devCamp"
4. Hacer clic en "Install"
5. Reiniciar VS Code si es necesario
6. Verificar la instalación en la barra de estado

### Creación de Snippets Personalizados en VS Code

1. **Acceder al menú de snippets**:
   - File > Preferences > User Snippets (Windows/Linux)
   - Code > Preferences > User Snippets (macOS)
   - O usar el comando: `Ctrl+Shift+P` > "Snippets"

2. **Seleccionar el lenguaje** para el snippet o crear uno global

3. **Formato básico de snippet**:
```json
"Nombre del Snippet": {
  "prefix": "shortcut",
  "body": [
    "línea 1",
    "línea 2 con ${1:placeholder}",
    "línea 3 con ${2:otro_placeholder}"
  ],
  "description": "Descripción del snippet"
}
```

4. **Variables disponibles**:
   - `$1`, `$2` - Posiciones del cursor (tabulación secuencial)
   - `${1:texto}` - Placeholder con valor predeterminado
   - `$0` - Posición final del cursor
   - `$TM_FILENAME` - Nombre del archivo actual
   - `$CURRENT_YEAR` - Año actual

**Ejemplo práctico (componente React):**
```json
"React Functional Component": {
  "prefix": "rfc",
  "body": [
    "import React from 'react';",
    "",
    "const ${1:ComponentName} = () => {",
    "  return (",
    "    <div>",
    "      $0",
    "    </div>",
    "  );",
    "};",
    "",
    "export default ${1:ComponentName};"
  ],
  "description": "React Functional Component"
}
```

## Console y JavaScript en el Navegador

### Ejecución de JavaScript en la Console del Navegador

1. **Abrir la consola del navegador**:
   - Chrome/Edge: `F12` o `Ctrl+Shift+J` (Windows/Linux) / `Cmd+Option+J` (Mac)
   - Firefox: `F12` o `Ctrl+Shift+K`

2. **Ejecutar código JavaScript**:
   - Escribir directamente en la consola y presionar Enter
   - Código multilínea: Shift+Enter para nuevas líneas

3. **Reutilizar código**:
   - Usar flechas arriba/abajo para navegar por el historial
   - Clic derecho > "Save as..." para guardar snippets

### Chrome Command Line API vs JavaScript Vanilla

| Chrome Command Line API | JavaScript Vanilla | Descripción |
|------------------------|-------------------|-------------|
| `$('selector')` | `document.querySelector('selector')` | Seleccionar un elemento |
| `$$('selector')` | `document.querySelectorAll('selector')` | Seleccionar múltiples elementos |
| `$0` - `$4` | N/A | Referencias a los últimos elementos inspeccionados |
| `copy(objeto)` | N/A | Copiar al portapapeles |
| `inspect(objeto)` | `console.dir(objeto)` | Inspeccionar objeto en el panel DOM |
| `monitorEvents(elemento)` | N/A | Monitorear eventos en un elemento |
| `debug(funcion)` | `debugger` | Establecer punto de interrupción |

### Procesar JavaScript desde un Archivo en el Navegador

**Método 1: Script en HTML**:
```html
<script src="miarchivo.js"></script>
```

**Método 2: Importar en Console**:
```javascript
// En la consola
let script = document.createElement('script');
script.src = 'ruta/a/miarchivo.js';
document.head.appendChild(script);
```

**Método 3: Fetch y eval** (no recomendado para producción):
```javascript
fetch('ruta/a/miarchivo.js')
  .then(response => response.text())
  .then(code => eval(code));
```

## Actividad de Construcción del Editor de Código

### Visualización del Dashboard de Actividad

**Componentes principales**:
1. **Contador de líneas**: Rastrear líneas de código escritas
2. **Temporización**: Medir tiempo de codificación activo
3. **Heatmap**: Visualizar períodos de mayor actividad
4. **Gráficos de progreso**: Comparar actividad diaria/semanal

**Implementación básica**:
```javascript
// Configuración básica del tracker
const codeTracker = {
  startTime: null,
  endTime: null,
  lineCount: 0,
  activeTime: 0,
  idleThreshold: 5 * 60 * 1000, // 5 minutos
  
  startSession() {
    this.startTime = new Date();
    this.trackActivity();
  },
  
  endSession() {
    this.endTime = new Date();
    this.calculateActiveTime();
    this.saveStats();
  },
  
  trackActivity() {
    // Implementación de seguimiento
  },
  
  updateLineCount(editor) {
    this.lineCount = editor.getLineCount();
  }
};
```
