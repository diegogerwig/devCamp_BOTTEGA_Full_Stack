# Cheatsheet de Git y GitHub

## 1. Crear un Repositorio Git Local

### Inicializar un repositorio
```bash
git init
```
Este comando crea un nuevo repositorio Git local en el directorio actual, inicializando un subdirectorio `.git` que contiene todos los metadatos necesarios.

### Configuración inicial
```bash
# Configurar nombre de usuario
git config --global user.name "Tu Nombre"

# Configurar email
git config --global user.email "tu.email@ejemplo.com"
```

### Primeros pasos con un repositorio nuevo
```bash
# Añadir archivos al área de preparación (staging area)
git add <nombre-archivo>
git add .  # Añadir todos los archivos

# Hacer el primer commit
git commit -m "Commit inicial"
```

## 2. Subir un Repositorio Local a GitHub

### Crear un repositorio en GitHub
1. Inicia sesión en GitHub
2. Haz clic en el botón "+" en la esquina superior derecha
3. Selecciona "New repository"
4. Proporciona un nombre y una descripción opcional
5. Deja las opciones de inicialización sin marcar (sin README, .gitignore, etc.)
6. Clic en "Create repository"

### Conectar tu repositorio local con GitHub
```bash
# Añadir el repositorio remoto
git remote add origin https://github.com/usuario/nombre-repositorio.git

# Verificar que se añadió correctamente
git remote -v
```

### Subir tu código a GitHub
```bash
# Primera vez que subes (con -u para establecer el upstream)
git push -u origin main  # O 'master' si es la rama predeterminada

# Subidas posteriores
git push
```

## 3. Flujo de Trabajo Git

### Ciclo básico de trabajo
```bash
# 1. Verificar estado del repositorio
git status

# 2. Actualizar tu repositorio local (si trabajas con otros)
git pull

# 3. Modificar archivos en tu directorio de trabajo

# 4. Ver cambios realizados
git diff

# 5. Añadir cambios al área de preparación
git add <archivo>
git add .  # Todos los archivos

# 6. Verificar qué se va a confirmar
git status

# 7. Confirmar cambios
git commit -m "Descripción del cambio"

# 8. Subir cambios al repositorio remoto
git push
```

### Trabajar con ramas
```bash
# Crear nueva rama
git branch <nombre-rama>

# Cambiar a una rama
git checkout <nombre-rama>

# Crear y cambiar a una nueva rama en un solo paso
git checkout -b <nombre-rama>

# Fusionar una rama con la rama actual
git merge <nombre-rama>

# Eliminar una rama
git branch -d <nombre-rama>
```

## 4. Examinar el Directorio .git

El directorio `.git` contiene toda la información y archivos necesarios para el funcionamiento de Git:

### Estructura básica
- **config**: Archivo de configuración específico del repositorio
- **HEAD**: Referencia a la rama actual
- **index**: Archivo que representa el área de preparación
- **objects/**: Directorio que contiene todos los objetos del repositorio (commits, árboles, blobs)
- **refs/**: Contiene referencias a commits (ramas, tags)
- **hooks/**: Scripts que se ejecutan en ciertos eventos de Git

### Comandos para explorar .git
```bash
# Ver contenido del HEAD
cat .git/HEAD

# Listar referencias
ls -la .git/refs/

# Ver configuración del repositorio
cat .git/config

# Ver objetos
find .git/objects -type f | sort
```

## 5. Ignorar Archivos con .gitignore

### Crear un archivo .gitignore
```bash
touch .gitignore
```

### Patrones comunes para .gitignore
```
# Ignorar un archivo específico
archivo-secreto.txt

# Ignorar un directorio completo
node_modules/
logs/

# Ignorar por extensión
*.log
*.tmp
*.swp

# Ignorar todos excepto uno específico
*.json
!package.json

# Ignorar archivos en cualquier directorio con cierto nombre
**/logs/

# Comentarios
# Este es un comentario en .gitignore
```

### Ejemplos para diferentes tipos de proyectos
```
# Para proyectos Node.js
node_modules/
npm-debug.log
.env

# Para proyectos Python
__pycache__/
*.py[cod]
venv/
.env

# Para proyectos Java
*.class
*.jar
target/
.idea/

# Para macOS
.DS_Store

# Para Windows
Thumbs.db
```

### Comandos relacionados con .gitignore
```bash
# Eliminar archivos del seguimiento que ahora están en .gitignore
git rm --cached <archivo>

# Ver archivos ignorados
git status --ignored
```

## Comandos Adicionales Útiles

### Ver historial
```bash
# Ver historial de commits
git log

# Ver historial en formato compacto
git log --oneline

# Ver historial con gráfico de ramas
git log --graph --oneline --all
```

### Deshacer cambios
```bash
# Descartar cambios en un archivo
git checkout -- <archivo>

# Deshacer el último commit (manteniendo los cambios)
git reset --soft HEAD~1

# Deshacer el último commit (descartando los cambios)
git reset --hard HEAD~1
```

### Etiquetas (Tags)
```bash
# Crear una etiqueta
git tag v1.0.0

# Crear una etiqueta anotada
git tag -a v1.0.0 -m "Versión 1.0.0"

# Subir etiquetas a GitHub
git push origin --tags
```
