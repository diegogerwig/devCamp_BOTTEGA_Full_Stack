# CHEATSHEET DE REACT

## 🚀 CONFIGURACIÓN INICIAL




### Instalación y Configuración del Entorno

#### Instalación en Mac
```bash
# Instalar Homebrew (si no está instalado)
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"

# Instalar Node y NPM
brew install node

# Verificar instalación
node -v
npm -v
```

#### Instalación en PC
1. Descargar el instalador de Node.js desde [nodejs.org](https://nodejs.org/)
2. Ejecutar el instalador y seguir las instrucciones
3. Verificar la instalación con `node -v` y `npm -v` en la terminal

#### Editor de Texto Recomendado: VS Code
- Descargar desde [code.visualstudio.com](https://code.visualstudio.com/)
- Extensiones recomendadas:
  - ES7+ React/Redux/React-Native snippets
  - Prettier - Code formatter
  - ESLint
  - Auto Rename Tag
  - Path Intellisense

#### Solución de Problemas con VS Code Formatting
- Configurar Prettier como formateador predeterminado en settings.json
- Habilitar "Format On Save" en la configuración
- Asegurarse de que las reglas de ESLint y Prettier no estén en conflicto

### Configuración de Git

```bash
# Configuración global
git config --global user.name "Tu Nombre"
git config --global user.email "tu@email.com"

# Inicializar repositorio
git init

# Añadir archivos
git add .

# Hacer commit
git commit -m "Commit inicial"

# Conectar con repositorio remoto
git remote add origin https://github.com/usuario/repositorio.git

# Subir cambios
git push -u origin master
```

### Creación de un Proyecto React

```bash
# Crear nuevo proyecto con Create React App
npx create-react-app nombre-proyecto

# Navegar al directorio del proyecto
cd nombre-proyecto

# Iniciar servidor de desarrollo
npm start
```

## 📁 ESTRUCTURA DE ARCHIVOS

### Directorios Principales

#### Directorio `src/`
- **index.js**: Punto de entrada de la aplicación
- **App.js**: Componente raíz
- **components/**: Carpeta para componentes reutilizables
- **assets/**: Imágenes, fuentes y otros recursos estáticos
- **styles/**: Archivos CSS o SCSS

#### Directorio `public/`
- **index.html**: Plantilla HTML principal
- **favicon.ico**: Icono del sitio
- **manifest.json**: Para aplicaciones PWA

### Archivos de Configuración

#### package.json
```json
{
  "name": "proyecto-react",
  "version": "0.1.0",
  "dependencies": {
    "react": "^18.2.0",
    "react-dom": "^18.2.0"
  },
  "scripts": {
    "start": "react-scripts start",
    "build": "react-scripts build",
    "test": "react-scripts test",
    "eject": "react-scripts eject"
  }
}
```

#### package-lock.json
- Asegura versiones exactas de dependencias
- No modificar manualmente
- Se genera automáticamente

#### Otros Archivos Importantes
- **Procfile**: Para despliegue en plataformas como Heroku
- **README.md**: Documentación del proyecto
- **server.js**: Para configurar un servidor personalizado

### Webpack y Babel

#### Webpack
- Empaquetador de módulos
- Maneja la carga y transformación de archivos
- Permite importar CSS, imágenes y otros archivos
- Configuración en `webpack.config.js` (oculto en Create React App)

#### Babel
- Transpilador de JavaScript
- Convierte JSX a JavaScript
- Transforma características modernas a código compatible
- Configuración en `.babelrc` (oculto en Create React App)

### Gestión de Dependencias

```bash
# Instalar dependencia
npm install nombre-paquete

# Instalar dependencia de desarrollo
npm install --save-dev nombre-paquete

# Desinstalar dependencia
npm uninstall nombre-paquete

# Actualizar dependencias
npm update
```

## 💻 COMPONENTES REACT

### Tipos de Componentes

#### Componentes Funcionales
```jsx
import React from 'react';

function MiComponente(props) {
  return (
    <div>
      <h1>Hola, {props.nombre}</h1>
    </div>
  );
}

export default MiComponente;
```

#### Componentes de Clase
```jsx
import React, { Component } from 'react';

class MiComponente extends Component {
  constructor(props) {
    super(props);
    this.state = {
      contador: 0
    };
  }
  
  render() {
    return (
      <div>
        <h1>Hola, {this.props.nombre}</h1>
        <p>Contador: {this.state.contador}</p>
      </div>
    );
  }
}

export default MiComponente;
```

### Props y State

#### Props
- Datos pasados de componente padre a hijo
- Inmutables (no se pueden modificar dentro del componente)
- Se acceden con `props` en componentes funcionales o `this.props` en clases

```jsx
// Componente padre
<MiComponente nombre="Juan" edad={25} />

// Componente hijo (funcional)
function MiComponente(props) {
  return <p>Hola {props.nombre}, tienes {props.edad} años</p>;
}

// Componente hijo (clase)
class MiComponente extends Component {
  render() {
    return <p>Hola {this.props.nombre}, tienes {this.props.edad} años</p>;
  }
}
```

#### State
- Datos internos del componente que pueden cambiar
- Solo disponible en componentes de clase o con hooks en funcionales
- Se debe modificar usando `setState()` en clases o la función setter en hooks

```jsx
// En componente de clase
this.setState({ contador: this.state.contador + 1 });

// En componente funcional con hooks
const [contador, setContador] = useState(0);
setContador(contador + 1);
```

### Ciclo de Vida de Componentes

#### Métodos de Ciclo de Vida (Componentes de Clase)
```jsx
class Componente extends Component {
  // Montaje
  constructor(props) {
    super(props);
    // Inicialización de state
  }
  
  componentDidMount() {
    // Después del primer render
    // Ideal para peticiones API
  }
  
  // Actualización
  componentDidUpdate(prevProps, prevState) {
    // Después de actualizar (no en el render inicial)
  }
  
  // Desmontaje
  componentWillUnmount() {
    // Antes de eliminar el componente
    // Limpieza de recursos
  }
  
  render() {
    return <div>Contenido</div>;
  }
}
```

#### Hooks (Componentes Funcionales)
```jsx
import React, { useState, useEffect } from 'react';

function Componente() {
  const [datos, setDatos] = useState([]);
  
  // Similar a componentDidMount y componentDidUpdate
  useEffect(() => {
    // Código a ejecutar
    
    // Limpieza (similar a componentWillUnmount)
    return () => {
      // Código de limpieza
    };
  }, [/* dependencias */]);
  
  return <div>Contenido</div>;
}
```

### JSX

#### Sintaxis Básica
```jsx
const elemento = <h1>Hola mundo</h1>;

