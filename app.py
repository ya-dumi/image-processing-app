import streamlit as st
import numpy as np
import cv2
from PIL import Image

# Title of the app
st.title("🌟 Simple Image Processing App")

# Image uploader widget
uploaded_file = st.file_uploader("Upload an image", type=["jpg", "jpeg", "png"])

if uploaded_file:
    image = Image.open(uploaded_file)
    img_array = np.array(image)

    st.subheader("Original Image")
    st.image(image, use_column_width=True)

    # Sidebar for selecting tasks
    st.sidebar.title("Select Processing Method")
    option = st.sidebar.radio(
        "Choose an option:",
        ["Original", "Gaussian Blur (Smooth)", "Sharpen", "Grayscale"]
    )

    # Perform actions based on user choice
    if option == "Gaussian Blur (Smooth)":
        st.subheader("Smoothed Image (Gaussian Blur)")
        # Apply Gaussian Blur
        blurred_img = cv2.GaussianBlur(img_array, (15, 15), 0)
        st.image(blurred_img, use_column_width=True)

    elif option == "Sharpen":
        st.subheader("Sharpened Image")
        # Kernel for sharpening
        sharpen_kernel = np.array([[0, -1, 0],
                                   [-1, 5, -1],
                                   [0, -1, 0]])
        sharpened_img = cv2.filter2D(img_array, -1, sharpen_kernel)
        st.image(sharpened_img, use_column_width=True)

    elif option == "Grayscale":
        st.subheader("Grayscale Image")
        gray_img = cv2.cvtColor(img_array, cv2.COLOR_RGB2GRAY)
        st.image(gray_img, use_column_width=True)

    else:
        st.write("Displaying original uploaded image.")

else:
    st.write("Please upload an image file to start.")
