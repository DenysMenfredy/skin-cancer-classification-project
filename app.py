import streamlit as st
from img_classification import skin_cancer_classification
from PIL import Image

st.title("Skin Cancer Classification")
st.header("Skin Cancer Classification Example")
st.text("Faça o upload de uma imagem de dermatoscopia para identificar se o cancer é maligno ou benigno")

uploaded_file = st.file_uploader("Escolha uma imagem...", type="jpg")
if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption='Imagem escolhida.', use_column_width=True)
    st.write("")
    st.write("Classifying...")
    label = skin_cancer_classification(image, 'efficientnetb0_89acc.h5')
    if label == 0:
        st.write("Cancer Benigno")
    else:
        st.write("Cancer Maligno")
