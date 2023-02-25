from PIL import Image, ImageEnhance

img =Image.open('myImage/cat.jpg')
# filter = ImageEnhance.Brightness(img)
# new_image = filter.enhance(0.5)
# new_image.show()
img.save('pngImage.webp')