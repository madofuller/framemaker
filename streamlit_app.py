import streamlit as st
from PIL import Image
import matplotlib.pyplot as plt



image_one = st.file_uploader()
image_two = st.file_uploader()


Image.open(image_one) 

#Second Image
Image.open(image_two)

Image.Image.paste(image_one, image_two)

fig = plt.figure()
plt.imshow(image_one)
plt.axis("off")
st.pyplot(fig)