// Con múltiples elementos (deben estar envueltos)
const elemento = (
  <div>
    <h1>Título</h1>
    <p>Párrafo</p>
  </div>
);

// Fragmentos (evita divs innecesarios)
const elemento = (
  <>
    <h1>Título</h1>
    <p>Párrafo</p>
  </>
);
```

#### Expresiones en JSX
```jsx
const nombre = 'Usuario';
const elemento = <h1>Hola, {nombre}</h1>;

// Con operaciones
const elemento = <h1>Resultado: {2 + 2}</h1>;

// Con funciones
const formatoNombre = (usuario) => usuario.nombre + ' ' + usuario.apellido;
const elemento = <h1>Hola, {formatoNombre(usuario)}</h1>;
```

#### Atributos en JSX
```jsx
// Atributos estáticos
const elemento = <div className="contenedor">Contenido</div>;

// Atributos dinámicos
const className = 'contenedor';
const elemento = <div className={className}>Contenido</div>;

// Estilos inline
const estilo = { color: 'red', fontSize: '20px' };
const elemento = <div style={estilo}>Contenido</div>;
```

## 🔄 MANEJO DE DATOS

### Renderizado Condicional

#### Operador Ternario
```jsx
function Componente({ estaLogueado }) {
  return (
    <div>
      {estaLogueado ? <BienvenidaUsuario /> : <BienvenidaInvitado />}
    </div>
  );
}
```

#### Operador &&
```jsx
function Componente({ mostrarMensaje }) {
  return (
    <div>
      {mostrarMensaje && <p>Este mensaje es condicional</p>}
    </div>
  );
}
```

#### Variables para Elementos JSX
```jsx
function Componente({ tipo }) {
  let mensaje;
  
  if (tipo === 'error') {
    mensaje = <p className="error">Error</p>;
  } else if (tipo === 'exito') {
    mensaje = <p className="exito">Operación exitosa</p>;
  } else {
    mensaje = <p>Estado normal</p>;
  }
  
  return <div>{mensaje}</div>;
}
```

### Listas y Keys

#### Renderizado de Listas
```jsx
function ListaElementos({ items }) {
  return (
    <ul>
      {items.map(item => (
        <li key={item.id}>{item.texto}</li>
      ))}
    </ul>
  );
}
```

#### Importancia de la Key Prop
- Ayuda a React a identificar qué elementos han cambiado
- Debe ser única entre hermanos
- Preferiblemente usar IDs estables, no índices de array

### Filtrado de Datos

```jsx
function ListaFiltrada({ items, filtro }) {
  const itemsFiltrados = items.filter(item => 
    item.categoria === filtro || filtro === 'todos'
  );
  
  return (
    <ul>
      {itemsFiltrados.map(item => (
        <li key={item.id}>{item.nombre}</li>
      ))}
    </ul>
  );
}
```

## 🌐 RUTAS Y NAVEGACIÓN

### React Router

#### Configuración Básica
```jsx
import { BrowserRouter, Routes, Route } from 'react-router-dom';

