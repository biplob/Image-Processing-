from PIL import Image
file = 'myImage/nature2.jpg'
img = Image.open(file)
# img.show()
data = img.getdata()
# print(list(data))
# print(img.size)
width, height = img.size

# print('Width', width)
# print('Height', height)
# new_image = img.resize((350, 200))
# new_image.save('Resized.jpg')
new_width = 930
ratio = new_width / width
new_height = int(height * ratio)
new_image = img.resize((new_width, new_height))
new_image.show()
img.show()
# new_image.save('new_imag.jpg')