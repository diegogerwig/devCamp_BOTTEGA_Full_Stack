# Guía de Estudio React - Temario Completo

## 📊 Debugging y Herramientas de Desarrollo

### JavaScript Debugger
- **Conceptos clave:**
  - Puntos de interrupción (breakpoints)
  - Variables de inspección
  - Stack trace
  - Consola de depuración

### React Developer Tools
Las React DevTools son una extensión de navegador que permite inspeccionar la jerarquía de componentes de React en las herramientas de desarrollador del navegador. **La depuración es una parte muy importante del desarrollo de software**, permitiendo detectar errores en el código de forma temprana y ser más eficiente.

- **Funcionalidades principales:**
  - **Inspección de componentes:** Ver la estructura jerárquica de componentes React, mostrar props y estado de cada componente
  - **Edición en tiempo real:** Editar props y estado directamente desde la herramienta con cambios inmediatos
  - **Profiler para rendimiento:** Análisis de rendimiento para registrar y analizar la renderización de componentes
  - **Hooks debugging:** Depuración avanzada de hooks
  - **Depuración mejorada:** Facilita encontrar problemas al inspeccionar la estructura interna de la aplicación
  - **Desarrollo más rápido:** Acelera el proceso al proporcionar una visión clara de la estructura y estado

**En resumen, React Developer Tools mejora significativamente la experiencia de desarrollo con React al proporcionar herramientas poderosas para inspeccionar, depurar y optimizar aplicaciones React directamente desde el navegador.**

### Logging de Datos desde APIs
```javascript
// Ejemplo básico de logging
useEffect(() => {
  fetch('/api/data')
    .then(response => response.json())
    .then(data => {
      console.log('API Response:', data);
      setData(data);
    })
    .catch(error => console.error('Error:', error));
}, []);
```

## 🌐 Comunicación con APIs - AXIOS

Axios es una popular librería de JavaScript utilizada para realizar solicitudes HTTP desde el navegador o desde un entorno Node.js. Muchos proyectos en la web necesitan interactuar con una API REST en algún momento de su desarrollo, y axios nos brinda una interfaz sencilla y potente para interactuar con APIs y servicios web.

### Las principales características de axios son:
1. **Es un cliente HTTP basado en promesas:** Utiliza promesas de JavaScript, facilitando el manejo de operaciones asincrónicas
2. **Compatibilidad:** Funciona tanto en el navegador como en Node.js
3. **Transformación automática de datos:** Puede transformar automáticamente los datos de respuesta en formato JSON
4. **Interceptores:** Permite interceptar y modificar solicitudes y respuestas antes de que sean manejadas

### Beneficios de uso
1. **Sintaxis simple** ➡️ API más intuitiva comparado con Fetch
2. **Manejo de errores mejorado** ➡️ Manejo más robusto y consistente de errores
3. **Cancelación de solicitudes** ➡️ Permite cancelar solicitudes en curso para optimizar rendimiento
4. **Configuración global** ➡️ Establecer configuraciones por defecto para todas las solicitudes
5. **Transformación de datos** ➡️ Facilita la manipulación de datos en solicitudes y respuestas

### Instalación y configuración
```bash
npm install axios
```

```javascript
import axios from 'axios';
```

### Ejemplo de uso con React
```javascript
import React, { useState, useEffect } from 'react';
import axios from 'axios';

const DataComponent = () => {
  const [data, setData] = useState(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    const fetchData = async () => {
      try {
        setLoading(true);
        const response = await axios.get('https://api.example.com/data');
        setData(response.data);
      } catch (error) {
        setError(error.message);
        console.error('Error:', error);
      } finally {
        setLoading(false);
      }
    };

    fetchData();
  }, []);

  if (loading) return <div>Cargando...</div>;
  if (error) return <div>Error: {error}</div>;

  return (
    <div>
      {data && (
        <pre>{JSON.stringify(data, null, 2)}</pre>
      )}
    </div>
  );
};
```

### Desglose paso a paso del código axios:

**PASO 1:** `const [data, setData] = useState(null);`
- Hook useState para crear variable de estado `data` y función `setData`
- Inicialmente `data` se establece como `null`

**PASO 2:** `useEffect(() => { ... }, [])`
- Hook useEffect para ejecutar efectos secundarios
- Se usa para realizar petición HTTP cuando el componente se monta

**PASO 3:** `axios.get('https://api.example.com/data')`
- Petición GET a la URL especificada utilizando Axios

