# React Cheatsheet: Guía Completa

## 🚀 Creación de Proyectos

### Create React App (CRA)
```bash
# Crear un nuevo proyecto
npx create-react-app mi-aplicacion

# Navegar al proyecto y ejecutar
cd mi-aplicacion
npm start
```

### Vite (Más rápido)
```bash
# Crear un proyecto con React template
npm create vite@latest mi-aplicacion --template react

# Navegar e instalar dependencias
cd mi-aplicacion
npm install

# Iniciar servidor de desarrollo
npm run dev
```

### Next.js (React con SSR)
```bash
# Crear un proyecto Next.js
npx create-next-app mi-aplicacion

# Navegar e iniciar
cd mi-aplicacion
npm run dev
```

## 📦 Gestión de Dependencias

### Instalar paquetes
```bash
# Dependencias de producción
npm install nombre-paquete
# o
npm i nombre-paquete

# Dependencias de desarrollo
npm install --save-dev nombre-paquete
# o
npm i -D nombre-paquete
```

### Desinstalar paquetes
```bash
npm uninstall nombre-paquete
```

### Actualizar paquetes
```bash
# Ver paquetes desactualizados
npm outdated

# Actualizar todo
npm update

# Actualizar un paquete específico
npm update nombre-paquete
```

### Listar paquetes instalados
```bash
npm list --depth=0
```

## 🔧 Configuración de Proyectos

### Archivos de configuración importantes
- `package.json` - Dependencias y scripts
- `.gitignore` - Archivos a ignorar en Git
- `.env` - Variables de entorno (crear si no existe)
- `vite.config.js` / `webpack.config.js` - Configuración del bundler

### Configurar .gitignore básico
```
# Dependencies
/node_modules
/.pnp
.pnp.js

# Testing
/coverage

# Production
/build
/dist

# Misc
.DS_Store
.env.local
.env.development.local
.env.test.local
.env.production.local

npm-debug.log*
yarn-debug.log*
yarn-error.log*
```

### Variables de entorno
```
# Archivo .env (debe comenzar con REACT_APP_ en CRA)
REACT_APP_API_URL=https://api.example.com
```

## 💻 Estructura de Proyecto Recomendada

```
mi-aplicacion/
├── node_modules/
├── public/               # Archivos estáticos públicos
├── src/                  # Código fuente
│   ├── assets/           # Imágenes, fuentes, etc.
│   ├── components/       # Componentes reutilizables
│   │   ├── common/       # Componentes genéricos (Button, Input, etc.)
│   │   └── layout/       # Componentes de estructura (Header, Footer, etc.)
│   ├── hooks/            # Custom hooks
│   ├── pages/            # Componentes a nivel de página/ruta
│   ├── services/         # Servicios (API, autenticación, etc.)
│   ├── store/            # Estado global (Redux, Context)
│   ├── styles/           # Estilos globales
│   ├── utils/            # Funciones utilitarias
│   ├── App.js            # Componente principal
│   └── index.js          # Punto de entrada
├── .env                  # Variables de entorno
├── .gitignore           
├── package.json
└── README.md
```

## 🏗️ Comandos Comunes

### Scripts NPM (definidos en package.json)
```bash
# Iniciar en desarrollo
npm start           # Create React App
npm run dev         # Vite, Next.js

# Compilar para producción
npm run build

# Ejecutar tests
npm test

# Linting
npm run lint

# Formatear código
npm run format      # Si está configurado con Prettier
```

## 🔄 Control de Versiones (Git)

```bash
# Inicializar repositorio
git init

# Primer commit
git add .
git commit -m "Inicialización del proyecto"

# Conectar a repositorio remoto
git remote add origin https://github.com/usuario/repositorio.git
git branch -M main
git push -u origin main
```

## 📱 Extensiones Útiles para VSCode

- ES7 React/Redux/GraphQL/React-Native snippets
- Prettier - Code formatter
- ESLint
- Auto Import
- Path Intellisense
- vscode-styled-components
- Color Highlight

## 🧩 Librerías Populares para React

### Gestión de Estado
- Redux + React-Redux
- Zustand
- Recoil
- Jotai
- Context API (integrado en React)

### Routing
- React Router
- TanStack Router

### Formularios
- React Hook Form
- Formik + Yup
- Final Form

### UI Frameworks
- Material UI
- Chakra UI
- Ant Design
- Tailwind CSS
- Styled Components
- Emotion

### Fetching de Datos
- React Query / TanStack Query
- SWR
- Apollo Client (GraphQL)
- RTK Query

## 📦 Deploy de Aplicaciones React

### Opciones Gratuitas/Económicas
- Vercel
- Netlify
- GitHub Pages
- Firebase Hosting
- Surge

### Pasos para deploy en Vercel
```bash
# Instalar CLI de Vercel
npm i -g vercel

# Login y deploy
vercel login
vercel
```

### Pasos para deploy en Netlify
```bash
# Build
npm run build

# Instalar CLI de Netlify
npm i -g netlify-cli

# Login y deploy
netlify login
netlify deploy
```

## 🧪 Testing

### Jest (incluido en CRA)
```bash
# Ejecutar tests
npm test

# Con cobertura
npm test -- --coverage
```

### React Testing Library
```jsx
import { render, screen, fireEvent } from '@testing-library/react';
import MiComponente from './MiComponente';

test('renderiza correctamente', () => {
  render(<MiComponente />);
  const elemento = screen.getByText('Texto esperado');
  expect(elemento).toBeInTheDocument();
  
  fireEvent.click(elemento);
  // Más assertions...
});
```

## 🐛 Debugging

### React Developer Tools
1. Instalar extensión para Chrome/Firefox
2. Usar las pestañas "Components" y "Profiler" en DevTools

### Console logging
```jsx
useEffect(() => {
  console.log('Estado actual:', estado);
}, [estado]);
```

## 🛠️ Optimización de Rendimiento

### Memoización
```jsx
// Evitar re-renders innecesarios
import React, { memo, useMemo, useCallback } from 'react';

// Componente memoizado
const MiComponente = memo(function MiComponente(props) {
  // ...
});

// Valores memoizados
const valorCalculado = useMemo(() => {
  return calcularValor(dependencia);
}, [dependencia]);

// Funciones memoizadas
const manejarClick = useCallback(() => {
  hacerAlgo(dependencia);
}, [dependencia]);
```

### Code Splitting
```jsx
import React, { lazy, Suspense } from 'react';

// Carga diferida de componentes
const ComponentePesado = lazy(() => import('./ComponentePesado'));

function App() {
  return (
    <Suspense fallback={<div>Cargando...</div>}>
      <ComponentePesado />
    </Suspense>
  );
}
```
