import streamlit as st
import numpy as np

st.title("Laboratório de Computação Gráfica")
st.header("Henrique Liuti")
st.write("Meu primeiro app Streamlit - UniFil 2026/2")

st.subheader("Gradiente gerado com NumPy")
gradiente = np.tile(np.linspace(0, 255, 256, dtype=np.uint8), (100, 1))
st.image(gradiente, caption="Gradiente em tons de cinza")
