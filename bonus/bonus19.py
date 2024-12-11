import streamlit as st
from PIL import Image

def image_converter(param_image):
    img = Image.open(param_image)
    gray_img = img.convert("L")  # L is an algorithm that converts to grayscale
    return gray_img

uploaded_image = st.file_uploader("Upload Image")

with st.expander("Start Camera"):
    # Start the camera
    camera_image = st.camera_input("Camera")
    print(camera_image)


if camera_image:
    st.image(image_converter(camera_image))

elif uploaded_image:
    st.image(image_converter(uploaded_image))
