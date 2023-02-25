from PIL import Image
file =  r'myImage/nature.jpg'
img = Image.open(file)
# print(img)
print(img.format, img.size, img.mode)
img.show()
img.save('modify/nature.jpg')

