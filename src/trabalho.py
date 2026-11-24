import cv2
import numpy as np
import streamlit as st
from PIL import Image

st.title("Trabalho de Computação Gráfica")

st.header("1. Saturação")
foto = Image.open("imagens/minha_foto.jpg")
img = np.array(foto)
hsv = cv2.cvtColor(img, cv2.COLOR_RGB2HSV)
fator_s = st.slider("Saturação", 0.0, 2.0, 1.5)
s = hsv[:, :, 1].astype(float)
s = s * fator_s
s = np.clip(s, 0, 255)
hsv2 = hsv.copy()
hsv2[:, :, 1] = s
st.image(cv2.cvtColor(hsv2, cv2.COLOR_HSV2RGB), width=300)

st.header("2. Brilho")
fator_v = st.slider("Brilho", 0.0, 2.0, 0.5)
v = hsv[:, :, 2].astype(float)
v = v * fator_v
v = np.clip(v, 0, 255)
hsv2 = hsv.copy()
hsv2[:, :, 2] = v
st.image(cv2.cvtColor(hsv2, cv2.COLOR_HSV2RGB), width=300)

st.header("3. Matiz girada")
giro = st.slider("Giro (graus)", 0, 360, 120)
h = hsv[:, :, 0].astype(int)
h = h + giro // 2
h = h % 180
hsv2 = hsv.copy()
hsv2[:, :, 0] = h
st.image(cv2.cvtColor(hsv2, cv2.COLOR_HSV2RGB), width=300)

st.header("4. Tons de cinza")
col1, col2 = st.columns(2)
r = img[:, :, 0].astype(float)
g = img[:, :, 1].astype(float)
b = img[:, :, 2].astype(float)
soma = r + g + b
media = (soma / 3).astype(np.uint8)
col1.image(media, caption="média", width=300)
peso_r = col2.slider("Peso do R", 0.0, 1.0, 0.3)
peso_g = col2.slider("Peso do G", 0.0, 1.0, 0.59)
peso_b = col2.slider("Peso do B", 0.0, 1.0, 0.11)
ponderada = peso_r * r + peso_g * g + peso_b * b
ponderada = np.clip(ponderada, 0, 255).astype(np.uint8)
col2.image(ponderada, caption="média ponderada", width=300)

st.header("5. Canais")
col1, col2 = st.columns(2)
col1.image(img[:, :, 0], caption="R", width=150)
col1.image(img[:, :, 1], caption="G", width=150)
col1.image(img[:, :, 2], caption="B", width=150)
canal = col2.slider("Canal (0 = R, 1 = G, 2 = B)", 0, 2, 0)
so_canal = np.zeros(img.shape, dtype=np.uint8)
so_canal[:, :, canal] = img[:, :, canal]
col2.image(so_canal, caption="canal escolhido", width=300)