**PASO 4:** `.then(response => { setData(response.data); })`
- Si la petición es exitosa, `response.data` contiene los datos de la API
- Se guardan en el estado usando `setData`

**PASO 5:** `.catch(error => { console.error('Error:', error); })`
- Si ocurre error durante la petición, se captura y registra en consola

**PASO 6:** `}, []`
- Array vacío indica que el efecto solo se ejecuta una vez al montar el componente

### Usos recomendados de axios:
- **Desarrollo de aplicaciones web modernas:** Ideal para proyectos con interacción frecuente con APIs RESTful
- **Aplicaciones React o Angular:** Se integra perfectamente facilitando gestión de estado
- **Proyectos Node.js:** Para solicitudes HTTP desde el lado del servidor
- **Aplicaciones que requieren cancelación de solicitudes:** Búsquedas en tiempo real o cargas interrumpibles
- **Escenarios de autenticación complejos:** Simplifica flujos de autenticación y renovación de tokens

## 🔧 Refactoring y Mejores Prácticas

### Destructuring en Componentes
```javascript
// Antes
const PortfolioItem = (props) => {
  return <div>{props.title}</div>;
};

// Después - con destructuring
const PortfolioItem = ({ title, description, image }) => {
  return (
    <div>
      <h3>{title}</h3>
      <p>{description}</p>
    </div>
  );
};
```

### Extracción de API Key Names
- Usar el debugger para identificar nombres de claves
- Crear constantes para keys reutilizables
- Mapeo consistente de datos

## 🖼️ Manejo de Imágenes

### Renderizado de Imágenes desde API
```javascript
const ImageComponent = ({ imageUrl, altText }) => {
  return (
    <img 
      src={imageUrl} 
      alt={altText}
      onError={(e) => {
        e.target.src = '/placeholder-image.jpg';
      }}
    />
  );
};
```

### Importación de Imágenes Estáticas
```javascript
// Método 1: Import directo
import logoImage from '../assets/logo.png';

// Método 2: Require dinámico
const imagePath = require('../assets/image.jpg');

// Uso en componente
<img src={logoImage} alt="Logo" />
```

### Imágenes como Background con Inline Styles
```javascript
const BackgroundImage = ({ imageUrl, children }) => {
  const backgroundStyle = {
    backgroundImage: `url(${imageUrl})`,
    backgroundSize: 'cover',
    backgroundPosition: 'center',
    minHeight: '400px'
  };

  return (
    <div style={backgroundStyle}>
      {children}
    </div>
  );
};
```

## 🎨 Estilos y SCSS

### Estructura Principal de SCSS
```scss
// main.scss
@import 'variables';
@import 'mixins';
@import 'base';
@import 'components/navigation';
@import 'components/portfolio';
@import 'components/auth';
```

### Variables SCSS para Style Guide
```scss
// _variables.scss
$primary-color: #007bff;
$secondary-color: #6c757d;
$font-primary: 'Roboto', sans-serif;
$font-secondary: 'Open Sans', sans-serif;

$breakpoint-mobile: 768px;
$breakpoint-tablet: 1024px;
```

### Mixins para Estilos de Botones
```scss
// _mixins.scss
@mixin button-base {
  padding: 12px 24px;
  border: none;
  border-radius: 4px;
  cursor: pointer;
  transition: all 0.3s ease;
  
  &:hover {
    transform: translateY(-2px);
  }
}

@mixin button-primary {
  @include button-base;
  background-color: $primary-color;
  color: white;
  
  &:hover {
    background-color: darken($primary-color, 10%);
  }
}
```

### Fuentes Personalizadas
```scss
// En tu SCSS principal
@import url('https://fonts.googleapis.com/css2?family=Roboto:wght@300;400;700&display=swap');

body {
  font-family: 'Roboto', sans-serif;
}
```

## 🧭 Navegación y Layout

### Container Flexbox para Navegación
```scss
.navigation-container {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 1rem 2rem;
  background-color: $primary-color;
}

.nav-links-wrapper {
  display: flex;
  gap: 2rem;
  
  .nav-link {
    color: white;
    text-decoration: none;
    font-weight: 500;
    transition: color 0.3s ease;
    
    &:hover {
      color: $secondary-color;
    }
    
    &.active {
      border-bottom: 2px solid white;
    }
  }
}
```

