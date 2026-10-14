🔗 Enlaces Públicos del Proyecto

Backend (API y Render): https://backend-equipo4-5pb1.onrender.com
Endpoint de Prueba de Sentry: https://backend-equipo4-5pb1.onrender.com/sentry-debug
Interfaz de usuario (GitHub Pages): https://mabelpertot.github.io/tp-despliegue-equipo4
Repositorio en GitHub: https://github.com/mabelpertot/tp-despliegue-equipo4.git

☁️ Arquitectura de Despliegue y Herramientas Utilizadas

Para este trabajo práctico se diseñó una arquitectura desacoplada utilizando exclusivamente servicios en la nube con planos gratuitos ( Free Tier ):

Frontend (GitHub Page): Hospedaje del cliente web con despliegue continuo automatizado desde GitHub.
Backend / API REST (Render): servidor en FastAPI (Python) vinculado  
directamente al repositorio para automatizar el CD ante cada git push que gestiona variables de entorno seguras (SENTRY_DSN).
Observabilidad y Monitoreo (Sentry): Integración del SDK oficial para la captura de errores en tiempo real, provisto de un middleware de manejo de excepciones que retorna un código de seguimiento único ( res.sentry).

👥 Autores / Equipo
Desarrollado por el Equipo 4 para el proyecto TP DGS
Ken Morita Alejandro, Moreno Amparo, Pertot Mabel, Ramírez Erik, Ramírez Sebastían