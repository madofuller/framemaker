import streamlit as st
from PIL import Image



# Open images and store them in a list
images = [Image.open(x) for x in ['canvas3.png', 'christmas card.jpg']]
total_width = 2160
max_height = 3840


# find the width and height of the final image
for img in images:
    total_width += img.size[0]
    max_height = max(max_height, img.size[1])
# create a new image with the appropriate height and width
new_img = Image.new('RGB', (total_width, max_height))
# Write the contents of the new image
current_width = 0
for img in images:
  new_img.paste(img, (current_width,0))
  current_width += img.size[0]
# Save the image
new_img.save('NewImage.jpg')
st.image(new_img)
