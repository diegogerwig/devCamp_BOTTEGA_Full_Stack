# GIT COMMANDS CHEATSHEET COMPLETO

## Fundamentos de Git

### Git Pull
```bash
# Obtener y fusionar cambios del repositorio remoto
git pull <remote> <branch>

# Ejemplo: Obtener cambios de origin en la rama main
git pull origin main
```

### Git Branches (Ramas)

```bash
# Listar todas las ramas
git branch

# Crear una nueva rama
git branch <nombre-rama>

# Cambiar a una rama
git checkout <nombre-rama>

# Crear y cambiar a una nueva rama (atajo)
git checkout -b <nombre-rama>

# Ver ramas fusionadas y no fusionadas
git branch --merged
git branch --no-merged
```

### Workflow Básico de Branching

1. Crear una rama para una nueva función:
   ```bash
   git checkout -b feature/nueva-funcion
   ```

2. Hacer cambios y commits:
   ```bash
   git add .
   git commit -m "Implementar nueva función"
   ```

3. Pushear la rama al remoto:
   ```bash
   git push -u origin feature/nueva-funcion
   ```

4. Fusionar con la rama principal:
   ```bash
   git checkout main
   git merge feature/nueva-funcion
   ```

### Push y Merge de Ramas Remotas

```bash
# Enviar rama al repositorio remoto
git push <remote> <nombre-rama>

# Configurar tracking para la rama remota
git push -u origin <nombre-rama>

# Fusionar rama desde el remoto
git checkout main
git pull origin main
git merge <nombre-rama>
git push origin main
```

## Git Rebase

### Descripción
El comando `git rebase` es una herramienta poderosa que permite reorganizar el historial de commits, modificando la base desde donde se ramificó tu rama. A diferencia de `merge`, que crea un nuevo commit que une dos ramas, `rebase` reescribe el historial de commits para crear una línea de desarrollo más limpia y lineal.

### Casos de uso
- **Mantener una historia de proyecto más limpia**: Elimina commits de merge innecesarios
- **Actualizar una rama de feature con los últimos cambios de la rama principal**
- **Limpiar commits antes de fusionar con la rama principal**
- **Combinar, editar o reordenar commits**

### Comandos de Rebase

```bash
# Rebase básico: actualizar tu rama con los últimos cambios de main
git checkout feature/funcion
git rebase main
```

Este comando toma todos los commits de tu rama `feature/funcion` que no están en `main`, los "guarda" temporalmente, actualiza tu rama con los últimos commits de `main`, y luego aplica tus cambios encima.

```bash
# Rebase interactivo
git rebase -i HEAD~3  # Manipular los últimos 3 commits
```

El rebase interactivo abre un editor donde puedes:
- `pick`: mantener el commit como está
- `reword`: cambiar el mensaje del commit
- `edit`: detener para modificar el commit
- `squash`: combinar con el commit anterior (mantiene ambos mensajes)
- `fixup`: combinar con el commit anterior (descarta su mensaje)
- `drop`: eliminar el commit

```bash
# Después de resolver conflictos durante un rebase
git add <archivos-resueltos>
git rebase --continue

# Si quieres cancelar el rebase
git rebase --abort
```

### Advertencias
- **Nunca rebase commits que ya has publicado/compartido** (commits que ya están en el repositorio remoto y otros desarrolladores pueden haber basado su trabajo en ellos)
- Puede generar conflictos que deberás resolver manualmente
- Reescribe el historial, lo que puede complicar la colaboración

## Git Stash

### Descripción
El comando `git stash` te permite guardar temporalmente cambios que has hecho en tu copia de trabajo para que puedas trabajar en otra cosa, y luego volver a aplicar esos cambios más tarde. Es como un "portapapeles" para cambios en progreso que aún no estás listo para hacer commit.

### Casos de uso
- **Cambiar rápidamente de contexto**: Necesitas trabajar en otra rama pero no quieres hacer commit de tu trabajo actual incompleto
- **Limpiar tu espacio de trabajo**: Guardar cambios para aplicarlos después de actualizar tu rama con cambios remotos
- **Experimentar**: Guardar tu estado actual antes de probar una idea arriesgada
- **Recuperar cambios descartados**: Stash guarda incluso archivos no rastreados si se le indica

### Comandos de Stash

```bash
# Guardar todos los cambios rastreados (staged y unstaged)
git stash

# Guardar con un mensaje descriptivo
git stash save "mensaje descriptivo"

# Guardar incluyendo archivos no rastreados (-u)
git stash -u

# Guardar incluyendo archivos ignorados también (-a)
git stash -a
```

```bash
# Ver la lista de stashes guardados
git stash list
# Ejemplo de salida:
# stash@{0}: WIP on feature/x: abc1234 Último commit en feature/x
# stash@{1}: On main: Cambios antes de cambiar a feature/x
```

```bash
# Ver el contenido de un stash específico
git stash show stash@{0}
git stash show -p stash@{0}  # -p muestra los cambios en formato de diff
```

```bash
# Aplicar stash (manteniéndolo en la lista)
git stash apply  # Aplica el stash más reciente
git stash apply stash@{2}  # Aplica un stash específico

# Aplicar y eliminar stash (pop)
git stash pop
git stash pop stash@{2}
```

```bash
# Crear una rama desde un stash
git stash branch nueva-rama stash@{1}
```

```bash
# Limpiar stashes
git stash drop stash@{0}  # Elimina un stash específico
git stash clear  # Elimina todos los stashes
```

### Buenas prácticas
- Usa mensajes descriptivos con `git stash save "mensaje"` para recordar qué contiene cada stash
- No mantengas stashes por mucho tiempo, son soluciones temporales
- Considera usar ramas para cambios más importantes o de larga duración en lugar de stash
- Usa `git stash list` regularmente para revisar tus stashes guardados
- Limpia stashes antiguos que ya no necesites