### Estilos para Portfolio Items
```scss
.portfolio-items-container {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
  gap: 2rem;
  padding: 2rem;
}

.portfolio-item {
  position: relative;
  height: 300px;
  border-radius: 8px;
  overflow: hidden;
  cursor: pointer;
  
  .background-image {
    width: 100%;
    height: 100%;
    background-size: cover;
    background-position: center;
  }
  
  .text-overlay {
    position: absolute;
    bottom: 0;
    left: 0;
    right: 0;
    background: linear-gradient(transparent, rgba(0,0,0,0.8));
    color: white;
    padding: 2rem;
    transform: translateY(100%);
    transition: transform 0.3s ease;
  }
  
  &:hover .text-overlay {
    transform: translateY(0);
  }
}
```

## 🔐 Autenticación

### Comportamiento de Autenticación
**Flujo típico:**
1. Usuario ingresa credenciales
2. Validación del formulario
3. Envío de datos al servidor
4. Manejo de respuesta (éxito/error)
5. Almacenamiento de sesión
6. Redirección según estado

### Componente de Login
```javascript
import React, { useState } from 'react';

const LoginComponent = ({ onLogin }) => {
  const [credentials, setCredentials] = useState({
    email: '',
    password: ''
  });
  const [errors, setErrors] = useState({});
  const [isLoading, setIsLoading] = useState(false);

  const handleInputChange = (e) => {
    const { name, value } = e.target;
    setCredentials(prev => ({
      ...prev,
      [name]: value
    }));
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    setIsLoading(true);
    setErrors({});

    try {
      const response = await fetch('/api/login', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify(credentials)
      });

      if (response.ok) {
        const userData = await response.json();
        onLogin(userData);
      } else {
        const errorData = await response.json();
        setErrors(errorData.errors || { general: 'Login failed' });
      }
    } catch (error) {
      setErrors({ general: 'Network error occurred' });
    } finally {
      setIsLoading(false);
    }
  };

  return (
    <form onSubmit={handleSubmit} className="login-form">
      <div className="form-group">
        <label htmlFor="email">Email:</label>
        <input
          type="email"
          id="email"
          name="email"
          value={credentials.email}
          onChange={handleInputChange}
          required
        />
        {errors.email && <span className="error">{errors.email}</span>}
      </div>

      <div className="form-group">
        <label htmlFor="password">Password:</label>
        <input
          type="password"
          id="password"
          name="password"
          value={credentials.password}
          onChange={handleInputChange}
          required
        />
        {errors.password && <span className="error">{errors.password}</span>}
      </div>

      {errors.general && <div className="error general-error">{errors.general}</div>}

      <button type="submit" disabled={isLoading}>
        {isLoading ? 'Logging in...' : 'Log In'}
      </button>
    </form>
  );
};
```

### Manejo de Sesión de Autenticación
```javascript
// Context para autenticación
const AuthContext = createContext();

export const AuthProvider = ({ children }) => {
  const [user, setUser] = useState(null);
  const [isAuthenticated, setIsAuthenticated] = useState(false);

  const login = (userData) => {
    setUser(userData);
    setIsAuthenticated(true);
    localStorage.setItem('authToken', userData.token);
  };

  const logout = () => {
    setUser(null);
    setIsAuthenticated(false);
    localStorage.removeItem('authToken');
  };

  const value = {
    user,
    isAuthenticated,
    login,
    logout
  };

  return (
    <AuthContext.Provider value={value}>
      {children}
    </AuthContext.Provider>
  );
};
```

## 📋 Formularios en React

### Fundamentos de React Forms
```javascript
const FormComponent = () => {
  const [formData, setFormData] = useState({
    name: '',
    email: '',
    message: ''
  });

  const handleChange = (e) => {
    const { name, value } = e.target;
    setFormData(prevData => ({
      ...prevData,
      [name]: value
    }));
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    // Procesar datos del formulario
    console.log('Form submitted:', formData);
  };

  return (
    <form onSubmit={handleSubmit}>
      {/* Campos del formulario */}
    </form>
  );
};
```

## 🎯 Event Listeners - Manejo de Eventos

Un event listener es una función que se encarga de escuchar y responder a eventos específicos que ocurren en elementos del DOM o en objetos de JavaScript. En React, es una función que se ejecuta en respuesta a un evento específico, como un clic de botón o un cambio en un campo de entrada.

### Beneficios del uso de Event Listeners en React:

