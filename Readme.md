# 🚀 Trabajo Práctico DGS: Despliegue - Equipo 4

Este repositorio contiene la integración del proyecto del Equipo 4, configurado para su despliegue continuo y monitoreo en la nube.

---

## 🔗 Enlaces Públicos del Proyecto

* **Backend (API y Render):** https://backend-equipo4-5pb1.onrender.com
* **Endpoint de Prueba de Sentry:** https://backend-equipo4-5pb1.onrender.com/sentry-debug
* **Interfaz de Usuario (GitHub Pages):** https://mabelpertot.github.io/tp-despliegue-equipo4
* **Repositorio en GitHub:** https://github.com/mabelpertot/tp-despliegue-equipo4.git

## ☁️ Arquitectura de Despliegue y Herramientas Utilizadas

Para este trabajo práctico se diseñó una arquitectura desacoplada utilizando exclusivamente servicios en la nube con planos gratuitos ( Free Tier ):

* **Frontend / GitHub Pages** Hospedaje del cliente web con despliegue continuo automatizado desde GitHub.
* **Backend / API REST (Render):** Servidor en FastAPI (Python) vinculado  
directamente al repositorio para automatizar el CD ante cada git push que gestiona variables de entorno seguras (SENTRY_DSN).
**Monitoreo de Errores/ Sentry:** Observabilidad y Monitoreo : Integración del SDK oficial para la captura de errores en tiempo real, provisto de un middleware de manejo de excepciones que retorna un código de seguimiento único ( res.sentry).

---

## 👥 Equipo 4
Ken Morita Alejandro, Moreno Amparo, Pertot Mabel, Ramírez Erik, Ramírez Sebastían