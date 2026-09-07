{\rtf1\ansi\ansicpg1252\cocoartf2639
\cocoatextscaling0\cocoaplatform0{\fonttbl\f0\fnil\fcharset0 HelveticaNeue;}
{\colortbl;\red255\green255\blue255;\red0\green0\blue0;}
{\*\expandedcolortbl;;\cssrgb\c0\c0\c0\c84706;}
\paperw11900\paperh16840\margl1440\margr1440\vieww11520\viewh8400\viewkind0
\deftab720
\pard\pardeftab720\partightenfactor0

\f0\fs24 \cf2 \expnd0\expndtw0\kerning0
\
import gradio as gr\
import requests\
import base64\
import io\
import time\
from PIL import Image\
\
URL_API = "http://127.0.0.1:7860/sdapi/v1/txt2img"\
\
def funcion_generar_imagen(prompt_usuario, negative_prompt, pasos_steps, guia_cfg, ancho, alto, semilla):\
    configuracion = \{\
        "prompt": prompt_usuario,\
        "negative_prompt": negative_prompt,\
        "steps": int(pasos_steps),\
        "cfg_scale": float(guia_cfg),\
        "width": int(ancho),\
        "height": int(alto),\
        "seed": int(semilla)\
    \}\
    \
    tiempo_inicio = time.time()\
    try:\
        respuesta = requests.post(URL_API, json=configuracion)\
        if respuesta.status_code == 200:\
            datos = respuesta.json()\
            imagen_base64 = datos['images'][0]\
            bytes_imagen = base64.b64decode(imagen_base64)\
            imagen_final = Image.open(io.BytesIO(bytes_imagen))\
            tiempo_total = time.time() - tiempo_inicio\
            log_resultado = (\
                f"DATOS DE RENDIMIENTO:\\n"\
                f"- Estado: 200 OK\\n"\
                f"- Tiempo de c\'f3mputo: \{tiempo_total:.2f\} s\\n"\
                f"- Resoluci\'f3n activa: \{ancho\}x\{alto\} px\\n"\
                f"- Semilla aplicada: \{semilla\}"\
            )\
            return imagen_final, log_resultado\
        else:\
            return None, f"Error del servidor. C\'f3digo: \{respuesta.status_code\}"\
    except Exception as e:\
        return None, f"Error de conexi\'f3n con la API: \{e\}"\
\
tema_profesional = gr.themes.Soft(\
    primary_hue="blue",\
    secondary_hue="slate",\
    neutral_hue="zinc",\
    font=[gr.themes.GoogleFont("Inter"), "ui-sans-serif", "system-ui"]\
)\
\
with gr.Blocks(title="TFG: Ingenier\'eda de Sonido e Imagen") as mi_cliente:\
    \
    gr.HTML("""\
    <div style='text-align: left; padding-bottom: 20px; border-bottom: 1px solid #e4e4e7; margin-bottom: 30px;'>\
        <h1 style='margin: 0; font-size: 28px; font-weight: 800; color: #18181b; letter-spacing: -0.5px;'>Prototipo basado en Stable Diffusion</h1>\
        <p style='margin: 6px 0 0 0; color: #71717a; font-size: 14px; font-weight: 400;'>Ajuste de par\'e1metros y s\'edntesis de imagen local</p>\
    </div>\
    """)\
    \
    with gr.Row():\
        with gr.Column(scale=1):\
            gr.Markdown("### Configuraci\'f3n de la Se\'f1al de Entrada")\
            \
            caja_prompt = gr.Textbox(\
                label="Prompt de Entrada (Descriptor Textual)", \
                placeholder="Escriba la descripci\'f3n de la imagen que desea generar...",\
                lines=2\
            )\
            \
            caja_negative_prompt = gr.Textbox(\
                label="Prompt Negativo (Elementos a Excluir)", \
                placeholder="Evitar: blurry, low quality, deformed, bad anatomy...",\
                value="blurry, low quality",\
                lines=2\
            )\
            \
            with gr.Accordion("Par\'e1metros de Control Avanzado", open=True):\
                deslizador_steps = gr.Slider(\
                    minimum=1, maximum=50, value=15, step=1, \
                    label="Pasos de Desruido (Steps)",\
                    info="Menos pasos reducen exponencialmente el tiempo de c\'f3mputo."\
                )\
                \
                deslizador_cfg = gr.Slider(\
                    minimum=1.0, maximum=20.0, value=7.0, step=0.5, \
                    label="Factor de Gu\'eda (CFG Scale)",\
                    info="Fidelidad matem\'e1tica respecto al texto de entrada."\
                )\
                \
                with gr.Row():\
                    deslizador_ancho = gr.Slider(\
                        minimum=128, maximum=512, value=256, step=64, \
                        label="Ancho (P\'edxeles)"\
                    )\
                    deslizador_alto = gr.Slider(\
                        minimum=128, maximum=512, value=256, step=64, \
                        label="Alto (P\'edxeles)"\
                    )\
                \
                selector_semilla = gr.Number(\
                    value=-1, \
                    label="Semilla (Seed)", \
                    precision=0,\
                    info="Usa -1 para aleatorio. Usa un n\'famero fijo para replicar resultados."\
                )\
            \
            boton_enviar = gr.Button("GENERAR IMAGEN", variant="primary", size="lg")\
        \
        with gr.Column(scale=1):\
            gr.Markdown("### Salida del Sistema")\
            \
            componente_imagen = gr.Image(\
                label="Imagen Generada", \
                interactive=False\
            )\
            \
            consola_telemetria = gr.Textbox(\
                label="Datos de Rendimiento", \
                interactive=False,\
                lines=5,\
                placeholder="Esperando ejecuci\'f3n del pipeline..."\
            )\
\
    boton_enviar.click(\
        fn=funcion_generar_imagen,\
        inputs=[\
            caja_prompt, \
            caja_negative_prompt, \
            deslizador_steps, \
            deslizador_cfg, \
            deslizador_ancho, \
            deslizador_alto, \
            selector_semilla\
        ],\
        outputs=[componente_imagen, consola_telemetria]\
    )\
\
mi_cliente.launch(server_name="127.0.0.1", server_port=7861, theme=tema_profesional)}