function App() {
  return (
    <BrowserRouter>
      <Routes>
        <Route path="/" element={<Inicio />} />
        <Route path="/about" element={<About />} />
        <Route path="/contacto" element={<Contacto />} />
        {/* Ruta catch-all para 404 */}
        <Route path="*" element={<NotFound />} />
      </Routes>
    </BrowserRouter>
  );
}
```

#### Componentes de Navegación

##### Link
```jsx
import { Link } from 'react-router-dom';

function Navegacion() {
  return (
    <nav>
      <Link to="/">Inicio</Link>
      <Link to="/about">Sobre Nosotros</Link>
      <Link to="/contacto">Contacto</Link>
    </nav>
  );
}
```

##### NavLink (con estilos activos)
```jsx
import { NavLink } from 'react-router-dom';

function Navegacion() {
  return (
    <nav>
      <NavLink 
        to="/" 
        style={({ isActive }) => isActive ? { color: 'red' } : undefined}
      >
        Inicio
      </NavLink>
      <NavLink 
        to="/about"
        className={({ isActive }) => isActive ? 'link-activo' : undefined}
      >
        Sobre Nosotros
      </NavLink>
    </nav>
  );
}
```

#### Acceso a Parámetros de URL
```jsx
import { useParams } from 'react-router-dom';

function PerfilUsuario() {
  const { userId } = useParams();
  
  return <div>Perfil del usuario {userId}</div>;
}

// En el router
<Route path="/usuario/:userId" element={<PerfilUsuario />} />
```

## 📡 COMUNICACIÓN CON APIS

### Axios

#### Instalación
```bash
npm install axios
```

#### Peticiones GET
```jsx
import axios from 'axios';
import { useState, useEffect } from 'react';

function ComponenteAPI() {
  const [datos, setDatos] = useState([]);
  const [cargando, setCargando] = useState(true);
  const [error, setError] = useState(null);
  
  useEffect(() => {
    axios.get('https://api.ejemplo.com/datos')
      .then(respuesta => {
        setDatos(respuesta.data);
        setCargando(false);
      })
      .catch(err => {
        setError(err.message);
        setCargando(false);
      });
  }, []);
  
  if (cargando) return <p>Cargando...</p>;
  if (error) return <p>Error: {error}</p>;
  
  return (
    <ul>
      {datos.map(item => (
        <li key={item.id}>{item.nombre}</li>
      ))}
    </ul>
  );
}
```

#### Organización de Peticiones API
```jsx
// api.js - Centralizar peticiones
import axios from 'axios';

const API = axios.create({
  baseURL: 'https://api.ejemplo.com'
});

export const obtenerDatos = () => API.get('/datos');
export const obtenerDetalle = (id) => API.get(`/datos/${id}`);
export const crearDato = (nuevoDato) => API.post('/datos', nuevoDato);

// En el componente
import { useState, useEffect } from 'react';
import { obtenerDatos } from '../api';

