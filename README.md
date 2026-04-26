# hackathon404-team-11
Agente IA Salvador + Chavitos.

Problema.
El ciclo de vulnerabilidad (hambre, rezago educativo y abandono) es explotado por algoritmos de 
redes sociales que presentan ofertas delictivas como salidas económicasrápidas. Este fenómeno no
es solo social; representa una pérdida crítica en el PIB Nacional al destruir el capital humano 
productivo del país.

Tecnologías y herramientas utilizadas.

Para la construcción de este prototipo, los Vantablack Devs hemos integrado un stack de alta eficiencia:

    Lenguajes: Python (Backend/AI)

    IA & Orquestación: Gemini 2.5 Flash y el Agent Development Kit (ADK) de Google.

    Infraestructura: google cloud  nube.

    Gestión de Paquetes: uv para un entorno Python determinista y veloz.

    Entorno de Desarrollo: VS Code con integración de Gemini CLI para Vibe Coding.

    
Instrucciones para ejecutar.

Para la ejecución del sistema agéntico se usó el Agent Development Kit (ADK) de Google. Se utilizó el lenguaje Python, 
la API de Gemini 2.5 flash. Se utilizó la herramienta de generación de código Gemini CLI. Para ejecutar el programa es
necesario obtener una API KEY a partir del siguiente sitio de Google AI Studio en la sección de API Key: API keys | Google
AI Studio. Se descarga el entorno de Agent Development Kit (ADK). El sitio oficial es:  Agent Development Kit (ADK) - Agent
Development Kit (ADK). Luego se ejecuta el commando: pip install google-adk. El cual es únicamente válido para lenguaje Python,
otros lenguajes como Java, Go y Typescript no son sustentados en el actual proyecto, únicamente Python. Es necesario contar con
npm y una versión de Python superior a la 3.10 para poder realizar de forma satisfactoria la instalación de los paquetes antes
mencionados contenidos en el comando: pip install google-adk. Se coloca el API Key en la carpeta de .env en donde está indicado
como API_EXAMPLE. Posteriormente para ejecutar el sistema agéntico en el browser se procede a colocar en la terminal de la 
carpeta raíz del código el comando: adk web. Esto desplegará en una UI en el navegador predeterminado como Chrome, FireFox, 
Edge y Safari. 

Documentación y herramientas IA
Se utilizó la documentación de Agent Development Kit (ADK): https://adk.dev
La documentación del Agent Development Kit (ADK) se utilizó para configurar el entorno usando el IDE de Visual Studio Code (VSC) y las herramientas de la terminal dentro de una carpeta creada especialmente para este proyecto. A continuación se instaló Gemini CLI  https://geminicli.com mediante la terminal de forma global. Se utilizó la documentación del ADK como parte del context engineering para la creación del sistema agéntico. Se creó primero un proyecto de forma manual dentro de Visual Studio Code usando el lenguaje Python. La creación del primer prototipo del proyecto tenía por fin la validación de la implementación correcta de la API Key, de la correcta importación de ciertos paquetes en el archivo de agent.py, además de realizar una prueba básica en diferentes navegadores predeterminados Luego se usaron varios prompts con Gemini CLI para irle dando forma al proyecto, en cada iteración de hacían prueba a partir de los resultados de la validación en campo realizada con padres de familia, tutores y menores de edad. De esta forma de obtuvo una retroalimentación en tiempo real y se pudieron hacer los ajustes necesarios a la aplicación agéntica. Se siguió este procedimiento hasta conseguir que la aplicación además de la detección de amenazas, pudiera enviar un mensaje a un contacto del menor de edad en caso de alguna amenaza o riesgo digital a tomar en consideración.

Ha habido a limitaciones de tokens y rate limits de las APIs durante el hackathon. Sin embargo, la arquitectura multiagente fue completamente diseñada e incluida en el código fuente como módulos estructurados, junto con su lógica, flujo de datos e instrucciones (prompts).

Este repositorio se enfoca en el diseño del sistema, la lógica de decisión y la interacción entre agentes, que representan el valor central de la solución. Cada agente está documentado con su funcionalidad, inputs, outputs e instrucciones, permitiendo su implementación y escalabilidad en un entorno productivo. Hay ciertos agentes que se han podido implementar y tester, el objetivo es que los siguientes agentes sean integrados por lo que es necesario de apoyo de recursos.