## Git Fetch vs Git Pull

```bash
# Fetch: obtiene cambios sin fusionar
git fetch <remote>
git fetch origin

# Pull: equivale a fetch + merge
git pull <remote> <branch>
```

| Git Fetch | Git Pull |
|-----------|----------|
| Solo descarga cambios | Descarga y fusiona cambios |
| No modifica tu trabajo actual | Puede modificar tu trabajo actual |
| Seguro para usar en cualquier momento | Puede causar conflictos |
| Requiere merge manual posterior | Realiza el merge automáticamente |

## Eliminar Ramas

```bash
# Eliminar rama local
git branch -d <nombre-rama>  # Solo si está fusionada
git branch -D <nombre-rama>  # Forzar eliminación

# Eliminar rama remota
git push <remote> --delete <nombre-rama>
git push origin --delete feature/funcion
```

## Resolución de Conflictos en Merge

1. Git marca los conflictos en los archivos:
   ```
   <<<<<<< HEAD
   Código en tu rama actual
   =======
   Código en la rama que estás fusionando
   >>>>>>> nombre-rama
   ```

2. Editar manualmente para resolver
3. Marcar como resuelto y continuar:
   ```bash
   git add <archivo-con-conflictos>
   git commit  # o git rebase --continue si estás en rebase
   ```

## Revertir a Commits Anteriores

```bash
# Revertir al último commit (descartar cambios sin commit)
git reset --hard HEAD

# Revertir un solo archivo a una versión anterior
git checkout <commit-hash> -- <ruta-archivo>

# Ver historial de commits
git log
git log --oneline --graph --decorate

# Ver un commit específico
git show <commit-hash>

# Revertir todo el proyecto a una versión anterior
git reset --hard <commit-hash>  # CUIDADO: destruye el historial
git revert <commit-hash>        # Mejor opción: crea nuevo commit
```

## Comandos Git Adicionales Útiles

### Git Status y Diff

```bash
# Ver estado actual del repositorio
git status

# Ver cambios detallados entre working directory y staging
git diff

# Ver cambios ya añadidos al staging
git diff --staged

# Ver cambios entre commits
git diff <commit-hash1>..<commit-hash2>

# Ver cambios entre ramas
git diff <rama1>..<rama2>
```

### Git Commit

```bash
# Hacer commit con mensaje
git commit -m "Mensaje descriptivo"

# Añadir archivos y hacer commit en un solo paso
git commit -am "Mensaje descriptivo"

# Modificar el último commit (antes de push)
git commit --amend

# Modificar el último commit con nuevo mensaje
git commit --amend -m "Nuevo mensaje de commit"
```

### Git Remote

```bash
# Ver repositorios remotos
git remote -v

# Añadir un repositorio remoto
git remote add <nombre> <url>

# Eliminar un remoto
git remote remove <nombre>

# Cambiar URL de un remoto
git remote set-url <nombre> <nueva-url>
```

### Git Tag

```bash
# Crear un tag ligero
git tag <nombre-tag>

# Crear un tag anotado
git tag -a <nombre-tag> -m "Mensaje del tag"

# Listar tags
git tag

# Publicar tags al remoto
git push origin --tags

# Eliminar tag local
git tag -d <nombre-tag>

# Eliminar tag remoto
git push origin --delete <nombre-tag>
```

### Git Alias

```bash
# Crear alias para comandos frecuentes
git config --global alias.co checkout
git config --global alias.br branch
git config --global alias.ci commit
git config --global alias.st status

# Ejemplo de alias más complejo
git config --global alias.lgg "log --graph --pretty=format:'%Cred%h%Creset -%C(yellow)%d%Creset %s %Cgreen(%cr) %C(bold blue)<%an>%Creset' --abbrev-commit"
```

### Git Cherry-Pick

```bash
# Aplicar un commit específico a tu rama actual
git cherry-pick <commit-hash>

# Cherry-pick sin crear un commit
git cherry-pick -n <commit-hash>

# Cherry-pick con resolución de conflictos
git cherry-pick <commit-hash>
# Resolver conflictos, luego:
git add <archivos-resueltos>
git cherry-pick --continue
```

### Git Worktree

```bash
# Crear un nuevo worktree (área de trabajo adicional)
git worktree add ../<nueva-carpeta> <rama>

# Listar worktrees
git worktree list

# Limpiar worktrees desaparecidos
git worktree prune
```

### Git Config

```bash
# Configuración básica
git config --global user.name "Tu Nombre"
git config --global user.email "tu.email@ejemplo.com"

# Ver todas las configuraciones
git config --list

# Usar editor específico
git config --global core.editor "code --wait"

# Configurar herramienta de diff
git config --global diff.tool vscode
```

### Git Bisect

```bash
# Comenzar la búsqueda binaria
git bisect start

# Marcar commit actual como malo
git bisect bad

# Marcar un commit anterior como bueno
git bisect good <commit-hash>

# Marcar el commit actual como bueno/malo después de probar
git bisect good
git bisect bad

# Terminar bisect y volver a HEAD
git bisect reset
```

### Git Clean

```bash
# Ver qué archivos se eliminarían (simulación)
git clean -n

# Eliminar archivos no rastreados
git clean -f

# Eliminar archivos no rastreados e ignorados
git clean -fdx

# Eliminar directorios no rastreados
git clean -fd
```

### Git Reflog

```bash
# Ver historial de referencias (útil para recuperar commits perdidos)
git reflog

# Volver a un estado anterior usando reflog
git reset --hard HEAD@{2}
```
