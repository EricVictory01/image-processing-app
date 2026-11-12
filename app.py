import streamlit as st
from PIL import Image
import numpy as np

# App Title and Description
st.title("🖼️ Interactive Image Processing App")
st.write("Upload an image to inspect its properties, resize it dynamically, and download the result.")

# File uploader widget
uploaded_file = st.file_uploader("Choose an image file...", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    # Open the image using Pillow
    image = Image.open(uploaded_file)
    
    st.subheader("Original Image")
    st.image(image, caption="Uploaded Image", use_container_width=True)
    
    # Convert image to a NumPy array (just like in your notebook)
    img_array = np.array(image)
    
    # Display array properties
    st.write(f"**Data Type:** `{type(img_array)}`")
    st.write(f"**Image Shape (Height, Width, Color Channels):** `{img_array.shape}`")
    
    st.divider()
    st.subheader("Resize Image")
    
    # Sliders for custom dimensions
    col1, col2 = st.columns(2)
    with col1:
        new_width = st.slider("Select Width (pixels)", min_value=50, max_value=2000, value=300, step=10)
    with col2:
        new_height = st.slider("Select Height (pixels)", min_value=50, max_value=2000, value=300, step=10)
    
    if st.button("Process & Resize"):
        # Resize using Pillow
        img_resized = image.resize((new_width, new_height))
        
        st.subheader("Resized Output")
        st.image(img_resized, caption=f"Resized to {new_width}x{new_height}", use_container_width=False)
        
        # Save and provide download button
        output_filename = "nedu_image_resized.jpg"
        img_resized.save(output_filename)
        
        with open(output_filename, "rb") as file:
            st.download_button(
                label="📥 Download Resized Image",
                data=file,
                file_name=output_filename,
                mime="image/jpeg"
            )