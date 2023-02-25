import os
from PIL import Image
imagess = os.listdir('images')

for image in imagess:
   img = Image.open('images/'+image)
   h, w = img.size
   width = 600
   ratio = width / w
   height = int(ratio * h)
   resize = img.resize((width, height))
   resize.save('Resized/'+image)