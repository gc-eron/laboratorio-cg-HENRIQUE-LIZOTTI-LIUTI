import numpy as np
import streamlit as st


def ampliar(imagem, k=30):
    return imagem.repeat(k, axis=0).repeat(k, axis=1)


st.title("Bandeira da Suécia")

azul = (0, 106, 167)
amarelo = (254, 204, 0)

bandeira = np.zeros((10, 16, 3), dtype=np.uint8)
bandeira[:] = azul
bandeira[4:6, :] = amarelo  # faixa horizontal da cruz
bandeira[:, 5:7] = amarelo  # faixa vertical da cruz

st.image(ampliar(bandeira))
