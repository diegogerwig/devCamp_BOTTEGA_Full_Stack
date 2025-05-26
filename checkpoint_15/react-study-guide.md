# Guía de Estudio React - Temario Completo

## 📊 Debugging y Herramientas de Desarrollo

### JavaScript Debugger
- **Conceptos clave:**
  - Puntos de interrupción (breakpoints)
  - Variables de inspección
  - Stack trace
  - Consola de depuración

### React Developer Tools
- **Funcionalidades principales:**
  - Inspección de componentes
  - Props y state en tiempo real
  - Profiler para rendimiento
  - Hooks debugging

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
- Aprovechar React DevTools
- Puntos de interrupción en el debugger

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