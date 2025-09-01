Mi Portafolio Personal
¡Bienvenido al repositorio de mi portafolio personal! Este es un proyecto de una sola página (landing page) diseñado para ser limpio, moderno y fácil de personalizar. Está construido con tecnologías web modernas que no requieren compilación, lo que lo hace perfecto para alojar en cualquier dominio o servicio de hosting estático.

✨ Ver la demo en vivo ✨
🚀 Características Principales
Diseño Moderno: Interfaz limpia y profesional construida con Tailwind CSS y daisyUI.

Fácil de Personalizar: Toda tu información personal (nombre, redes, etc.) se gestiona desde un único objeto JavaScript.

Tema Claro y Oscuro: Incluye un interruptor para cambiar entre modos, y la preferencia se guarda en el navegador del usuario.

Totalmente Responsivo: Se adapta perfectamente a cualquier tamaño de pantalla, desde móviles hasta escritorios.

Optimizado: Carga rápida al no depender de frameworks pesados de JavaScript.

Iconografía: Utiliza Boxicons para un aspecto visual consistente.

🛠️ Cómo Empezar
Puedes usar este proyecto como plantilla para tu propio portafolio. ¡Solo sigue estos pasos!

Clonar el Repositorio:

git clone [https://github.com/maximo-alvarez/portafolio.git] (https://github.com/maximo-alvarez/portafolio.git)
cd portafolio

Abrir index.html: Abre el archivo index.html en tu editor de código favorito.

Personalizar tu Información: Ve al final del archivo, dentro de la etiqueta <script>. Encontrarás un objeto llamado profileData. ¡Aquí es donde ocurre la magia!

const profileData = {
    name: "Tu Nombre Aquí",
    specialty: "Tu Especialidad (Ej: Frontend Developer)",
    email: "tu.correo@ejemplo.com",
    phone: {
        display: "Tu número visible",
        link: "+1234567890" // Formato internacional para llamadas
    },
    socials: {
        github: "[https://github.com/tu-usuario](https://github.com/tu-usuario)",
        linkedin: "[https://linkedin.com/in/tu-usuario](https://linkedin.com/in/tu-usuario)",
        twitter: "[https://twitter.com/tu-usuario](https://twitter.com/tu-usuario)"
    }
};

Actualizar Contenido Adicional:

Avatar: Reemplaza la imagen en la Hero Section con la tuya. La ruta actual es uploaded:maximo.jpg.... Cambia src a la ruta de tu imagen.

Habilidades: Modifica los badges en la sección de "Habilidades Técnicas". Puedes encontrar más iconos en Boxicons.

Clientes y Proyectos: Actualiza las imágenes, títulos y descripciones en las secciones correspondientes.

¡Listo para Publicar! Sube los archivos a tu servicio de hosting preferido (como GitHub Pages, Vercel, Netlify, o tu propio servidor).

💻 Stack Tecnológico
HTML5

CSS3 con Tailwind CSS

Componentes de UI de daisyUI

JavaScript (Vanilla) para la interactividad y la carga de datos.

Iconos de Boxicons

❤️ Apoya Este Proyecto
Si este proyecto te ha sido útil o te ha inspirado, ¡considera hacer una donación! Tu apoyo me ayuda a seguir creando y compartiendo herramientas de código abierto.

PayPal: [https://www.paypal.com/ncp/payment/RFGNA6MYU5ZJS]

¡Cualquier contribución es muy apreciada!
