components
helpers/utils
hooks
models
services
viewmodels
views
static=styles/animations/assets/images/fonts/

mi_proyecto_frontend/
│
├── app.py                      # Archivo principal de la aplicación
├── requirements.txt            # Dependencias del proyecto
├── .env                        # Variables de entorno (contraseñas, API keys)
├── .gitignore                  # Archivos que NO subir a git
│
├── templates/                  # 📄 Archivos HTML
│   ├── base.html              # Plantilla base (layout principal)
│   ├── index.html             # Página principal
│   ├── email.html             # Tu formulario de email
│   ├── dashboard.html         # Otras páginas
│   └── partials/              # Fragmentos HTML reutilizables
│       ├── header.html
│       ├── footer.html
│       └── sidebar.html
│
├── static/                    # 🎨 Archivos estáticos (todo lo que ve el navegador)
│   │
│   ├── css/                   # Estilos
│   │   ├── main.css          # Estilos principales
│   │   ├── components.css    # Estilos de componentes específicos
│   │   ├── animations.css    # Animaciones CSS puras
│   │   └── responsive.css    # Media queries
│   │
│   ├── js/                    # JavaScript
│   │   ├── main.js           # Código principal
│   │   ├── animations.js     # Animaciones con GSAP
│   │   ├── api.js            # Peticiones al backend
│   │   ├── components.js     # Componentes reutilizables
│   │   └── vendor/           # Librerías externas (si no usas CDN)
│   │       ├── gsap.min.js
│   │       └── axios.min.js
│   │
│   ├── images/                # Imágenes
│   │   ├── icons/
│   │   ├── backgrounds/
│   │   ├── logos/
│   │   └── uploads/          # Imágenes subidas por usuarios
│   │
│   ├── fonts/                 # Fuentes locales
│   │   ├── inter.woff2
│   │   └── poppins.woff2
│   │
│   └── assets/                # Otros recursos
│       ├── videos/
│       ├── audio/
│       └── documents/
│
├── utils/                     # 🛠️ Utilidades de Python (backend lógico)
│   ├── __init__.py
│   ├── email_sender.py       # Tu lógica de envío de emails
│   ├── validators.py         # Validaciones de datos
│   ├── decorators.py         # Decoradores personalizados
│   └── helpers.py            # Funciones auxiliares
│
├── forms/                     # 📋 Manejo de formularios (si usas WTForms)
│   ├── __init__.py
│   └── email_form.py
│
├── middleware/                # 🔧 Middlewares (para logging, autenticación)
│   ├── __init__.py
│   └── auth.py
│
├── blueprints/               # 🚏 Rutas organizadas (para proyectos grandes)
│   ├── __init__.py
│   ├── main.py              # Rutas principales
│   ├── email.py             # Rutas de email
│   └── api.py               # Endpoints de API
│
├── config.py                 # ⚙️ Configuración del proyecto
│
├── logs/                     # 📝 Logs del sistema
│   └── app.log
│
├── tests/                    # 🧪 Tests unitarios
│   ├── __init__.py
│   ├── test_email.py
│   └── test_forms.py
│
└── venv/                     # 🐍 Entorno virtual (no se sube a git)
