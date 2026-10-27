import numpy as np
import streamlit as st


def ampliar(imagem, k=30):
    return imagem.repeat(k, axis=0).repeat(k, axis=1)


st.title("Imagem como matriz")

# Experimentos 1, 2 e 3: imagem preta, um pixel branco e metade de baixo cinza
imagem = np.zeros((8, 8), dtype=np.uint8)
imagem[2, 5] = 255
imagem[4:, :] = 128
st.image(ampliar(imagem))
st.write(imagem)

# Experimento 4: imagem colorida com três faixas
faixas = np.zeros((6, 9, 3), dtype=np.uint8)
faixas[:2, :] = (110, 50, 150)
faixas[2:4, :] = (240, 190, 40)
faixas[4:, :] = (30, 160, 150)
st.image(ampliar(faixas))

# Atividade: bandeira
st.subheader("Bandeira da Itália")

verde = (0, 146, 70)
branco = (241, 242, 241)
vermelho = (206, 43, 55)

bandeira = np.zeros((12, 18, 3), dtype=np.uint8)
bandeira[:, :6] = verde        # faixa da esquerda
bandeira[:, 6:12] = branco     # faixa do meio
bandeira[:, 12:] = vermelho    # faixa da direita
st.image(ampliar(bandeira))
