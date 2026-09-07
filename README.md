# Prototipo de interfaz cliente para Stable Diffusion

Este repositorio contiene el código fuente desarrollado para el Trabajo de Fin de Grado en Ingeniería de Sonido e Imagen de Carlota Díaz-Pavón Sánchez.

## Descripción
Interfaz web interactiva desarrollada con Gradio que consume la API local de AUTOMATIC1111 (`sdapi/v1/txt2img`) para la generación sintética de imágenes y la monitorización de latencia.

## Instalación y ejecución
1. Instalar dependencias:
   ```bash
   pip install -r requirements.txt

2. Iniciar Terminal 1 (servidor):
   ```bash
   ./webui.sh --api
   ```
   *Servidor activo en: http://127.0.0.1:7860*

3. Iniciar Terminal 2 (interfaz):
   ```bash
   python3 cliente_avanzado.py
   ```
   *Interfaz activa en: http://127.0.0.1:7861*
