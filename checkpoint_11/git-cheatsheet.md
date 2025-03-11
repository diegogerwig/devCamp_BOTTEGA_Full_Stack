# GIT COMMANDS CHEATSHEET

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

### Git Rebase

```bash
# Rebase de tu rama sobre main
git checkout feature/funcion
git rebase main

# Rebase interactivo (i = interactivo)
git rebase -i HEAD~3  # Rebase de los últimos 3 commits

# Continuar rebase después de resolver conflictos
git rebase --continue

# Abortar rebase
git rebase --abort
```

### Git Stash

```bash
# Guardar cambios actuales sin commit
git stash

# Guardar con un mensaje descriptivo
git stash save "mensaje descriptivo"

# Listar stashes guardados
git stash list

# Aplicar el último stash y mantenerlo en la lista
git stash apply

# Aplicar un stash específico
git stash apply stash@{n}

# Aplicar y eliminar el último stash
git stash pop

# Eliminar el último stash
git stash drop

# Eliminar todos los stashes
git stash clear
```

### Git Fetch vs Git Pull

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

### Eliminar Ramas

```bash
# Eliminar rama local
git branch -d <nombre-rama>  # Solo si está fusionada
git branch -D <nombre-rama>  # Forzar eliminación

# Eliminar rama remota
git push <remote> --delete <nombre-rama>
git push origin --delete feature/funcion
```

### Resolución de Conflictos en Merge

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

### Revertir a Commits Anteriores

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