1. **Interactividad mejorada:** Permiten crear interfaces altamente interactivas, respondiendo a acciones del usuario en tiempo real
2. **Sintaxis simplificada:** React proporciona sintaxis simplificada usando propiedades especiales en elementos JSX
3. **Rendimiento optimizado:** React utiliza un sistema de eventos que mejora rendimiento y garantiza compatibilidad entre navegadores
4. **Manejo centralizado de eventos:** Permite manejar eventos de manera centralizada, facilitando gestión y mantenimiento del código

### Ejemplos de Event Listeners

#### Ejemplo 1: Manejo de clics en un botón
```javascript
function Button() {
  const handleClick = () => {
    console.log('Botón clickeado');
  };

  return <button onClick={handleClick}>Haz clic</button>;
}
```

#### Ejemplo 2: Manejo de cambios en un campo de entrada
```javascript
function InputField() {
  const [value, setValue] = useState('');

  const handleChange = (event) => {
    setValue(event.target.value);
  };

  return <input type="text" value={value} onChange={handleChange} />;
}
```

#### Ejemplo 3: Manejo de eventos del teclado
```javascript
function KeyboardListener() {
  useEffect(() => {
    const handleKeyDown = (event) => {
      if (event.key === 'Escape') {
        console.log('Tecla Escape presionada');
      }
    };

    document.addEventListener('keydown', handleKeyDown);

    return () => {
      document.removeEventListener('keydown', handleKeyDown);
    };
  }, []);

  return <div>Presiona la tecla Escape</div>;
}
```

### Event Listeners para Actualizar Estilos
```javascript
const InteractiveComponent = () => {
  const [isHovered, setIsHovered] = useState(false);
  const [isClicked, setIsClicked] = useState(false);

  const handleMouseEnter = () => setIsHovered(true);
  const handleMouseLeave = () => setIsHovered(false);
  const handleClick = () => setIsClicked(!isClicked);

  const dynamicStyles = {
    backgroundColor: isHovered ? '#f0f0f0' : 'white',
    transform: isClicked ? 'scale(0.95)' : 'scale(1)',
    transition: 'all 0.2s ease'
  };

  return (
    <div
      style={dynamicStyles}
      onMouseEnter={handleMouseEnter}
      onMouseLeave={handleMouseLeave}
      onClick={handleClick}
    >
      Interactive Element
    </div>
  );
};
```

**En resumen, los event listeners en React son fundamentales para crear aplicaciones interactivas y receptivas. Proporcionan una forma eficiente y declarativa de manejar las interacciones del usuario, mejorando la experiencia general de la aplicación.**

## 🧹 Limpieza y Organización

### Limpieza del App Component
```javascript
// App.js organizado
import React from 'react';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import { AuthProvider } from './contexts/AuthContext';
import Navigation from './components/Navigation';
import HomePage from './pages/HomePage';
import AuthPage from './pages/AuthPage';
import './styles/main.scss';

function App() {
  return (
    <AuthProvider>
      <Router>
        <div className="App">
          <Navigation />
          <main className="main-content">
            <Routes>
              <Route path="/" element={<HomePage />} />
              <Route path="/auth" element={<AuthPage />} />
            </Routes>
          </main>
        </div>
      </Router>
    </AuthProvider>
  );
}

export default App;
```

## 🎯 Conceptos Clave para Recordar

**Debugging:**
- Usar console.log estratégicamente
- Aprovechar React DevTools para inspección de componentes y profiling
- Puntos de interrupción en el debugger
- Edición en tiempo real de props y estado

**Comunicación con APIs:**
- Axios como cliente HTTP basado en promesas
- Manejo de errores robusto y cancelación de solicitudes
- Configuración global y transformación automática de datos
- Integración perfecta con React para gestión de estado

**Event Listeners:**
- Fundamentales para interactividad y UX mejorada
- Sintaxis simplificada en React con JSX
- Manejo centralizado y rendimiento optimizado
- Limpieza adecuada de listeners para evitar memory leaks

**Estilos:**
- Organizar SCSS en archivos modulares
- Usar variables para consistency
- Mixins para reutilización
- Flexbox/Grid para layouts

**Autenticación:**
- Validación tanto client como server-side
- Manejo de errores apropiado
- Almacenamiento seguro de tokens
- Estados de loading

**Formularios:**
- Controlled components
- Validación en tiempo real
- Manejo de submit events
- Estados de formulario

**Mejores Prácticas:**
- Destructuring para props
- Componentes reutilizables
- Separación de responsabilidades
- Naming conventions consistentes
- Limpieza de efectos secundarios en useEffect