# hackathon404-team-11
Agente IA Salvador

El ciclo de vulnerabilidad (hambre, rezago educativo y abandono) es explotado por algoritmos de 
redes sociales que presentan ofertas delictivas como salidas económicasrápidas. Este fenómeno no
es solo social; representa una pérdida crítica en el PIB Nacional al destruir el capital humano 
productivo del país.

Tecnologías y herramientas utilizadas

Para la construcción de este prototipo, los Vantablack Devs hemos integrado un stack de alta eficiencia:

    Lenguajes: Python (Backend/AI)

    IA & Orquestación: Gemini 2.5 Flash y el Agent Development Kit (ADK) de Google.

    Infraestructura: google cloud  nube.

    Gestión de Paquetes: uv para un entorno Python determinista y veloz.

    Entorno de Desarrollo: VS Code con integración de Gemini CLI para Vibe Coding.
    
Instrucciones para ejecutar

Para la ejecución del sistema agéntico se usó el Agent Development Kit (ADK) de Google. Se utilizó el lenguaje Python, la API de Gemini 2.5 flash. Se utilizó la herramienta de generación de código Gemini CLI. 
Para ejecutar el programa es necesario obtener una API KEY a partir del siguiente sitio de Google AI Studio en la sección de API Key: API keys | Google AI Studio. 
Se descarga el entorno de Agent Development Kit (ADK). El sitio oficial es:  Agent Development Kit (ADK) - Agent Development Kit (ADK). Luego se ejecuta el commando: pip install google-adk.
El cual es únicamente válido para lenguaje Python, otros lenguajes como Java, Go y Typescript no son sustentados en el actual proyecto, únicamente Python. Es necesario contar con npm y una versión de Python superior a la 3.10 para poder realizar de forma satisfactoria la instalación de los paquetes antes mencionados contenidos en el comando: pip install google-adk
Se coloca el API Key en la carpeta de .env en donde está indicado como API_EXAMPLE
Posteriormente para ejecutar el sistema agéntico en el browser se procede a colocar en la terminal de la carpeta raíz del código el comando: adk web
Esto desplegará en una UI en el navegador predeterminado como Chrome, FireFox, Edge y Safari. 


Integrantes  del equipo 
Vilchis Agustini Brandon
Orlando Porfirio Jiménez Jiménez
Mariano Ventura Castro
Carlos de la Rosa Cuentas-Zavala
Rodríguez Ramírez Leví Gael
