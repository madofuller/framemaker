import streamlit as st



st.file_uploader("Upload Image")
#First Image
image_one = Image.open("Capture.PNG") 

#Second Image
image_two = Image.open("github.PNG")

Image.Image.paste(image_one, image_two)

fig = plt.figure()
plt.imshow(image_one)
plt.axis("off")
st.pyplot(fig)