He aqui la explicación del sistema multiagente:

Agente 1:
El Agente Conductual (Behavioral Agent) no intenta identificar si un usuario es menor de edad. En su lugar, detecta señales conductuales tempranas asociadas con la vulnerabilidad, la manipulación, el grooming o el riesgo de reclutamiento.

Su salida es una puntuación de riesgo conductual que alimenta la siguiente capa de la arquitectura: el Agente de Red (Network Agent).

-Agente de texto
-Agente de imagen
-Agente de audio
-Agente de video
-Agente de notificación
Los previos mencionados han sido implementados

Agente dos
El Agente de Red (Network Agent) analiza los patrones de interacción en lugar de limitarse únicamente al contenido de los mensajes. Identifica señales de riesgo a nivel de red, tales como contactos desde cuentas nuevas, una alta intensidad de interacción, la falta de conexiones mutuas, solicitudes de migración de plataforma y el contacto repetido con usuarios vulnerables. Su propósito es detectar estructuras de interacción sospechosas sin realizar acusaciones directas.

Agente tres
El Agente de Riesgo Acumulado (Cumulative Risk Agent) combina las señales conductuales y de red en una única puntuación de riesgo priorizada. En lugar de tomar decisiones binarias, asigna niveles de intervención proporcionales, tales como monitoreo pasivo, intervención preventiva, intervención activa o escalación segura.

Agente cuatro
El Agente de Inmunización Cognitiva genera micro-intervenciones educativas personalizadas que ayudan al usuario a reconocer patrones de manipulación antes de que el riesgo escale. Su objetivo es fortalecer la toma de decisiones del usuario mediante prevención, reflexión y apoyo confiable.

Agente cinco:
El Agente de Inmunización Cognitiva genera micro-intervenciones educativas personalizadas que ayudan al usuario a reconocer patrones de manipulación antes de que el riesgo escale. Su objetivo es fortalecer la toma de decisiones del usuario mediante prevención, reflexión y apoyo confiable.

Agente seis:
El Agente de Inteligencia Defensiva analiza escenarios simulados y datos sintéticos para identificar patrones generales de manipulación y reclutamiento. No interactúa con usuarios reales ni genera tácticas operativas, sino que fortalece el sistema mediante reglas preventivas basadas en aprendizaje seguro.

Agente siete
El Agente de Riesgo Contextual ajusta el nivel de riesgo utilizando factores sociales y territoriales no invasivos, como vulnerabilidad comunitaria, índices de violencia o patrones de actividad. Trata el contexto como un factor de riesgo, no como una acusación, permitiendo una evaluación más realista del entorno.

Agente 8:
El Agente de Explicabilidad traduce las decisiones del sistema en explicaciones claras y comprensibles. Resume los factores de riesgo, explica cómo se combinaron las señales y justifica la intervención seleccionada, garantizando transparencia, confianza y uso ético del sistema.

Agente 9 — Telecom Identity Link Agent

El Agente de Vinculación de Identidad Telefónica conecta las señales de riesgo del sistema con interacciones que migran hacia canales asociados a números telefónicos, como mensajería privada. Su objetivo es reducir el anonimato en escenarios de alto riesgo mediante correlaciones seguras y anonimización, sin almacenar información sensible. Este agente permite detectar patrones donde múltiples cuentas convergen en un mismo punto de contacto, fortaleciendo la capacidad preventiva del sistema en etapas críticas del reclutamiento.


 Agente 10 — Platform Vulnerability Agent

El Agente de Vulnerabilidad en Plataformas analiza dinámicas de riesgo en entornos digitales como TikTok, Roblox y Minecraft, donde la captación puede ocurrir de forma indirecta. Identifica patrones de exposición a contenido aspiracional de riesgo, normalización de dinero fácil o poder, así como interacciones sociales que pueden escalar hacia manipulación o reclutamiento. Su objetivo es intervenir antes del contacto directo, abordando las raíces culturales y sociales que facilitan la vulnerabilidad.


Video DEMO: https://youtube.com/shorts/Q5t2gnSr8po?si=G5tY_lVyxc90F6Au

Integrantes  del equipo.

Carlos Eduardo de la Rosa Cuentas-Zavala
Mariano Ventura Castro
Orlando Porfirio Jiménez Jiménez
Rodríguez Ramírez Leví Gael
Vilchis Agustini Brandon