function ComponenteAPI() {
  const [datos, setDatos] = useState([]);
  
  useEffect(() => {
    async function cargarDatos() {
      try {
        const respuesta = await obtenerDatos();
        setDatos(respuesta.data);
      } catch (error) {
        console.error('Error al cargar datos:', error);
      }
    }
    
    cargarDatos();
  }, []);
  
  // Renderizado...
}
```

## 📝 PROYECTO DE PORTFOLIO

### Estructura Recomendada
```
portfolio-react/
├── public/
├── src/
│   ├── components/
│   │   ├── App.js
│   │   ├── Navigation.js
│   │   ├── Home.js
│   │   ├── About.js
│   │   ├── Portfolio/
│   │   │   ├── PortfolioContainer.js
│   │   │   ├── PortfolioItem.js
│   │   │   └── PortfolioFilter.js
│   │   └── Contact.js
│   ├── styles/
│   ├── api/
│   │   └── index.js
│   ├── helpers/
│   ├── hooks/
│   ├── assets/
│   └── index.js
├── package.json
└── README.md
```

### Desarrollo del Contenedor del Portfolio
```jsx
import React, { Component } from 'react';
import axios from 'axios';
import PortfolioItem from './PortfolioItem';
import PortfolioFilter from './PortfolioFilter';

class PortfolioContainer extends Component {
  constructor() {
    super();
    this.state = {
      isLoading: false,
      data: [],
      filteredData: []
    };
  }
  
  componentDidMount() {
    this.getPortfolioItems();
  }
  
  getPortfolioItems() {
    this.setState({ isLoading: true });
    
    axios.get('https://api.ejemplo.com/portfolio-items')
      .then(response => {
        this.setState({
          data: response.data,
          filteredData: response.data,
          isLoading: false
        });
      })
      .catch(error => {
        console.log('Error al cargar los items:', error);
        this.setState({ isLoading: false });
      });
  }
  
  handleFilter = filter => {
    if (filter === 'CLEAR_FILTERS') {
      this.setState({ filteredData: this.state.data });
    } else {
      this.setState({
        filteredData: this.state.data.filter(item => item.category === filter)
      });
    }
  }
  
  render() {
    if (this.state.isLoading) {
      return <div>Cargando...</div>;
    }
    
    return (
      <div className="portfolio-container">
        <PortfolioFilter handleFilter={this.handleFilter} />
        
        <div className="portfolio-items-wrapper">
          {this.state.filteredData.map(portfolioItem => (
            <PortfolioItem 
              key={portfolioItem.id} 
              item={portfolioItem} 
            />
          ))}
        </div>
      </div>
    );
  }
}

export default PortfolioContainer;
```

### Item de Portfolio
```jsx
import React from 'react';
import { Link } from 'react-router-dom';

const PortfolioItem = ({ item }) => {
  return (
    <div className="portfolio-item-wrapper">
      <div 
        className="portfolio-img-background" 
        style={{ backgroundImage: `url(${item.thumb_image})` }} 
      />
      
      <div className="img-text-wrapper">
        <div className="logo-wrapper">
          <img src={item.logo} alt={item.name} />
        </div>
        
        <div className="subtitle">
          {item.description}
        </div>
      </div>
      
      <Link to={`/portfolio/${item.id}`} className="btn-view-details">
        Ver detalles
      </Link>
    </div>
  );
};

export default PortfolioItem;
```

## 🔍 CONSEJOS AVANZADOS

### Optimización de Rendimiento
- Usar React.memo para componentes funcionales
- Implementar shouldComponentUpdate en componentes de clase
- Usar React.PureComponent cuando sea apropiado
- Evitar renderizados innecesarios

### Patrones de Diseño Comunes
- Componentes de Presentación vs Contenedores
- Render Props
- Componentes de Orden Superior (HOC)
- Composición vs Herencia

### Debug y Testing
- React DevTools para Chrome/Firefox
- Jest para testing unitario
- React Testing Library para test de integración

### Buenas Prácticas
- Mantener componentes pequeños y enfocados
- Usar PropTypes para validación de props
- Elevar el estado cuando sea necesario
- Evitar mutaciones directas del estado
