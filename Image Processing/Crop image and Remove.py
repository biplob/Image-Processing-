from PIL import Image
img = Image.open('myImage/cat.jpg')
cropped = img.crop((90,50, 300, 300))
cropped.show()